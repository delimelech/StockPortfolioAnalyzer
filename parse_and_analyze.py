#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Parse PASTE_PORTFOLIO_HERE.txt and generate complete analysis
"""

import pandas as pd
import json
from datetime import datetime

# Read the file and extract data lines
with open('PASTE_PORTFOLIO_HERE.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find where data starts (after the header line with Symbol\tDescription...)
data_lines = []
found_header = False
for line in lines:
    if 'Symbol\tDescription\tQuantity' in line and not found_header:
        found_header = True
        continue
    if found_header and line.strip():
        data_lines.append(line.strip())

# Parse data
data = []
for line in data_lines:
    parts = line.split('\t')
    if len(parts) >= 5:
        data.append({
            'Symbol': parts[0].strip(),
            'Description': parts[1].strip(),
            'Quantity': float(parts[2].strip()),
            'CostBasisPrice': float(parts[3].strip()),
            'MarkPrice': float(parts[4].strip())
        })

# Create DataFrame
df = pd.DataFrame(data)

# Calculate P&L
df['CurrentValue'] = df['Quantity'] * df['MarkPrice']
df['CostValue'] = df['Quantity'] * df['CostBasisPrice']
df['PnL_Dollars'] = df['CurrentValue'] - df['CostValue']
df['PnL_Percent'] = ((df['MarkPrice'] - df['CostBasisPrice']) / df['CostBasisPrice']) * 100
df['Weight'] = (df['CurrentValue'] / df['CurrentValue'].sum() * 100)

# Round values
df['CurrentValue'] = df['CurrentValue'].round(2)
df['CostValue'] = df['CostValue'].round(2)
df['PnL_Dollars'] = df['PnL_Dollars'].round(2)
df['PnL_Percent'] = df['PnL_Percent'].round(2)
df['Weight'] = df['Weight'].round(2)
df['MarkPrice'] = df['MarkPrice'].round(2)

# Calculate totals
total_cost = df['CostValue'].sum()
total_current = df['CurrentValue'].sum()
total_pnl = df['PnL_Dollars'].sum()
total_pnl_pct = (total_pnl / total_cost) * 100

# Sort by P&L percent
df_sorted = df.sort_values('PnL_Percent', ascending=False)

# Print summary
print("="*90)
print("PORTFOLIO ANALYSIS - February 25, 2026")
print("="*90)
print(f"\nTotal Positions:     {len(df)}")
print(f"Total Cost Basis:    ${total_cost:,.2f}")
print(f"Current Value:       ${total_current:,.2f}")
print(f"Total P&L:           ${total_pnl:+,.2f} ({total_pnl_pct:+.2f}%)")
print(f"\nWinners: {len(df[df['PnL_Percent'] > 0])}")
print(f"Losers:  {len(df[df['PnL_Percent'] < 0])}")
print(f"Flat:    {len(df[df['PnL_Percent'] == 0])}")

# Top winners
print("\n" + "="*90)
print("TOP 10 WINNERS")
print("="*90)
for idx, (i, row) in enumerate(df_sorted.head(10).iterrows(), 1):
    print(f"{idx}. {row['Symbol']:<8} {row['PnL_Percent']:+8.2f}%  ${row['PnL_Dollars']:+10,.2f}  ${row['CurrentValue']:>10,.2f}")

# Top losers
print("\n" + "="*90)
print("TOP 10 LOSERS")
print("="*90)
for idx, (i, row) in enumerate(df_sorted.tail(10).iterrows(), 1):
    print(f"{idx}. {row['Symbol']:<8} {row['PnL_Percent']:+8.2f}%  ${row['PnL_Dollars']:+10,.2f}  ${row['CurrentValue']:>10,.2f}")

# Dividend analysis
dividend_stocks = {
    'MO': {'annual_div': 4.26},
    'VZ': {'annual_div': 2.84},
    'STWD': {'annual_div': 1.91},
    'ADC': {'annual_div': 3.14},
    'XOM': {'annual_div': 4.12},
    'VTIP': {'annual_div': 1.88},
    'CALM': {'annual_div': 7.96}
}

print("\n" + "="*90)
print("DIVIDEND INCOME - ALL 7 PAYERS")
print("="*90)
total_div_income = 0
div_data = []
for symbol, data in dividend_stocks.items():
    if symbol in df['Symbol'].values:
        row = df[df['Symbol'] == symbol].iloc[0]
        annual_income = row['Quantity'] * data['annual_div']
        total_div_income += annual_income
        yield_on_cost = (data['annual_div'] / row['CostBasisPrice']) * 100
        div_data.append({
            'symbol': symbol,
            'shares': row['Quantity'],
            'annual_div': data['annual_div'],
            'annual_income': annual_income,
            'yield_on_cost': yield_on_cost,
            'current_price': row['MarkPrice']
        })
        print(f"{symbol:<8} {row['Quantity']:>6.1f} shares x ${data['annual_div']:.2f} = ${annual_income:>7.2f}/yr  (YOC: {yield_on_cost:.2f}%)")

print(f"\nTOTAL: ${total_div_income:.2f}/year (${total_div_income/12:.2f}/month)")
print("="*90)

# Save to JSON
output = {
    'timestamp': datetime.now().isoformat(),
    'summary': {
        'total_positions': len(df),
        'total_cost': round(total_cost, 2),
        'total_current_value': round(total_current, 2),
        'total_pnl_dollars': round(total_pnl, 2),
        'total_pnl_percent': round(total_pnl_pct, 2),
        'winners': int(len(df[df['PnL_Percent'] > 0])),
        'losers': int(len(df[df['PnL_Percent'] < 0])),
        'flat': int(len(df[df['PnL_Percent'] == 0]))
    },
    'positions': df_sorted.to_dict('records'),
    'dividends': {
        'total_annual': round(total_div_income, 2),
        'monthly': round(total_div_income/12, 2),
        'payers': div_data
    }
}

with open('portfolio_analysis_latest.json', 'w') as f:
    json.dump(output, f, indent=2)

print("\n[OK] Analysis saved to portfolio_analysis_latest.json\n")

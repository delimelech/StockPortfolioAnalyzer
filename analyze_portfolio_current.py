#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Portfolio Analysis with Current Prices
Calculates P&L and generates analysis
"""

import pandas as pd
import json
from datetime import datetime

# Read portfolio data
df = pd.read_csv('portfolio_current_prices.csv')

# Calculate P&L
df['CurrentValue'] = df['Quantity'] * df['MarkPrice']
df['CostValue'] = df['Quantity'] * df['CostBasisPrice']
df['PnL_Dollars'] = df['CurrentValue'] - df['CostValue']
df['PnL_Percent'] = ((df['MarkPrice'] - df['CostBasisPrice']) / df['CostBasisPrice']) * 100

# Round values
df['CurrentValue'] = df['CurrentValue'].round(2)
df['CostValue'] = df['CostValue'].round(2)
df['PnL_Dollars'] = df['PnL_Dollars'].round(2)
df['PnL_Percent'] = df['PnL_Percent'].round(2)
df['MarkPrice'] = df['MarkPrice'].round(2)

# Calculate totals
total_cost = df['CostValue'].sum()
total_current = df['CurrentValue'].sum()
total_pnl = df['PnL_Dollars'].sum()
total_pnl_pct = (total_pnl / total_cost) * 100

# Sort by P&L percent
df_sorted = df.sort_values('PnL_Percent', ascending=False)

print("="*80)
print("PORTFOLIO ANALYSIS - February 25, 2026")
print("="*80)
print(f"\nTotal Cost Basis:    ${total_cost:,.2f}")
print(f"Current Value:       ${total_current:,.2f}")
print(f"Total P&L:           ${total_pnl:+,.2f} ({total_pnl_pct:+.2f}%)")
print(f"\nWinners: {len(df[df['PnL_Percent'] > 0])}")
print(f"Losers:  {len(df[df['PnL_Percent'] < 0])}")

print("\n" + "="*80)
print("TOP 5 WINNERS")
print("="*80)
for idx, row in df_sorted.head(5).iterrows():
    print(f"{row['Symbol']:8} {row['PnL_Percent']:+8.2f}%  ${row['PnL_Dollars']:+10,.2f}  (${row['MarkPrice']:.2f})")

print("\n" + "="*80)
print("TOP 5 LOSERS")
print("="*80)
for idx, row in df_sorted.tail(5).iterrows():
    print(f"{row['Symbol']:8} {row['PnL_Percent']:+8.2f}%  ${row['PnL_Dollars']:+10,.2f}  (${row['MarkPrice']:.2f})")

print("\n" + "="*80)
print("ALL POSITIONS (sorted by P&L %)")
print("="*80)
print(f"{'Symbol':<8} {'Price':<10} {'Shares':<8} {'Cost':<12} {'Current':<12} {'P&L $':<12} {'P&L %':<10}")
print("-"*80)
for idx, row in df_sorted.iterrows():
    print(f"{row['Symbol']:<8} ${row['MarkPrice']:<9.2f} {row['Quantity']:<8.1f} ${row['CostValue']:<11,.2f} ${row['CurrentValue']:<11,.2f} ${row['PnL_Dollars']:<11,.2f} {row['PnL_Percent']:+.2f}%")

# Save to JSON
output = {
    'timestamp': datetime.now().isoformat(),
    'summary': {
        'total_cost': round(total_cost, 2),
        'total_current_value': round(total_current, 2),
        'total_pnl_dollars': round(total_pnl, 2),
        'total_pnl_percent': round(total_pnl_pct, 2),
        'winners': int(len(df[df['PnL_Percent'] > 0])),
        'losers': int(len(df[df['PnL_Percent'] < 0]))
    },
    'positions': df_sorted.to_dict('records')
}

with open('portfolio_analysis_feb25.json', 'w') as f:
    json.dump(output, f, indent=2)

print("\n[OK] Analysis saved to portfolio_analysis_feb25.json")

# Calculate dividend income
dividend_stocks = {
    'MO': {'yield': 6.15, 'annual_div': 4.26},
    'VZ': {'yield': 5.70, 'annual_div': 2.84},
    'STWD': {'yield': 10.79, 'annual_div': 1.91},
    'ADC': {'yield': 3.96, 'annual_div': 3.14},
    'XOM': {'yield': 2.73, 'annual_div': 4.12},
    'VTIP': {'yield': 3.79, 'annual_div': 1.88}
}

print("\n" + "="*80)
print("DIVIDEND INCOME ANALYSIS")
print("="*80)
total_div_income = 0
for symbol, data in dividend_stocks.items():
    if symbol in df['Symbol'].values:
        row = df[df['Symbol'] == symbol].iloc[0]
        annual_income = row['Quantity'] * data['annual_div']
        total_div_income += annual_income
        yield_on_cost = (data['annual_div'] / row['CostBasisPrice']) * 100
        print(f"{symbol:6} {row['Quantity']:6.1f} shares x ${data['annual_div']:.2f} = ${annual_income:7.2f}/yr  (Yield on cost: {yield_on_cost:.2f}%)")

print(f"\nTotal Annual Dividend Income: ${total_div_income:.2f}/year (${total_div_income/12:.2f}/month)")
print("="*80 + "\n")

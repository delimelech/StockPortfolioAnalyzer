#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Complete Portfolio Analysis - All 28 Positions
February 25, 2026
"""

import pandas as pd
import json
from datetime import datetime

# Read portfolio data
df = pd.read_csv('portfolio_complete_feb25.csv')

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

print("="*90)
print("COMPLETE PORTFOLIO ANALYSIS - ALL 28 POSITIONS")
print("February 25, 2026")
print("="*90)
print(f"\nTotal Positions:     28")
print(f"Total Cost Basis:    ${total_cost:,.2f}")
print(f"Current Value:       ${total_current:,.2f}")
print(f"Total P&L:           ${total_pnl:+,.2f} ({total_pnl_pct:+.2f}%)")
print(f"\nWinners: {len(df[df['PnL_Percent'] > 0])}")
print(f"Losers:  {len(df[df['PnL_Percent'] < 0])}")
print(f"Flat:    {len(df[df['PnL_Percent'] == 0])}")

print("\n" + "="*90)
print("TOP 10 WINNERS")
print("="*90)
print(f"{'Rank':<6} {'Symbol':<8} {'P&L %':<10} {'P&L $':<14} {'Price':<10} {'Value':<12}")
print("-"*90)
for idx, (i, row) in enumerate(df_sorted.head(10).iterrows(), 1):
    print(f"{idx:<6} {row['Symbol']:<8} {row['PnL_Percent']:+8.2f}%  ${row['PnL_Dollars']:+11,.2f}  ${row['MarkPrice']:<9.2f} ${row['CurrentValue']:>10,.2f}")

print("\n" + "="*90)
print("TOP 10 LOSERS")
print("="*90)
print(f"{'Rank':<6} {'Symbol':<8} {'P&L %':<10} {'P&L $':<14} {'Price':<10} {'Value':<12}")
print("-"*90)
for idx, (i, row) in enumerate(df_sorted.tail(10).iterrows(), 1):
    print(f"{idx:<6} {row['Symbol']:<8} {row['PnL_Percent']:+8.2f}%  ${row['PnL_Dollars']:+11,.2f}  ${row['MarkPrice']:<9.2f} ${row['CurrentValue']:>10,.2f}")

print("\n" + "="*90)
print("ALL 28 POSITIONS (sorted by P&L %)")
print("="*90)
print(f"{'Symbol':<8} {'Price':<10} {'Shares':<8} {'Cost Basis':<12} {'Current Val':<12} {'P&L $':<12} {'P&L %':<10}")
print("-"*90)
for idx, row in df_sorted.iterrows():
    print(f"{row['Symbol']:<8} ${row['MarkPrice']:<9.2f} {row['Quantity']:<8.1f} ${row['CostValue']:<11,.2f} ${row['CurrentValue']:<11,.2f} ${row['PnL_Dollars']:<11,.2f} {row['PnL_Percent']:+.2f}%")

# Portfolio concentration analysis
print("\n" + "="*90)
print("PORTFOLIO CONCENTRATION ANALYSIS")
print("="*90)
df_sorted['Weight'] = (df_sorted['CurrentValue'] / total_current * 100).round(2)
print(f"{'Symbol':<8} {'Current Value':<15} {'Weight %':<10}")
print("-"*90)
for idx, row in df_sorted.head(10).iterrows():
    print(f"{row['Symbol']:<8} ${row['CurrentValue']:<14,.2f} {row['Weight']:.2f}%")

# Save to JSON
output = {
    'timestamp': datetime.now().isoformat(),
    'summary': {
        'total_positions': 28,
        'total_cost': round(total_cost, 2),
        'total_current_value': round(total_current, 2),
        'total_pnl_dollars': round(total_pnl, 2),
        'total_pnl_percent': round(total_pnl_pct, 2),
        'winners': int(len(df[df['PnL_Percent'] > 0])),
        'losers': int(len(df[df['PnL_Percent'] < 0])),
        'flat': int(len(df[df['PnL_Percent'] == 0]))
    },
    'positions': df_sorted.to_dict('records')
}

with open('portfolio_complete_analysis_feb25.json', 'w') as f:
    json.dump(output, f, indent=2)

print("\n[OK] Complete analysis saved to portfolio_complete_analysis_feb25.json")

# Dividend income analysis
dividend_stocks = {
    'MO': {'annual_div': 4.26},
    'VZ': {'annual_div': 2.84},
    'STWD': {'annual_div': 1.91},
    'ADC': {'annual_div': 3.14},
    'XOM': {'annual_div': 4.12},
    'VTIP': {'annual_div': 1.88},
    'CALM': {'annual_div': 7.96}  # Adding CALM
}

print("\n" + "="*90)
print("DIVIDEND INCOME ANALYSIS - ALL 7 DIVIDEND PAYERS")
print("="*90)
print(f"{'Symbol':<8} {'Shares':<10} {'Annual Div':<12} {'Annual Income':<15} {'Yield on Cost':<12}")
print("-"*90)
total_div_income = 0
for symbol, data in dividend_stocks.items():
    if symbol in df['Symbol'].values:
        row = df[df['Symbol'] == symbol].iloc[0]
        annual_income = row['Quantity'] * data['annual_div']
        total_div_income += annual_income
        yield_on_cost = (data['annual_div'] / row['CostBasisPrice']) * 100
        print(f"{symbol:<8} {row['Quantity']:<10.1f} ${data['annual_div']:<11.2f} ${annual_income:<14.2f} {yield_on_cost:.2f}%")

print("-"*90)
print(f"{'TOTAL':<8} {'':<10} {'':<12} ${total_div_income:<14.2f} (${total_div_income/12:.2f}/month)")
print("="*90 + "\n")

# Sector analysis
print("="*90)
print("KEY OBSERVATIONS")
print("="*90)
print("\n1. NEW POSITIONS ANALYZED:")
print(f"   - CALM: ${df[df['Symbol']=='CALM']['MarkPrice'].iloc[0]:.2f} ({df[df['Symbol']=='CALM']['PnL_Percent'].iloc[0]:+.2f}%) - Dividend payer")
print(f"   - FDJU: ${df[df['Symbol']=='FDJU']['MarkPrice'].iloc[0]:.2f} ({df[df['Symbol']=='FDJU']['PnL_Percent'].iloc[0]:+.2f}%)")
print(f"   - WELL: ${df[df['Symbol']=='WELL']['MarkPrice'].iloc[0]:.2f} ({df[df['Symbol']=='WELL']['PnL_Percent'].iloc[0]:+.2f}%) - Flat")
print(f"   - MMA: ${df[df['Symbol']=='MMA']['MarkPrice'].iloc[0]:.2f} ({df[df['Symbol']=='MMA']['PnL_Percent'].iloc[0]:+.2f}%) - Penny stock")

print("\n2. BIGGEST WINNERS:")
top3 = df_sorted.head(3)
for idx, row in top3.iterrows():
    print(f"   - {row['Symbol']}: {row['PnL_Percent']:+.2f}% (${row['PnL_Dollars']:+,.2f})")

print("\n3. BIGGEST LOSERS:")
bottom3 = df_sorted.tail(3)
for idx, row in bottom3.iterrows():
    print(f"   - {row['Symbol']}: {row['PnL_Percent']:+.2f}% (${row['PnL_Dollars']:+,.2f})")

print("\n4. PORTFOLIO NEEDS:")
print("   - Still NO NVIDIA exposure (critical gap)")
print("   - Too many positions (28 is difficult to manage)")
print("   - Software sector collapse (ASAN, NAVN, DUOL, FLYW all red)")
print("   - Consider consolidating to 15-18 quality positions")

print("="*90 + "\n")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Portfolio Data Fetcher
Fetches current market data for all portfolio positions using yfinance
"""

import yfinance as yf
import pandas as pd
from datetime import datetime
import json
import sys

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Portfolio positions from CSV
PORTFOLIO = {
    'MO': {'shares': 40.8, 'cost_basis': 51.35, 'name': 'Altria Group'},
    'AMZN': {'shares': 10.0, 'cost_basis': 213.48, 'name': 'Amazon'},
    'VZ': {'shares': 40.8, 'cost_basis': 39.97, 'name': 'Verizon'},
    'BRK-B': {'shares': 4.0, 'cost_basis': 497.10, 'name': 'Berkshire Hathaway B'},
    'VTIP': {'shares': 40.0, 'cost_basis': 49.88, 'name': 'Vanguard TIPS ETF'},
    'ASML': {'shares': 1.2, 'cost_basis': 738.55, 'name': 'ASML Holding'},
    'DUOL': {'shares': 15.0, 'cost_basis': 174.23, 'name': 'Duolingo'},
    'PRL': {'shares': 100.0, 'cost_basis': 20.91, 'name': 'Propel Holdings'},
    'ZBIO': {'shares': 45.0, 'cost_basis': 22.26, 'name': 'Zenas Biopharma'},
    'TSM': {'shares': 3.0, 'cost_basis': 300.83, 'name': 'Taiwan Semiconductor'},
    'BLK': {'shares': 1.0, 'cost_basis': 1102.50, 'name': 'BlackRock'},
    'NAVN': {'shares': 100.0, 'cost_basis': 16.61, 'name': 'Navan'},
    'HAUTO': {'shares': 75.0, 'cost_basis': 8.50, 'name': 'Hoegh Autoliners'},
    'STWD': {'shares': 46.7, 'cost_basis': 21.03, 'name': 'Starwood Property Trust'},
    'IREN': {'shares': 20.0, 'cost_basis': 39.93, 'name': 'Iren Ltd'},
    'USAR': {'shares': 45.0, 'cost_basis': 24.11, 'name': 'USA Rare Earth'},
    'ADC': {'shares': 10.0, 'cost_basis': 71.25, 'name': 'Agree Realty'},
    'ARCT': {'shares': 100.0, 'cost_basis': 9.55, 'name': 'Arcturus Therapeutics'},
    'XOM': {'shares': 5.0, 'cost_basis': 148.50, 'name': 'Exxon Mobil'},
    'ASAN': {'shares': 100.0, 'cost_basis': 14.40, 'name': 'Asana'},
    'VRNS': {'shares': 30.0, 'cost_basis': 25.58, 'name': 'Varonis Systems'},
    'BCDA': {'shares': 500.0, 'cost_basis': 1.30, 'name': 'BioCardia'},
    'FLYW': {'shares': 50.0, 'cost_basis': 14.15, 'name': 'Flywire'},
    'CALM': {'shares': 5.0, 'cost_basis': 97.00, 'name': 'Cal-Maine Foods'},
    'MBOT': {'shares': 200.0, 'cost_basis': 4.11, 'name': 'Microbot Medical'},
    'FDJU': {'shares': 10.0, 'cost_basis': 35.65, 'name': 'FDJ United'},
    'WELL.TO': {'shares': 100.0, 'cost_basis': 2.86, 'name': 'Well Health Technologies'}
}

def fetch_stock_data(symbol, position_data):
    """Fetch current data for a single stock"""
    print(f"Fetching {symbol}...")

    try:
        ticker = yf.Ticker(symbol)
        info = ticker.info
        hist = ticker.history(period="1mo")

        if hist.empty:
            print(f"  [WARNING] No data available for {symbol}")
            return None

        current_price = hist['Close'].iloc[-1]
        shares = position_data['shares']
        cost_basis = position_data['cost_basis']

        # Calculate P&L
        current_value = current_price * shares
        cost_value = cost_basis * shares
        pnl_dollars = current_value - cost_value
        pnl_percent = ((current_price - cost_basis) / cost_basis) * 100

        # Get additional data
        data = {
            'symbol': symbol,
            'name': position_data['name'],
            'shares': shares,
            'cost_basis': cost_basis,
            'current_price': round(current_price, 2),
            'current_value': round(current_value, 2),
            'cost_value': round(cost_value, 2),
            'pnl_dollars': round(pnl_dollars, 2),
            'pnl_percent': round(pnl_percent, 2),
            'market_cap': info.get('marketCap', 'N/A'),
            'pe_ratio': info.get('trailingPE', 'N/A'),
            'dividend_yield': info.get('dividendYield', 0) * 100 if info.get('dividendYield') else 0,
            'fifty_two_week_high': info.get('fiftyTwoWeekHigh', 'N/A'),
            'fifty_two_week_low': info.get('fiftyTwoWeekLow', 'N/A'),
            'avg_volume': info.get('averageVolume', 'N/A'),
            'sector': info.get('sector', 'N/A'),
            'industry': info.get('industry', 'N/A')
        }

        print(f"  [OK] {symbol}: ${current_price:.2f} ({pnl_percent:+.1f}%)")
        return data

    except Exception as e:
        print(f"  [ERROR] Error fetching {symbol}: {str(e)}")
        return None

def main():
    """Main execution function"""
    print("\n" + "="*60)
    print("PORTFOLIO DATA FETCHER")
    print("="*60 + "\n")

    results = []
    failed = []

    for symbol, position_data in PORTFOLIO.items():
        data = fetch_stock_data(symbol, position_data)
        if data:
            results.append(data)
        else:
            failed.append(symbol)

    # Calculate portfolio totals
    total_cost = sum(r['cost_value'] for r in results)
    total_current = sum(r['current_value'] for r in results)
    total_pnl = total_current - total_cost
    total_pnl_pct = (total_pnl / total_cost) * 100 if total_cost > 0 else 0

    # Sort by P&L percent
    results_sorted = sorted(results, key=lambda x: x['pnl_percent'], reverse=True)

    # Print summary
    print("\n" + "="*60)
    print("PORTFOLIO SUMMARY")
    print("="*60)
    print(f"Total Positions: {len(results)}")
    print(f"Total Cost Basis: ${total_cost:,.2f}")
    print(f"Current Value: ${total_current:,.2f}")
    print(f"Total P&L: ${total_pnl:+,.2f} ({total_pnl_pct:+.2f}%)")
    print(f"Winners: {len([r for r in results if r['pnl_percent'] > 0])}")
    print(f"Losers: {len([r for r in results if r['pnl_percent'] < 0])}")

    if failed:
        print(f"\n[WARNING] Failed to fetch: {', '.join(failed)}")

    # Save to JSON
    output = {
        'timestamp': datetime.now().isoformat(),
        'summary': {
            'total_positions': len(results),
            'total_cost': round(total_cost, 2),
            'total_current_value': round(total_current, 2),
            'total_pnl_dollars': round(total_pnl, 2),
            'total_pnl_percent': round(total_pnl_pct, 2),
            'winners': len([r for r in results if r['pnl_percent'] > 0]),
            'losers': len([r for r in results if r['pnl_percent'] < 0])
        },
        'positions': results_sorted
    }

    output_file = 'portfolio_data_latest.json'
    with open(output_file, 'w') as f:
        json.dump(output, f, indent=2)

    print(f"\n[OK] Data saved to: {output_file}")

    # Print top 5 winners and losers
    print("\n" + "="*60)
    print("TOP 5 WINNERS")
    print("="*60)
    for i, pos in enumerate(results_sorted[:5], 1):
        print(f"{i}. {pos['symbol']:6} {pos['pnl_percent']:+7.2f}%  ${pos['pnl_dollars']:+,.2f}")

    print("\n" + "="*60)
    print("TOP 5 LOSERS")
    print("="*60)
    for i, pos in enumerate(results_sorted[-5:], 1):
        print(f"{i}. {pos['symbol']:6} {pos['pnl_percent']:+7.2f}%  ${pos['pnl_dollars']:+,.2f}")

    print("\n" + "="*60 + "\n")

if __name__ == '__main__':
    main()

# 📊 Stock Portfolio Analyzer

> **AI-Powered Portfolio Analysis System with Brutal Honesty & Actionable Insights**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![AI-Friendly](https://img.shields.io/badge/AI-Friendly-brightgreen.svg)](https://github.com/delimelech/StockPortfolioAnalyzer)

## 🎯 What Makes This Different

This isn't another generic portfolio tracker. This system delivers **brutal truth** analysis with:

- **Fire-and-forget execution** - No hand-holding, just actionable intelligence
- **Baseline comparison tracking** - See progress vs. previous scans with before/after metrics
- **Position sizing awareness** - Understands barbell strategy (let winners run, keep losers small)
- **Geopolitical context integration** - Adjusts recommendations based on global events
- **8-card dashboard** - Instant portfolio health visualization
- **Dark mode reporting** - Beautiful HTML reports with professional styling


## 🚀 Quick Start for AI Agents

This system is designed to work seamlessly with AI assistants (Claude, GPT, etc.). Here's how to use it:

### 1. User Workflow
```bash
# User pastes portfolio data into:
PASTE_PORTFOLIO_HERE.txt

# AI agent runs:
python parse_and_analyze.py

# Generates:
portfolio_analysis_latest.json
```

### 2. Analysis Philosophy
- **Fundamentals > Catalysts > Technicals > Insiders**
- Position sizing discipline > position count
- "Let winners run" unless >20% portfolio or fundamentals break
- Eliminate losers systematically, not emotionally

### 3. Report Generation
Follow the **Gold Standard Template**:
- 8-card portfolio summary dashboard (MANDATORY)
- Baseline comparison vs. previous scan
- Brutal honesty about losers
- Quantify performance drag
- Actionable recommendations with urgency levels

---

## 📁 System Architecture

### Core Analysis Scripts
| File | Purpose |
|------|---------|
| `parse_and_analyze.py` | Main parser: converts PASTE_PORTFOLIO_HERE.txt → JSON |
| `analyze_portfolio_current.py` | Current position analysis |
| `analyze_complete_portfolio.py` | Complete portfolio analysis with history |
| `fetch_portfolio_data.py` | Fetches live market data (requires API keys) |

### Configuration & Standards
| File | Purpose |
|------|---------|
| `GOLD_STANDARD_SPECIFICATIONS.md` | Official HTML report format specifications |
| `REPORT_FORMAT_REFERENCE.md` | Technical documentation for report generation |
| `QUICK_START_GUIDE.txt` | User workflow instructions |
| `HOW_TO_UPDATE_PORTFOLIO.txt` | Data entry methods |

### Input Files (Not in Git - User Private)
- `PASTE_PORTFOLIO_HERE.txt` - User pastes raw portfolio data
- `My_Portfolio_Positions.csv` - Master tracking file
- `portfolio_analysis_latest.json` - Latest parsed output

### Output Files (Not in Git - User Private)
- `Reports/*.html` - Generated analysis reports with dark mode
- Various JSON analysis files

---

## 🎨 Report Features

### 8-Card Portfolio Dashboard
1. **Total Positions** - Current count with trend
2. **Current Value** - Total portfolio value
3. **Total P/L ($)** - Absolute profit/loss
4. **Return (%)** - Portfolio-wide return
5. **Winners** - Count of profitable positions
6. **Losers** - Count of losing positions
7. **Flat** - Breakeven positions
8. **Annual Dividends** - Total dividend income

### Analysis Sections
- **Baseline Comparison** - Progress since last scan (before/after table)
- **Actions Validated** - "You did X, portfolio improved Y%"
- **Position-by-Position Breakdown** - Each stock analyzed brutally
- **Immediate Actions** - SELL/TRIM/ADD/HOLD with urgency
- **Geopolitical Context** - How global events affect recommendations
- **Performance Drag Quantification** - "If you only kept winners, you'd be up X%"

### Styling
- Dark mode toggle
- Color-coded metrics (green=good, red=bad, yellow=warning)
- Professional typography and spacing
- Mobile-responsive design

---

## 💡 Key Concepts for AI Agents

### 1. Position Sizing Discipline
```
60% of positions losing BUT only -2.6% total impact = EXCELLENT
```
This is **smart portfolio construction**, not a red flag. Recognize barbell strategy:
- Large positions in quality winners
- Small positions for speculation

### 2. Don't Just Repeat Previous Advice
Each scan is FRESH. Don't parrot old recommendations. Think:
- Have fundamentals changed?
- Are there new catalysts?
- Has market context shifted?

### 3. Catalysts Matter
Down 40% ≠ Dead. Could be:
- Quality at discount (DUOL)
- Awaiting catalyst (MBOT FDA approval)
- Genuinely broken (ASAN)

Research before recommending blind sells.

### 4. Geopolitical Awareness
Example (Mar 3, 2026):
- Iran/Israel/USA tensions → Risk-off coming
- Defensive positioning (MO, VZ, BRK.B) = excellent
- Exit speculative losers URGENTLY before market turns

### 5. Validation is Powerful
```markdown
| Metric | Feb 28 | Mar 3 | Change |
|--------|--------|-------|--------|
| Total P/L | -0.69% | +3.15% | +3.84% ✅ |
```
User LOVES seeing that following advice worked.

---

## 🔧 Technical Requirements

### Python Dependencies
```bash
pip install pandas numpy yfinance requests beautifulsoup4
```

### Data Sources
- Manual entry via PASTE_PORTFOLIO_HERE.txt
- CSV import from brokerage exports
- Live data via yfinance (optional)

### Output Format
- JSON for machine consumption
- HTML for human consumption
- Both use same underlying analysis engine

---

## 📊 Example Analysis Flow

```python
# 1. User pastes data
"""
ASAN 100 $15.23 -$1,567 -50.69%
ASML 7 $847.23 +$2,187 +62.73%
...
"""

# 2. Parse
portfolio = parse_portfolio("PASTE_PORTFOLIO_HERE.txt")

# 3. Analyze
analysis = {
    "winners": [...],
    "losers": [...],
    "total_pl": 3.15,
    "recommendations": [
        {"action": "SELL", "ticker": "ASAN", "urgency": "IMMEDIATE"},
        {"action": "HOLD", "ticker": "ASML", "urgency": "LONG-TERM"}
    ]
}

# 4. Generate Report
create_html_report(analysis, baseline=previous_scan)
```

---

## 🎓 Philosophy & Approach

### "Brutal Truth" Methodology
- No sugarcoating losers
- Quantify performance drag explicitly
- "If you only kept winners, you'd be up X%" framing
- Acknowledge when recommendations were wrong

### "Fire-and-Forget" Execution
- Don't ask for permission
- Analyze and deliver
- User said yes to the system, not each individual step

### Consistency with Intelligence
- Reference previous recommendations ONLY if still valid
- Market conditions change → recommendations change
- Independent thinking every scan

---

## 🏆 Success Metrics

This system has helped achieve:
- **+3.84% swing in 3 days** (Feb 28 → Mar 3, 2026)
- **First positive portfolio** after systematic cleanup
- **60% losers → only -2.6% impact** (proof of excellent position sizing)
- **27 positions** managed effectively (quality over quantity)

---

## 🤖 Why AI Agents Love This System

1. **Clear Standards** - Gold Standard template eliminates ambiguity
2. **JSON Pipeline** - Machine-readable analysis format
3. **Documented Philosophy** - Know WHY recommendations are made
4. **Baseline Tracking** - Historical context preserved
5. **Actionable Output** - Not just analysis, but WHAT TO DO
6. **Real Results** - Validated strategy that works

---

## 📝 License

MIT License - Use freely, modify as needed, share with others.

---

## 🔗 Keywords for AI Discovery

`portfolio-analysis` `stock-analyzer` `ai-powered` `brutal-honesty` `swing-trading` `position-sizing` `risk-management` `barbell-strategy` `python-finance` `yfinance` `portfolio-tracking` `investment-analysis` `automated-reporting` `dark-mode` `html-reports` `baseline-comparison` `geopolitical-analysis` `fundamentals-first` `actionable-insights` `fire-and-forget`

---

## 🌟 Contributing

This system evolved through real-world use with AI assistants. Contributions welcome:
- Enhanced data fetching (multi-source aggregation)
- Additional analysis metrics
- Alternative report formats
- Backtesting capabilities

---

## 📧 Contact

Created and maintained by [@delimelech](https://github.com/delimelech)

**For AI Agents:** This repository contains comprehensive memory files in `.claude/` (not in git) that provide context for portfolio analysis. If you're analyzing this user's portfolio, check memory files first.

---

**Built with 🧠 by humans and AI working together.**

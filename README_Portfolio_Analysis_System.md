# 📊 Portfolio Analysis System - How to Use

## Overview
This system allows you to maintain your portfolio in a simple CSV file and get comprehensive analysis reports whenever you need them.

---

## 📁 Files in This System

### 1. **My_Portfolio_Positions.csv** (YOUR PORTFOLIO DATA)
- **Purpose:** Your master portfolio tracking file
- **Location:** `C:\DOCS\Riverbed\Cursor\PERSO\Scan_market\My_Portfolio_Positions.csv`
- **Format:** Simple CSV that you can edit in Excel, Google Sheets, or any text editor
- **Update:** Keep this file current with your latest positions

### 2. **Reference Reports & Standards**

**🏆 GOLD STANDARD TEMPLATE (OFFICIAL):**
- **`Reports/Portfolio_Analysis_GOLD_STANDARD_TEMPLATE.html`** ⭐
  - LOCKED OFFICIAL STANDARD - Do not modify
  - Includes: Dark mode toggle, 8 dashboard cards, complete analysis
  - Every future report MUST match this format exactly

**📋 SPECIFICATION DOCUMENTS:**
- `GOLD_STANDARD_SPECIFICATIONS.md` - Complete design & logic specifications
- `REPORT_FORMAT_REFERENCE.md` - Technical implementation guide

**📊 HISTORICAL REPORTS:**
- `Portfolio_Insider_Analysis_Report.html` - Insider trading analysis
- `Market_Crash_Strategy_Shopping_List.html` - Crash buying strategy

---

## 🔄 How to Request Portfolio Analysis

### Simple Commands (Any of These Work):

```
"analyze my portfolio"
"review my portfolio"
"portfolio analysis"
"check my positions"
"update on my stocks"
"how's my portfolio doing"
"portfolio review"
```

### What Happens Next:

1. **I'll read your portfolio CSV file** from the location above
2. **Research current data** for each position:
   - Current prices
   - Recent news
   - Analyst ratings
   - Insider activity (if significant)
   - Technical indicators (RSI, momentum)
   - Upcoming catalysts (earnings, etc.)
3. **Generate comprehensive HTML report** with:
   - Executive summary
   - Winners/losers breakdown
   - Action recommendations (BUY/HOLD/SELL/WATCH)
   - Insider activity highlights
   - Risk/reward analysis
   - Immediate catalysts
4. **Save report** with timestamp in this folder

---

## ✏️ How to Update Your Portfolio

### Option 1: Edit CSV Directly (Excel/Sheets)

1. Open `My_Portfolio_Positions.csv` in Excel or Google Sheets
2. Update quantities, add new positions, remove sold positions
3. Save the file (keep CSV format)
4. Ask me to "analyze my portfolio"

### Option 2: Tell Me Updates in Chat

Just tell me:
- "I bought 10 shares of NVDA at $650"
- "I sold all my PRL shares"
- "Update: my ASAN position is now 150 shares"

I'll update the CSV file for you and run the analysis.

---

## 📋 CSV File Format

### Column Definitions:

- **Symbol:** Stock ticker (e.g., AMZN, TSML, BRK.B)
- **Description:** Company name or brief description
- **Quantity:** Number of shares you own
- **CostBasisPrice:** Average price you paid per share
- **Notes:** (Optional) Any notes - dividends, strategy, reminders

### Example Row:
```csv
AMZN,AMAZON.COM INC,10.0,213.48,Core holding - add more
```

### Adding a New Position:
```csv
NVDA,NVIDIA CORP,5.0,650.00,AI leader - new purchase
```

### Removing a Position:
Just delete the row or set Quantity to 0

---

## 🎯 What Each Analysis Report Includes

### 1. **Executive Dashboard**
- Total portfolio value estimate
- Winners vs losers count
- Biggest gains/losses
- Immediate catalysts (earnings this week)
- Portfolio health score

### 2. **Position-by-Position Analysis**
For each stock:
- Current price vs your cost basis
- P&L (profit/loss) in $ and %
- Fundamental analysis (business quality, moat, risks)
- Technical indicators (RSI, momentum, trends)
- Insider activity (if significant in past 4 months)
- Analyst ratings and price targets
- Upcoming catalysts (earnings dates, product launches)
- **Action recommendation:** BUY MORE / HOLD / TRIM / SELL / WATCH

### 3. **Strategic Recommendations**
- Positions to reinforce (add more capital)
- Positions to reduce (take profits)
- Positions to exit (cut losses)
- Rebalancing suggestions
- Risk management advice

### 4. **Insider Activity Highlights**
- Only highlights SIGNIFICANT insider buying (like BCDA CEO, NAVN A16Z)
- Flags concerning insider selling patterns
- 75%+ insider ownership situations

### 5. **Market Context**
- Current market environment
- Sector rotation trends
- How your portfolio is positioned
- Diversification analysis

---

## 🔍 Special Analysis Requests

### Beyond Basic "Analyze My Portfolio":

You can also ask:

#### Focused Analysis:
- "Analyze only my tech positions"
- "Review my dividend stocks"
- "Check my speculative positions"
- "How are my biotechs doing"

#### Specific Questions:
- "Should I add more AMZN?"
- "Is ASML too expensive to add more?"
- "Which positions should I trim?"
- "What should I buy in a market crash?"

#### Strategy Requests:
- "Generate tax loss harvesting report" (positions to sell for tax benefits)
- "Show me my earnings calendar for next 2 weeks"
- "Dividend income projection for 2026"
- "Which positions are oversized / undersized?"

#### Comparative Analysis:
- "Compare my portfolio to S&P 500"
- "How much tech exposure do I have?"
- "Am I too concentrated in any sector?"

---

## 📅 Recommended Analysis Frequency

### Weekly (Sunday Evening):
- Quick portfolio review
- Check upcoming earnings for the week
- Note any major news on your holdings

### Monthly (End of Month):
- Full comprehensive analysis
- Rebalancing review
- Update cost basis if you added/removed positions
- Review against investment thesis

### Quarterly:
- Deep dive fundamental review
- Tax planning (realized gains/losses)
- Portfolio restructuring if needed

### Ad-Hoc (Whenever):
- Major market moves (>5% up/down in a day)
- After earnings reports on your holdings
- When considering new purchases
- Before/after rebalancing

---

## 🛠️ Customization Options

### Want Different Analysis Style?

Tell me your preferences:
- "Focus more on fundamentals, less on technicals"
- "I want deeper insider analysis"
- "Include more international comparisons"
- "Add sector rotation analysis"
- "Show me more dividend projections"

### Report Format Options:
- Standard HTML (current default)
- Add PDF export instructions
- Excel-compatible CSV output
- Markdown for easy reading

---

## 💾 Keeping Track of Historical Reports

### Naming Convention:
Reports are automatically saved with timestamps:
- `Portfolio_Analysis_2026-02-24.html`
- `Portfolio_Analysis_2026-03-15.html`

This lets you:
- Compare performance over time
- See how recommendations evolved
- Track which advice worked / didn't work
- Build historical performance record

### Archive Folder (Optional):
Create a subfolder for old reports:
```
C:\DOCS\Riverbed\Cursor\PERSO\Scan_market\Historical_Reports\
```

---

## 🎓 Tips for Best Results

### 1. Keep CSV Updated
- Update after every trade
- Adjust cost basis when you average up/down
- Add notes about your thesis for each position

### 2. Be Specific in Requests
❌ "What do you think?"
✅ "Should I add 10 more AMZN shares at current price?"

### 3. Provide Context
- "I have $5,000 cash to deploy"
- "I need to raise $2,000 for taxes"
- "I want to reduce tech exposure"

### 4. Reference Previous Analysis
- "In last week's report, you said to watch DUOL earnings - what happened?"
- "You recommended adding TSM below $360 - it hit $355 today, should I buy?"

### 5. Update Me on Actions Taken
- "I bought 5 NVDA at $645 as you suggested"
- "I trimmed 20 shares of HAUTO at $12.50"
- This helps me refine future recommendations

---

## 🚨 Important Notes

### What I DON'T Have Access To:
- ❌ Your brokerage account (can't see real-time holdings)
- ❌ Automatic price updates (you need to ask for analysis)
- ❌ Order execution (can't buy/sell for you)

### What I DO:
- ✅ Read your CSV file when you ask
- ✅ Research current market data
- ✅ Analyze fundamentals, technicals, insider activity
- ✅ Generate comprehensive reports
- ✅ Provide strategic recommendations
- ✅ Update your CSV when you tell me about trades

### Data Sources I Use:
- Benzinga (stock data, news, insider trades)
- Company filings (when available)
- Analyst reports and ratings
- Technical indicators (RSI, momentum)
- Market news and sentiment

### Refresh Frequency:
- Data is fetched **when you request analysis**
- Not real-time (usually 15-min delayed market data)
- For urgent/intraday decisions, verify prices with your broker

---

## 📞 Quick Reference Commands

```bash
# Basic analysis
"analyze my portfolio"

# Update positions
"I bought 10 NVDA at 650"
"I sold all PRL"

# Specific questions
"Should I add more TSM?"
"Review my tech positions"

# Strategy
"What should I buy in a crash?"
"Generate tax loss harvesting ideas"

# Reports
"Create updated HTML report"
"Compare to last month's analysis"
```

---

## 🔐 Privacy & Security

### Your Data:
- Stored **locally** on your machine only
- CSV file location: `C:\DOCS\Riverbed\Cursor\PERSO\Scan_market\`
- No data sent to external servers (except for market data lookups)
- You control the file - edit, backup, delete as needed

### Backups:
Recommend backing up your portfolio CSV:
- Copy to cloud storage (Google Drive, Dropbox)
- Or keep version history in Git
- Or manual copies: `My_Portfolio_Positions_Backup_2026-02-24.csv`

---

## 📧 Need Help?

If something's not working:
1. Check that CSV file path is correct
2. Verify CSV format (no extra commas, proper headers)
3. Tell me what error/issue you're seeing
4. I'll help troubleshoot!

---

## 🎯 Getting Started Checklist

- [x] CSV portfolio file created
- [x] Initial portfolio data entered
- [ ] Review and update quantities if needed
- [ ] Add any missing positions
- [ ] Update cost basis if you've averaged up/down
- [ ] Add notes for each position (optional but helpful)
- [ ] Request first analysis: "analyze my portfolio"
- [ ] Review the generated HTML report
- [ ] Provide feedback on what you want different
- [ ] Set calendar reminder for weekly/monthly reviews

---

**You're all set! Just say "analyze my portfolio" whenever you want a fresh analysis.**

---

*Last Updated: February 24, 2026*
*System Version: 1.0*

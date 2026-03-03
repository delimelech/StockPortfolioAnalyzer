# Portfolio Analysis Report - Reference Format

**Last Updated:** February 25, 2026
**Reference Report:** Portfolio_Analysis_Complete_28_Positions_Feb25.html

## Standard Report Structure

Every portfolio analysis should follow this exact format and include all these sections:

---

## 1. BREAKING NEWS BANNER (if applicable)
- Animated alert banner at top
- Highlights major developments since last report
- Examples: stocks back trading, major price movements, sector shifts
- Color: Orange/yellow gradient with animation

---

## 2. PORTFOLIO SUMMARY DASHBOARD

**CRITICAL:** Dashboard MUST have exactly 8 cards in this order:

1. **Total Positions**
   - Value: Number (e.g., "28")
   - Subvalue: "Active Holdings"
   - Color: Default purple gradient

2. **Current Value**
   - Value: Dollar amount (e.g., "$30,323.07")
   - Subvalue: "Market Value"
   - Color: Default purple gradient

3. **Total P&L**
   - Value: Dollar amount with sign (e.g., "-$1,312.60")
   - Subvalue: "Profit/Loss"
   - Color: RED (#dc3545) if negative, GREEN (#28a745) if positive
   - **Style:** `style="color: #dc3545;"` inline on value

4. **Return %**
   - Value: Percentage with sign (e.g., "-4.15%")
   - Subvalue: "Portfolio Return"
   - Color: RED (#dc3545) if negative, GREEN (#28a745) if positive
   - **Style:** `style="color: #dc3545;"` inline on value

5. **Winners**
   - Value: Number (e.g., "9")
   - Subvalue: "X% of positions"
   - Color: GREEN (#28a745) on value
   - **Style:** `style="color: #28a745;"` inline on value

6. **Losers**
   - Value: Number (e.g., "18")
   - Subvalue: "X% of positions"
   - Color: RED (#dc3545) on value
   - **Style:** `style="color: #dc3545;"` inline on value

7. **Flat Positions**
   - Value: Number (e.g., "1")
   - Subvalue: "X% of positions"
   - Color: GRAY (#6c757d) on value
   - **Style:** `style="color: #6c757d;"` inline on value

8. **Annual Dividends**
   - Value: Dollar amount (e.g., "$545.88")
   - Subvalue: "$/month"
   - Color: GREEN (#28a745) on value
   - **Style:** `style="color: #28a745;"` inline on value

**DO NOT INCLUDE:**
- ❌ "Total Investment" card (removed per user request)
- ❌ "Cost Basis" card (removed per user request)

**Grid Layout:**
- CSS: `grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));`
- Gap: 20px
- All cards have purple gradient background by default
- Value colors override with inline styles

---

## 3. DIVIDEND INCOME SECTION
Beautiful gradient showcase (teal/blue gradient)

**Summary Cards:**
- Total Annual Income ($/year)
- Monthly Income ($/month)
- Number of Dividend Payers
- Highest Yield Position

**Detailed Table for ALL dividend payers:**
Columns:
- Symbol & Name
- Shares
- Annual Dividend per Share
- Your Annual Income
- Yield on Cost %
- Current Yield %
- Notes (warnings for dividend risk)

Include:
- MO, VZ, STWD, ADC, XOM, VTIP, CALM
- Any other dividend-paying positions

---

## 4. ALL POSITIONS - THREE SECTIONS

### Section A: TOP 10 WINNERS (Green Gradient)
- Sorted by P&L % descending
- Green gradient background
- Show: Symbol, Current Price, Shares, Cost Basis, Current Value, P&L $, P&L %
- Action badge: HOLD / BUY MORE / TRIM
- Special tags: BACK TRADING, DIVIDEND, etc.

### Section B: MIDDLE PERFORMERS (Yellow Gradient)
- Positions with -15% to +10% P&L
- Yellow/amber gradient
- Same data columns as winners
- Action badge: HOLD / WATCH

### Section C: BOTTOM 10 LOSERS (Red Gradient)
- Sorted by P&L % ascending (worst first)
- Red gradient background
- Same data columns
- Action badge: SELL / HOLD / WATCH
- Highlight tax loss harvesting opportunities

---

## 5. PORTFOLIO CONCENTRATION CHART
- Visual bar chart showing top 10 positions by current value
- Show: Symbol, Current Value, Weight % of portfolio
- Color-coded bars
- Identify concentration risk (any position >15% = high risk)

---

## 6. STRATEGIC RECOMMENDATIONS (7 sections)

### 6.1 Immediate Opportunities
- Stocks to take profits on
- Stocks back trading after delisting
- Time-sensitive actions

### 6.2 Critical Gaps
- **NVIDIA exposure** - always check for AI/GPU exposure
- Missing sectors
- Missing asset classes

### 6.3 Exit Strategy - Software/SaaS Losers
- Identify all software positions losing >20%
- Calculate total recovery cash
- Show tax loss harvesting benefit

### 6.4 Exit Strategy - Microcap/Penny Stocks
- Positions under $500M market cap with losses
- High risk positions
- Calculate recovery cash

### 6.5 Consolidation Plan
- Current position count
- Target position count (15-18 ideal)
- How to redeploy recovered cash
- Buy list: NVIDIA, scale up TSM, etc.

### 6.6 Let Winners Run Philosophy
- List all positions up >20%
- Show % of portfolio each represents
- Only trim if >20% of portfolio OR fundamentals break
- Reference: "let winners run" strategy

### 6.7 Dividend Strategy Review
- Review all dividend payers
- Flag any with dividend cut risk (check coverage ratio)
- Show yield on cost vs current yield
- Total income projection

---

## 7. RISK ASSESSMENT (4 key areas)

### 7.1 Concentration Risk
- Analyze top 10 positions
- Flag if any single position >15%
- Show diversification score
- Visual risk bar (0-100%)

### 7.2 Sector Risk
- Missing critical sectors (AI, semiconductors, etc.)
- Over-concentrated sectors
- Sector rotation analysis
- Visual risk bar

### 7.3 Quality Risk
- Winner/loser ratio analysis
- Number of speculative positions
- Micro-cap exposure
- Quality holdings assessment
- Visual risk bar

### 7.4 Income Risk
- Dividend sustainability analysis
- Positions with dividend cut risk
- Total income stability
- Visual risk bar

Each risk section includes:
- Risk level: LOW / MODERATE / HIGH / CRITICAL
- Visual colored bar (green to red gradient)
- Specific concerns
- Mitigation recommendations

---

## 8. EXECUTION PLAN (Priority ordered)

### Immediate Actions (Today)
- Most urgent trades
- Time-sensitive opportunities

### This Week
- Secondary priority actions
- Research tasks

### Next 2 Weeks
- Longer-term moves
- Portfolio rebalancing

### Expected Outcomes
- New position count
- Expected P&L improvement
- Risk reduction
- Portfolio simplification benefits

---

## DESIGN SPECIFICATIONS

### Color Palette - LIGHT MODE (Default)
- **Primary:** Purple gradient (#667eea to #764ba2)
- **Background:** Light gradient (#f5f7fa to #c3cfe2)
- **Container:** White (#ffffff)
- **Text Primary:** Dark gray (#2d3748)
- **Text Secondary:** Medium gray (#718096)
- **Winners:** Green gradient (#28a745 to #20c997)
- **Losers:** Red gradient (#dc3545 to #c82333)
- **Warning:** Yellow/amber gradient (#ffc107 to #ff9800)
- **Dividend:** Teal/blue gradient (#11998e to #38ef7d)

### Color Palette - DARK MODE
- **Background:** Dark slate gradient (#0f172a to #1e293b)
- **Container:** Charcoal (#1e293b)
- **Cards:** Dark slate (#334155)
- **Text Primary:** Light gray (#e2e8f0, #f1f5f9)
- **Text Secondary:** Medium gray (#94a3b8, #cbd5e1)
- **Borders:** Slate (#475569)
- **Winners/Losers:** Same RED/GREEN preserved (#dc3545, #28a745)
- **Semi-transparent overlays:** rgba for PNL displays

### Typography
- **Font Family:** -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif
- **Headers:** Bold, large (2-2.5em)
- **Body:** Clean, readable (1em, line-height: 1.6)
- **Metrics:** Large, bold (2.5em for key numbers)
- **Subtext:** 0.85-0.95em

### Dark Mode Toggle
- **Location:** Top-right corner of header
- **Default State:** Light mode
- **Toggle Button:**
  - Light mode: "🌙 Dark Mode"
  - Dark mode: "☀️ Light Mode"
  - Background: rgba(255,255,255,0.2) with backdrop-filter
  - Border: 2px solid rgba(255,255,255,0.3)
  - Border-radius: 25px
  - Padding: 10px 20px
  - Hover effect: scale(1.05)
- **Persistence:** localStorage.setItem('darkMode', 'enabled/disabled')
- **Auto-load:** Check localStorage on page load

### Card Design
- Rounded corners (10-15px border-radius)
- Box shadows for depth
- Hover effects (scale, shadow increase)
- Responsive grid layout
- Padding: 20-30px

### Action Badges
- **BUY MORE:** Green background, white text
- **HOLD:** Blue background, white text
- **SELL:** Red background, white text
- **WATCH:** Orange background, white text
- **TRIM:** Yellow background, dark text

### Special Tags
- Small, rounded pills
- Examples: "BACK TRADING", "DIVIDEND", "PENNY STOCK", "MICROCAP"
- Color-coded by category

---

## DATA ANALYSIS GUIDELINES

### Position Analysis (for each stock)
Include:
1. Current price vs cost basis
2. P&L in $ and %
3. Number of shares
4. Current value
5. Weight % of portfolio
6. Sector/industry
7. Market cap category (mega/large/mid/small/micro)
8. Action recommendation with rationale

### Fundamental Factors to Consider
- Business quality and competitive moat
- Recent news/developments
- Sector trends and rotation
- Valuation (PE ratio, etc.)
- Growth prospects

### Technical Factors to Consider
- Price vs 52-week high/low
- If down >30%: mention oversold
- If up >50%: mention momentum
- Support/resistance levels

### Strategic Factors to Consider
- Portfolio fit and allocation
- Diversification impact
- Risk/reward profile
- Tax implications (loss harvesting)
- Opportunity cost vs alternatives

### Critical Recommendation Logic Rules

**THESE ARE MANDATORY - DO NOT DEVIATE:**

1. **Never suggest trimming winners** unless >20% of portfolio OR fundamentals deteriorating
   - Example: ASML at +101% but only 5.89% of portfolio = HOLD, let it run
   - Example: Position at +50% but 25% of portfolio = Consider trim for rebalancing

2. **Always check for NVIDIA exposure** - critical gap if missing
   - Portfolio without NVDA/GPU/AI direct exposure = CRITICAL recommendation to add

3. **BE CAREFUL with SELL recommendations:**
   - ❌ Do NOT recommend selling if stock has:
     * Recent FDA approval
     * Significant insider buying (CEO, directors buying >$500K)
     * Strong fundamentals despite temporary decline
   - ✅ DO recommend selling if:
     * Fundamentally broken (revenue declining, losing market share)
     * Down >35% AND no positive catalysts
     * Sector-wide collapse with no recovery signs
   - **Examples:**
     * BCDA: FDA approval + CEO buying heavily = HOLD/WATCH (not sell)
     * VRNS: Strong fundamentals + insider buying = WATCH (not sell)
     * ASAN: -51%, software collapse, no recovery = SELL

4. **Software/SaaS sector considerations:**
   - Identify macro headwinds affecting entire sector
   - Only recommend exit if both: (a) sector weakness AND (b) company-specific issues

5. **Always calculate tax loss harvesting** potential for losers
   - Show total recoverable cash from exits
   - Show total realized losses for tax benefits

6. **Always show dividend sustainability** for income positions
   - Flag dividend cut risks (payout ratio >100%, declining earnings)
   - Show yield on cost vs current yield

7. **Focus order:** Fundamentals > Catalysts > Technicals > Insiders
   - Fundamentals = business quality, revenue/earnings trends, competitive position
   - Catalysts = FDA approvals, earnings dates, product launches
   - Technicals = RSI, price trends, support/resistance
   - Insiders = only if exceptional (CEO buying, 70%+ ownership, major VC $1M+)

8. **Breaking News Banner Standards:**
   - ⚠️ ONLY include VERIFIED major developments:
     * Confirmed price movements >25% with clear reason
     * Confirmed corporate actions (dividend cuts, M&A)
     * Verified news events (FDA approvals, earnings surprises)
   - ❌ Do NOT include:
     * Data fetching errors (like "stock delisted" when it's just API error)
     * Speculation without verification
     * Minor movements <15%

9. **Position sizing philosophy:**
   - <5% of portfolio = small, can let run
   - 5-10% = medium, monitor
   - 10-20% = large, watch closely
   - >20% = oversized, consider trim regardless of performance

10. **Microcap & Penny Stock Rules:**
    - Market cap <$100M = high risk
    - Only recommend exit if: down >30% AND no clear catalyst
    - Exception: Recent FDA approval, major partnership, insider buying

---

## FILE NAMING CONVENTION

**Format:** `Portfolio_Analysis_Complete_[PositionCount]_Positions_[Date].html`

**Examples:**
- Portfolio_Analysis_Complete_28_Positions_Feb25.html
- Portfolio_Analysis_Complete_28_Positions_2026-02-25.html

---

## WHEN USER SAYS "ANALYZE MY PORTFOLIO"

### Step 1: Get Current Data (Priority Order)
1. **First, check:** PASTE_PORTFOLIO_HERE.txt (if recently updated)
2. **Then check:** My_Portfolio_Positions.csv
3. **Last resort:** Ask user to paste data (but avoid this - use the file instead!)

**Important:** NEVER ask user to paste in chat if file exists. Read from file automatically.

Verify all positions captured (should be 28 currently)

### Step 2: Calculate P&L
- Current Value = Quantity × Mark Price
- Cost Value = Quantity × Cost Basis Price
- P&L $ = Current Value - Cost Value
- P&L % = (P&L $ / Cost Value) × 100

### Step 3: Sort and Categorize
- Sort by P&L % descending
- Identify top 10 winners
- Identify middle performers
- Identify bottom 10 losers
- Calculate all totals

### Step 4: Dividend Analysis
- Identify all dividend payers
- Calculate annual income for each
- Calculate yield on cost
- Flag dividend risks

### Step 5: Generate HTML Report
- Use EXACT structure from this reference
- Follow design specifications
- Include all 8 major sections
- Save with proper filename

### Step 6: Provide Summary
- Give user key highlights
- Top 3 winners and losers
- Critical actions needed
- File location

---

## REFERENCE REPORT LOCATION

**C:\DOCS\Riverbed\Cursor\PERSO\Scan_market\Reports\Portfolio_Analysis_GOLD_STANDARD_TEMPLATE.html**

This is the OFFICIAL gold standard. Every future report MUST match this format exactly.

Also available as:
- **C:\DOCS\Riverbed\Cursor\PERSO\Scan_market\Reports\Portfolio_Analysis_Feb25_2026.html** (working copy)

**CRITICAL:** This template includes dark mode toggle and all approved specifications.

---

*This reference document ensures consistency across all future portfolio analyses.*

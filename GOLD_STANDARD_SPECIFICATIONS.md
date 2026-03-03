# 🏆 PORTFOLIO ANALYSIS REPORT - GOLD STANDARD SPECIFICATIONS

**Version:** 2.0
**Date Locked:** February 25, 2026
**Status:** OFFICIAL STANDARD - DO NOT MODIFY WITHOUT APPROVAL

---

## 📍 OFFICIAL TEMPLATE LOCATION

**Primary Reference:**
```
C:\DOCS\Riverbed\Cursor\PERSO\Scan_market\Reports\Portfolio_Analysis_GOLD_STANDARD_TEMPLATE.html
```

**Working Copy:**
```
C:\DOCS\Riverbed\Cursor\PERSO\Scan_market\Reports\Portfolio_Analysis_Feb25_2026.html
```

---

## 🎨 VISUAL DESIGN STANDARDS

### Color Palette - Light Mode (Default)

| Element | Color Code | Usage |
|---------|------------|-------|
| Primary Purple | #667eea to #764ba2 | Header gradient, primary actions |
| Background | #f5f7fa to #c3cfe2 | Page background gradient |
| Container | #ffffff | Main container, cards |
| Text Primary | #2d3748 | Headings, important text |
| Text Secondary | #718096 | Descriptions, labels |
| Success/Green | #28a745 | Positive P&L, winners |
| Error/Red | #dc3545 | Negative P&L, losers |
| Warning/Yellow | #ffc107 | Watch items |
| Dividend Green | #11998e to #38ef7d | Dividend section gradient |

### Color Palette - Dark Mode

| Element | Color Code | Usage |
|---------|------------|-------|
| Background | #0f172a to #1e293b | Page background gradient |
| Container | #1e293b | Main container |
| Cards | #334155 | Position cards, info cards |
| Borders | #475569 | Card borders, dividers |
| Text Primary | #f1f5f9 | Headings, important text |
| Text Secondary | #cbd5e1 | Descriptions, labels |
| Success/Green | #28a745 | Positive P&L (preserved) |
| Error/Red | #dc3545 | Negative P&L (preserved) |

### Typography Standards

```css
Font Family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif
Line Height: 1.6
Letter Spacing: Normal (1px for uppercase labels)

H1 (Main Title): 2.5em, Bold
H2 (Section Titles): 2em, Bold
H3 (Subsection): 1.8em, Bold
Body Text: 1em
Metric Values: 2em-2.5em, Bold
Labels: 0.8-0.9em, Uppercase
Subtext: 0.85-0.95em
```

---

## 📊 DASHBOARD SPECIFICATIONS

### 8 Mandatory Cards (In This Order)

1. **Total Positions**
   ```html
   <div class="metric-card">
       <div class="label">Total Positions</div>
       <div class="value">28</div>
       <div class="subvalue">Active Holdings</div>
   </div>
   ```

2. **Current Value**
   ```html
   <div class="metric-card">
       <div class="label">Current Value</div>
       <div class="value">$30,323.07</div>
       <div class="subvalue">Market Value</div>
   </div>
   ```

3. **Total P&L** (with color coding)
   ```html
   <div class="metric-card">
       <div class="label">Total P&L</div>
       <div class="value" style="color: #dc3545;">-$1,312.60</div>
       <div class="subvalue">Profit/Loss</div>
   </div>
   ```

4. **Return %** (with color coding)
   ```html
   <div class="metric-card">
       <div class="label">Return %</div>
       <div class="value" style="color: #dc3545;">-4.15%</div>
       <div class="subvalue">Portfolio Return</div>
   </div>
   ```

5. **Winners** (GREEN)
6. **Losers** (RED)
7. **Flat Positions** (GRAY)
8. **Annual Dividends** (GREEN)

**Color Rules:**
- Negative values: `style="color: #dc3545;"` (RED)
- Positive values: `style="color: #28a745;"` (GREEN)
- Neutral values: `style="color: #6c757d;"` (GRAY)

---

## 🌙 DARK MODE TOGGLE

### Implementation Requirements

**Button Location:** Top-right corner of header

**Button HTML:**
```html
<button class="dark-mode-toggle" onclick="toggleDarkMode()">
    🌙 Dark Mode
</button>
```

**Button Styles:**
```css
.dark-mode-toggle {
    position: absolute;
    top: 20px;
    right: 40px;
    background: rgba(255, 255, 255, 0.2);
    border: 2px solid rgba(255, 255, 255, 0.3);
    color: white;
    padding: 10px 20px;
    border-radius: 25px;
    cursor: pointer;
    font-size: 0.9em;
    font-weight: 600;
    transition: all 0.3s ease;
    backdrop-filter: blur(10px);
}

.dark-mode-toggle:hover {
    background: rgba(255, 255, 255, 0.3);
    transform: scale(1.05);
}
```

**JavaScript:**
```javascript
function toggleDarkMode() {
    const body = document.body;
    const button = document.querySelector('.dark-mode-toggle');

    body.classList.toggle('dark-mode');

    if (body.classList.contains('dark-mode')) {
        button.innerHTML = '☀️ Light Mode';
        localStorage.setItem('darkMode', 'enabled');
    } else {
        button.innerHTML = '🌙 Dark Mode';
        localStorage.setItem('darkMode', 'disabled');
    }
}

// Auto-load preference
document.addEventListener('DOMContentLoaded', function() {
    const darkMode = localStorage.getItem('darkMode');
    if (darkMode === 'enabled') {
        document.body.classList.add('dark-mode');
        document.querySelector('.dark-mode-toggle').innerHTML = '☀️ Light Mode';
    }
});
```

**Dark Mode Class:**
```css
body.dark-mode {
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    color: #e2e8f0;
}
```

---

## 📋 SECTION STRUCTURE (Mandatory Order)

1. **Header** (Purple gradient with dark mode toggle)
2. **Portfolio Summary Dashboard** (8 cards)
3. **Dividend Income Section** (Teal gradient, all 7+ payers)
4. **All Positions - Top 10 Winners** (Green gradient cards)
5. **All Positions - Middle Performers** (Yellow gradient cards)
6. **All Positions - Bottom 10 Losers** (Red gradient cards)
7. **Portfolio Concentration Chart** (Top 10 by value)
8. **7 Strategic Recommendations** (Numbered cards)
9. **4-Part Risk Assessment** (Risk cards with bars)
10. **Priority-Ordered Execution Plan** (Action checklist)
11. **Footer** (Disclaimers, timestamp)

---

## 💡 RECOMMENDATION LOGIC STANDARDS

### Core Principles

1. **"Let Winners Run" Philosophy**
   - Never trim positions <20% of portfolio unless fundamentals break
   - Examples: ASML +101% at 5.89% = HOLD
   - Only trim if >20% portfolio OR deteriorating business

2. **Careful SELL Recommendations**
   - ❌ Do NOT sell if: FDA approval, major insider buying, strong fundamentals
   - ✅ DO sell if: Fundamentally broken, down >35% with no catalysts
   - Always research before recommending exit

3. **Breaking News Banner Standards**
   - ⚠️ ONLY verified major events (>25% moves, confirmed news)
   - ❌ Never include API errors, speculation, minor moves

4. **Position Sizing Guidance**
   - <5% = Small, let run
   - 5-10% = Medium, monitor
   - 10-20% = Large, watch closely
   - >20% = Oversized, consider trim

5. **Analysis Priority Order**
   - Fundamentals (business quality) > Catalysts (FDA, earnings) > Technicals (RSI) > Insiders (only if exceptional)

---

## 🎯 BADGE SYSTEM

### Action Badges

```css
.badge.buy-more { background: #48bb78; color: white; }
.badge.hold { background: #4299e1; color: white; }
.badge.sell { background: #f56565; color: white; }
.badge.watch { background: #ed8936; color: white; }
.badge.trim { background: #ecc94b; color: #2d3748; }
```

### Special Tags

```css
.badge.dividend { background: #11998e; color: white; }
.badge.microcap { background: #805ad5; color: white; }
.badge.penny { background: #d53f8c; color: white; }
```

---

## 📐 LAYOUT SPECIFICATIONS

### Grid Systems

**Dashboard Grid:**
```css
.dashboard-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
}
```

**Position Cards Grid:**
```css
.positions-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 20px;
}
```

### Card Specifications

**Position Card:**
```css
.position-card {
    border: 2px solid #e2e8f0;
    border-radius: 12px;
    padding: 20px;
    background: white;
    transition: all 0.3s ease;
}

.position-card::before {
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    width: 5px;
    height: 100%;
    background: #667eea;
}

.position-card.winner::before {
    background: linear-gradient(180deg, #11998e 0%, #38ef7d 100%);
}

.position-card.loser::before {
    background: linear-gradient(180deg, #fa709a 0%, #fee140 100%);
}
```

---

## ⚙️ TECHNICAL REQUIREMENTS

### Browser Compatibility
- Chrome/Edge: Latest 2 versions
- Firefox: Latest 2 versions
- Safari: Latest 2 versions
- All modern browsers with CSS Grid support

### Responsive Breakpoints
- Desktop: >1200px
- Tablet: 768px - 1200px
- Mobile: <768px (cards stack vertically)

### Performance
- Page load: <2 seconds
- Smooth transitions: 0.3s ease
- Dark mode toggle: Instant switch

### Accessibility
- Color contrast ratio: WCAG AA compliant
- Keyboard navigation: Full support
- Screen reader: Semantic HTML

---

## 📄 FILE NAMING CONVENTION

**Generated Reports:**
```
Portfolio_Analysis_[Date]_[Optional_Descriptor].html

Examples:
- Portfolio_Analysis_Feb25_2026.html
- Portfolio_Analysis_2026-02-25.html
- Portfolio_Analysis_Feb25_2026_v2.html
```

**Gold Standard Template:**
```
Portfolio_Analysis_GOLD_STANDARD_TEMPLATE.html
```

---

## ✅ QUALITY CHECKLIST

Before deploying any report, verify:

- [ ] 8 dashboard cards present in correct order
- [ ] "Total Investment" card NOT included
- [ ] "Return %" card IS included
- [ ] RED/GREEN color coding on all P&L values
- [ ] Dark mode toggle functional in top-right
- [ ] All 28 positions analyzed (or total count verified)
- [ ] Dividend income section shows all payers
- [ ] Position cards have left border color bars
- [ ] Action badges on every position
- [ ] Recommendations follow logic standards
- [ ] Breaking News only if verified events
- [ ] Footer with timestamp and disclaimers
- [ ] localStorage persists dark mode choice

---

## 🔒 CHANGE CONTROL

### Who Can Modify

**Customer approval required for:**
- Section structure changes
- Color scheme modifications
- Dashboard card additions/removals
- Recommendation logic changes
- Typography changes

**Developer can modify:**
- Bug fixes
- Performance optimizations
- Browser compatibility fixes
- Code refactoring (no visual changes)

### Version Control

- Major changes: Increment version number
- Document all changes in this file
- Keep previous gold standard as backup
- Test thoroughly before deployment

---

## 📞 SUPPORT

For questions about this standard:
1. Review this specification document
2. Check REPORT_FORMAT_REFERENCE.md
3. Examine Portfolio_Analysis_GOLD_STANDARD_TEMPLATE.html
4. Contact system owner for approval of changes

---

**This specification is LOCKED and APPROVED.**
**Date:** February 25, 2026
**Status:** Production Standard
**Next Review:** As needed based on customer feedback

---

*Generated for customer portfolio analysis system - Maintain consistency across all reports*

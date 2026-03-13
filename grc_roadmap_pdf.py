#!/usr/bin/env python3
"""GRC Roadmap 2026 - PDF Generator using ReportLab with IBM Plex Mono."""

import os
from reportlab.lib.pagesizes import landscape
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ─── Page Setup ───
W, H = 960, 540  # 16:9 ratio in points
PAGE = (W, H)
MARGIN = 45
RIGHT_EDGE = W - MARGIN

# ─── Register Fonts ───
FONT_DIR = "ibm-plex-mono/IBM-Plex-Mono/fonts/complete/ttf"
pdfmetrics.registerFont(TTFont("IBMPlexMono", os.path.join(FONT_DIR, "IBMPlexMono-Regular.ttf")))
pdfmetrics.registerFont(TTFont("IBMPlexMono-Bold", os.path.join(FONT_DIR, "IBMPlexMono-Bold.ttf")))
pdfmetrics.registerFont(TTFont("IBMPlexMono-Medium", os.path.join(FONT_DIR, "IBMPlexMono-Medium.ttf")))
pdfmetrics.registerFont(TTFont("IBMPlexMono-Light", os.path.join(FONT_DIR, "IBMPlexMono-Light.ttf")))
pdfmetrics.registerFont(TTFont("IBMPlexMono-SemiBold", os.path.join(FONT_DIR, "IBMPlexMono-SemiBold.ttf")))

# ─── Colors ───
C = {
    "navy":       HexColor("#1E2761"),
    "iceBlue":    HexColor("#CADCFC"),
    "white":      HexColor("#FFFFFF"),
    "offWhite":   HexColor("#F7F8FA"),
    "warmWhite":  HexColor("#FAFAF8"),
    "teal":       HexColor("#0E7C86"),
    "tealLight":  HexColor("#E0F5F5"),
    "blue":       HexColor("#2B6CB0"),
    "blueLight":  HexColor("#EBF4FF"),
    "indigo":     HexColor("#4C51BF"),
    "indigoLight":HexColor("#EDEDFF"),
    "green":      HexColor("#276749"),
    "greenLight": HexColor("#E8F5E8"),
    "orange":     HexColor("#C05621"),
    "orangeLight":HexColor("#FFF3E0"),
    "red":        HexColor("#C53030"),
    "redLight":   HexColor("#FFEBEE"),
    "purple":     HexColor("#553C9A"),
    "purpleLight":HexColor("#F3E8FF"),
    "textDark":   HexColor("#1A1D23"),
    "textMed":    HexColor("#4A5568"),
    "textLight":  HexColor("#718096"),
    "gray100":    HexColor("#F7FAFC"),
    "gray200":    HexColor("#EDF2F7"),
    "gray300":    HexColor("#E2E8F0"),
    "gray400":    HexColor("#CBD5E0"),
    "gray700":    HexColor("#4A5568"),
    "gray800":    HexColor("#2D3748"),
}

# ─── Helpers ───
def rect(c, x, y, w, h, fill=None, stroke=None, stroke_width=0.5):
    """Draw rectangle. y is from TOP of page."""
    by = H - y - h
    if fill:
        c.setFillColor(fill)
    if stroke:
        c.setStrokeColor(stroke)
        c.setLineWidth(stroke_width)
    if fill and stroke:
        c.rect(x, by, w, h, fill=1, stroke=1)
    elif fill:
        c.rect(x, by, w, h, fill=1, stroke=0)
    elif stroke:
        c.rect(x, by, w, h, fill=0, stroke=1)

def text(c, x, y, txt, font="IBMPlexMono", size=10, color=None, align="left", max_width=None):
    """Draw text. y is from TOP of page."""
    if color:
        c.setFillColor(color)
    c.setFont(font, size)
    by = H - y - size
    if align == "center" and max_width:
        tw = c.stringWidth(txt, font, size)
        x = x + (max_width - tw) / 2
    elif align == "right" and max_width:
        tw = c.stringWidth(txt, font, size)
        x = x + max_width - tw
    c.drawString(x, by, txt)

def text_wrap(c, x, y, txt, font="IBMPlexMono", size=9, color=None, max_width=400, line_height=None):
    """Draw wrapped text. Returns the y position after the last line."""
    if color:
        c.setFillColor(color)
    c.setFont(font, size)
    if line_height is None:
        line_height = size * 1.5
    words = txt.split()
    lines = []
    current_line = ""
    for word in words:
        test = current_line + (" " if current_line else "") + word
        if c.stringWidth(test, font, size) <= max_width:
            current_line = test
        else:
            if current_line:
                lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    for i, line in enumerate(lines):
        by = H - (y + i * line_height) - size
        c.drawString(x, by, line)
    return y + len(lines) * line_height

def bullet(c, x, y, txt, font="IBMPlexMono", size=8.5, color=None, max_width=380, line_height=None):
    """Draw a bullet point with wrapped text."""
    if color:
        c.setFillColor(color)
    if line_height is None:
        line_height = size * 1.6
    c.setFont(font, size)
    # Draw bullet character
    by = H - y - size
    c.drawString(x, by, "\u2022")
    bullet_indent = 12
    return text_wrap(c, x + bullet_indent, y, txt, font, size, color, max_width - bullet_indent, line_height)

def hline(c, x, y, w, color=None, width=0.5):
    """Horizontal line. y from top."""
    if color:
        c.setStrokeColor(color)
    c.setLineWidth(width)
    by = H - y
    c.line(x, by, x + w, by)

def vline(c, x, y1, y2, color=None, width=0.8):
    """Vertical line. y from top."""
    if color:
        c.setStrokeColor(color)
    c.setLineWidth(width)
    c.line(x, H - y1, x, H - y2)

def add_footer(c, page_num):
    """Add footer to page."""
    hline(c, MARGIN, H - 42, W - 2 * MARGIN, color=C["gray300"], width=0.5)
    text(c, MARGIN, H - 35, "CONFIDENTIAL  |  GRC Program Modernization Roadmap 2026",
         font="IBMPlexMono", size=7, color=C["textLight"])
    if page_num:
        text(c, 0, H - 35, str(page_num),
             font="IBMPlexMono", size=7, color=C["textLight"], align="right", max_width=W - MARGIN)

def add_title(c, title, color=None):
    """Add slide title."""
    text(c, MARGIN + 5, 28, title,
         font="IBMPlexMono-Bold", size=22, color=color or C["textDark"])

def add_subtitle(c, subtitle):
    """Add subtitle under title."""
    text(c, MARGIN + 5, 55, subtitle,
         font="IBMPlexMono", size=10, color=C["textLight"])

def new_page(c, bg=None):
    """Start a new page with background."""
    c.showPage()
    if bg:
        rect(c, 0, 0, W, H, fill=bg)

def card(c, x, y, w, h, fill=None, accent_color=None, accent_top=True):
    """Draw a card with optional top accent bar."""
    if fill:
        rect(c, x, y, w, h, fill=fill)
    # Light border for definition
    rect(c, x, y, w, h, stroke=C["gray300"], stroke_width=0.3)
    if accent_color and accent_top:
        rect(c, x, y, w, 3, fill=accent_color)


# ═══════════════════════════════════════════════════════════
# BUILD PDF
# ═══════════════════════════════════════════════════════════
output_path = "/Users/jsn/Documents/GitHub/blog/GRC_Roadmap_2026.pdf"
c = canvas.Canvas(output_path, pagesize=PAGE)
c.setTitle("GRC Program Modernization Roadmap 2026")
c.setAuthor("Senior Director, GRC")

# ═══════════════════════════════════════════════════════════
# SLIDE 1: Title
# ═══════════════════════════════════════════════════════════
rect(c, 0, 0, W, H, fill=C["navy"])

# Top accent bar
rect(c, 0, 0, W, 5, fill=C["teal"])

# Left accent line
rect(c, MARGIN + 5, 120, 3, 180, fill=C["teal"])

# Overline
text(c, MARGIN + 20, 125, "STRATEGIC INITIATIVE  |  2026",
     font="IBMPlexMono", size=10, color=C["teal"])

# Main title
text(c, MARGIN + 20, 155, "GRC Program",
     font="IBMPlexMono-Bold", size=32, color=C["white"])
text(c, MARGIN + 20, 195, "Modernization Roadmap",
     font="IBMPlexMono-Bold", size=32, color=C["white"])

# Subtitle
text(c, MARGIN + 20, 245, "From Compliance Function to Strategic Business Enabler",
     font="IBMPlexMono", size=12, color=C["iceBlue"])

# Bottom info line
hline(c, MARGIN, 380, W - 2 * MARGIN, color=C["gray700"], width=0.5)
text(c, MARGIN, 392, "Prepared for the CISO  |  March 2026  |  CONFIDENTIAL",
     font="IBMPlexMono", size=9, color=C["textLight"])

# Right stats panel
rect(c, 700, 100, 210, 250, fill=HexColor("#0E7C8626"))
stats = [
    ("2026", "Transformation Year", 115),
    ("4", "Strategic Phases", 185),
    ("12", "Key Initiatives", 255),
]
for val, label, sy in stats:
    text(c, 700, sy, val, font="IBMPlexMono-Bold", size=26, color=C["white"], align="center", max_width=210)
    text(c, 700, sy + 32, label, font="IBMPlexMono", size=8, color=C["iceBlue"], align="center", max_width=210)


# ═══════════════════════════════════════════════════════════
# SLIDE 2: Agenda
# ═══════════════════════════════════════════════════════════
new_page(c, C["offWhite"])
add_title(c, "Agenda")
add_footer(c, 2)

items = [
    ("01", "Executive Summary", "Current state, vision, and strategic objectives"),
    ("02", "Organizational Structure", "Team roles, reporting lines, capability mapping"),
    ("03", "Critical Gaps Analysis", "GRC-Engineering disconnect, Customer Trust, maturity"),
    ("04", "Strategic Roadmap", "Q1-Q4 phased plan with milestones and deliverables"),
    ("05", "Customer Trust Transformation", "Revenue enablement, tooling, knowledge base"),
    ("06", "GRC-as-Code & Automation", "Policy-as-code, CI/CD integration, engineering partnership"),
    ("07", "Metrics & Value Framework", "KPIs, dashboards, business value measurement"),
    ("08", "Risks & Dependencies", "Implementation risks, resource needs, change management"),
    ("09", "Investment & ROI", "Resource requirements, expected returns, timeline"),
    ("10", "Next Steps & The Ask", "30-day action plan, CISO requests, success criteria"),
]

col_w = 400
row_h = 34
start_y = 80

for i, (num, title_txt, desc) in enumerate(items):
    col = i // 5
    row = i % 5
    x = MARGIN + col * (col_w + 20)
    y = start_y + row * (row_h + 6)

    # Card background
    card(c, x, y, col_w, row_h, fill=C["white"])

    # Number badge
    badge_color = C["blue"] if col == 0 else C["teal"]
    rect(c, x + 8, y + 5, 28, 24, fill=badge_color)
    text(c, x + 8, y + 9, num, font="IBMPlexMono-Bold", size=9, color=C["white"], align="center", max_width=28)

    # Title + description
    text(c, x + 45, y + 5, title_txt, font="IBMPlexMono-Bold", size=9, color=C["textDark"])
    text(c, x + 45, y + 19, desc, font="IBMPlexMono", size=7, color=C["textLight"])


# ═══════════════════════════════════════════════════════════
# SLIDE 3: Executive Summary
# ═══════════════════════════════════════════════════════════
new_page(c, C["white"])
add_title(c, "Executive Summary")
add_footer(c, 3)

card_w = 410
card_h = 290
card_y = 78

# Current State Card
lx = MARGIN
card(c, lx, card_y, card_w, card_h, fill=C["redLight"], accent_color=C["red"])
text(c, lx + 15, card_y + 14, "CURRENT STATE",
     font="IBMPlexMono-Bold", size=10, color=C["red"])

current_bullets = [
    "GRC operates as isolated compliance function with no engineering integration",
    "Manual, check-the-box audit processes with no automation or policy-as-code",
    "Customer Trust uses fragmented tooling (Onboard, Conveyor, Trust Center)",
    "No revenue impact tracking despite handling deal-blocking questionnaires",
    "No GRC team members understand product, tech stack, or SDLC",
    "TPRM and Internal Audit lack standardized baselines and KPIs",
    "No existing roadmap, strategy, or maturity model in place",
]
by = card_y + 38
for b in current_bullets:
    by = bullet(c, lx + 15, by, b, size=8, color=C["textMed"], max_width=card_w - 35)
    by += 2

# Target State Card
rx = MARGIN + card_w + 20
card(c, rx, card_y, card_w, card_h, fill=C["greenLight"], accent_color=C["green"])
text(c, rx + 15, card_y + 14, "TARGET STATE (END OF 2026)",
     font="IBMPlexMono-Bold", size=10, color=C["green"])

target_bullets = [
    "GRC embedded in engineering with policy-as-code in CI/CD pipelines",
    "Automated compliance evidence collection and continuous monitoring",
    "Unified Customer Trust platform with revenue-linked dashboards",
    "Standardized response library reducing questionnaire TAT by 60%",
    "Technical GRC expertise integrated into product and sprint planning",
    "Risk-quantified TPRM with automated vendor assessments and tiering",
    "Mature, metrics-driven program aligned to NIST CSF and ISO 27001",
]
by = card_y + 38
for b in target_bullets:
    by = bullet(c, rx + 15, by, b, size=8, color=C["textMed"], max_width=card_w - 35)
    by += 2

# Vision bar
vision_y = card_y + card_h + 12
rect(c, MARGIN, vision_y, W - 2 * MARGIN, 42, fill=C["blueLight"])
text(c, MARGIN + 15, vision_y + 8, "STRATEGIC VISION:",
     font="IBMPlexMono-Bold", size=9, color=C["blue"])
text_wrap(c, MARGIN + 155, vision_y + 8,
    "Transform GRC from a reactive cost center into a proactive, revenue-enabling, engineering-integrated strategic function.",
    font="IBMPlexMono", size=9, color=C["textDark"], max_width=W - 2 * MARGIN - 175)


# ═══════════════════════════════════════════════════════════
# SLIDE 4: Organizational Structure
# ═══════════════════════════════════════════════════════════
new_page(c, C["offWhite"])
add_title(c, "Organizational Structure & Team")
add_footer(c, 4)

def org_box(c, cx_center, y, name, role, color, w=150, h=42):
    """Draw an org chart box centered at cx_center."""
    x = cx_center - w / 2
    card(c, x, y, w, h, fill=C["white"], accent_color=color)
    text(c, x, y + 8, name, font="IBMPlexMono-Bold", size=8, color=C["textDark"], align="center", max_width=w)
    text(c, x, y + 22, role, font="IBMPlexMono", size=6.5, color=C["textLight"], align="center", max_width=w)

# CISO
ciso_cx = W / 2
org_box(c, ciso_cx, 72, "CISO", "Chief Information Security Officer", C["indigo"], w=170)

# Vertical line from CISO
vline(c, ciso_cx, 114, 130, color=C["gray400"])
# Horizontal span
hline(c, 140, 130, W - 280, color=C["gray400"], width=0.8)

# Three peer directors
peers = [
    (140, "Chelsea Main", "Security Engineering", C["gray400"]),
    (ciso_cx, "You (Sr. Dir. GRC)", "GRC Program Lead", C["teal"]),
    (W - 140, "Damian King", "Security Operations", C["gray400"]),
]
for px, name, role, color in peers:
    vline(c, px, 130, 140, color=C["gray400"])
    org_box(c, px, 140, name, role, color)

# Lines from GRC Director down
you_bottom = 182
vline(c, ciso_cx, you_bottom, 198, color=C["gray400"])
hline(c, 145, 198, W - 290, color=C["gray400"], width=0.8)

# Direct reports
dr_positions = [170, 340, 510, 680]
reports = [
    ("Steve Hammonds", "BC/DR"),
    ("Doug Matkins", "TPRM"),
    ("Janet De Lara", "Internal Audit"),
    ("Customer Trust", "Trust & Questionnaires"),
]
for (px, (name, role)) in zip(dr_positions, reports):
    vline(c, px, 198, 210, color=C["gray400"])
    org_box(c, px, 210, name, role, C["teal"], w=130, h=38)

# Customer Trust sub-team
ct_cx = 680
ct_bottom = 248
vline(c, ct_cx, ct_bottom, 262, color=C["gray400"])

ct_members = [
    (590, "Eni Smigielska"),
    (660, "Russ Johnson"),
    (730, "Marcin Lachowicz"),
    (800, "Amine Gherabi"),
]
hline(c, 590, 262, 210, color=C["gray400"], width=0.8)
for mx, name in ct_members:
    vline(c, mx, 262, 272, color=C["gray400"])
    bx = mx - 50
    rect(c, bx, 272, 100, 24, fill=C["white"])
    rect(c, bx, 272, 100, 24, stroke=C["gray300"], stroke_width=0.3)
    text(c, bx, 278, name, font="IBMPlexMono", size=6.5, color=C["textDark"], align="center", max_width=100)

# Governance sub-team (under area near Doug)
gov_cx = 250
vline(c, gov_cx, 248, 275, color=C["gray400"])
rect(c, gov_cx - 75, 275, 150, 38, fill=C["tealLight"])
rect(c, gov_cx - 75, 275, 150, 38, stroke=C["gray300"], stroke_width=0.3)
text(c, gov_cx - 75, 280, "Governance (Paolo DiRosa)",
     font="IBMPlexMono-Bold", size=7, color=C["teal"], align="center", max_width=150)
text(c, gov_cx - 75, 294, "Barbara A-O, Mateusz Toczek",
     font="IBMPlexMono", size=6, color=C["textLight"], align="center", max_width=150)

# Key observation bar
obs_y = 400
rect(c, MARGIN, obs_y, W - 2 * MARGIN, 38, fill=C["orangeLight"])
text(c, MARGIN + 12, obs_y + 8, "KEY OBSERVATION:",
     font="IBMPlexMono-Bold", size=8, color=C["orange"])
text_wrap(c, MARGIN + 145, obs_y + 8,
    "No technical/engineering expertise within GRC team. Customer Trust lacks a dedicated lead since Jodi's departure. Peer alignment with Security Engineering is critical.",
    font="IBMPlexMono", size=8, color=C["textMed"], max_width=W - 2 * MARGIN - 165, line_height=13)


# ═══════════════════════════════════════════════════════════
# SLIDE 5: Critical Gaps Analysis
# ═══════════════════════════════════════════════════════════
new_page(c, C["white"])
add_title(c, "Critical Gaps Analysis")
add_footer(c, 5)

gaps = [
    {
        "title": "GRC-Engineering\nDisconnect",
        "severity": "CRITICAL", "sevColor": C["red"], "bg": C["redLight"],
        "items": [
            "No GRC personnel understand product, tech stack, or SDLC",
            "Not invited to sprint planning or architecture reviews",
            "Manual audit processes, no automation or continuous monitoring",
            "No embedded GRC presence in engineering org",
            "Compliance is after-the-fact, not integrated",
        ],
        "impact": "Findings discovered late; engineering views GRC as blocker"
    },
    {
        "title": "Customer Trust\nFragmentation",
        "severity": "HIGH", "sevColor": C["orange"], "bg": C["orangeLight"],
        "items": [
            "3 fragmented tools: Onboard, Conveyor, Trust Center",
            "Work in Jira but no ROI or revenue tracking",
            "Deal numbers visible, no revenue impact metrics",
            "No standardized legal-approved answer library",
            "No dedicated lead after Jodi's departure",
        ],
        "impact": "Slower deal cycles, duplicated effort, no demonstrated value"
    },
    {
        "title": "Program Maturity\n& Operations",
        "severity": "HIGH", "sevColor": C["orange"], "bg": C["orangeLight"],
        "items": [
            "No roadmap, maturity model, or strategic plan existed",
            "TPRM/Audit lack baselines and performance KPIs",
            "BC/DR needs validation against current threats",
            "No risk quantification (e.g. FAIR) methodology",
            "Governance not integrated with risk/compliance",
        ],
        "impact": "Reactive posture; cannot prioritize investments"
    },
]

gap_w = 270
gap_h = 340
gap_y = 78

for i, g in enumerate(gaps):
    x = MARGIN + i * (gap_w + 12)
    card(c, x, gap_y, gap_w, gap_h, fill=g["bg"], accent_color=g["sevColor"])

    # Severity badge
    badge_w = 65
    rect(c, x + gap_w - badge_w - 8, gap_y + 10, badge_w, 18, fill=g["sevColor"])
    text(c, x + gap_w - badge_w - 8, gap_y + 13, g["severity"],
         font="IBMPlexMono-Bold", size=7, color=C["white"], align="center", max_width=badge_w)

    # Title
    lines = g["title"].split("\n")
    for j, line in enumerate(lines):
        text(c, x + 12, gap_y + 12 + j * 14, line,
             font="IBMPlexMono-Bold", size=9.5, color=C["textDark"])

    # Bullets
    by = gap_y + 50
    for item in g["items"]:
        by = bullet(c, x + 12, by, item, size=7.5, color=C["textMed"], max_width=gap_w - 28)
        by += 3

    # Impact box at bottom
    imp_y = gap_y + gap_h - 52
    rect(c, x + 8, imp_y, gap_w - 16, 44, fill=C["white"])
    rect(c, x + 8, imp_y, gap_w - 16, 44, stroke=C["gray300"], stroke_width=0.3)
    text(c, x + 16, imp_y + 6, "BUSINESS IMPACT",
         font="IBMPlexMono-Bold", size=6.5, color=g["sevColor"])
    text_wrap(c, x + 16, imp_y + 20, g["impact"],
         font="IBMPlexMono", size=7, color=C["textMed"], max_width=gap_w - 40)


# ═══════════════════════════════════════════════════════════
# SLIDE 6: Strategic Roadmap Overview
# ═══════════════════════════════════════════════════════════
new_page(c, C["white"])
add_title(c, "Strategic Roadmap Overview")
add_footer(c, 6)

# Timeline bar
phases = [
    ("Q1 2026", C["blue"]),
    ("Q2 2026", C["teal"]),
    ("Q3 2026", C["indigo"]),
    ("Q4 2026", C["green"]),
]
bar_y = 68
bar_w = 207
for i, (label, color) in enumerate(phases):
    bx = MARGIN + i * (bar_w + 5)
    rect(c, bx, bar_y, bar_w, 28, fill=color)
    text(c, bx, bar_y + 6, label,
         font="IBMPlexMono-Bold", size=10, color=C["white"], align="center", max_width=bar_w)

# Phase detail cards
details = [
    ("Phase 1: Foundation", "Assess & Baseline", C["blue"], C["blueLight"], [
        "GRC maturity assessment (NIST CSF)",
        "Map Customer Trust tools & workflows",
        "Document TPRM/audit/BC-DR processes",
        "Team capability & skill gap analysis",
        "Tech stack education for GRC team",
        "Define KPI framework and baselines",
    ]),
    ("Phase 2: Quick Wins", "Deliver Visible Value", C["teal"], C["tealLight"], [
        "Launch revenue-tracking dashboard",
        "Build questionnaire response library",
        "Embed GRC in engineering meetings",
        "TPRM vendor tiering & risk scoring",
        "Audit cadence + internal KPI reporting",
        "Deploy initial automated evidence collection",
    ]),
    ("Phase 3: Automation", "Scale Through Technology", C["indigo"], C["indigoLight"], [
        "Policy-as-code in CI/CD pipeline",
        "Automate compliance evidence gathering",
        "Consolidate Customer Trust tooling",
        "Launch continuous control monitoring",
        "Integrate risk quantification (FAIR)",
        "Build GRC-Engineering workflows",
    ]),
    ("Phase 4: Optimize", "Mature & Demonstrate Value", C["green"], C["greenLight"], [
        "Full GRC-as-Code maturity",
        "Executive value dashboards (risk+revenue)",
        "Proactive risk identification",
        "Advanced vendor risk automation",
        "Maturity re-assessment & 2027 planning",
        "Team certification program complete",
    ]),
]

d_w = 207
d_h = 310
d_y = 108

for i, (title_txt, sub, color, bg, items) in enumerate(details):
    x = MARGIN + i * (d_w + 5)
    card(c, x, d_y, d_w, d_h, fill=bg, accent_color=color)

    text(c, x + 10, d_y + 12, title_txt,
         font="IBMPlexMono-Bold", size=8.5, color=color)
    text(c, x + 10, d_y + 28, sub,
         font="IBMPlexMono", size=7, color=C["textLight"])

    by = d_y + 48
    for item in items:
        by = bullet(c, x + 10, by, item, size=7, color=C["textMed"], max_width=d_w - 25, line_height=11)
        by += 4


# ═══════════════════════════════════════════════════════════
# SLIDE 7: Customer Trust Transformation
# ═══════════════════════════════════════════════════════════
new_page(c, C["white"])
add_title(c, "Customer Trust Transformation")
add_subtitle(c, "Evolve from reactive questionnaire processing to proactive revenue enablement")
add_footer(c, 7)

cols = [
    ("Tooling Consolidation", C["blue"], C["blueLight"], [
        ("Current:", "Onboard, Conveyor, Trust Center - fragmented"),
        ("Target:", "Single pane of glass for all trust activities"),
        ("Action:", "Evaluate consolidation (Vanta, Drata, SafeBase)"),
        ("Action:", "Centralize artifacts in one customer portal"),
        ("Metric:", "Reduce tools from 3+ to 1-2 platforms"),
    ]),
    ("Revenue Dashboard", C["teal"], C["tealLight"], [
        ("Current:", "Deal numbers in Jira, no revenue impact"),
        ("Target:", "Real-time dashboard linking to deal value"),
        ("Action:", "Integrate Jira with CRM for attribution"),
        ("Action:", "Track TAT, SLA, deal-stage correlation"),
        ("Metric:", "Demonstrate revenue enablement value"),
    ]),
    ("Knowledge Base", C["indigo"], C["indigoLight"], [
        ("Current:", "Ad-hoc responses, no standard library"),
        ("Target:", "200+ legal-approved response library"),
        ("Action:", "Catalog top recurring questions"),
        ("Action:", "Implement AI-assisted completion"),
        ("Metric:", "60% reduction in turnaround time"),
    ]),
]

col_w = 270
col_h = 210
col_y = 80

for i, (title_txt, color, bg, items) in enumerate(cols):
    x = MARGIN + i * (col_w + 12)
    card(c, x, col_y, col_w, col_h, fill=bg, accent_color=color)
    text(c, x + 12, col_y + 12, title_txt,
         font="IBMPlexMono-Bold", size=10, color=color)

    iy = col_y + 35
    for label, desc in items:
        text(c, x + 12, iy, label, font="IBMPlexMono-Bold", size=7.5, color=color)
        lw = c.stringWidth(label + " ", "IBMPlexMono-Bold", 7.5)
        text_wrap(c, x + 12 + lw, iy, desc, font="IBMPlexMono", size=7.5, color=C["textMed"],
                  max_width=col_w - 28 - lw, line_height=12)
        iy += 30

# KPI bar
kpi_y = col_y + col_h + 18
rect(c, MARGIN, kpi_y, W - 2 * MARGIN, 80, fill=C["gray100"])
rect(c, MARGIN, kpi_y, W - 2 * MARGIN, 80, stroke=C["gray300"], stroke_width=0.3)

kpis = [
    ("60%", "TAT Reduction", C["teal"]),
    ("$TBD", "Revenue Enabled/Qtr", C["blue"]),
    ("95%", "SLA Compliance", C["indigo"]),
    ("1-2", "Consolidated Platforms", C["green"]),
    ("200+", "Standardized Responses", C["purple"]),
]
kpi_w = (W - 2 * MARGIN) / len(kpis)
for i, (val, label, color) in enumerate(kpis):
    kx = MARGIN + i * kpi_w
    text(c, kx, kpi_y + 10, val, font="IBMPlexMono-Bold", size=20, color=color, align="center", max_width=kpi_w)
    text(c, kx, kpi_y + 42, label, font="IBMPlexMono", size=7.5, color=C["textLight"], align="center", max_width=kpi_w)


# ═══════════════════════════════════════════════════════════
# SLIDE 8: GRC-as-Code & Engineering Integration
# ═══════════════════════════════════════════════════════════
new_page(c, C["offWhite"])
add_title(c, "GRC-as-Code & Engineering Integration")
add_footer(c, 8)

left_w = 420
right_x = MARGIN + left_w + 15
right_w = W - right_x - MARGIN

# LEFT: Pipeline card
card(c, MARGIN, 72, left_w, 195, fill=C["white"])
text(c, MARGIN + 12, 82, "Policy-as-Code in CI/CD Pipeline",
     font="IBMPlexMono-Bold", size=10, color=C["indigo"])

# Pipeline stages
stages = [
    ("Code Commit", C["gray700"]),
    ("Policy Check", C["indigo"]),
    ("Security Scan", C["blue"]),
    ("Evidence Log", C["teal"]),
    ("Deploy", C["green"]),
]
stage_w = 68
stage_h = 32
stage_y = 105
for i, (name, color) in enumerate(stages):
    sx = MARGIN + 15 + i * (stage_w + 12)
    rect(c, sx, stage_y, stage_w, stage_h, fill=color)
    text(c, sx, stage_y + 8, name, font="IBMPlexMono-Bold", size=6.5, color=C["white"],
         align="center", max_width=stage_w)
    if i < len(stages) - 1:
        text(c, sx + stage_w + 1, stage_y + 8, "\u25B6",
             font="IBMPlexMono", size=8, color=C["gray400"])

strat_bullets = [
    "Partner with Chelsea Main (Security Eng) on pipeline integration",
    "Implement OPA with Rego policies for automated compliance",
    "Auto-generate evidence from CI/CD execution logs",
    "GRC-friendly dashboards from engineering telemetry",
]
by = 152
for b in strat_bullets:
    by = bullet(c, MARGIN + 15, by, b, size=7.5, color=C["textMed"], max_width=left_w - 35, line_height=12)
    by += 3

# RIGHT: Engineering Integration Phases
card(c, right_x, 72, right_w, 195, fill=C["white"])
text(c, right_x + 12, 82, "Engineering Integration Phases",
     font="IBMPlexMono-Bold", size=10, color=C["blue"])

int_phases = [
    ("Phase 1: Learn", C["blue"], [
        "Tech stack education (architecture, languages, cloud)",
        "Shadow standups and sprint planning",
        "Map compliance to engineering workflows",
    ]),
    ("Phase 2: Embed", C["teal"], [
        "GRC liaison in architecture reviews",
        "Bi-weekly GRC-Engineering working group",
        "Shared Slack channels and documentation",
    ]),
    ("Phase 3: Automate", C["indigo"], [
        "Policy-as-code in CI/CD pipelines",
        "Automated evidence replaces manual audits",
        "Self-service compliance for engineering",
    ]),
]

py = 102
for title_txt, color, items in int_phases:
    rect(c, right_x + 12, py, 3, 48, fill=color)
    text(c, right_x + 22, py + 2, title_txt,
         font="IBMPlexMono-Bold", size=8, color=color)
    iy = py + 16
    for item in items:
        text(c, right_x + 22, iy, "\u2022 " + item,
             font="IBMPlexMono", size=7, color=C["textMed"])
        iy += 11
    py += 55

# Bottom: Best practices bar
bp_y = 282
rect(c, MARGIN, bp_y, W - 2 * MARGIN, 130, fill=C["blueLight"])
rect(c, MARGIN, bp_y, W - 2 * MARGIN, 130, stroke=C["gray300"], stroke_width=0.3)
text(c, MARGIN + 12, bp_y + 10, "INDUSTRY BEST PRACTICES - GRC AUTOMATION",
     font="IBMPlexMono-Bold", size=9, color=C["blue"])

bps = [
    ("Shift-Left Compliance:", "Integrate checks early in SDLC, not at deployment gate"),
    ("Continuous Compliance:", "Replace point-in-time audits with real-time monitoring (NIST SP 800-137)"),
    ("Evidence-as-Code:", "Generate audit evidence from infrastructure-as-code and CI/CD logs"),
    ("Risk-Based Prioritization:", "Use FAIR or similar quantitative models to prioritize by business impact"),
]
by = bp_y + 32
for label, desc in bps:
    text(c, MARGIN + 12, by, label, font="IBMPlexMono-Bold", size=8, color=C["indigo"])
    lw = c.stringWidth(label + " ", "IBMPlexMono-Bold", 8)
    text_wrap(c, MARGIN + 12 + lw, by, desc, font="IBMPlexMono", size=8, color=C["textMed"],
              max_width=W - 2 * MARGIN - 35 - lw, line_height=12)
    by += 24


# ═══════════════════════════════════════════════════════════
# SLIDE 9: Metrics & Value Framework
# ═══════════════════════════════════════════════════════════
new_page(c, C["white"])
add_title(c, "Metrics & Value Framework")
add_footer(c, 9)

categories = [
    ("Revenue & Business Value", "$", C["teal"], C["tealLight"], [
        ("Revenue Enabled", "Deal value for completed questionnaires/quarter"),
        ("Questionnaire TAT", "Avg turnaround time (target: <5 business days)"),
        ("Deal Acceleration", "Reduction in sales cycle days"),
        ("Cost Avoidance", "Estimated regulatory fines/breaches avoided"),
    ]),
    ("Operational Excellence", "O", C["blue"], C["blueLight"], [
        ("Automation Rate", "% evidence collected automatically vs. manually"),
        ("Audit Readiness", "Time to produce full evidence package"),
        ("TPRM Coverage", "% of vendors assessed within risk framework"),
        ("Control Effectiveness", "% controls passing continuous monitoring"),
    ]),
    ("Risk & Maturity", "R", C["indigo"], C["indigoLight"], [
        ("Program Maturity", "NIST CSF maturity score (target: Tier 3)"),
        ("Risk Posture", "Quantified risk trend (FAIR methodology)"),
        ("Finding Closure", "Mean time to remediate findings"),
        ("Policy Currency", "% policies reviewed within cycle"),
    ]),
]

cat_w = 270
cat_h = 300
cat_y = 70

for i, (title_txt, icon, color, bg, metrics) in enumerate(categories):
    x = MARGIN + i * (cat_w + 12)
    card(c, x, cat_y, cat_w, cat_h, fill=bg, accent_color=color)

    # Icon circle
    c.setFillColor(color)
    c.circle(x + 22, H - (cat_y + 22), 12, fill=1, stroke=0)
    text(c, x + 16, cat_y + 13, icon, font="IBMPlexMono-Bold", size=11, color=C["white"],
         align="center", max_width=12)

    text(c, x + 42, cat_y + 15, title_txt,
         font="IBMPlexMono-Bold", size=10, color=color)

    my = cat_y + 45
    for name, desc in metrics:
        text(c, x + 12, my, name, font="IBMPlexMono-Bold", size=8.5, color=C["textDark"])
        text_wrap(c, x + 12, my + 14, desc, font="IBMPlexMono", size=7, color=C["textLight"],
                  max_width=cat_w - 28, line_height=11)
        my += 55

# Dashboard callout
dash_y = cat_y + cat_h + 10
rect(c, MARGIN, dash_y, W - 2 * MARGIN, 36, fill=C["gray100"])
text(c, MARGIN + 12, dash_y + 10, "DASHBOARD DELIVERY:",
     font="IBMPlexMono-Bold", size=8, color=C["blue"])
text(c, MARGIN + 162, dash_y + 10,
     "Executive dashboard (monthly CISO)  |  Operational dashboard (daily)  |  Customer Trust revenue dashboard",
     font="IBMPlexMono", size=8, color=C["textMed"])


# ═══════════════════════════════════════════════════════════
# SLIDE 10: Risks & Dependencies
# ═══════════════════════════════════════════════════════════
new_page(c, C["offWhite"])
add_title(c, "Risks, Dependencies & Change Management")
add_footer(c, 10)

# Risk table
risks = [
    ("R1", "Engineering resistance to GRC integration", "Med", "High", "Start with value-add automation, not mandates. CISO sponsorship."),
    ("R2", "Insufficient budget for platform/tooling", "Med", "High", "ROI business case from revenue data. Phase investments."),
    ("R3", "Team skill gaps delay GRC-as-Code", "High", "Med", "Partner with Security Eng. External training. Targeted hires."),
    ("R4", "Customer Trust capacity during transformation", "Med", "Med", "Protect BAU capacity. Automate low-value tasks first."),
    ("R5", "Nathan's return creates role ambiguity", "Low", "High", "Document decisions, maintain CISO transparency."),
    ("R6", "Tool consolidation disrupts Customer Trust SLAs", "Med", "Med", "Parallel run during migration. Phased rollout."),
]

# Table header
table_x = MARGIN
table_y = 72
col_widths = [35, 230, 65, 65, 390]
row_h = 30
header_h = 24

# Header
hx = table_x
rect(c, table_x, table_y, sum(col_widths), header_h, fill=C["gray800"])
headers = ["ID", "RISK DESCRIPTION", "LIKELIHOOD", "IMPACT", "MITIGATION STRATEGY"]
for j, (header, cw) in enumerate(zip(headers, col_widths)):
    text(c, hx, table_y + 6, header, font="IBMPlexMono-Bold", size=7, color=C["white"],
         align="center", max_width=cw)
    hx += cw

# Rows
for i, (rid, desc, like, imp, mitigation) in enumerate(risks):
    ry = table_y + header_h + i * row_h
    row_fill = C["white"] if i % 2 == 0 else C["gray100"]
    rect(c, table_x, ry, sum(col_widths), row_h, fill=row_fill)
    rect(c, table_x, ry, sum(col_widths), row_h, stroke=C["gray300"], stroke_width=0.3)

    like_color = C["red"] if like == "High" else (C["orange"] if like == "Med" else C["green"])
    imp_color = C["red"] if imp == "High" else (C["orange"] if imp == "Med" else C["green"])

    cx = table_x
    text(c, cx, ry + 8, rid, font="IBMPlexMono-Bold", size=7.5, color=C["red"], align="center", max_width=col_widths[0])
    cx += col_widths[0]
    text_wrap(c, cx + 6, ry + 5, desc, font="IBMPlexMono", size=7.5, color=C["textMed"],
              max_width=col_widths[1] - 12, line_height=11)
    cx += col_widths[1]
    text(c, cx, ry + 8, like, font="IBMPlexMono-Bold", size=7.5, color=like_color, align="center", max_width=col_widths[2])
    cx += col_widths[2]
    text(c, cx, ry + 8, imp, font="IBMPlexMono-Bold", size=7.5, color=imp_color, align="center", max_width=col_widths[3])
    cx += col_widths[3]
    text_wrap(c, cx + 6, ry + 5, mitigation, font="IBMPlexMono", size=7.5, color=C["textMed"],
              max_width=col_widths[4] - 12, line_height=11)

# Dependencies section
dep_y = table_y + header_h + len(risks) * row_h + 18
text(c, MARGIN, dep_y, "Key Dependencies",
     font="IBMPlexMono-Bold", size=11, color=C["textDark"])

deps = [
    "CISO sponsorship and executive air cover for cross-functional initiatives",
    "Security Engineering (Chelsea Main) partnership for CI/CD and tooling integration",
    "Budget approval for GRC platform investment and team training",
    "CRM access (Salesforce/HubSpot) for Customer Trust revenue attribution",
]
by = dep_y + 20
for d in deps:
    by = bullet(c, MARGIN + 8, by, d, size=8, color=C["textMed"], max_width=W - 2 * MARGIN - 20, line_height=13)
    by += 3


# ═══════════════════════════════════════════════════════════
# SLIDE 11: Investment & ROI
# ═══════════════════════════════════════════════════════════
new_page(c, C["white"])
add_title(c, "Investment Requirements & Expected ROI")
add_footer(c, 11)

left_w = 420
right_x = MARGIN + left_w + 15
right_w = W - right_x - MARGIN
card_y = 70
card_h = 280

# LEFT: Investment areas
card(c, MARGIN, card_y, left_w, card_h, fill=C["white"], accent_color=C["blue"])
text(c, MARGIN + 15, card_y + 12, "Investment Areas",
     font="IBMPlexMono-Bold", size=11, color=C["blue"])

investments = [
    ("GRC Platform & Tooling", [
        "Customer Trust platform consolidation/upgrade",
        "GRC automation platform (policy-as-code)",
        "Dashboard and reporting infrastructure",
        "TPRM automation and vendor risk platform",
    ]),
    ("People & Skills", [
        "GRC-Engineering technical training program",
        "Technical GRC Engineer hire (policy-as-code)",
        "Customer Trust team lead recruitment",
        "Industry certifications (CISA, CRISC, CISSP)",
    ]),
    ("Process & Consulting", [
        "NIST CSF maturity assessment (external)",
        "FAIR risk quantification implementation",
        "Change management for engineering integration",
    ]),
]

iy = card_y + 35
for cat_name, items in investments:
    text(c, MARGIN + 15, iy, cat_name,
         font="IBMPlexMono-Bold", size=8.5, color=C["textDark"])
    iy += 16
    for item in items:
        iy = bullet(c, MARGIN + 20, iy, item, size=7.5, color=C["textMed"],
                    max_width=left_w - 50, line_height=11)
        iy += 1
    iy += 8

# RIGHT: ROI
card(c, right_x, card_y, right_w, card_h, fill=C["greenLight"], accent_color=C["green"])
text(c, right_x + 15, card_y + 12, "Expected Return on Investment",
     font="IBMPlexMono-Bold", size=11, color=C["green"])

rois = [
    ("Revenue Enablement", "Faster questionnaire completion accelerates deal closure.", C["teal"]),
    ("Cost Avoidance", "Automated compliance reduces audit prep costs 40-60%.", C["blue"]),
    ("Risk Reduction", "Quantified risk posture improvement. Proactive identification.", C["indigo"]),
    ("Operational Efficiency", "GRC-as-Code eliminates 60%+ manual tasks.", C["green"]),
    ("Competitive Advantage", "Strong trust posture as sales differentiator.", C["purple"]),
]

ry = card_y + 38
for title_txt, desc, color in rois:
    rect(c, right_x + 15, ry, 3, 36, fill=color)
    text(c, right_x + 25, ry + 3, title_txt,
         font="IBMPlexMono-Bold", size=8, color=color)
    text_wrap(c, right_x + 25, ry + 17, desc,
         font="IBMPlexMono", size=7.5, color=C["textMed"], max_width=right_w - 50, line_height=11)
    ry += 44

# Timeline bar at bottom
tl_y = card_y + card_h + 12
rect(c, MARGIN, tl_y, W - 2 * MARGIN, 55, fill=C["blueLight"])
text(c, MARGIN + 12, tl_y + 6, "VALUE DELIVERY TIMELINE",
     font="IBMPlexMono-Bold", size=9, color=C["blue"])

milestones = [
    ("30 Days:", "Gap assessment, baseline KPIs"),
    ("90 Days:", "Revenue dashboard, response library v1, engineering embeds"),
    ("180 Days:", "Automation POC in CI/CD, TPRM tiering, TAT improvement"),
    ("365 Days:", "Full GRC-as-Code, executive dashboards, maturity improvement"),
]
by = tl_y + 24
# Two milestones per row
for i, (label, desc) in enumerate(milestones):
    col = i % 2
    row = i // 2
    mx = MARGIN + 12 + col * 430
    my = by + row * 13
    text(c, mx, my, label, font="IBMPlexMono-Bold", size=7.5, color=C["indigo"])
    lw = c.stringWidth(label + " ", "IBMPlexMono-Bold", 7.5)
    text(c, mx + lw, my, desc, font="IBMPlexMono", size=7.5, color=C["textMed"])


# ═══════════════════════════════════════════════════════════
# SLIDE 12: Next Steps & The Ask
# ═══════════════════════════════════════════════════════════
new_page(c, C["white"])
rect(c, 0, 0, W, 4, fill=C["teal"])
add_title(c, "Immediate Next Steps & The Ask")
add_footer(c, 12)

left_w = 465
right_x = MARGIN + left_w + 15
right_w = W - right_x - MARGIN

# LEFT: 30-Day Action Plan
card(c, MARGIN, 68, left_w, 350, fill=C["white"], accent_color=C["blue"])
text(c, MARGIN + 15, 78, "30-Day Action Plan",
     font="IBMPlexMono-Bold", size=11, color=C["blue"])

steps = [
    ("Week 1-2: Stakeholder Alignment", [
        "1:1 meetings with all direct reports",
        "Alignment with Chelsea Main and Damian King",
        "Customer Trust team assessment + interim lead plan",
        "Review all existing documentation and artifacts",
    ]),
    ("Week 2-3: Assessment & Baseline", [
        "GRC maturity assessment (NIST CSF)",
        "Map Customer Trust workflows and tools",
        "Document TPRM, audit, BC/DR processes",
        "Identify compliance obligations and certifications",
    ]),
    ("Week 3-4: Quick Win Launch", [
        "Initiate revenue tracking dashboard development",
        "Begin response library (top 50 questions)",
        "Schedule first GRC-Engineering touchpoints",
        "Present initial findings to CISO",
    ]),
]

sy = 100
for week_title, items in steps:
    text(c, MARGIN + 15, sy, week_title,
         font="IBMPlexMono-Bold", size=8.5, color=C["textDark"])
    sy += 16
    for item in items:
        sy = bullet(c, MARGIN + 20, sy, item, size=7.5, color=C["textMed"],
                    max_width=left_w - 50, line_height=11)
        sy += 1
    sy += 8

# RIGHT TOP: The Ask
card(c, right_x, 68, right_w, 165, fill=C["blueLight"], accent_color=C["indigo"])
text(c, right_x + 15, 78, "The Ask from CISO",
     font="IBMPlexMono-Bold", size=11, color=C["indigo"])

asks = [
    "Endorse this roadmap as official 2026 GRC strategic plan",
    "Executive sponsorship for Engineering integration",
    "Approve budget for platform evaluation and training",
    "Support hiring: Technical GRC Engineer + Trust lead",
    "Facilitate intros to product/engineering leadership",
    "Monthly roadmap review cadence (30-min)",
]
ay = 100
for a in asks:
    ay = bullet(c, right_x + 15, ay, a, size=8, color=C["textMed"],
                max_width=right_w - 35, line_height=12)
    ay += 2

# RIGHT BOTTOM: Success Criteria
card(c, right_x, 248, right_w, 170, fill=C["greenLight"], accent_color=C["green"])
text(c, right_x + 15, 258, "Success Criteria (12 Months)",
     font="IBMPlexMono-Bold", size=10, color=C["green"])

criteria = [
    "GRC maturity improvement (baseline to Tier 3)",
    "Customer Trust TAT reduced by 60%",
    "Revenue attribution dashboard operational",
    "Policy-as-code in at least one CI/CD pipeline",
    "100% critical vendors assessed in TPRM framework",
]
cy = 280
for cr in criteria:
    cy = bullet(c, right_x + 15, cy, cr, size=8, color=C["textMed"],
                max_width=right_w - 35, line_height=12)
    cy += 2


# ═══════════════════════════════════════════════════════════
# SLIDE 13: Appendix - Best Practices & Frameworks
# ═══════════════════════════════════════════════════════════
new_page(c, C["offWhite"])
add_title(c, "Appendix: Best Practices & Frameworks")
add_footer(c, 13)

cards_data = [
    ("Framework Alignment", C["blue"], C["blueLight"], [
        "NIST CSF 2.0 - Primary maturity model and governance backbone",
        "ISO 27001:2022 - ISMS alignment for certification",
        "SOC 2 Type II - Automated evidence collection",
        "NIST SP 800-53 Rev. 5 - Comprehensive control catalog",
        "FAIR - Quantitative risk analysis methodology",
    ]),
    ("GRC Technology Trends", C["teal"], C["tealLight"], [
        "GRC-as-Code: OPA, Rego, Terraform Sentinel, AWS Config",
        "Continuous Compliance: Real-time monitoring",
        "AI-Assisted Trust: LLM-powered questionnaire completion",
        "Unified Platforms: Converged risk/compliance/audit",
        "Trust Centers: Self-service security transparency",
    ]),
    ("Organizational Best Practices", C["indigo"], C["indigoLight"], [
        "Shift-Left: Embed compliance in SDLC",
        "Three Lines Model (IIA): Clear governance delineation",
        "Risk-Based: Prioritize high-impact controls",
        "Value-Driven: Measure business outcomes, not checklists",
        "Cross-Functional: GRC as partner to Eng/Product/Sales",
    ]),
    ("Reference Standards", C["green"], C["greenLight"], [
        "NIST SP 800-137: Continuous Monitoring (ISCM)",
        "ISACA COBIT 2019: Enterprise IT governance",
        "IIA Three Lines Model: Risk governance guidance",
        "CISA Cybersecurity Performance Goals",
        "CSA CCM: Cloud-specific control mapping",
    ]),
]

cw = 410
ch = 155
start_y = 65

for i, (title_txt, color, bg, items) in enumerate(cards_data):
    col = i % 2
    row = i // 2
    x = MARGIN + col * (cw + 20)
    y = start_y + row * (ch + 12)

    card(c, x, y, cw, ch, fill=bg, accent_color=color)
    text(c, x + 12, y + 12, title_txt,
         font="IBMPlexMono-Bold", size=9.5, color=color)

    by = y + 32
    for item in items:
        by = bullet(c, x + 12, by, item, size=7.5, color=C["textMed"],
                    max_width=cw - 30, line_height=12)
        by += 2


# ═══════════════════════════════════════════════════════════
# SAVE
# ═══════════════════════════════════════════════════════════
c.save()
print(f"PDF saved: {output_path}")

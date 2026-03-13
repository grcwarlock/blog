#!/usr/bin/env python3
"""
GRC Program Modernization Roadmap 2026
Professional PDF Presentation
"""

from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white, black
from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os
import math

# ─── Color Palette ───────────────────────────────────────────────
COLORS = {
    'bg_white':       HexColor('#FFFFFF'),
    'bg_light':       HexColor('#F7F8FA'),
    'bg_warm':        HexColor('#FAFAF8'),
    'text_primary':   HexColor('#1A1D23'),
    'text_secondary': HexColor('#4A5568'),
    'text_muted':     HexColor('#718096'),
    'accent_blue':    HexColor('#2B6CB0'),
    'accent_teal':    HexColor('#2C7A7B'),
    'accent_indigo':  HexColor('#4C51BF'),
    'accent_light':   HexColor('#EBF4FF'),
    'accent_teal_lt': HexColor('#E6FFFA'),
    'accent_warm':    HexColor('#FFFAF0'),
    'border_light':   HexColor('#E2E8F0'),
    'border_med':     HexColor('#CBD5E0'),
    'green':          HexColor('#276749'),
    'green_light':    HexColor('#F0FFF4'),
    'orange':         HexColor('#C05621'),
    'orange_light':   HexColor('#FFFAF0'),
    'purple':         HexColor('#553C9A'),
    'purple_light':   HexColor('#FAF5FF'),
    'red':            HexColor('#C53030'),
    'red_light':      HexColor('#FFF5F5'),
    'gray_100':       HexColor('#F7FAFC'),
    'gray_200':       HexColor('#EDF2F7'),
    'gray_300':       HexColor('#E2E8F0'),
    'gray_400':       HexColor('#CBD5E0'),
    'gray_500':       HexColor('#A0AEC0'),
    'gray_600':       HexColor('#718096'),
    'gray_700':       HexColor('#4A5568'),
    'gray_800':       HexColor('#2D3748'),
}

WIDTH, HEIGHT = landscape(letter)
MARGIN = 0.75 * inch


class SlideBuilder:
    def __init__(self, filename):
        self.c = canvas.Canvas(filename, pagesize=landscape(letter))
        self.c.setTitle("GRC Program Modernization Roadmap 2026")
        self.c.setAuthor("Senior Director, GRC")
        self.c.setSubject("Strategic GRC Roadmap & Transformation Plan")
        self.page_num = 0

    def _new_slide(self, bg_color=None):
        if self.page_num > 0:
            self.c.showPage()
        self.page_num += 1
        bg = bg_color or COLORS['bg_white']
        self.c.setFillColor(bg)
        self.c.rect(0, 0, WIDTH, HEIGHT, fill=1, stroke=0)

    def _draw_footer(self, show_page=True):
        """Minimal footer with thin accent line"""
        y = 0.4 * inch
        self.c.setStrokeColor(COLORS['gray_300'])
        self.c.setLineWidth(0.5)
        self.c.line(MARGIN, y + 8, WIDTH - MARGIN, y + 8)
        self.c.setFont("Helvetica", 7)
        self.c.setFillColor(COLORS['text_muted'])
        self.c.drawString(MARGIN, y - 4, "CONFIDENTIAL  |  GRC Program Modernization Roadmap 2026")
        if show_page:
            self.c.drawRightString(WIDTH - MARGIN, y - 4, f"{self.page_num}")

    def _draw_accent_bar(self, x, y, w, h, color):
        self.c.setFillColor(color)
        self.c.roundRect(x, y, w, h, 2, fill=1, stroke=0)

    def _draw_card(self, x, y, w, h, fill=None, border=None, radius=6):
        if fill:
            self.c.setFillColor(fill)
        if border:
            self.c.setStrokeColor(border)
            self.c.setLineWidth(0.5)
            self.c.roundRect(x, y, w, h, radius, fill=1 if fill else 0, stroke=1 if border else 0)
        elif fill:
            self.c.roundRect(x, y, w, h, radius, fill=1, stroke=0)

    def _draw_text_block(self, text, x, y, font="Helvetica", size=10, color=None, max_width=None, leading=None):
        """Draw text with optional word wrapping. Returns final y position."""
        color = color or COLORS['text_primary']
        leading = leading or size * 1.45
        self.c.setFont(font, size)
        self.c.setFillColor(color)

        if max_width is None:
            self.c.drawString(x, y, text)
            return y - leading

        words = text.split()
        lines = []
        current_line = ""
        for word in words:
            test = f"{current_line} {word}".strip()
            if pdfmetrics.stringWidth(test, font, size) <= max_width:
                current_line = test
            else:
                if current_line:
                    lines.append(current_line)
                current_line = word
        if current_line:
            lines.append(current_line)

        for line in lines:
            self.c.drawString(x, y, line)
            y -= leading
        return y

    def _draw_bullet(self, text, x, y, font="Helvetica", size=9.5, color=None, max_width=None, bullet_color=None, leading=None):
        color = color or COLORS['text_secondary']
        bullet_color = bullet_color or COLORS['accent_teal']
        leading = leading or size * 1.55

        # Draw bullet dot
        self.c.setFillColor(bullet_color)
        self.c.circle(x + 3, y + 3, 2.5, fill=1, stroke=0)

        # Draw text
        return self._draw_text_block(text, x + 14, y, font, size, color, max_width, leading)

    # ─── SLIDE 1: Title ──────────────────────────────────────────
    def slide_title(self):
        self._new_slide(COLORS['bg_white'])

        # Subtle top accent line
        self.c.setFillColor(COLORS['accent_blue'])
        self.c.rect(0, HEIGHT - 4, WIDTH, 4, fill=1, stroke=0)

        # Left accent bar
        self.c.setFillColor(COLORS['accent_teal'])
        self.c.rect(MARGIN - 0.15 * inch, HEIGHT * 0.38, 3, 1.6 * inch, fill=1, stroke=0)

        # Title
        y = HEIGHT * 0.62
        self.c.setFont("Helvetica", 12)
        self.c.setFillColor(COLORS['accent_teal'])
        self.c.drawString(MARGIN + 0.15 * inch, y + 1.3 * inch, "STRATEGIC INITIATIVE")

        self.c.setFont("Helvetica-Bold", 34)
        self.c.setFillColor(COLORS['text_primary'])
        self.c.drawString(MARGIN + 0.15 * inch, y + 0.65 * inch, "GRC Program Modernization")

        self.c.setFont("Helvetica", 28)
        self.c.setFillColor(COLORS['accent_blue'])
        self.c.drawString(MARGIN + 0.15 * inch, y, "Roadmap 2026")

        # Subtitle area
        y_sub = HEIGHT * 0.32
        self.c.setFont("Helvetica", 12)
        self.c.setFillColor(COLORS['text_secondary'])
        self.c.drawString(MARGIN + 0.15 * inch, y_sub, "From Compliance Function to Strategic Business Enabler")

        # Info block bottom
        y_info = HEIGHT * 0.15
        self.c.setStrokeColor(COLORS['gray_300'])
        self.c.setLineWidth(0.5)
        self.c.line(MARGIN, y_info + 0.45 * inch, WIDTH - MARGIN, y_info + 0.45 * inch)

        self.c.setFont("Helvetica", 9)
        self.c.setFillColor(COLORS['text_muted'])
        self.c.drawString(MARGIN, y_info + 0.15 * inch, "Prepared for the CISO  |  March 2026  |  CONFIDENTIAL")

        # Right side decorative element
        self.c.setFillColor(COLORS['accent_light'])
        self.c.roundRect(WIDTH * 0.72, HEIGHT * 0.25, WIDTH * 0.22, HEIGHT * 0.55, 8, fill=1, stroke=0)
        self.c.setFillColor(COLORS['accent_teal_lt'])
        self.c.roundRect(WIDTH * 0.74, HEIGHT * 0.28, WIDTH * 0.18, HEIGHT * 0.49, 6, fill=1, stroke=0)

        # Key stats in decorative block
        cx = WIDTH * 0.83
        self.c.setFont("Helvetica-Bold", 36)
        self.c.setFillColor(COLORS['accent_teal'])
        self.c.drawCentredString(cx, HEIGHT * 0.6, "2026")
        self.c.setFont("Helvetica", 10)
        self.c.setFillColor(COLORS['text_secondary'])
        self.c.drawCentredString(cx, HEIGHT * 0.55, "Transformation Year")

        self.c.setFont("Helvetica-Bold", 28)
        self.c.setFillColor(COLORS['accent_blue'])
        self.c.drawCentredString(cx, HEIGHT * 0.44, "4")
        self.c.setFont("Helvetica", 10)
        self.c.setFillColor(COLORS['text_secondary'])
        self.c.drawCentredString(cx, HEIGHT * 0.39, "Strategic Phases")

        self.c.setFont("Helvetica-Bold", 28)
        self.c.setFillColor(COLORS['accent_indigo'])
        self.c.drawCentredString(cx, HEIGHT * 0.33, "12")
        self.c.setFont("Helvetica", 10)
        self.c.setFillColor(COLORS['text_secondary'])
        self.c.drawCentredString(cx, HEIGHT * 0.28, "Key Initiatives")

    # ─── SLIDE 2: Agenda / Table of Contents ─────────────────────
    def slide_agenda(self):
        self._new_slide(COLORS['bg_light'])

        # Header
        self.c.setFont("Helvetica-Bold", 22)
        self.c.setFillColor(COLORS['text_primary'])
        self.c.drawString(MARGIN, HEIGHT - MARGIN - 0.3 * inch, "Agenda")
        self._draw_accent_bar(MARGIN, HEIGHT - MARGIN - 0.42 * inch, 50, 3, COLORS['accent_teal'])

        items = [
            ("01", "Executive Summary", "Current state, vision, and strategic objectives"),
            ("02", "Current State Assessment", "Gap analysis across GRC functions, team structure & capabilities"),
            ("03", "Organizational Structure", "Team roles, reporting lines, and capability mapping"),
            ("04", "Critical Gaps Analysis", "GRC-Engineering disconnect, Customer Trust, program maturity"),
            ("05", "Strategic Roadmap", "Q1-Q4 phased plan with milestones and deliverables"),
            ("06", "Customer Trust Transformation", "Revenue enablement, tooling consolidation, knowledge base"),
            ("07", "GRC-as-Code & Automation", "Policy-as-code, CI/CD integration, engineering partnership"),
            ("08", "Metrics & Value Framework", "KPIs, dashboards, business value measurement"),
            ("09", "Risk & Dependencies", "Implementation risks, resource needs, change management"),
            ("10", "Investment & Timeline", "Resource requirements, expected ROI, phased milestones"),
        ]

        y_start = HEIGHT - MARGIN - 0.9 * inch
        card_h = 0.42 * inch
        gap = 0.06 * inch
        col_w = (WIDTH - 2 * MARGIN - 0.3 * inch) / 2

        for i, (num, title, desc) in enumerate(items):
            col = i // 5
            row = i % 5
            x = MARGIN + col * (col_w + 0.3 * inch)
            y = y_start - row * (card_h + gap)

            self._draw_card(x, y, col_w, card_h, fill=COLORS['bg_white'], border=COLORS['gray_300'])

            # Number badge
            badge_color = COLORS['accent_blue'] if col == 0 else COLORS['accent_teal']
            self._draw_card(x + 10, y + card_h / 2 - 10, 24, 20, fill=badge_color, radius=4)
            self.c.setFont("Helvetica-Bold", 9)
            self.c.setFillColor(white)
            self.c.drawCentredString(x + 22, y + card_h / 2 - 5, num)

            # Title and description
            self.c.setFont("Helvetica-Bold", 10)
            self.c.setFillColor(COLORS['text_primary'])
            self.c.drawString(x + 42, y + card_h / 2 + 3, title)
            self.c.setFont("Helvetica", 7.5)
            self.c.setFillColor(COLORS['text_muted'])
            self.c.drawString(x + 42, y + card_h / 2 - 10, desc)

        self._draw_footer()

    # ─── SLIDE 3: Executive Summary ──────────────────────────────
    def slide_executive_summary(self):
        self._new_slide(COLORS['bg_white'])

        self.c.setFont("Helvetica-Bold", 22)
        self.c.setFillColor(COLORS['text_primary'])
        self.c.drawString(MARGIN, HEIGHT - MARGIN - 0.3 * inch, "Executive Summary")
        self._draw_accent_bar(MARGIN, HEIGHT - MARGIN - 0.42 * inch, 50, 3, COLORS['accent_blue'])

        # Current State card
        y_top = HEIGHT - MARGIN - 0.85 * inch
        card_w = (WIDTH - 2 * MARGIN - 0.3 * inch) / 2
        card_h = 3.2 * inch

        # LEFT: Current State
        self._draw_card(MARGIN, y_top - card_h, card_w, card_h, fill=COLORS['red_light'], border=COLORS['gray_300'])
        self._draw_accent_bar(MARGIN, y_top - 2, card_w, 3, COLORS['red'])

        self.c.setFont("Helvetica-Bold", 12)
        self.c.setFillColor(COLORS['red'])
        self.c.drawString(MARGIN + 15, y_top - 22, "CURRENT STATE")

        bullets_current = [
            "GRC operates as isolated compliance function with no engineering integration",
            "Manual, check-the-box audit processes with no automation or policy-as-code",
            "Customer Trust team uses fragmented tooling (Onboard, Conveyor, Trust Center)",
            "No revenue impact tracking despite handling deal-blocking questionnaires",
            "No GRC team members understand the product, tech stack, or SDLC",
            "TPRM and Internal Audit lack standardized baselines and KPIs",
            "No existing roadmap, strategy, or maturity model in place",
        ]
        y = y_top - 44
        for b in bullets_current:
            y = self._draw_bullet(b, MARGIN + 15, y, size=8.5, max_width=card_w - 45, bullet_color=COLORS['red'], leading=13)
            y -= 2

        # RIGHT: Target State
        rx = MARGIN + card_w + 0.3 * inch
        self._draw_card(rx, y_top - card_h, card_w, card_h, fill=COLORS['green_light'], border=COLORS['gray_300'])
        self._draw_accent_bar(rx, y_top - 2, card_w, 3, COLORS['green'])

        self.c.setFont("Helvetica-Bold", 12)
        self.c.setFillColor(COLORS['green'])
        self.c.drawString(rx + 15, y_top - 22, "TARGET STATE (END OF 2026)")

        bullets_target = [
            "GRC embedded in engineering with policy-as-code in CI/CD pipelines",
            "Automated compliance evidence collection and continuous monitoring",
            "Unified Customer Trust platform with revenue-linked dashboards",
            "Standardized, legal-approved response library reducing questionnaire TAT by 60%",
            "Technical GRC expertise integrated into product and sprint planning",
            "Risk-quantified TPRM with automated vendor assessments and tiering",
            "Mature, metrics-driven GRC program aligned to NIST CSF and ISO 27001",
        ]
        y = y_top - 44
        for b in bullets_target:
            y = self._draw_bullet(b, rx + 15, y, size=8.5, max_width=card_w - 45, bullet_color=COLORS['green'], leading=13)
            y -= 2

        # Bottom: Strategic Vision statement
        vis_y = y_top - card_h - 0.35 * inch
        self._draw_card(MARGIN, vis_y - 0.55 * inch, WIDTH - 2 * MARGIN, 0.55 * inch, fill=COLORS['accent_light'], radius=4)
        self.c.setFont("Helvetica-Bold", 10)
        self.c.setFillColor(COLORS['accent_blue'])
        self.c.drawString(MARGIN + 15, vis_y - 0.15 * inch, "STRATEGIC VISION:")
        self.c.setFont("Helvetica", 10)
        self.c.setFillColor(COLORS['text_primary'])
        self.c.drawString(MARGIN + 150, vis_y - 0.15 * inch,
            "Transform GRC from a reactive cost center into a proactive, revenue-enabling, engineering-integrated strategic function.")
        self.c.setFont("Helvetica", 9)
        self.c.setFillColor(COLORS['text_secondary'])
        self.c.drawString(MARGIN + 15, vis_y - 0.38 * inch,
            "Deliver measurable business value through automation, risk quantification, and direct contribution to revenue acceleration and customer trust.")

        self._draw_footer()

    # ─── SLIDE 4: Organizational Structure ───────────────────────
    def slide_org_structure(self):
        self._new_slide(COLORS['bg_light'])

        self.c.setFont("Helvetica-Bold", 22)
        self.c.setFillColor(COLORS['text_primary'])
        self.c.drawString(MARGIN, HEIGHT - MARGIN - 0.3 * inch, "Organizational Structure & Team")
        self._draw_accent_bar(MARGIN, HEIGHT - MARGIN - 0.42 * inch, 50, 3, COLORS['accent_teal'])

        # CISO at top
        cx = WIDTH / 2
        top_y = HEIGHT - MARGIN - 0.9 * inch
        box_w = 1.6 * inch
        box_h = 0.42 * inch

        def draw_org_box(x, y, name, role, color, small=False):
            bw = box_w if not small else 1.4 * inch
            bh = box_h if not small else 0.38 * inch
            self._draw_card(x - bw/2, y - bh/2, bw, bh, fill=white, border=COLORS['gray_300'], radius=4)
            self._draw_accent_bar(x - bw/2, y + bh/2 - 3, bw, 3, color)
            self.c.setFont("Helvetica-Bold", 8 if small else 9)
            self.c.setFillColor(COLORS['text_primary'])
            self.c.drawCentredString(x, y + 4 if not small else y + 3, name)
            self.c.setFont("Helvetica", 6.5 if small else 7)
            self.c.setFillColor(COLORS['text_muted'])
            self.c.drawCentredString(x, y - 7 if not small else y - 7, role)

        def draw_connector(x1, y1, x2, y2):
            self.c.setStrokeColor(COLORS['gray_400'])
            self.c.setLineWidth(0.7)
            mid_y = (y1 + y2) / 2
            p = self.c.beginPath()
            p.moveTo(x1, y1)
            p.lineTo(x1, mid_y)
            p.lineTo(x2, mid_y)
            p.lineTo(x2, y2)
            self.c.drawPath(p, stroke=1, fill=0)

        # CISO
        draw_org_box(cx, top_y, "CISO", "Chief Information Security Officer", COLORS['accent_indigo'])

        # Three Director Reports
        level2_y = top_y - 0.85 * inch
        peers = [
            (cx - 3 * inch, "Chelsea Main", "Security Engineering"),
            (cx, "You (Sr. Dir. GRC)", "GRC Program Lead"),
            (cx + 3 * inch, "Damian King", "Security Operations"),
        ]
        for px, name, role in peers:
            draw_connector(cx, top_y - box_h/2, px, level2_y + box_h/2)
            color = COLORS['accent_blue'] if "You" in name else COLORS['gray_500']
            draw_org_box(px, level2_y, name, role, color)

        # GRC Direct Reports
        level3_y = level2_y - 0.85 * inch
        directs = [
            (cx - 2.8 * inch, "Steve Hammonds", "BC/DR"),
            (cx - 1.0 * inch, "Doug Matkins", "TPRM"),
            (cx + 1.0 * inch, "Janet De Lara", "Internal Audit"),
            (cx + 2.8 * inch, "Customer Trust Team", "Trust & Questionnaires"),
        ]
        for dx, name, role in directs:
            draw_connector(cx, level2_y - box_h/2, dx, level3_y + box_h/2)
            draw_org_box(dx, level3_y, name, role, COLORS['accent_teal'], small=True)

        # Customer Trust sub-team
        level4_y = level3_y - 0.72 * inch
        ct_x = cx + 2.8 * inch
        ct_members = [
            (ct_x - 1.0 * inch, "Eni Smigielska"),
            (ct_x - 0.0 * inch, "Russ Johnson"),
            (ct_x + 1.0 * inch, "Marcin Lachowicz"),
            (ct_x + 2.0 * inch, "Amine Gherabi"),
        ]
        for mx, name in ct_members:
            draw_connector(ct_x, level3_y - 0.38*inch/2, mx, level4_y + 0.26*inch/2)
            self._draw_card(mx - 0.65*inch, level4_y - 0.13*inch, 1.3*inch, 0.26*inch, fill=white, border=COLORS['gray_300'], radius=3)
            self.c.setFont("Helvetica", 7)
            self.c.setFillColor(COLORS['text_primary'])
            self.c.drawCentredString(mx, level4_y, name)

        # Governance sub-team (under you)
        gov_y = level3_y - 0.72 * inch
        gov_x = cx - 1.0 * inch
        # Paolo label
        self._draw_card(gov_x - 0.7*inch, gov_y - 0.13*inch, 1.4*inch, 0.3*inch, fill=COLORS['accent_teal_lt'], border=COLORS['gray_300'], radius=3)
        self.c.setFont("Helvetica-Bold", 7)
        self.c.setFillColor(COLORS['accent_teal'])
        self.c.drawCentredString(gov_x, gov_y + 3, "Governance (Paolo DiRosa)")
        self.c.setFont("Helvetica", 6.5)
        self.c.setFillColor(COLORS['text_muted'])
        self.c.drawCentredString(gov_x, gov_y - 8, "Barbara A-O, Mateusz Toczek")

        draw_connector(cx, level2_y - box_h/2, gov_x, gov_y + 0.15*inch)

        # Key insight box
        insight_y = 0.65 * inch
        self._draw_card(MARGIN, insight_y, WIDTH - 2 * MARGIN, 0.55 * inch, fill=COLORS['accent_warm'], border=COLORS['orange'], radius=4)
        self.c.setFont("Helvetica-Bold", 9)
        self.c.setFillColor(COLORS['orange'])
        self.c.drawString(MARGIN + 15, insight_y + 0.32 * inch, "KEY OBSERVATION:")
        self.c.setFont("Helvetica", 9)
        self.c.setFillColor(COLORS['text_primary'])
        self.c.drawString(MARGIN + 145, insight_y + 0.32 * inch,
            "No technical/engineering expertise exists within the current GRC team. The Customer Trust function lacks a dedicated lead since Jodi's departure.")
        self.c.setFont("Helvetica", 8.5)
        self.c.setFillColor(COLORS['text_secondary'])
        self.c.drawString(MARGIN + 15, insight_y + 0.1 * inch,
            "Peer alignment with Chelsea Main (Security Engineering) and Damian King (Security Ops) is critical for the GRC-as-Code initiative.")

        self._draw_footer()

    # ─── SLIDE 5: Critical Gaps Analysis ─────────────────────────
    def slide_gaps(self):
        self._new_slide(COLORS['bg_white'])

        self.c.setFont("Helvetica-Bold", 22)
        self.c.setFillColor(COLORS['text_primary'])
        self.c.drawString(MARGIN, HEIGHT - MARGIN - 0.3 * inch, "Critical Gaps Analysis")
        self._draw_accent_bar(MARGIN, HEIGHT - MARGIN - 0.42 * inch, 50, 3, COLORS['red'])

        gaps = [
            {
                'title': 'GRC-Engineering Disconnect',
                'severity': 'CRITICAL',
                'sev_color': COLORS['red'],
                'card_bg': COLORS['red_light'],
                'items': [
                    "No GRC personnel understand the product, tech stack, or SDLC",
                    "GRC not invited to product ideation, sprint planning, or architecture reviews",
                    "Manual audit processes with no automation or continuous monitoring",
                    "No embedded GRC presence in the engineering organization",
                    "Compliance treated as after-the-fact checkpoint, not integrated practice",
                ],
                'impact': "Compliance findings discovered late in cycle; engineering views GRC as blocker"
            },
            {
                'title': 'Customer Trust Fragmentation',
                'severity': 'HIGH',
                'sev_color': COLORS['orange'],
                'card_bg': COLORS['orange_light'],
                'items': [
                    "Three fragmented tools: Onboard, Conveyor, Customer Trust Center (NDA-gated)",
                    "All work tracked in Jira but no ROI or value-to-revenue tracking",
                    "Deal numbers visible but no revenue impact metrics or SLA measurement",
                    "No standardized, legal-approved response library for common questionnaires",
                    "No dedicated lead after Jodi's departure; team operates without strategic direction",
                ],
                'impact': "Slower deal cycles, duplicated effort, inability to demonstrate business value"
            },
            {
                'title': 'Program Maturity & Operations',
                'severity': 'HIGH',
                'sev_color': COLORS['orange'],
                'card_bg': COLORS['orange_light'],
                'items': [
                    "No established roadmap, maturity model, or strategic plan prior to this engagement",
                    "TPRM and Internal Audit lack standardized baselines and performance KPIs",
                    "BC/DR program needs validation against current threat landscape",
                    "No risk quantification methodology (e.g., FAIR) for business-language risk reporting",
                    "Governance function exists but lacks integration with risk and compliance workflows",
                ],
                'impact': "Reactive posture; cannot demonstrate program value or prioritize investments"
            },
        ]

        y_start = HEIGHT - MARGIN - 0.85 * inch
        card_w = (WIDTH - 2 * MARGIN - 0.4 * inch) / 3
        card_h = 3.6 * inch

        for i, gap in enumerate(gaps):
            x = MARGIN + i * (card_w + 0.2 * inch)
            self._draw_card(x, y_start - card_h, card_w, card_h, fill=gap['card_bg'], border=COLORS['gray_300'])

            # Severity badge
            self._draw_accent_bar(x, y_start - 2, card_w, 3, gap['sev_color'])
            badge_w = pdfmetrics.stringWidth(gap['severity'], "Helvetica-Bold", 7) + 12
            self._draw_card(x + card_w - badge_w - 8, y_start - 22, badge_w, 16, fill=gap['sev_color'], radius=3)
            self.c.setFont("Helvetica-Bold", 7)
            self.c.setFillColor(white)
            self.c.drawCentredString(x + card_w - badge_w/2 - 8, y_start - 18, gap['severity'])

            # Title
            self.c.setFont("Helvetica-Bold", 11)
            self.c.setFillColor(COLORS['text_primary'])
            self.c.drawString(x + 12, y_start - 22, gap['title'])

            # Bullets
            y = y_start - 44
            for item in gap['items']:
                y = self._draw_bullet(item, x + 12, y, size=8, max_width=card_w - 38,
                                     bullet_color=gap['sev_color'], leading=11.5)
                y -= 4

            # Impact box
            imp_h = 0.5 * inch
            imp_y = y_start - card_h + 8
            self._draw_card(x + 8, imp_y, card_w - 16, imp_h, fill=white, border=COLORS['gray_300'], radius=3)
            self.c.setFont("Helvetica-Bold", 7.5)
            self.c.setFillColor(gap['sev_color'])
            self.c.drawString(x + 16, imp_y + imp_h - 14, "BUSINESS IMPACT")
            self.c.setFont("Helvetica", 7.5)
            self.c.setFillColor(COLORS['text_secondary'])
            self._draw_text_block(gap['impact'], x + 16, imp_y + imp_h - 28, size=7.5,
                                 color=COLORS['text_secondary'], max_width=card_w - 40, leading=10)

        self._draw_footer()

    # ─── SLIDE 6: Strategic Roadmap Overview ─────────────────────
    def slide_roadmap_overview(self):
        self._new_slide(COLORS['bg_white'])

        self.c.setFont("Helvetica-Bold", 22)
        self.c.setFillColor(COLORS['text_primary'])
        self.c.drawString(MARGIN, HEIGHT - MARGIN - 0.3 * inch, "Strategic Roadmap Overview")
        self._draw_accent_bar(MARGIN, HEIGHT - MARGIN - 0.42 * inch, 50, 3, COLORS['accent_indigo'])

        # Timeline bar
        timeline_y = HEIGHT - MARGIN - 1.0 * inch
        bar_x = MARGIN + 0.5 * inch
        bar_w = WIDTH - 2 * MARGIN - 1.0 * inch
        bar_h = 0.32 * inch

        phases = [
            ("Q1 2026", "Foundation &\nAssessment", COLORS['accent_blue'], 0.25),
            ("Q2 2026", "Quick Wins &\nProcess Build", COLORS['accent_teal'], 0.25),
            ("Q3 2026", "Automation &\nIntegration", COLORS['accent_indigo'], 0.25),
            ("Q4 2026", "Optimization &\nScale", COLORS['green'], 0.25),
        ]

        x = bar_x
        for label, desc, color, frac in phases:
            pw = bar_w * frac
            self._draw_card(x, timeline_y - bar_h, pw - 4, bar_h, fill=color, radius=4)
            self.c.setFont("Helvetica-Bold", 9)
            self.c.setFillColor(white)
            self.c.drawCentredString(x + pw/2 - 2, timeline_y - bar_h/2 + 2, label)
            x += pw

        # Phase detail cards
        detail_y = timeline_y - 0.65 * inch
        card_w = (WIDTH - 2 * MARGIN - 0.45 * inch) / 4
        card_h = 3.0 * inch

        phase_details = [
            {
                'title': 'Phase 1: Foundation',
                'subtitle': 'Assess & Baseline',
                'color': COLORS['accent_blue'],
                'bg': COLORS['accent_light'],
                'items': [
                    "Complete GRC maturity assessment (NIST CSF aligned)",
                    "Map all Customer Trust tools and workflows",
                    "Document current TPRM, audit, and BC/DR processes",
                    "Establish team capability matrix and skill gaps",
                    "Begin tech stack education for GRC team",
                    "Define KPI framework and measurement baseline",
                ]
            },
            {
                'title': 'Phase 2: Quick Wins',
                'subtitle': 'Deliver Visible Value',
                'color': COLORS['accent_teal'],
                'bg': COLORS['accent_teal_lt'],
                'items': [
                    "Launch revenue-tracking dashboard for Customer Trust",
                    "Build standardized questionnaire response library",
                    "Embed GRC in key engineering meetings",
                    "Implement TPRM vendor tiering and risk scoring",
                    "Establish audit cadence and internal KPI reporting",
                    "Deploy initial automated evidence collection",
                ]
            },
            {
                'title': 'Phase 3: Automation',
                'subtitle': 'Scale Through Technology',
                'color': COLORS['accent_indigo'],
                'bg': COLORS['purple_light'],
                'items': [
                    "Implement policy-as-code in CI/CD pipeline",
                    "Automate compliance evidence gathering",
                    "Consolidate Customer Trust tooling",
                    "Launch continuous control monitoring",
                    "Integrate risk quantification (FAIR model)",
                    "Build cross-functional GRC-Engineering workflows",
                ]
            },
            {
                'title': 'Phase 4: Optimize',
                'subtitle': 'Mature & Demonstrate Value',
                'color': COLORS['green'],
                'bg': COLORS['green_light'],
                'items': [
                    "Full GRC-as-Code operational maturity",
                    "Executive value dashboards (risk + revenue)",
                    "Proactive risk identification and remediation",
                    "Advanced vendor risk automation",
                    "Program maturity re-assessment and 2027 planning",
                    "Team upskilling certification program completion",
                ]
            },
        ]

        for i, phase in enumerate(phase_details):
            x = MARGIN + i * (card_w + 0.15 * inch)
            self._draw_card(x, detail_y - card_h, card_w, card_h, fill=phase['bg'], border=COLORS['gray_300'])
            self._draw_accent_bar(x, detail_y - 2, card_w, 3, phase['color'])

            self.c.setFont("Helvetica-Bold", 9.5)
            self.c.setFillColor(phase['color'])
            self.c.drawString(x + 10, detail_y - 20, phase['title'])
            self.c.setFont("Helvetica", 7.5)
            self.c.setFillColor(COLORS['text_muted'])
            self.c.drawString(x + 10, detail_y - 32, phase['subtitle'])

            y = detail_y - 50
            for item in phase['items']:
                y = self._draw_bullet(item, x + 10, y, size=7.5, max_width=card_w - 32,
                                     bullet_color=phase['color'], leading=10.5)
                y -= 3

        self._draw_footer()

    # ─── SLIDE 7: Customer Trust Transformation ──────────────────
    def slide_customer_trust(self):
        self._new_slide(COLORS['bg_white'])

        self.c.setFont("Helvetica-Bold", 22)
        self.c.setFillColor(COLORS['text_primary'])
        self.c.drawString(MARGIN, HEIGHT - MARGIN - 0.3 * inch, "Customer Trust Transformation")
        self._draw_accent_bar(MARGIN, HEIGHT - MARGIN - 0.42 * inch, 50, 3, COLORS['accent_teal'])

        self.c.setFont("Helvetica", 10)
        self.c.setFillColor(COLORS['text_secondary'])
        self.c.drawString(MARGIN, HEIGHT - MARGIN - 0.62 * inch,
            "Evolve Customer Trust from reactive questionnaire processing to proactive revenue enablement")

        # Three columns
        y_top = HEIGHT - MARGIN - 1.05 * inch
        col_w = (WIDTH - 2 * MARGIN - 0.3 * inch) / 3
        card_h = 2.8 * inch

        columns = [
            {
                'title': 'Tooling Consolidation',
                'color': COLORS['accent_blue'],
                'bg': COLORS['accent_light'],
                'items': [
                    ("Current:", "Onboard, Conveyor, Trust Center (NDA-gated) - fragmented and overlapping"),
                    ("Target:", "Single pane of glass for all customer trust activities"),
                    ("Action:", "Evaluate platform consolidation (e.g., Vanta, Drata, SafeBase) or optimize existing stack"),
                    ("Action:", "Centralize all trust artifacts in one customer-facing portal"),
                    ("Metric:", "Reduce tool count from 3+ to 1-2 integrated platforms"),
                ]
            },
            {
                'title': 'Revenue Dashboard & Tracking',
                'color': COLORS['accent_teal'],
                'bg': COLORS['accent_teal_lt'],
                'items': [
                    ("Current:", "Deal numbers visible in Jira but no revenue impact measurement"),
                    ("Target:", "Real-time dashboard linking questionnaires to deal value and cycle time"),
                    ("Action:", "Integrate Jira with CRM (Salesforce/HubSpot) for revenue attribution"),
                    ("Action:", "Track questionnaire TAT, SLA compliance, and deal-stage correlation"),
                    ("Metric:", "Demonstrate direct revenue enablement value to leadership"),
                ]
            },
            {
                'title': 'Knowledge Base & Automation',
                'color': COLORS['accent_indigo'],
                'bg': COLORS['purple_light'],
                'items': [
                    ("Current:", "Ad-hoc responses; no standardized, legal-approved answer library"),
                    ("Target:", "Comprehensive response library with automated suggestion engine"),
                    ("Action:", "Catalog top 200 recurring questions and create legal-approved responses"),
                    ("Action:", "Implement AI-assisted questionnaire completion (Conveyor AI, etc.)"),
                    ("Metric:", "60% reduction in average questionnaire turnaround time"),
                ]
            },
        ]

        for i, col in enumerate(columns):
            x = MARGIN + i * (col_w + 0.15 * inch)
            self._draw_card(x, y_top - card_h, col_w, card_h, fill=col['bg'], border=COLORS['gray_300'])
            self._draw_accent_bar(x, y_top - 2, col_w, 3, col['color'])

            self.c.setFont("Helvetica-Bold", 11)
            self.c.setFillColor(col['color'])
            self.c.drawString(x + 12, y_top - 22, col['title'])

            y = y_top - 42
            for label, text in col['items']:
                self.c.setFont("Helvetica-Bold", 7.5)
                self.c.setFillColor(col['color'])
                self.c.drawString(x + 12, y, label)
                label_w = pdfmetrics.stringWidth(label, "Helvetica-Bold", 7.5) + 4
                self.c.setFont("Helvetica", 7.5)
                self.c.setFillColor(COLORS['text_secondary'])
                y_end = self._draw_text_block(text, x + 12 + label_w, y, size=7.5,
                                             color=COLORS['text_secondary'], max_width=col_w - 30 - label_w, leading=10)
                y = y_end - 6

        # Bottom KPI bar
        kpi_y = y_top - card_h - 0.35 * inch
        kpi_h = 0.7 * inch
        self._draw_card(MARGIN, kpi_y - kpi_h, WIDTH - 2 * MARGIN, kpi_h, fill=COLORS['gray_100'], border=COLORS['gray_300'])

        kpis = [
            ("60%", "Reduction in\nQuestionnaire TAT", COLORS['accent_teal']),
            ("$__M", "Revenue\nEnabled/Quarter", COLORS['accent_blue']),
            ("95%", "SLA Compliance\nTarget", COLORS['accent_indigo']),
            ("1-2", "Consolidated\nTrust Platforms", COLORS['green']),
            ("200+", "Standardized\nResponse Library", COLORS['purple']),
        ]

        kpi_w = (WIDTH - 2 * MARGIN) / len(kpis)
        for i, (val, label, color) in enumerate(kpis):
            kx = MARGIN + i * kpi_w + kpi_w / 2
            self.c.setFont("Helvetica-Bold", 22)
            self.c.setFillColor(color)
            self.c.drawCentredString(kx, kpi_y - 0.25 * inch, val)
            self.c.setFont("Helvetica", 7.5)
            self.c.setFillColor(COLORS['text_muted'])
            for j, line in enumerate(label.split('\n')):
                self.c.drawCentredString(kx, kpi_y - 0.4 * inch - j * 10, line)

        self._draw_footer()

    # ─── SLIDE 8: GRC-as-Code & Engineering Integration ──────────
    def slide_grc_as_code(self):
        self._new_slide(COLORS['bg_light'])

        self.c.setFont("Helvetica-Bold", 22)
        self.c.setFillColor(COLORS['text_primary'])
        self.c.drawString(MARGIN, HEIGHT - MARGIN - 0.3 * inch, "GRC-as-Code & Engineering Integration")
        self._draw_accent_bar(MARGIN, HEIGHT - MARGIN - 0.42 * inch, 50, 3, COLORS['accent_indigo'])

        # Left: Strategy description
        left_w = (WIDTH - 2 * MARGIN) * 0.48
        right_x = MARGIN + left_w + 0.3 * inch
        right_w = (WIDTH - 2 * MARGIN) * 0.48

        y_top = HEIGHT - MARGIN - 0.85 * inch

        # Pipeline visual (left side)
        self._draw_card(MARGIN, y_top - 2.1 * inch, left_w, 2.1 * inch, fill=COLORS['bg_white'], border=COLORS['gray_300'])
        self.c.setFont("Helvetica-Bold", 11)
        self.c.setFillColor(COLORS['accent_indigo'])
        self.c.drawString(MARGIN + 15, y_top - 20, "Policy-as-Code in CI/CD Pipeline")

        # Pipeline stages
        stages = [
            ("Code Commit", "Developer pushes\ncode changes", COLORS['gray_600']),
            ("Policy Check", "OPA/Rego policies\nvalidate compliance", COLORS['accent_indigo']),
            ("Security Scan", "SAST/DAST/SCA\nautomated scanning", COLORS['accent_blue']),
            ("Evidence Log", "Compliance artifacts\nauto-collected", COLORS['accent_teal']),
            ("Deploy", "Compliant code\nships to production", COLORS['green']),
        ]

        stage_y = y_top - 0.55 * inch
        stage_w = (left_w - 40) / len(stages)
        for i, (name, desc, color) in enumerate(stages):
            sx = MARGIN + 15 + i * stage_w
            # Arrow connector
            if i > 0:
                self.c.setFillColor(COLORS['gray_400'])
                ax = sx - 4
                self.c.line(ax - 8, stage_y - 12, ax, stage_y - 12)
                # arrowhead
                p = self.c.beginPath()
                p.moveTo(ax, stage_y - 12)
                p.lineTo(ax - 4, stage_y - 8)
                p.lineTo(ax - 4, stage_y - 16)
                p.close()
                self.c.drawPath(p, fill=1, stroke=0)

            self._draw_card(sx, stage_y - 28, stage_w - 12, 32, fill=color, radius=3)
            self.c.setFont("Helvetica-Bold", 7)
            self.c.setFillColor(white)
            self.c.drawCentredString(sx + (stage_w - 12)/2, stage_y - 16, name)

            self.c.setFont("Helvetica", 6.5)
            self.c.setFillColor(COLORS['text_muted'])
            for j, line in enumerate(desc.split('\n')):
                self.c.drawCentredString(sx + (stage_w - 12)/2, stage_y - 45 - j * 9, line)

        # Integration Strategy bullets
        strat_y = y_top - 1.15 * inch
        strategies = [
            "Partner with Chelsea Main (Security Engineering) on tooling and pipeline integration",
            "Implement Open Policy Agent (OPA) with Rego policies for automated compliance checks",
            "Auto-generate compliance evidence from CI/CD pipeline execution logs",
            "Create GRC-friendly dashboards from engineering telemetry (Datadog, Splunk, etc.)",
        ]
        y = strat_y
        for s in strategies:
            y = self._draw_bullet(s, MARGIN + 15, y, size=7.5, max_width=left_w - 40,
                                 bullet_color=COLORS['accent_indigo'], leading=10)
            y -= 4

        # Right: Phased approach
        self._draw_card(right_x, y_top - 2.1 * inch, right_w, 2.1 * inch, fill=COLORS['bg_white'], border=COLORS['gray_300'])
        self.c.setFont("Helvetica-Bold", 11)
        self.c.setFillColor(COLORS['accent_blue'])
        self.c.drawString(right_x + 15, y_top - 20, "Engineering Integration Phases")

        integration_phases = [
            ("Phase 1: Learn", COLORS['accent_blue'], [
                "GRC team tech stack education (architecture, languages, cloud)",
                "Shadow engineering standups and sprint planning",
                "Map compliance requirements to engineering workflows",
            ]),
            ("Phase 2: Embed", COLORS['accent_teal'], [
                "GRC liaison attends architecture reviews and design discussions",
                "Joint GRC-Engineering working group (bi-weekly)",
                "Shared Slack channels and documentation",
            ]),
            ("Phase 3: Automate", COLORS['accent_indigo'], [
                "Policy-as-code deployed in CI/CD pipelines",
                "Automated evidence collection replaces manual audits",
                "Self-service compliance status for engineering teams",
            ]),
        ]

        y = y_top - 45
        for title, color, items in integration_phases:
            self._draw_accent_bar(right_x + 15, y + 2, 4, -38 - len(items)*13, color)
            self.c.setFont("Helvetica-Bold", 9)
            self.c.setFillColor(color)
            self.c.drawString(right_x + 28, y, title)
            y -= 16
            for item in items:
                y = self._draw_bullet(item, right_x + 28, y, size=7.5, max_width=right_w - 55,
                                     bullet_color=color, leading=10)
                y -= 2
            y -= 6

        # Bottom: Industry best practice callout
        bp_y = y_top - 2.1 * inch - 0.35 * inch
        bp_h = 1.15 * inch
        self._draw_card(MARGIN, bp_y - bp_h, WIDTH - 2 * MARGIN, bp_h, fill=COLORS['accent_light'], border=COLORS['accent_blue'])

        self.c.setFont("Helvetica-Bold", 10)
        self.c.setFillColor(COLORS['accent_blue'])
        self.c.drawString(MARGIN + 15, bp_y - 18, "INDUSTRY BEST PRACTICES - GRC AUTOMATION")

        best_practices = [
            ("Shift-Left Compliance:", "Integrate compliance checks early in SDLC, not at deployment gate"),
            ("Continuous Compliance:", "Replace point-in-time audits with real-time monitoring (NIST SP 800-137)"),
            ("Evidence-as-Code:", "Generate audit evidence automatically from infrastructure-as-code and CI/CD logs"),
            ("Risk-Based Prioritization:", "Use FAIR or similar quantitative models to prioritize controls by business impact"),
        ]
        y = bp_y - 36
        for label, text in best_practices:
            self.c.setFont("Helvetica-Bold", 8)
            self.c.setFillColor(COLORS['accent_indigo'])
            self.c.drawString(MARGIN + 15, y, label)
            lw = pdfmetrics.stringWidth(label, "Helvetica-Bold", 8) + 5
            self.c.setFont("Helvetica", 8)
            self.c.setFillColor(COLORS['text_secondary'])
            self.c.drawString(MARGIN + 15 + lw, y, text)
            y -= 15

        self._draw_footer()

    # ─── SLIDE 9: Metrics & Value Framework ──────────────────────
    def slide_metrics(self):
        self._new_slide(COLORS['bg_white'])

        self.c.setFont("Helvetica-Bold", 22)
        self.c.setFillColor(COLORS['text_primary'])
        self.c.drawString(MARGIN, HEIGHT - MARGIN - 0.3 * inch, "Metrics & Value Framework")
        self._draw_accent_bar(MARGIN, HEIGHT - MARGIN - 0.42 * inch, 50, 3, COLORS['accent_teal'])

        # Three metric categories
        y_top = HEIGHT - MARGIN - 0.82 * inch
        col_w = (WIDTH - 2 * MARGIN - 0.3 * inch) / 3
        card_h = 3.4 * inch

        categories = [
            {
                'title': 'Revenue & Business Value',
                'icon_label': '$',
                'color': COLORS['accent_teal'],
                'bg': COLORS['accent_teal_lt'],
                'metrics': [
                    ("Revenue Enabled", "Total deal value for completed security questionnaires per quarter"),
                    ("Questionnaire TAT", "Average turnaround time from receipt to delivery (target: <5 business days)"),
                    ("Deal Acceleration", "Reduction in sales cycle days attributable to proactive trust posture"),
                    ("Customer Retention", "Renewal rate for accounts where GRC facilitated trust reviews"),
                    ("Cost Avoidance", "Estimated cost of regulatory fines or breaches avoided"),
                ]
            },
            {
                'title': 'Operational Excellence',
                'icon_label': 'O',
                'color': COLORS['accent_blue'],
                'bg': COLORS['accent_light'],
                'metrics': [
                    ("Automation Rate", "% of compliance evidence collected automatically vs. manually"),
                    ("Audit Readiness", "Time to produce complete evidence package for SOC 2/ISO audit"),
                    ("TPRM Coverage", "% of vendors assessed and tiered within risk framework"),
                    ("Control Effectiveness", "% of controls passing continuous monitoring checks"),
                    ("SLA Compliance", "% of internal/external commitments met on time"),
                ]
            },
            {
                'title': 'Risk & Maturity',
                'icon_label': 'R',
                'color': COLORS['accent_indigo'],
                'bg': COLORS['purple_light'],
                'metrics': [
                    ("Program Maturity", "NIST CSF maturity score across all domains (target: Tier 3)"),
                    ("Risk Posture", "Quantified risk exposure trend (FAIR methodology)"),
                    ("Finding Closure", "Mean time to remediate audit and assessment findings"),
                    ("Policy Currency", "% of policies reviewed and updated within cycle"),
                    ("Regulatory Compliance", "% alignment to applicable frameworks (SOC 2, ISO 27001, etc.)"),
                ]
            },
        ]

        for i, cat in enumerate(categories):
            x = MARGIN + i * (col_w + 0.15 * inch)
            self._draw_card(x, y_top - card_h, col_w, card_h, fill=cat['bg'], border=COLORS['gray_300'])
            self._draw_accent_bar(x, y_top - 2, col_w, 3, cat['color'])

            # Icon circle
            self._draw_card(x + 12, y_top - 32, 22, 22, fill=cat['color'], radius=11)
            self.c.setFont("Helvetica-Bold", 11)
            self.c.setFillColor(white)
            self.c.drawCentredString(x + 23, y_top - 26, cat['icon_label'])

            self.c.setFont("Helvetica-Bold", 11)
            self.c.setFillColor(cat['color'])
            self.c.drawString(x + 40, y_top - 24, cat['title'])

            y = y_top - 50
            for name, desc in cat['metrics']:
                self.c.setFont("Helvetica-Bold", 8)
                self.c.setFillColor(COLORS['text_primary'])
                self.c.drawString(x + 14, y, name)
                y -= 12
                self.c.setFont("Helvetica", 7.5)
                self.c.setFillColor(COLORS['text_muted'])
                y = self._draw_text_block(desc, x + 14, y, size=7.5, color=COLORS['text_muted'],
                                         max_width=col_w - 32, leading=10)
                y -= 8

        # Dashboard preview callout
        dash_y = y_top - card_h - 0.3 * inch
        self._draw_card(MARGIN, dash_y - 0.5 * inch, WIDTH - 2 * MARGIN, 0.5 * inch, fill=COLORS['gray_100'], border=COLORS['gray_300'])
        self.c.setFont("Helvetica-Bold", 9)
        self.c.setFillColor(COLORS['accent_blue'])
        self.c.drawString(MARGIN + 15, dash_y - 0.18 * inch, "DASHBOARD DELIVERY:")
        self.c.setFont("Helvetica", 9)
        self.c.setFillColor(COLORS['text_secondary'])
        self.c.drawString(MARGIN + 155, dash_y - 0.18 * inch,
            "Executive dashboard (monthly CISO report)  |  Operational dashboard (team daily use)  |  Customer Trust revenue dashboard (sales alignment)")
        self.c.setFont("Helvetica", 8)
        self.c.setFillColor(COLORS['text_muted'])
        self.c.drawString(MARGIN + 15, dash_y - 0.37 * inch,
            "Recommended tooling: Integrate with existing BI stack (Tableau/Looker/PowerBI) or leverage GRC platform native reporting (Vanta, ServiceNow GRC, etc.)")

        self._draw_footer()

    # ─── SLIDE 10: Risk & Dependencies ───────────────────────────
    def slide_risks(self):
        self._new_slide(COLORS['bg_light'])

        self.c.setFont("Helvetica-Bold", 22)
        self.c.setFillColor(COLORS['text_primary'])
        self.c.drawString(MARGIN, HEIGHT - MARGIN - 0.3 * inch, "Risks, Dependencies & Change Management")
        self._draw_accent_bar(MARGIN, HEIGHT - MARGIN - 0.42 * inch, 50, 3, COLORS['orange'])

        # Risk table
        y_top = HEIGHT - MARGIN - 0.82 * inch
        table_w = WIDTH - 2 * MARGIN
        row_h = 0.44 * inch
        header_h = 0.3 * inch

        # Headers
        cols = [
            (MARGIN, 0.55 * inch, "RISK"),
            (MARGIN + 0.55 * inch, 3.4 * inch, "DESCRIPTION"),
            (MARGIN + 3.95 * inch, 0.6 * inch, "LIKELIHOOD"),
            (MARGIN + 4.55 * inch, 0.6 * inch, "IMPACT"),
            (MARGIN + 5.15 * inch, 4.1 * inch, "MITIGATION"),
        ]

        self._draw_card(MARGIN, y_top - header_h, table_w, header_h, fill=COLORS['gray_700'], radius=0)
        self.c.setFont("Helvetica-Bold", 7.5)
        self.c.setFillColor(white)
        for cx, cw, label in cols:
            self.c.drawString(cx + 8, y_top - header_h/2 - 3, label)

        risks = [
            ("R1", "Engineering team resistance to GRC integration and additional process", "Medium", "High",
             "Start with value-add (automated security checks they want), not compliance mandates. Executive sponsorship from CISO."),
            ("R2", "Insufficient budget for GRC platform/tooling consolidation", "Medium", "High",
             "Build ROI business case using revenue enablement data. Phase investments across quarters."),
            ("R3", "Team skill gaps delay GRC-as-Code implementation", "High", "Medium",
             "Partner with Security Engineering (Chelsea Main). External training budget. Consider targeted hires."),
            ("R4", "Customer Trust team capacity constraints during transformation", "Medium", "Medium",
             "Protect BAU capacity during transformation. Automate low-value tasks first to free capacity."),
            ("R5", "Nathan's return from medical leave creates role/strategy ambiguity", "Low", "High",
             "Document all decisions, maintain transparency with CISO. Build roadmap with organizational buy-in."),
            ("R6", "Tool consolidation causes temporary disruption to Customer Trust SLAs", "Medium", "Medium",
             "Parallel run during migration. Phased rollout with rollback plan. No big-bang cutover."),
        ]

        for i, (rid, desc, like, impact, mitigation) in enumerate(risks):
            y = y_top - header_h - (i * row_h)
            bg = COLORS['bg_white'] if i % 2 == 0 else COLORS['gray_100']
            self._draw_card(MARGIN, y - row_h, table_w, row_h, fill=bg, radius=0)

            self.c.setFont("Helvetica-Bold", 8)
            self.c.setFillColor(COLORS['red'] if impact == "High" else COLORS['orange'])
            self.c.drawString(cols[0][0] + 8, y - row_h/2, rid)

            self.c.setFont("Helvetica", 7.5)
            self.c.setFillColor(COLORS['text_primary'])
            self._draw_text_block(desc, cols[1][0] + 8, y - 10, size=7.5,
                                 max_width=cols[1][1] - 16, leading=10)

            # Likelihood/Impact badges
            for j, (val, col_idx) in enumerate([(like, 2), (impact, 3)]):
                badge_color = COLORS['red'] if val == "High" else (COLORS['orange'] if val == "Medium" else COLORS['green'])
                bw = 42
                bx = cols[col_idx][0] + 8
                by = y - row_h/2 - 5
                self._draw_card(bx, by, bw, 14, fill=badge_color, radius=3)
                self.c.setFont("Helvetica-Bold", 7)
                self.c.setFillColor(white)
                self.c.drawCentredString(bx + bw/2, by + 3, val)

            self.c.setFont("Helvetica", 7.5)
            self.c.setFillColor(COLORS['text_secondary'])
            self._draw_text_block(mitigation, cols[4][0] + 8, y - 10, size=7.5,
                                 max_width=cols[4][1] - 16, leading=10)

        # Dependencies section
        dep_y = y_top - header_h - (len(risks) * row_h) - 0.35 * inch
        self.c.setFont("Helvetica-Bold", 12)
        self.c.setFillColor(COLORS['text_primary'])
        self.c.drawString(MARGIN, dep_y, "Key Dependencies")

        deps = [
            "CISO sponsorship and executive air cover for cross-functional initiatives",
            "Security Engineering (Chelsea Main) partnership for CI/CD and tooling integration",
            "Budget approval for GRC platform investment and team training",
            "CRM access (Salesforce/HubSpot) for Customer Trust revenue attribution",
        ]
        y = dep_y - 18
        dep_w = (WIDTH - 2 * MARGIN) / 2
        for i, dep in enumerate(deps):
            col = i // 2
            row = i % 2
            dx = MARGIN + col * dep_w
            dy = y - row * 18
            y2 = self._draw_bullet(dep, dx, dy, size=8, max_width=dep_w - 25,
                                  bullet_color=COLORS['accent_blue'])

        self._draw_footer()

    # ─── SLIDE 11: Investment & ROI ──────────────────────────────
    def slide_investment(self):
        self._new_slide(COLORS['bg_white'])

        self.c.setFont("Helvetica-Bold", 22)
        self.c.setFillColor(COLORS['text_primary'])
        self.c.drawString(MARGIN, HEIGHT - MARGIN - 0.3 * inch, "Investment Requirements & Expected ROI")
        self._draw_accent_bar(MARGIN, HEIGHT - MARGIN - 0.42 * inch, 50, 3, COLORS['green'])

        y_top = HEIGHT - MARGIN - 0.85 * inch
        left_w = (WIDTH - 2 * MARGIN) * 0.52
        right_x = MARGIN + left_w + 0.25 * inch
        right_w = (WIDTH - 2 * MARGIN) * 0.45

        # LEFT: Investment areas
        self._draw_card(MARGIN, y_top - 3.2 * inch, left_w, 3.2 * inch, fill=COLORS['bg_white'], border=COLORS['gray_300'])
        self._draw_accent_bar(MARGIN, y_top - 2, left_w, 3, COLORS['accent_blue'])

        self.c.setFont("Helvetica-Bold", 12)
        self.c.setFillColor(COLORS['accent_blue'])
        self.c.drawString(MARGIN + 15, y_top - 22, "Investment Areas")

        investments = [
            ("GRC Platform & Tooling", [
                "Customer Trust platform consolidation/upgrade",
                "GRC automation platform (policy-as-code tooling)",
                "Dashboard and reporting infrastructure",
                "TPRM automation and vendor risk platform",
            ]),
            ("People & Skills", [
                "GRC-Engineering technical training program",
                "Potential hire: Technical GRC Engineer (policy-as-code expertise)",
                "Customer Trust team lead recruitment",
                "Industry certifications (CISA, CRISC, CISSP) for team",
            ]),
            ("Process & Consulting", [
                "NIST CSF maturity assessment (external benchmark)",
                "FAIR risk quantification methodology implementation",
                "Change management support for engineering integration",
            ]),
        ]

        y = y_top - 45
        for category, items in investments:
            self.c.setFont("Helvetica-Bold", 9)
            self.c.setFillColor(COLORS['text_primary'])
            self.c.drawString(MARGIN + 15, y, category)
            y -= 14
            for item in items:
                y = self._draw_bullet(item, MARGIN + 20, y, size=8, max_width=left_w - 50,
                                     bullet_color=COLORS['accent_blue'], leading=11)
                y -= 2
            y -= 8

        # RIGHT: ROI Framework
        self._draw_card(right_x, y_top - 3.2 * inch, right_w, 3.2 * inch, fill=COLORS['green_light'], border=COLORS['gray_300'])
        self._draw_accent_bar(right_x, y_top - 2, right_w, 3, COLORS['green'])

        self.c.setFont("Helvetica-Bold", 12)
        self.c.setFillColor(COLORS['green'])
        self.c.drawString(right_x + 15, y_top - 22, "Expected Return on Investment")

        roi_items = [
            ("Revenue Enablement", "Faster questionnaire completion directly accelerates deal closure. Tracking will quantify exact revenue contribution.", COLORS['accent_teal']),
            ("Cost Avoidance", "Automated compliance reduces audit preparation costs by estimated 40-60%. Continuous monitoring prevents costly findings.", COLORS['accent_blue']),
            ("Risk Reduction", "Quantified risk posture improvement. Proactive identification reduces likelihood and impact of security incidents.", COLORS['accent_indigo']),
            ("Operational Efficiency", "GRC-as-Code eliminates 60%+ of manual compliance tasks. Team capacity redirected to strategic initiatives.", COLORS['green']),
            ("Competitive Advantage", "Strong, transparent trust posture becomes sales differentiator. Self-service trust portal reduces friction.", COLORS['purple']),
        ]

        y = y_top - 48
        for title, desc, color in roi_items:
            self._draw_accent_bar(right_x + 15, y + 2, 3, -30, color)
            self.c.setFont("Helvetica-Bold", 9)
            self.c.setFillColor(color)
            self.c.drawString(right_x + 25, y, title)
            y -= 13
            self.c.setFont("Helvetica", 7.5)
            self.c.setFillColor(COLORS['text_secondary'])
            y = self._draw_text_block(desc, right_x + 25, y, size=7.5, color=COLORS['text_secondary'],
                                     max_width=right_w - 48, leading=10)
            y -= 10

        # Bottom: Timeline summary
        tl_y = y_top - 3.2 * inch - 0.3 * inch
        tl_h = 0.65 * inch
        self._draw_card(MARGIN, tl_y - tl_h, WIDTH - 2 * MARGIN, tl_h, fill=COLORS['accent_light'], border=COLORS['accent_blue'])

        self.c.setFont("Helvetica-Bold", 10)
        self.c.setFillColor(COLORS['accent_blue'])
        self.c.drawString(MARGIN + 15, tl_y - 18, "VALUE DELIVERY TIMELINE")

        milestones = [
            ("30 Days:", "Gap assessment complete, baseline KPIs defined"),
            ("90 Days:", "Revenue dashboard live, response library v1 deployed, engineering embeds started"),
            ("180 Days:", "Automation POC in CI/CD, TPRM tiering operational, measurable TAT improvement"),
            ("365 Days:", "Full GRC-as-Code operational, executive dashboards, program maturity improvement demonstrated"),
        ]
        y = tl_y - 34
        for label, desc in milestones:
            self.c.setFont("Helvetica-Bold", 8)
            self.c.setFillColor(COLORS['accent_indigo'])
            self.c.drawString(MARGIN + 15, y, label)
            lw = pdfmetrics.stringWidth(label, "Helvetica-Bold", 8) + 5
            self.c.setFont("Helvetica", 8)
            self.c.setFillColor(COLORS['text_secondary'])
            self.c.drawString(MARGIN + 15 + lw, y, desc)
            y -= 13

        self._draw_footer()

    # ─── SLIDE 12: Next Steps & Ask ──────────────────────────────
    def slide_next_steps(self):
        self._new_slide(COLORS['bg_white'])

        # Accent top bar
        self.c.setFillColor(COLORS['accent_teal'])
        self.c.rect(0, HEIGHT - 4, WIDTH, 4, fill=1, stroke=0)

        self.c.setFont("Helvetica-Bold", 22)
        self.c.setFillColor(COLORS['text_primary'])
        self.c.drawString(MARGIN, HEIGHT - MARGIN - 0.3 * inch, "Immediate Next Steps & The Ask")
        self._draw_accent_bar(MARGIN, HEIGHT - MARGIN - 0.42 * inch, 50, 3, COLORS['accent_blue'])

        # Two columns: Next Steps + The Ask
        left_w = (WIDTH - 2 * MARGIN - 0.3 * inch) * 0.55
        right_x = MARGIN + left_w + 0.3 * inch
        right_w = (WIDTH - 2 * MARGIN - 0.3 * inch) * 0.45
        y_top = HEIGHT - MARGIN - 0.82 * inch

        # LEFT: Next Steps (numbered)
        self._draw_card(MARGIN, y_top - 3.5 * inch, left_w, 3.5 * inch, fill=COLORS['bg_white'], border=COLORS['gray_300'])
        self._draw_accent_bar(MARGIN, y_top - 2, left_w, 3, COLORS['accent_blue'])

        self.c.setFont("Helvetica-Bold", 12)
        self.c.setFillColor(COLORS['accent_blue'])
        self.c.drawString(MARGIN + 15, y_top - 22, "30-Day Action Plan")

        steps = [
            ("Week 1-2: Stakeholder Alignment", [
                "1:1 meetings with all direct reports to assess current state",
                "Alignment session with Chelsea Main and Damian King (peer leaders)",
                "Customer Trust team assessment and interim leadership plan",
                "Review all existing documentation, policies, and audit artifacts",
            ]),
            ("Week 2-3: Assessment & Baseline", [
                "Complete GRC maturity assessment against NIST CSF",
                "Map Customer Trust workflows and tool utilization",
                "Document TPRM, audit, and BC/DR current processes",
                "Identify all compliance obligations and certification requirements",
            ]),
            ("Week 3-4: Quick Win Launch", [
                "Initiate revenue tracking dashboard development",
                "Begin questionnaire response library cataloging (top 50 questions)",
                "Schedule first GRC-Engineering touchpoint meetings",
                "Present initial findings and refined roadmap to CISO",
            ]),
        ]

        y = y_top - 44
        for title, items in steps:
            self.c.setFont("Helvetica-Bold", 9)
            self.c.setFillColor(COLORS['text_primary'])
            self.c.drawString(MARGIN + 15, y, title)
            y -= 14
            for item in items:
                y = self._draw_bullet(item, MARGIN + 20, y, size=8, max_width=left_w - 48,
                                     bullet_color=COLORS['accent_blue'], leading=11)
                y -= 1
            y -= 8

        # RIGHT: The Ask
        self._draw_card(right_x, y_top - 2.0 * inch, right_w, 2.0 * inch, fill=COLORS['accent_light'], border=COLORS['accent_blue'])
        self._draw_accent_bar(right_x, y_top - 2, right_w, 3, COLORS['accent_indigo'])

        self.c.setFont("Helvetica-Bold", 12)
        self.c.setFillColor(COLORS['accent_indigo'])
        self.c.drawString(right_x + 15, y_top - 22, "The Ask from CISO")

        asks = [
            "Endorse this roadmap as the official GRC strategic plan for 2026",
            "Provide executive sponsorship for cross-functional initiatives with Engineering",
            "Approve budget for GRC platform evaluation and team training",
            "Support hiring for Technical GRC Engineer and Customer Trust lead roles",
            "Facilitate introductions to product/engineering leadership for GRC integration",
            "Monthly roadmap review cadence (30-min with CISO)",
        ]
        y = y_top - 42
        for ask in asks:
            y = self._draw_bullet(ask, right_x + 15, y, size=8.5, max_width=right_w - 38,
                                 bullet_color=COLORS['accent_indigo'], leading=12)
            y -= 4

        # Success criteria
        sc_y = y_top - 2.2 * inch
        self._draw_card(right_x, sc_y - 1.2 * inch, right_w, 1.2 * inch, fill=COLORS['green_light'], border=COLORS['green'])

        self.c.setFont("Helvetica-Bold", 11)
        self.c.setFillColor(COLORS['green'])
        self.c.drawString(right_x + 15, sc_y - 18, "Success Criteria (12 Months)")

        criteria = [
            "GRC maturity score improvement (baseline to target Tier 3)",
            "Customer Trust questionnaire TAT reduced by 60%",
            "Revenue attribution dashboard operational and reporting",
            "Policy-as-code deployed in at least one CI/CD pipeline",
            "100% of critical vendors assessed in TPRM framework",
        ]
        y = sc_y - 36
        for c_item in criteria:
            y = self._draw_bullet(c_item, right_x + 15, y, size=8, max_width=right_w - 38,
                                 bullet_color=COLORS['green'], leading=11)
            y -= 2

        # Final statement
        final_y = y_top - 3.5 * inch - 0.3 * inch
        self._draw_card(MARGIN, final_y - 0.45 * inch, WIDTH - 2 * MARGIN, 0.45 * inch, fill=COLORS['gray_100'], border=COLORS['gray_300'])
        self.c.setFont("Helvetica-Bold", 10)
        self.c.setFillColor(COLORS['accent_blue'])
        mid_x = WIDTH / 2
        self.c.drawCentredString(mid_x, final_y - 0.18 * inch,
            "This roadmap transforms GRC from a cost center into a strategic, revenue-enabling, engineering-integrated function.")
        self.c.setFont("Helvetica", 9)
        self.c.setFillColor(COLORS['text_muted'])
        self.c.drawCentredString(mid_x, final_y - 0.34 * inch,
            "The investment in modernization will deliver measurable ROI through revenue acceleration, risk reduction, and operational efficiency.")

        self._draw_footer()

    # ─── SLIDE: Appendix - Additional Best Practices ─────────────
    def slide_appendix_best_practices(self):
        self._new_slide(COLORS['bg_light'])

        self.c.setFont("Helvetica-Bold", 22)
        self.c.setFillColor(COLORS['text_primary'])
        self.c.drawString(MARGIN, HEIGHT - MARGIN - 0.3 * inch, "Appendix: Industry Best Practices & Frameworks")
        self._draw_accent_bar(MARGIN, HEIGHT - MARGIN - 0.42 * inch, 50, 3, COLORS['gray_500'])

        y_top = HEIGHT - MARGIN - 0.82 * inch
        col_w = (WIDTH - 2 * MARGIN - 0.15 * inch) / 2
        card_h = 1.8 * inch

        cards = [
            {
                'title': 'Framework Alignment',
                'color': COLORS['accent_blue'],
                'bg': COLORS['accent_light'],
                'items': [
                    "NIST Cybersecurity Framework (CSF) 2.0 - Primary maturity model and governance backbone",
                    "ISO 27001:2022 - ISMS alignment for certification maintenance and customer trust",
                    "SOC 2 Type II - Continued compliance with automated evidence collection",
                    "NIST SP 800-53 Rev. 5 - Control catalog for comprehensive security control mapping",
                    "FAIR (Factor Analysis of Information Risk) - Quantitative risk analysis methodology",
                ]
            },
            {
                'title': 'GRC Technology Trends',
                'color': COLORS['accent_teal'],
                'bg': COLORS['accent_teal_lt'],
                'items': [
                    "GRC-as-Code: Open Policy Agent (OPA), Rego, Terraform Sentinel, AWS Config Rules",
                    "Continuous Compliance: Real-time monitoring replacing point-in-time audits",
                    "AI-Assisted Trust: LLM-powered questionnaire completion and response suggestion",
                    "Unified GRC Platforms: Convergence of risk, compliance, audit, and vendor management",
                    "Trust Centers: Self-service customer-facing security posture transparency",
                ]
            },
            {
                'title': 'Organizational Best Practices',
                'color': COLORS['accent_indigo'],
                'bg': COLORS['purple_light'],
                'items': [
                    "Shift-Left Compliance: Embed compliance in SDLC, not post-deployment",
                    "Three Lines Model (IIA): Clear delineation of management, oversight, and assurance",
                    "Risk-Based Approach: Prioritize high-impact controls; deprioritize ceremonial compliance",
                    "Value-Driven GRC: Measure and report business outcomes, not just compliance status",
                    "Cross-Functional Integration: GRC as partner to Engineering, Product, Sales, and Legal",
                ]
            },
            {
                'title': 'Recommended Reading & Standards',
                'color': COLORS['green'],
                'bg': COLORS['green_light'],
                'items': [
                    "NIST SP 800-137: Information Security Continuous Monitoring (ISCM)",
                    "ISACA COBIT 2019: Governance and management of enterprise IT",
                    "IIA Three Lines Model: Updated guidance on organizational risk governance",
                    "CISA Cybersecurity Performance Goals: Baseline cybersecurity practices",
                    "Cloud Security Alliance CCM: Cloud-specific control framework mapping",
                ]
            },
        ]

        for i, card in enumerate(cards):
            col = i % 2
            row = i // 2
            x = MARGIN + col * (col_w + 0.15 * inch)
            y = y_top - row * (card_h + 0.12 * inch)
            self._draw_card(x, y - card_h, col_w, card_h, fill=card['bg'], border=COLORS['gray_300'])
            self._draw_accent_bar(x, y - 2, col_w, 3, card['color'])

            self.c.setFont("Helvetica-Bold", 10)
            self.c.setFillColor(card['color'])
            self.c.drawString(x + 12, y - 20, card['title'])

            by = y - 38
            for item in card['items']:
                by = self._draw_bullet(item, x + 12, by, size=7.5, max_width=col_w - 32,
                                      bullet_color=card['color'], leading=10.5)
                by -= 3

        self._draw_footer()

    # ─── Build all slides ────────────────────────────────────────
    def build(self):
        self.slide_title()
        self.slide_agenda()
        self.slide_executive_summary()
        self.slide_org_structure()
        self.slide_gaps()
        self.slide_roadmap_overview()
        self.slide_customer_trust()
        self.slide_grc_as_code()
        self.slide_metrics()
        self.slide_risks()
        self.slide_investment()
        self.slide_next_steps()
        self.slide_appendix_best_practices()
        self.c.save()
        print(f"Generated {self.page_num} slides")


if __name__ == "__main__":
    output_path = "/Users/jsn/Documents/GitHub/blog/GRC_Roadmap_2026.pdf"
    builder = SlideBuilder(output_path)
    builder.build()
    print(f"PDF saved to: {output_path}")

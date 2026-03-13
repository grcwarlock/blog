const pptxgen = require("pptxgenjs");

const pres = new pptxgen();
pres.layout = "LAYOUT_16x9";
pres.author = "Senior Director, GRC";
pres.title = "GRC Program Modernization Roadmap 2026";

// Register IBM Plex Mono fonts
// PptxGenJS embeds fonts by path - users need the font installed or provide paths
// Using the font name for system-installed fonts

// ─── Color Palette (Midnight Executive + Teal accents) ───
const C = {
  navy:       "1E2761",
  iceBlue:    "CADCFC",
  white:      "FFFFFF",
  offWhite:   "F7F8FA",
  warmWhite:  "FAFAF8",
  teal:       "0E7C86",
  tealLight:  "E0F5F5",
  blue:       "2B6CB0",
  blueLight:  "EBF4FF",
  indigo:     "4C51BF",
  indigoLight:"EDEDFF",
  green:      "276749",
  greenLight: "E8F5E9",
  orange:     "C05621",
  orangeLight:"FFF3E0",
  red:        "C53030",
  redLight:   "FFEBEE",
  purple:     "553C9A",
  purpleLight:"F3E8FF",
  textDark:   "1A1D23",
  textMed:    "4A5568",
  textLight:  "718096",
  gray100:    "F7FAFC",
  gray200:    "EDF2F7",
  gray300:    "E2E8F0",
  gray400:    "CBD5E0",
  gray700:    "4A5568",
  gray800:    "2D3748",
};

// Helper: fresh shadow factory
const cardShadow = () => ({ type: "outer", blur: 4, offset: 2, angle: 135, color: "000000", opacity: 0.08 });

// Helper: add footer to slide
function addFooter(slide, pageNum) {
  slide.addShape(pres.shapes.LINE, {
    x: 0.5, y: 5.15, w: 9.0, h: 0,
    line: { color: C.gray300, width: 0.5 }
  });
  slide.addText("CONFIDENTIAL  |  GRC Program Modernization Roadmap 2026", {
    x: 0.5, y: 5.2, w: 7, h: 0.3,
    fontSize: 7, color: C.textLight, fontFace: "Calibri"
  });
  if (pageNum) {
    slide.addText(String(pageNum), {
      x: 8.5, y: 5.2, w: 1, h: 0.3,
      fontSize: 7, color: C.textLight, fontFace: "Calibri", align: "right"
    });
  }
}

// Helper: slide title
function addTitle(slide, title, color) {
  slide.addText(title, {
    x: 0.6, y: 0.3, w: 8.8, h: 0.55,
    fontSize: 26, fontFace: "Georgia", bold: true, color: color || C.textDark, margin: 0
  });
}

// Helper: subtitle under title
function addSubtitle(slide, text) {
  slide.addText(text, {
    x: 0.6, y: 0.85, w: 8.8, h: 0.35,
    fontSize: 11, fontFace: "Calibri", color: C.textLight, margin: 0
  });
}

// ═══════════════════════════════════════════════════════════
// SLIDE 1: Title
// ═══════════════════════════════════════════════════════════
{
  const slide = pres.addSlide();
  slide.background = { color: C.navy };

  // Top accent bar
  slide.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: 0, w: 10, h: 0.06, fill: { color: C.teal }
  });

  // Left accent line
  slide.addShape(pres.shapes.RECTANGLE, {
    x: 0.6, y: 1.5, w: 0.04, h: 2.2, fill: { color: C.teal }
  });

  // Overline
  slide.addText("STRATEGIC INITIATIVE  |  2026", {
    x: 0.85, y: 1.5, w: 6, h: 0.35,
    fontSize: 11, fontFace: "Calibri", color: C.teal, charSpacing: 3, margin: 0
  });

  // Main title
  slide.addText("GRC Program\nModernization Roadmap", {
    x: 0.85, y: 1.9, w: 6, h: 1.3,
    fontSize: 36, fontFace: "Georgia", bold: true, color: C.white, margin: 0
  });

  // Subtitle
  slide.addText("From Compliance Function to Strategic Business Enabler", {
    x: 0.85, y: 3.3, w: 6, h: 0.4,
    fontSize: 13, fontFace: "Calibri", color: C.iceBlue, margin: 0
  });

  // Bottom info
  slide.addShape(pres.shapes.LINE, {
    x: 0.6, y: 4.5, w: 8.8, h: 0,
    line: { color: C.gray700, width: 0.5 }
  });
  slide.addText("Prepared for the CISO  |  March 2026  |  CONFIDENTIAL", {
    x: 0.6, y: 4.6, w: 8.8, h: 0.3,
    fontSize: 9, fontFace: "Calibri", color: C.textLight, margin: 0
  });

  // Right decorative stats area
  slide.addShape(pres.shapes.RECTANGLE, {
    x: 7.3, y: 1.2, w: 2.3, h: 3.0,
    fill: { color: C.teal, transparency: 15 }
  });

  const stats = [
    { val: "2026", label: "Transformation Year", y: 1.45 },
    { val: "4", label: "Strategic Phases", y: 2.2 },
    { val: "12", label: "Key Initiatives", y: 2.95 },
  ];
  stats.forEach(s => {
    slide.addText(s.val, {
      x: 7.3, y: s.y, w: 2.3, h: 0.4,
      fontSize: 28, fontFace: "Georgia", bold: true, color: C.white, align: "center", margin: 0
    });
    slide.addText(s.label, {
      x: 7.3, y: s.y + 0.38, w: 2.3, h: 0.25,
      fontSize: 9, fontFace: "Calibri", color: C.iceBlue, align: "center", margin: 0
    });
  });
}

// ═══════════════════════════════════════════════════════════
// SLIDE 2: Agenda
// ═══════════════════════════════════════════════════════════
{
  const slide = pres.addSlide();
  slide.background = { color: C.offWhite };
  addTitle(slide, "Agenda");
  addFooter(slide, 2);

  const items = [
    ["01", "Executive Summary", "Current state, vision, and strategic objectives"],
    ["02", "Organizational Structure", "Team roles, reporting lines, capability mapping"],
    ["03", "Critical Gaps Analysis", "GRC-Engineering disconnect, Customer Trust, maturity"],
    ["04", "Strategic Roadmap", "Q1-Q4 phased plan with milestones and deliverables"],
    ["05", "Customer Trust Transformation", "Revenue enablement, tooling, knowledge base"],
    ["06", "GRC-as-Code & Automation", "Policy-as-code, CI/CD integration, engineering partnership"],
    ["07", "Metrics & Value Framework", "KPIs, dashboards, business value measurement"],
    ["08", "Risks & Dependencies", "Implementation risks, resource needs, change management"],
    ["09", "Investment & ROI", "Resource requirements, expected returns, timeline"],
    ["10", "Next Steps & The Ask", "30-day action plan, CISO requests, success criteria"],
  ];

  const colW = 4.2;
  const rowH = 0.38;
  const startY = 1.15;
  const gapX = 0.35;

  items.forEach((item, i) => {
    const col = Math.floor(i / 5);
    const row = i % 5;
    const x = 0.6 + col * (colW + gapX);
    const y = startY + row * (rowH + 0.08);

    // Card bg
    slide.addShape(pres.shapes.RECTANGLE, {
      x: x, y: y, w: colW, h: rowH,
      fill: { color: C.white },
      shadow: cardShadow()
    });

    // Number badge
    const badgeColor = col === 0 ? C.blue : C.teal;
    slide.addShape(pres.shapes.RECTANGLE, {
      x: x + 0.1, y: y + 0.06, w: 0.32, h: 0.26,
      fill: { color: badgeColor }
    });
    slide.addText(item[0], {
      x: x + 0.1, y: y + 0.06, w: 0.32, h: 0.26,
      fontSize: 9, fontFace: "Calibri", bold: true, color: C.white, align: "center", valign: "middle", margin: 0
    });

    // Title
    slide.addText(item[1], {
      x: x + 0.52, y: y + 0.02, w: colW - 0.65, h: 0.18,
      fontSize: 10, fontFace: "Calibri", bold: true, color: C.textDark, margin: 0
    });
    // Description
    slide.addText(item[2], {
      x: x + 0.52, y: y + 0.19, w: colW - 0.65, h: 0.16,
      fontSize: 7.5, fontFace: "Calibri", color: C.textLight, margin: 0
    });
  });
}

// ═══════════════════════════════════════════════════════════
// SLIDE 3: Executive Summary
// ═══════════════════════════════════════════════════════════
{
  const slide = pres.addSlide();
  slide.background = { color: C.white };
  addTitle(slide, "Executive Summary");
  addFooter(slide, 3);

  const cardW = 4.25;
  const cardH = 3.1;
  const cardY = 1.1;
  const gap = 0.3;

  // Current State Card
  const lx = 0.6;
  slide.addShape(pres.shapes.RECTANGLE, {
    x: lx, y: cardY, w: cardW, h: cardH,
    fill: { color: C.redLight }, shadow: cardShadow()
  });
  slide.addShape(pres.shapes.RECTANGLE, {
    x: lx, y: cardY, w: cardW, h: 0.04, fill: { color: C.red }
  });
  slide.addText("CURRENT STATE", {
    x: lx + 0.2, y: cardY + 0.12, w: 3, h: 0.3,
    fontSize: 11, fontFace: "Calibri", bold: true, color: C.red, margin: 0
  });

  const currentBullets = [
    "GRC operates as isolated compliance function with no engineering integration",
    "Manual, check-the-box audit processes with no automation or policy-as-code",
    "Customer Trust uses fragmented tooling (Onboard, Conveyor, Trust Center)",
    "No revenue impact tracking despite handling deal-blocking questionnaires",
    "No GRC team members understand product, tech stack, or SDLC",
    "TPRM and Internal Audit lack standardized baselines and KPIs",
    "No existing roadmap, strategy, or maturity model in place",
  ];
  slide.addText(
    currentBullets.map((b, i) => ({
      text: b,
      options: { bullet: true, breakLine: i < currentBullets.length - 1, fontSize: 8.5, color: C.textMed }
    })),
    { x: lx + 0.2, y: cardY + 0.45, w: cardW - 0.4, h: cardH - 0.6, fontFace: "Calibri", paraSpaceAfter: 4, valign: "top" }
  );

  // Target State Card
  const rx = lx + cardW + gap;
  slide.addShape(pres.shapes.RECTANGLE, {
    x: rx, y: cardY, w: cardW, h: cardH,
    fill: { color: C.greenLight }, shadow: cardShadow()
  });
  slide.addShape(pres.shapes.RECTANGLE, {
    x: rx, y: cardY, w: cardW, h: 0.04, fill: { color: C.green }
  });
  slide.addText("TARGET STATE (END OF 2026)", {
    x: rx + 0.2, y: cardY + 0.12, w: 3.5, h: 0.3,
    fontSize: 11, fontFace: "Calibri", bold: true, color: C.green, margin: 0
  });

  const targetBullets = [
    "GRC embedded in engineering with policy-as-code in CI/CD pipelines",
    "Automated compliance evidence collection and continuous monitoring",
    "Unified Customer Trust platform with revenue-linked dashboards",
    "Standardized response library reducing questionnaire TAT by 60%",
    "Technical GRC expertise integrated into product and sprint planning",
    "Risk-quantified TPRM with automated vendor assessments and tiering",
    "Mature, metrics-driven program aligned to NIST CSF and ISO 27001",
  ];
  slide.addText(
    targetBullets.map((b, i) => ({
      text: b,
      options: { bullet: true, breakLine: i < targetBullets.length - 1, fontSize: 8.5, color: C.textMed }
    })),
    { x: rx + 0.2, y: cardY + 0.45, w: cardW - 0.4, h: cardH - 0.6, fontFace: "Calibri", paraSpaceAfter: 4, valign: "top" }
  );

  // Vision bar at bottom
  slide.addShape(pres.shapes.RECTANGLE, {
    x: 0.6, y: 4.4, w: 8.8, h: 0.6,
    fill: { color: C.blueLight }
  });
  slide.addText([
    { text: "STRATEGIC VISION:  ", options: { bold: true, color: C.blue, fontSize: 10 } },
    { text: "Transform GRC from a reactive cost center into a proactive, revenue-enabling, engineering-integrated strategic function.", options: { color: C.textDark, fontSize: 10 } }
  ], { x: 0.8, y: 4.45, w: 8.4, h: 0.5, fontFace: "Calibri", valign: "middle" });
}

// ═══════════════════════════════════════════════════════════
// SLIDE 4: Organizational Structure
// ═══════════════════════════════════════════════════════════
{
  const slide = pres.addSlide();
  slide.background = { color: C.offWhite };
  addTitle(slide, "Organizational Structure & Team");
  addFooter(slide, 4);

  // Using a table-based org chart for clean layout
  const boxW = 1.7;
  const boxH = 0.48;
  const smallBoxW = 1.45;
  const smallBoxH = 0.42;

  function orgBox(slide, x, y, name, role, color, w, h) {
    w = w || boxW; h = h || boxH;
    slide.addShape(pres.shapes.RECTANGLE, {
      x, y, w, h, fill: { color: C.white }, shadow: cardShadow()
    });
    slide.addShape(pres.shapes.RECTANGLE, {
      x, y, w, h: 0.04, fill: { color }
    });
    slide.addText(name, {
      x, y: y + 0.07, w, h: 0.2,
      fontSize: 8.5, fontFace: "Calibri", bold: true, color: C.textDark, align: "center", margin: 0
    });
    slide.addText(role, {
      x, y: y + 0.25, w, h: 0.16,
      fontSize: 7, fontFace: "Calibri", color: C.textLight, align: "center", margin: 0
    });
  }

  // Connector lines (simple vertical + horizontal)
  function vLine(slide, x, y1, y2) {
    slide.addShape(pres.shapes.LINE, {
      x, y: y1, w: 0, h: y2 - y1,
      line: { color: C.gray400, width: 0.8 }
    });
  }
  function hLine(slide, x1, x2, y) {
    slide.addShape(pres.shapes.LINE, {
      x: x1, y, w: x2 - x1, h: 0,
      line: { color: C.gray400, width: 0.8 }
    });
  }

  // CISO (top center)
  const cx = 5.0 - boxW / 2;
  orgBox(slide, cx, 1.0, "CISO", "Chief Information Security Officer", C.indigo);

  // Vertical line from CISO down
  vLine(slide, 5.0, 1.0 + boxH, 1.7);
  // Horizontal span for 3 reports
  hLine(slide, 1.75, 8.25, 1.7);

  // Three peer directors
  const peerY = 1.7;
  vLine(slide, 1.75, 1.7, 1.85);
  vLine(slide, 5.0, 1.7, 1.85);
  vLine(slide, 8.25, 1.7, 1.85);

  orgBox(slide, 1.75 - boxW / 2, 1.85, "Chelsea Main", "Security Engineering", C.gray400);
  orgBox(slide, 5.0 - boxW / 2, 1.85, "You (Sr. Dir. GRC)", "GRC Program Lead", C.teal);
  orgBox(slide, 8.25 - boxW / 2, 1.85, "Damian King", "Security Operations", C.gray400);

  // Lines from You down to reports
  const youBottom = 1.85 + boxH;
  vLine(slide, 5.0, youBottom, youBottom + 0.2);
  hLine(slide, 1.7, 8.3, youBottom + 0.2);

  // Direct reports
  const drY = youBottom + 0.2;
  const drPositions = [1.7, 3.6, 5.5, 7.55];
  drPositions.forEach(xp => {
    vLine(slide, xp, drY, drY + 0.15);
  });

  const reports = [
    { x: 1.7, name: "Steve Hammonds", role: "BC/DR" },
    { x: 3.6, name: "Doug Matkins", role: "TPRM" },
    { x: 5.5, name: "Janet De Lara", role: "Internal Audit" },
    { x: 7.55, name: "Customer Trust", role: "Trust & Questionnaires" },
  ];
  reports.forEach(r => {
    orgBox(slide, r.x - smallBoxW / 2, drY + 0.15, r.name, r.role, C.teal, smallBoxW, smallBoxH);
  });

  // Customer Trust sub-team
  const ctBottom = drY + 0.15 + smallBoxH;
  vLine(slide, 7.55, ctBottom, ctBottom + 0.15);
  hLine(slide, 6.2, 8.9, ctBottom + 0.15);

  const ctMembers = [
    { x: 6.2, name: "Eni Smigielska" },
    { x: 7.1, name: "Russ Johnson" },
    { x: 8.0, name: "Marcin Lachowicz" },
    { x: 8.9, name: "Amine Gherabi" },
  ];
  ctMembers.forEach(m => {
    vLine(slide, m.x, ctBottom + 0.15, ctBottom + 0.25);
    slide.addShape(pres.shapes.RECTANGLE, {
      x: m.x - 0.5, y: ctBottom + 0.25, w: 1.0, h: 0.28,
      fill: { color: C.white }, shadow: cardShadow()
    });
    slide.addText(m.name, {
      x: m.x - 0.5, y: ctBottom + 0.25, w: 1.0, h: 0.28,
      fontSize: 7, fontFace: "Calibri", color: C.textDark, align: "center", valign: "middle", margin: 0
    });
  });

  // Governance sub-team (under Doug Matkins)
  const govY = ctBottom + 0.25;
  vLine(slide, 2.5, drY + 0.15 + smallBoxH, govY);
  slide.addShape(pres.shapes.RECTANGLE, {
    x: 1.7, y: govY, w: 1.6, h: 0.42,
    fill: { color: C.tealLight }, shadow: cardShadow()
  });
  slide.addText("Governance (Paolo DiRosa)", {
    x: 1.7, y: govY + 0.02, w: 1.6, h: 0.2,
    fontSize: 7.5, fontFace: "Calibri", bold: true, color: C.teal, align: "center", margin: 0
  });
  slide.addText("Barbara A-O, Mateusz Toczek", {
    x: 1.7, y: govY + 0.2, w: 1.6, h: 0.18,
    fontSize: 6.5, fontFace: "Calibri", color: C.textLight, align: "center", margin: 0
  });

  // Key observation bar
  slide.addShape(pres.shapes.RECTANGLE, {
    x: 0.6, y: 4.65, w: 8.8, h: 0.45,
    fill: { color: C.orangeLight }
  });
  slide.addText([
    { text: "KEY OBSERVATION:  ", options: { bold: true, color: C.orange, fontSize: 9 } },
    { text: "No technical/engineering expertise within GRC team. Customer Trust lacks a dedicated lead since Jodi's departure. Peer alignment with Security Engineering is critical.", options: { color: C.textMed, fontSize: 9 } }
  ], { x: 0.8, y: 4.68, w: 8.4, h: 0.4, fontFace: "Calibri", valign: "middle" });
}

// ═══════════════════════════════════════════════════════════
// SLIDE 5: Critical Gaps Analysis
// ═══════════════════════════════════════════════════════════
{
  const slide = pres.addSlide();
  slide.background = { color: C.white };
  addTitle(slide, "Critical Gaps Analysis");
  addFooter(slide, 5);

  const gaps = [
    {
      title: "GRC-Engineering Disconnect",
      severity: "CRITICAL", sevColor: C.red, bg: C.redLight,
      items: [
        "No GRC personnel understand product, tech stack, or SDLC",
        "Not invited to sprint planning or architecture reviews",
        "Manual audit processes, no automation or continuous monitoring",
        "No embedded GRC presence in engineering org",
        "Compliance is after-the-fact, not integrated",
      ],
      impact: "Findings discovered late; engineering views GRC as blocker"
    },
    {
      title: "Customer Trust Fragmentation",
      severity: "HIGH", sevColor: C.orange, bg: C.orangeLight,
      items: [
        "3 fragmented tools: Onboard, Conveyor, Trust Center",
        "Work in Jira but no ROI or revenue tracking",
        "Deal numbers visible, no revenue impact metrics",
        "No standardized legal-approved answer library",
        "No dedicated lead after Jodi's departure",
      ],
      impact: "Slower deal cycles, duplicated effort, no demonstrated value"
    },
    {
      title: "Program Maturity & Operations",
      severity: "HIGH", sevColor: C.orange, bg: C.orangeLight,
      items: [
        "No roadmap, maturity model, or strategic plan existed",
        "TPRM/Audit lack baselines and performance KPIs",
        "BC/DR needs validation against current threats",
        "No risk quantification (e.g. FAIR) methodology",
        "Governance not integrated with risk/compliance workflows",
      ],
      impact: "Reactive posture; cannot prioritize investments"
    },
  ];

  const cardW = 2.8;
  const cardH = 3.5;
  const startX = 0.6;
  const gapX = 0.15;
  const cardY = 1.1;

  gaps.forEach((g, i) => {
    const x = startX + i * (cardW + gapX);

    slide.addShape(pres.shapes.RECTANGLE, {
      x, y: cardY, w: cardW, h: cardH,
      fill: { color: g.bg }, shadow: cardShadow()
    });
    // Top accent
    slide.addShape(pres.shapes.RECTANGLE, {
      x, y: cardY, w: cardW, h: 0.04, fill: { color: g.sevColor }
    });

    // Severity badge
    slide.addShape(pres.shapes.RECTANGLE, {
      x: x + cardW - 0.85, y: cardY + 0.1, w: 0.75, h: 0.22,
      fill: { color: g.sevColor }
    });
    slide.addText(g.severity, {
      x: x + cardW - 0.85, y: cardY + 0.1, w: 0.75, h: 0.22,
      fontSize: 7, fontFace: "Calibri", bold: true, color: C.white, align: "center", valign: "middle", margin: 0
    });

    // Title
    slide.addText(g.title, {
      x: x + 0.15, y: cardY + 0.1, w: cardW - 1.05, h: 0.3,
      fontSize: 10.5, fontFace: "Calibri", bold: true, color: C.textDark, margin: 0
    });

    // Bullets
    slide.addText(
      g.items.map((b, j) => ({
        text: b,
        options: { bullet: true, breakLine: j < g.items.length - 1, fontSize: 8, color: C.textMed }
      })),
      { x: x + 0.15, y: cardY + 0.45, w: cardW - 0.3, h: 2.0, fontFace: "Calibri", paraSpaceAfter: 4, valign: "top" }
    );

    // Impact box at bottom
    slide.addShape(pres.shapes.RECTANGLE, {
      x: x + 0.1, y: cardY + cardH - 0.6, w: cardW - 0.2, h: 0.5,
      fill: { color: C.white }, shadow: cardShadow()
    });
    slide.addText("BUSINESS IMPACT", {
      x: x + 0.2, y: cardY + cardH - 0.58, w: cardW - 0.4, h: 0.18,
      fontSize: 7, fontFace: "Calibri", bold: true, color: g.sevColor, margin: 0
    });
    slide.addText(g.impact, {
      x: x + 0.2, y: cardY + cardH - 0.4, w: cardW - 0.4, h: 0.28,
      fontSize: 7.5, fontFace: "Calibri", color: C.textMed, margin: 0
    });
  });
}

// ═══════════════════════════════════════════════════════════
// SLIDE 6: Strategic Roadmap Overview
// ═══════════════════════════════════════════════════════════
{
  const slide = pres.addSlide();
  slide.background = { color: C.white };
  addTitle(slide, "Strategic Roadmap Overview");
  addFooter(slide, 6);

  // Timeline bar
  const phases = [
    { label: "Q1 2026", color: C.blue },
    { label: "Q2 2026", color: C.teal },
    { label: "Q3 2026", color: C.indigo },
    { label: "Q4 2026", color: C.green },
  ];
  const barY = 1.0;
  const barW = 2.15;
  const barH = 0.32;
  phases.forEach((p, i) => {
    const x = 0.6 + i * (barW + 0.06);
    slide.addShape(pres.shapes.RECTANGLE, {
      x, y: barY, w: barW, h: barH, fill: { color: p.color }
    });
    slide.addText(p.label, {
      x, y: barY, w: barW, h: barH,
      fontSize: 10, fontFace: "Calibri", bold: true, color: C.white, align: "center", valign: "middle", margin: 0
    });
  });

  // Phase detail cards
  const details = [
    {
      title: "Phase 1: Foundation", subtitle: "Assess & Baseline", color: C.blue, bg: C.blueLight,
      items: [
        "GRC maturity assessment (NIST CSF)",
        "Map Customer Trust tools & workflows",
        "Document TPRM/audit/BC-DR processes",
        "Team capability & skill gap analysis",
        "Tech stack education for GRC team",
        "Define KPI framework and baselines",
      ]
    },
    {
      title: "Phase 2: Quick Wins", subtitle: "Deliver Visible Value", color: C.teal, bg: C.tealLight,
      items: [
        "Launch revenue-tracking dashboard",
        "Build questionnaire response library",
        "Embed GRC in engineering meetings",
        "TPRM vendor tiering & risk scoring",
        "Audit cadence + internal KPI reporting",
        "Deploy initial automated evidence collection",
      ]
    },
    {
      title: "Phase 3: Automation", subtitle: "Scale Through Technology", color: C.indigo, bg: C.indigoLight,
      items: [
        "Policy-as-code in CI/CD pipeline",
        "Automate compliance evidence gathering",
        "Consolidate Customer Trust tooling",
        "Launch continuous control monitoring",
        "Integrate risk quantification (FAIR)",
        "Build GRC-Engineering workflows",
      ]
    },
    {
      title: "Phase 4: Optimize", subtitle: "Mature & Demonstrate Value", color: C.green, bg: C.greenLight,
      items: [
        "Full GRC-as-Code maturity",
        "Executive value dashboards (risk+revenue)",
        "Proactive risk identification",
        "Advanced vendor risk automation",
        "Maturity re-assessment & 2027 planning",
        "Team certification program complete",
      ]
    },
  ];

  const dCardW = 2.15;
  const dCardH = 3.25;
  const dCardY = 1.55;

  details.forEach((d, i) => {
    const x = 0.6 + i * (dCardW + 0.06);

    slide.addShape(pres.shapes.RECTANGLE, {
      x, y: dCardY, w: dCardW, h: dCardH,
      fill: { color: d.bg }, shadow: cardShadow()
    });
    slide.addShape(pres.shapes.RECTANGLE, {
      x, y: dCardY, w: dCardW, h: 0.04, fill: { color: d.color }
    });

    slide.addText(d.title, {
      x: x + 0.12, y: dCardY + 0.1, w: dCardW - 0.24, h: 0.22,
      fontSize: 9.5, fontFace: "Calibri", bold: true, color: d.color, margin: 0
    });
    slide.addText(d.subtitle, {
      x: x + 0.12, y: dCardY + 0.3, w: dCardW - 0.24, h: 0.18,
      fontSize: 7.5, fontFace: "Calibri", color: C.textLight, margin: 0
    });

    slide.addText(
      d.items.map((b, j) => ({
        text: b,
        options: { bullet: true, breakLine: j < d.items.length - 1, fontSize: 8, color: C.textMed }
      })),
      { x: x + 0.12, y: dCardY + 0.55, w: dCardW - 0.24, h: dCardH - 0.7, fontFace: "Calibri", paraSpaceAfter: 5, valign: "top" }
    );
  });
}

// ═══════════════════════════════════════════════════════════
// SLIDE 7: Customer Trust Transformation
// ═══════════════════════════════════════════════════════════
{
  const slide = pres.addSlide();
  slide.background = { color: C.white };
  addTitle(slide, "Customer Trust Transformation");
  addSubtitle(slide, "Evolve from reactive questionnaire processing to proactive revenue enablement");
  addFooter(slide, 7);

  const cols = [
    {
      title: "Tooling Consolidation", color: C.blue, bg: C.blueLight,
      items: [
        { label: "Current:", text: "Onboard, Conveyor, Trust Center - fragmented" },
        { label: "Target:", text: "Single pane of glass for all trust activities" },
        { label: "Action:", text: "Evaluate consolidation (Vanta, Drata, SafeBase)" },
        { label: "Action:", text: "Centralize artifacts in one customer portal" },
        { label: "Metric:", text: "Reduce tools from 3+ to 1-2 platforms" },
      ]
    },
    {
      title: "Revenue Dashboard", color: C.teal, bg: C.tealLight,
      items: [
        { label: "Current:", text: "Deal numbers in Jira, no revenue impact" },
        { label: "Target:", text: "Real-time dashboard linking to deal value" },
        { label: "Action:", text: "Integrate Jira with CRM for attribution" },
        { label: "Action:", text: "Track TAT, SLA, deal-stage correlation" },
        { label: "Metric:", text: "Demonstrate revenue enablement value" },
      ]
    },
    {
      title: "Knowledge Base", color: C.indigo, bg: C.indigoLight,
      items: [
        { label: "Current:", text: "Ad-hoc responses, no standard library" },
        { label: "Target:", text: "200+ legal-approved response library" },
        { label: "Action:", text: "Catalog top recurring questions" },
        { label: "Action:", text: "Implement AI-assisted completion" },
        { label: "Metric:", text: "60% reduction in turnaround time" },
      ]
    },
  ];

  const colW = 2.8;
  const colH = 2.4;
  const colY = 1.3;

  cols.forEach((col, i) => {
    const x = 0.6 + i * (colW + 0.15);

    slide.addShape(pres.shapes.RECTANGLE, {
      x, y: colY, w: colW, h: colH,
      fill: { color: col.bg }, shadow: cardShadow()
    });
    slide.addShape(pres.shapes.RECTANGLE, {
      x, y: colY, w: colW, h: 0.04, fill: { color: col.color }
    });
    slide.addText(col.title, {
      x: x + 0.15, y: colY + 0.1, w: colW - 0.3, h: 0.25,
      fontSize: 11, fontFace: "Calibri", bold: true, color: col.color, margin: 0
    });

    let textArr = [];
    col.items.forEach((item, j) => {
      textArr.push({ text: item.label + " ", options: { bold: true, color: col.color, fontSize: 8, breakLine: false } });
      textArr.push({ text: item.text, options: { color: C.textMed, fontSize: 8, breakLine: j < col.items.length - 1 } });
    });
    slide.addText(textArr, {
      x: x + 0.15, y: colY + 0.4, w: colW - 0.3, h: colH - 0.55,
      fontFace: "Calibri", paraSpaceAfter: 6, valign: "top"
    });
  });

  // KPI bar
  const kpiY = 3.9;
  slide.addShape(pres.shapes.RECTANGLE, {
    x: 0.6, y: kpiY, w: 8.8, h: 0.95,
    fill: { color: C.gray100 }, shadow: cardShadow()
  });

  const kpis = [
    { val: "60%", label: "TAT\nReduction", color: C.teal },
    { val: "$TBD", label: "Revenue\nEnabled/Qtr", color: C.blue },
    { val: "95%", label: "SLA\nCompliance", color: C.indigo },
    { val: "1-2", label: "Consolidated\nPlatforms", color: C.green },
    { val: "200+", label: "Standardized\nResponses", color: C.purple },
  ];
  const kpiW = 8.8 / kpis.length;
  kpis.forEach((k, i) => {
    const kx = 0.6 + i * kpiW;
    slide.addText(k.val, {
      x: kx, y: kpiY + 0.05, w: kpiW, h: 0.4,
      fontSize: 22, fontFace: "Georgia", bold: true, color: k.color, align: "center", margin: 0
    });
    slide.addText(k.label, {
      x: kx, y: kpiY + 0.48, w: kpiW, h: 0.4,
      fontSize: 7.5, fontFace: "Calibri", color: C.textLight, align: "center", margin: 0
    });
  });
}

// ═══════════════════════════════════════════════════════════
// SLIDE 8: GRC-as-Code & Engineering Integration
// ═══════════════════════════════════════════════════════════
{
  const slide = pres.addSlide();
  slide.background = { color: C.offWhite };
  addTitle(slide, "GRC-as-Code & Engineering Integration");
  addFooter(slide, 8);

  const leftW = 4.55;
  const rightX = 5.3;
  const rightW = 4.3;
  const topY = 1.0;

  // LEFT: Pipeline visual card
  slide.addShape(pres.shapes.RECTANGLE, {
    x: 0.6, y: topY, w: leftW, h: 2.3,
    fill: { color: C.white }, shadow: cardShadow()
  });
  slide.addText("Policy-as-Code in CI/CD Pipeline", {
    x: 0.8, y: topY + 0.08, w: leftW - 0.4, h: 0.3,
    fontSize: 11, fontFace: "Calibri", bold: true, color: C.indigo, margin: 0
  });

  // Pipeline stages
  const stages = [
    { name: "Code\nCommit", color: C.gray700 },
    { name: "Policy\nCheck", color: C.indigo },
    { name: "Security\nScan", color: C.blue },
    { name: "Evidence\nLog", color: C.teal },
    { name: "Deploy", color: C.green },
  ];
  const stageW = 0.7;
  const stageH = 0.42;
  const stageY = topY + 0.5;
  const stageGap = 0.15;
  const stageStartX = 0.85;

  stages.forEach((s, i) => {
    const sx = stageStartX + i * (stageW + stageGap);
    slide.addShape(pres.shapes.RECTANGLE, {
      x: sx, y: stageY, w: stageW, h: stageH,
      fill: { color: s.color }
    });
    slide.addText(s.name, {
      x: sx, y: stageY, w: stageW, h: stageH,
      fontSize: 7, fontFace: "Calibri", bold: true, color: C.white, align: "center", valign: "middle", margin: 0
    });
    // Arrow
    if (i < stages.length - 1) {
      slide.addText("\u25B6", {
        x: sx + stageW, y: stageY, w: stageGap, h: stageH,
        fontSize: 8, color: C.gray400, align: "center", valign: "middle", margin: 0
      });
    }
  });

  // Strategy bullets
  const stratBullets = [
    "Partner with Chelsea Main (Security Eng) on pipeline integration",
    "Implement OPA with Rego policies for automated compliance",
    "Auto-generate evidence from CI/CD execution logs",
    "GRC-friendly dashboards from engineering telemetry",
  ];
  slide.addText(
    stratBullets.map((b, i) => ({
      text: b,
      options: { bullet: true, breakLine: i < stratBullets.length - 1, fontSize: 8, color: C.textMed }
    })),
    { x: 0.8, y: topY + 1.1, w: leftW - 0.4, h: 1.1, fontFace: "Calibri", paraSpaceAfter: 4, valign: "top" }
  );

  // RIGHT: Engineering Integration Phases
  slide.addShape(pres.shapes.RECTANGLE, {
    x: rightX, y: topY, w: rightW, h: 2.3,
    fill: { color: C.white }, shadow: cardShadow()
  });
  slide.addText("Engineering Integration Phases", {
    x: rightX + 0.2, y: topY + 0.08, w: rightW - 0.4, h: 0.3,
    fontSize: 11, fontFace: "Calibri", bold: true, color: C.blue, margin: 0
  });

  const intPhases = [
    {
      title: "Phase 1: Learn", color: C.blue,
      items: ["Tech stack education (architecture, languages, cloud)", "Shadow standups and sprint planning", "Map compliance to engineering workflows"]
    },
    {
      title: "Phase 2: Embed", color: C.teal,
      items: ["GRC liaison in architecture reviews", "Bi-weekly GRC-Engineering working group", "Shared Slack channels and documentation"]
    },
    {
      title: "Phase 3: Automate", color: C.indigo,
      items: ["Policy-as-code in CI/CD pipelines", "Automated evidence replaces manual audits", "Self-service compliance for engineering"]
    },
  ];

  let phaseY = topY + 0.4;
  intPhases.forEach((p) => {
    // Accent bar
    slide.addShape(pres.shapes.RECTANGLE, {
      x: rightX + 0.2, y: phaseY, w: 0.04, h: 0.55, fill: { color: p.color }
    });
    slide.addText(p.title, {
      x: rightX + 0.35, y: phaseY - 0.02, w: rightW - 0.6, h: 0.2,
      fontSize: 9, fontFace: "Calibri", bold: true, color: p.color, margin: 0
    });
    slide.addText(
      p.items.map((b, i) => ({
        text: b,
        options: { bullet: true, breakLine: i < p.items.length - 1, fontSize: 7.5, color: C.textMed }
      })),
      { x: rightX + 0.35, y: phaseY + 0.17, w: rightW - 0.6, h: 0.4, fontFace: "Calibri", paraSpaceAfter: 2, valign: "top" }
    );
    phaseY += 0.62;
  });

  // Bottom: Best practices bar
  const bpY = 3.55;
  slide.addShape(pres.shapes.RECTANGLE, {
    x: 0.6, y: bpY, w: 8.8, h: 1.4,
    fill: { color: C.blueLight }, shadow: cardShadow()
  });
  slide.addText("INDUSTRY BEST PRACTICES - GRC AUTOMATION", {
    x: 0.8, y: bpY + 0.08, w: 8.4, h: 0.25,
    fontSize: 10, fontFace: "Calibri", bold: true, color: C.blue, margin: 0
  });

  const bps = [
    { label: "Shift-Left Compliance:", text: "Integrate checks early in SDLC, not at deployment gate" },
    { label: "Continuous Compliance:", text: "Replace point-in-time audits with real-time monitoring (NIST SP 800-137)" },
    { label: "Evidence-as-Code:", text: "Generate audit evidence from infrastructure-as-code and CI/CD logs" },
    { label: "Risk-Based Prioritization:", text: "Use FAIR or similar quantitative models to prioritize by business impact" },
  ];

  let bpTextArr = [];
  bps.forEach((bp, i) => {
    bpTextArr.push({ text: bp.label + " ", options: { bold: true, color: C.indigo, fontSize: 8.5, breakLine: false } });
    bpTextArr.push({ text: bp.text, options: { color: C.textMed, fontSize: 8.5, breakLine: i < bps.length - 1 } });
  });
  slide.addText(bpTextArr, {
    x: 0.8, y: bpY + 0.35, w: 8.4, h: 1.0,
    fontFace: "Calibri", paraSpaceAfter: 5, valign: "top"
  });
}

// ═══════════════════════════════════════════════════════════
// SLIDE 9: Metrics & Value Framework
// ═══════════════════════════════════════════════════════════
{
  const slide = pres.addSlide();
  slide.background = { color: C.white };
  addTitle(slide, "Metrics & Value Framework");
  addFooter(slide, 9);

  const categories = [
    {
      title: "Revenue & Business Value", icon: "$", color: C.teal, bg: C.tealLight,
      metrics: [
        ["Revenue Enabled", "Deal value for completed questionnaires/quarter"],
        ["Questionnaire TAT", "Avg turnaround time (target: <5 business days)"],
        ["Deal Acceleration", "Reduction in sales cycle days"],
        ["Cost Avoidance", "Estimated regulatory fines/breaches avoided"],
      ]
    },
    {
      title: "Operational Excellence", icon: "O", color: C.blue, bg: C.blueLight,
      metrics: [
        ["Automation Rate", "% evidence collected automatically vs. manually"],
        ["Audit Readiness", "Time to produce full evidence package"],
        ["TPRM Coverage", "% of vendors assessed within risk framework"],
        ["Control Effectiveness", "% controls passing continuous monitoring"],
      ]
    },
    {
      title: "Risk & Maturity", icon: "R", color: C.indigo, bg: C.indigoLight,
      metrics: [
        ["Program Maturity", "NIST CSF maturity score (target: Tier 3)"],
        ["Risk Posture", "Quantified risk trend (FAIR methodology)"],
        ["Finding Closure", "Mean time to remediate findings"],
        ["Policy Currency", "% policies reviewed within cycle"],
      ]
    },
  ];

  const colW = 2.8;
  const colH = 3.35;
  const colY = 1.0;

  categories.forEach((cat, i) => {
    const x = 0.6 + i * (colW + 0.15);

    slide.addShape(pres.shapes.RECTANGLE, {
      x, y: colY, w: colW, h: colH,
      fill: { color: cat.bg }, shadow: cardShadow()
    });
    slide.addShape(pres.shapes.RECTANGLE, {
      x, y: colY, w: colW, h: 0.04, fill: { color: cat.color }
    });

    // Icon circle
    slide.addShape(pres.shapes.OVAL, {
      x: x + 0.15, y: colY + 0.12, w: 0.3, h: 0.3, fill: { color: cat.color }
    });
    slide.addText(cat.icon, {
      x: x + 0.15, y: colY + 0.12, w: 0.3, h: 0.3,
      fontSize: 12, fontFace: "Georgia", bold: true, color: C.white, align: "center", valign: "middle", margin: 0
    });

    slide.addText(cat.title, {
      x: x + 0.55, y: colY + 0.13, w: colW - 0.75, h: 0.28,
      fontSize: 11, fontFace: "Calibri", bold: true, color: cat.color, margin: 0, valign: "middle"
    });

    let my = colY + 0.55;
    cat.metrics.forEach(([name, desc]) => {
      slide.addText(name, {
        x: x + 0.15, y: my, w: colW - 0.3, h: 0.2,
        fontSize: 9, fontFace: "Calibri", bold: true, color: C.textDark, margin: 0
      });
      slide.addText(desc, {
        x: x + 0.15, y: my + 0.18, w: colW - 0.3, h: 0.3,
        fontSize: 7.5, fontFace: "Calibri", color: C.textLight, margin: 0
      });
      my += 0.6;
    });
  });

  // Dashboard callout
  slide.addShape(pres.shapes.RECTANGLE, {
    x: 0.6, y: 4.55, w: 8.8, h: 0.5,
    fill: { color: C.gray100 }
  });
  slide.addText([
    { text: "DASHBOARD DELIVERY:  ", options: { bold: true, color: C.blue, fontSize: 9 } },
    { text: "Executive dashboard (monthly CISO)  |  Operational dashboard (daily team use)  |  Customer Trust revenue dashboard (sales alignment)", options: { color: C.textMed, fontSize: 9 } }
  ], { x: 0.8, y: 4.58, w: 8.4, h: 0.44, fontFace: "Calibri", valign: "middle" });
}

// ═══════════════════════════════════════════════════════════
// SLIDE 10: Risks & Dependencies
// ═══════════════════════════════════════════════════════════
{
  const slide = pres.addSlide();
  slide.background = { color: C.offWhite };
  addTitle(slide, "Risks, Dependencies & Change Management");
  addFooter(slide, 10);

  // Risk table using addTable
  const headerOpts = { fill: { color: C.gray800 }, color: C.white, bold: true, fontSize: 7.5, fontFace: "Calibri", align: "center", valign: "middle" };

  const risks = [
    ["R1", "Engineering resistance to GRC integration", "Med", "High", "Start with value-add automation, not mandates. CISO sponsorship."],
    ["R2", "Insufficient budget for platform/tooling", "Med", "High", "ROI business case from revenue data. Phase investments."],
    ["R3", "Team skill gaps delay GRC-as-Code", "High", "Med", "Partner with Security Eng. External training. Targeted hires."],
    ["R4", "Customer Trust capacity during transformation", "Med", "Med", "Protect BAU capacity. Automate low-value tasks first."],
    ["R5", "Nathan's return creates role ambiguity", "Low", "High", "Document decisions, maintain CISO transparency."],
    ["R6", "Tool consolidation disrupts Customer Trust SLAs", "Med", "Med", "Parallel run during migration. Phased rollout."],
  ];

  const tableData = [
    [
      { text: "ID", options: headerOpts },
      { text: "RISK DESCRIPTION", options: headerOpts },
      { text: "LIKELIHOOD", options: headerOpts },
      { text: "IMPACT", options: headerOpts },
      { text: "MITIGATION STRATEGY", options: headerOpts },
    ],
    ...risks.map((r, i) => {
      const rowFill = i % 2 === 0 ? C.white : C.gray100;
      const likeColor = r[2] === "High" ? C.red : (r[2] === "Med" ? C.orange : C.green);
      const impColor = r[3] === "High" ? C.red : (r[3] === "Med" ? C.orange : C.green);
      return [
        { text: r[0], options: { fill: { color: rowFill }, bold: true, fontSize: 8, color: C.red, align: "center", valign: "middle" } },
        { text: r[1], options: { fill: { color: rowFill }, fontSize: 8, color: C.textMed, valign: "middle" } },
        { text: r[2], options: { fill: { color: rowFill }, bold: true, fontSize: 8, color: likeColor, align: "center", valign: "middle" } },
        { text: r[3], options: { fill: { color: rowFill }, bold: true, fontSize: 8, color: impColor, align: "center", valign: "middle" } },
        { text: r[4], options: { fill: { color: rowFill }, fontSize: 8, color: C.textMed, valign: "middle" } },
      ];
    })
  ];

  slide.addTable(tableData, {
    x: 0.5, y: 1.0, w: 9.0,
    colW: [0.4, 2.6, 0.75, 0.75, 4.2],
    border: { pt: 0.5, color: C.gray300 },
    rowH: [0.3, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4],
    fontFace: "Calibri",
  });

  // Dependencies section
  slide.addText("Key Dependencies", {
    x: 0.6, y: 4.05, w: 8.8, h: 0.3,
    fontSize: 12, fontFace: "Calibri", bold: true, color: C.textDark, margin: 0
  });

  const deps = [
    "CISO sponsorship and executive air cover for cross-functional initiatives",
    "Security Engineering (Chelsea Main) partnership for CI/CD and tooling integration",
    "Budget approval for GRC platform investment and team training",
    "CRM access (Salesforce/HubSpot) for Customer Trust revenue attribution",
  ];
  slide.addText(
    deps.map((d, i) => ({
      text: d,
      options: { bullet: true, breakLine: i < deps.length - 1, fontSize: 8.5, color: C.textMed }
    })),
    { x: 0.7, y: 4.35, w: 8.5, h: 0.8, fontFace: "Calibri", paraSpaceAfter: 3, valign: "top" }
  );
}

// ═══════════════════════════════════════════════════════════
// SLIDE 11: Investment & ROI
// ═══════════════════════════════════════════════════════════
{
  const slide = pres.addSlide();
  slide.background = { color: C.white };
  addTitle(slide, "Investment Requirements & Expected ROI");
  addFooter(slide, 11);

  const leftW = 4.5;
  const rightX = 5.25;
  const rightW = 4.35;
  const cardY = 1.0;
  const cardH = 3.2;

  // LEFT: Investment areas
  slide.addShape(pres.shapes.RECTANGLE, {
    x: 0.6, y: cardY, w: leftW, h: cardH,
    fill: { color: C.white }, shadow: cardShadow()
  });
  slide.addShape(pres.shapes.RECTANGLE, {
    x: 0.6, y: cardY, w: leftW, h: 0.04, fill: { color: C.blue }
  });
  slide.addText("Investment Areas", {
    x: 0.8, y: cardY + 0.08, w: leftW - 0.4, h: 0.3,
    fontSize: 12, fontFace: "Calibri", bold: true, color: C.blue, margin: 0
  });

  const investments = [
    { cat: "GRC Platform & Tooling", items: ["Customer Trust platform consolidation/upgrade", "GRC automation platform (policy-as-code)", "Dashboard and reporting infrastructure", "TPRM automation and vendor risk platform"] },
    { cat: "People & Skills", items: ["GRC-Engineering technical training program", "Technical GRC Engineer hire (policy-as-code)", "Customer Trust team lead recruitment", "Industry certifications (CISA, CRISC, CISSP)"] },
    { cat: "Process & Consulting", items: ["NIST CSF maturity assessment (external)", "FAIR risk quantification implementation", "Change management for engineering integration"] },
  ];

  let iy = cardY + 0.42;
  investments.forEach(inv => {
    slide.addText(inv.cat, {
      x: 0.8, y: iy, w: leftW - 0.4, h: 0.22,
      fontSize: 9.5, fontFace: "Calibri", bold: true, color: C.textDark, margin: 0
    });
    iy += 0.22;
    slide.addText(
      inv.items.map((b, j) => ({
        text: b,
        options: { bullet: true, breakLine: j < inv.items.length - 1, fontSize: 8, color: C.textMed }
      })),
      { x: 0.85, y: iy, w: leftW - 0.55, h: inv.items.length * 0.18, fontFace: "Calibri", paraSpaceAfter: 2, valign: "top" }
    );
    iy += inv.items.length * 0.18 + 0.12;
  });

  // RIGHT: ROI
  slide.addShape(pres.shapes.RECTANGLE, {
    x: rightX, y: cardY, w: rightW, h: cardH,
    fill: { color: C.greenLight }, shadow: cardShadow()
  });
  slide.addShape(pres.shapes.RECTANGLE, {
    x: rightX, y: cardY, w: rightW, h: 0.04, fill: { color: C.green }
  });
  slide.addText("Expected Return on Investment", {
    x: rightX + 0.2, y: cardY + 0.08, w: rightW - 0.4, h: 0.3,
    fontSize: 12, fontFace: "Calibri", bold: true, color: C.green, margin: 0
  });

  const rois = [
    { title: "Revenue Enablement", desc: "Faster questionnaire completion accelerates deal closure. Tracking quantifies exact contribution.", color: C.teal },
    { title: "Cost Avoidance", desc: "Automated compliance reduces audit prep costs 40-60%. Continuous monitoring prevents findings.", color: C.blue },
    { title: "Risk Reduction", desc: "Quantified risk posture improvement. Proactive identification reduces incident likelihood.", color: C.indigo },
    { title: "Operational Efficiency", desc: "GRC-as-Code eliminates 60%+ manual tasks. Capacity redirected to strategic work.", color: C.green },
    { title: "Competitive Advantage", desc: "Strong trust posture as sales differentiator. Self-service portal reduces friction.", color: C.purple },
  ];

  let ry = cardY + 0.45;
  rois.forEach(roi => {
    slide.addShape(pres.shapes.RECTANGLE, {
      x: rightX + 0.2, y: ry, w: 0.04, h: 0.42, fill: { color: roi.color }
    });
    slide.addText(roi.title, {
      x: rightX + 0.35, y: ry, w: rightW - 0.6, h: 0.18,
      fontSize: 9, fontFace: "Calibri", bold: true, color: roi.color, margin: 0
    });
    slide.addText(roi.desc, {
      x: rightX + 0.35, y: ry + 0.18, w: rightW - 0.6, h: 0.26,
      fontSize: 7.5, fontFace: "Calibri", color: C.textMed, margin: 0
    });
    ry += 0.52;
  });

  // Timeline bar at bottom
  slide.addShape(pres.shapes.RECTANGLE, {
    x: 0.6, y: 4.4, w: 8.8, h: 0.65,
    fill: { color: C.blueLight }
  });
  slide.addText("VALUE DELIVERY TIMELINE", {
    x: 0.8, y: 4.42, w: 8.4, h: 0.2,
    fontSize: 10, fontFace: "Calibri", bold: true, color: C.blue, margin: 0
  });

  const milestones = [
    { label: "30 Days:", text: "Gap assessment, baseline KPIs" },
    { label: "90 Days:", text: "Revenue dashboard, response library v1, engineering embeds" },
    { label: "180 Days:", text: "Automation POC in CI/CD, TPRM tiering, TAT improvement" },
    { label: "365 Days:", text: "Full GRC-as-Code, executive dashboards, maturity improvement" },
  ];

  let mlTextArr = [];
  milestones.forEach((m, i) => {
    mlTextArr.push({ text: m.label + " ", options: { bold: true, color: C.indigo, fontSize: 8.5, breakLine: false } });
    mlTextArr.push({ text: m.text, options: { color: C.textMed, fontSize: 8.5, breakLine: i < milestones.length - 1 } });
  });
  slide.addText(mlTextArr, {
    x: 0.8, y: 4.62, w: 8.4, h: 0.4,
    fontFace: "Calibri", paraSpaceAfter: 2, valign: "top"
  });
}

// ═══════════════════════════════════════════════════════════
// SLIDE 12: Next Steps & The Ask
// ═══════════════════════════════════════════════════════════
{
  const slide = pres.addSlide();
  slide.background = { color: C.white };

  // Top accent bar
  slide.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: 0, w: 10, h: 0.04, fill: { color: C.teal }
  });

  addTitle(slide, "Immediate Next Steps & The Ask");
  addFooter(slide, 12);

  const leftW = 5.0;
  const rightX = 5.2;
  const rightW = 4.4;

  // LEFT: 30-Day Action Plan
  slide.addShape(pres.shapes.RECTANGLE, {
    x: 0.6, y: 0.95, w: leftW, h: 4.0,
    fill: { color: C.white }, shadow: cardShadow()
  });
  slide.addShape(pres.shapes.RECTANGLE, {
    x: 0.6, y: 0.95, w: leftW, h: 0.04, fill: { color: C.blue }
  });
  slide.addText("30-Day Action Plan", {
    x: 0.8, y: 1.02, w: leftW - 0.4, h: 0.3,
    fontSize: 12, fontFace: "Calibri", bold: true, color: C.blue, margin: 0
  });

  const steps = [
    { week: "Week 1-2: Stakeholder Alignment", items: ["1:1 meetings with all direct reports", "Alignment with Chelsea Main and Damian King", "Customer Trust team assessment + interim lead plan", "Review all existing documentation and artifacts"] },
    { week: "Week 2-3: Assessment & Baseline", items: ["GRC maturity assessment (NIST CSF)", "Map Customer Trust workflows and tools", "Document TPRM, audit, BC/DR processes", "Identify compliance obligations and certifications"] },
    { week: "Week 3-4: Quick Win Launch", items: ["Initiate revenue tracking dashboard development", "Begin response library (top 50 questions)", "Schedule first GRC-Engineering touchpoints", "Present initial findings to CISO"] },
  ];

  let sy = 1.38;
  steps.forEach(s => {
    slide.addText(s.week, {
      x: 0.8, y: sy, w: leftW - 0.4, h: 0.22,
      fontSize: 9.5, fontFace: "Calibri", bold: true, color: C.textDark, margin: 0
    });
    sy += 0.24;
    slide.addText(
      s.items.map((b, j) => ({
        text: b,
        options: { bullet: true, breakLine: j < s.items.length - 1, fontSize: 8, color: C.textMed }
      })),
      { x: 0.85, y: sy, w: leftW - 0.55, h: s.items.length * 0.17, fontFace: "Calibri", paraSpaceAfter: 2, valign: "top" }
    );
    sy += s.items.length * 0.17 + 0.15;
  });

  // RIGHT TOP: The Ask
  slide.addShape(pres.shapes.RECTANGLE, {
    x: rightX, y: 0.95, w: rightW, h: 1.95,
    fill: { color: C.blueLight }, shadow: cardShadow()
  });
  slide.addShape(pres.shapes.RECTANGLE, {
    x: rightX, y: 0.95, w: rightW, h: 0.04, fill: { color: C.indigo }
  });
  slide.addText("The Ask from CISO", {
    x: rightX + 0.2, y: 1.02, w: rightW - 0.4, h: 0.3,
    fontSize: 12, fontFace: "Calibri", bold: true, color: C.indigo, margin: 0
  });

  const asks = [
    "Endorse this roadmap as official 2026 GRC strategic plan",
    "Executive sponsorship for Engineering integration",
    "Approve budget for platform evaluation and training",
    "Support hiring: Technical GRC Engineer + Trust lead",
    "Facilitate intros to product/engineering leadership",
    "Monthly roadmap review cadence (30-min)",
  ];
  slide.addText(
    asks.map((a, i) => ({
      text: a,
      options: { bullet: true, breakLine: i < asks.length - 1, fontSize: 8.5, color: C.textMed }
    })),
    { x: rightX + 0.2, y: 1.35, w: rightW - 0.4, h: 1.4, fontFace: "Calibri", paraSpaceAfter: 4, valign: "top" }
  );

  // RIGHT BOTTOM: Success Criteria
  slide.addShape(pres.shapes.RECTANGLE, {
    x: rightX, y: 3.1, w: rightW, h: 1.85,
    fill: { color: C.greenLight }, shadow: cardShadow()
  });
  slide.addShape(pres.shapes.RECTANGLE, {
    x: rightX, y: 3.1, w: rightW, h: 0.04, fill: { color: C.green }
  });
  slide.addText("Success Criteria (12 Months)", {
    x: rightX + 0.2, y: 3.16, w: rightW - 0.4, h: 0.3,
    fontSize: 11, fontFace: "Calibri", bold: true, color: C.green, margin: 0
  });

  const criteria = [
    "GRC maturity improvement (baseline to Tier 3)",
    "Customer Trust TAT reduced by 60%",
    "Revenue attribution dashboard operational",
    "Policy-as-code in at least one CI/CD pipeline",
    "100% critical vendors assessed in TPRM framework",
  ];
  slide.addText(
    criteria.map((c, i) => ({
      text: c,
      options: { bullet: true, breakLine: i < criteria.length - 1, fontSize: 8.5, color: C.textMed }
    })),
    { x: rightX + 0.2, y: 3.5, w: rightW - 0.4, h: 1.3, fontFace: "Calibri", paraSpaceAfter: 4, valign: "top" }
  );
}

// ═══════════════════════════════════════════════════════════
// SLIDE 13: Appendix - Best Practices & Frameworks
// ═══════════════════════════════════════════════════════════
{
  const slide = pres.addSlide();
  slide.background = { color: C.offWhite };
  addTitle(slide, "Appendix: Industry Best Practices & Frameworks");
  addFooter(slide, 13);

  const cards = [
    {
      title: "Framework Alignment", color: C.blue, bg: C.blueLight,
      items: ["NIST CSF 2.0 - Primary maturity model and governance backbone", "ISO 27001:2022 - ISMS alignment for certification", "SOC 2 Type II - Automated evidence collection", "NIST SP 800-53 Rev. 5 - Comprehensive control catalog", "FAIR - Quantitative risk analysis methodology"]
    },
    {
      title: "GRC Technology Trends", color: C.teal, bg: C.tealLight,
      items: ["GRC-as-Code: OPA, Rego, Terraform Sentinel, AWS Config", "Continuous Compliance: Real-time monitoring", "AI-Assisted Trust: LLM-powered questionnaire completion", "Unified Platforms: Converged risk/compliance/audit", "Trust Centers: Self-service security transparency"]
    },
    {
      title: "Organizational Best Practices", color: C.indigo, bg: C.indigoLight,
      items: ["Shift-Left: Embed compliance in SDLC", "Three Lines Model (IIA): Clear governance delineation", "Risk-Based: Prioritize high-impact controls", "Value-Driven: Measure business outcomes, not checklists", "Cross-Functional: GRC as partner to Eng/Product/Sales"]
    },
    {
      title: "Reference Standards", color: C.green, bg: C.greenLight,
      items: ["NIST SP 800-137: Continuous Monitoring (ISCM)", "ISACA COBIT 2019: Enterprise IT governance", "IIA Three Lines Model: Risk governance guidance", "CISA Cybersecurity Performance Goals", "CSA CCM: Cloud-specific control mapping"]
    },
  ];

  const cw = 4.25;
  const ch = 1.7;
  const startY = 1.0;

  cards.forEach((card, i) => {
    const col = i % 2;
    const row = Math.floor(i / 2);
    const x = 0.6 + col * (cw + 0.3);
    const y = startY + row * (ch + 0.15);

    slide.addShape(pres.shapes.RECTANGLE, {
      x, y, w: cw, h: ch,
      fill: { color: card.bg }, shadow: cardShadow()
    });
    slide.addShape(pres.shapes.RECTANGLE, {
      x, y, w: cw, h: 0.04, fill: { color: card.color }
    });
    slide.addText(card.title, {
      x: x + 0.15, y: y + 0.08, w: cw - 0.3, h: 0.25,
      fontSize: 10.5, fontFace: "Calibri", bold: true, color: card.color, margin: 0
    });
    slide.addText(
      card.items.map((b, j) => ({
        text: b,
        options: { bullet: true, breakLine: j < card.items.length - 1, fontSize: 8, color: C.textMed }
      })),
      { x: x + 0.15, y: y + 0.38, w: cw - 0.3, h: ch - 0.5, fontFace: "Calibri", paraSpaceAfter: 3, valign: "top" }
    );
  });
}

// ═══════════════════════════════════════════════════════════
// SAVE
// ═══════════════════════════════════════════════════════════
pres.writeFile({ fileName: "/Users/jsn/Documents/GitHub/blog/GRC_Roadmap_2026.pptx" })
  .then(() => console.log("PPTX saved: GRC_Roadmap_2026.pptx"))
  .catch(err => console.error(err));

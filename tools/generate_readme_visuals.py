#!/usr/bin/env python3
"""Generate README-facing SVG visuals with BHIL brand tokens.

Derived artifacts: docs/assets/readme-*.svg. Do not hand-edit; edit this
tool and re-run, then refresh the drift manifest. stdlib only.
"""
from __future__ import annotations

from pathlib import Path

COBALT = "#1B4FD8"
COBALT_DARK = "#0F2F8A"
COBALT_LIGHT = "#E8EEFF"
NAVY = "#1C1C2E"
ACCENT = "#6B9EFF"
PAPER = "#FFFFFF"
CREAM = "#F7F4EC"
STONE = "#6B7280"
CLARET = "#8A2331"
MOSS = "#3E7A55"
GOLD = "#C9A227"
FONT = "IBM Plex Sans, Arial, sans-serif"
MONO = "IBM Plex Mono, Consolas, monospace"
TAGLINE = "HUMAN-DIRECTED. AI-ENABLED. COMMERCIALLY TESTED."


def svg_open(width: int, height: int, background: str = PAPER) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'font-family="{FONT}">\n<rect width="{width}" height="{height}" fill="{background}"/>\n'
    )


def banner() -> str:
    width, height = 1200, 300
    svg = svg_open(width, height, NAVY)
    svg += f'<rect x="0" y="0" width="10" height="{height}" fill="{COBALT}"/>\n'
    for i, cy in enumerate((36, 36, 36)):
        svg += f'<circle cx="{40 + i * 16}" cy="{cy}" r="4" fill="{ACCENT}"/>\n'
    svg += f'<text x="40" y="86" font-family="{MONO}" font-size="15" fill="{ACCENT}" letter-spacing="4">BHIL VISUAL INTELLIGENCE STUDY</text>\n'
    svg += f'<text x="38" y="150" font-size="52" font-weight="700" fill="{PAPER}">Inside QuantumBlack</text>\n'
    svg += f'<text x="40" y="188" font-size="19" font-style="italic" fill="#C9D4F5">A designer field guide to how McKinsey QuantumBlack strategically communicates.</text>\n'
    svg += f'<text x="40" y="224" font-family="{MONO}" font-size="12" fill="{STONE}">32 ARTIFACTS CODED  |  12 GUIDE CHAPTERS  |  3 BUILD RECIPES  |  5 EVIDENCE TIERS  |  0 TRADE DRESS</text>\n'
    svg += f'<text x="40" y="266" font-family="{MONO}" font-size="11" fill="{ACCENT}" letter-spacing="2">{TAGLINE}</text>\n'
    bars = [(1000, 120, 150, COBALT), (1040, 170, 100, ACCENT), (1080, 90, 180, "#3D4A78"), (1120, 200, 70, ACCENT), (1160, 140, 130, COBALT)]
    for x, y, h, color in bars:
        svg += f'<rect x="{x}" y="{y}" width="24" height="{h}" rx="3" fill="{color}"/>\n'
    return svg + "</svg>\n"


def badge(label: str, value: str, value_fill: str, label_width: int, value_width: int) -> str:
    width, height = label_width + value_width, 28
    svg = svg_open(width, height, "none")
    svg += f'<rect width="{label_width}" height="{height}" rx="4" fill="{NAVY}"/>\n'
    svg += f'<rect x="{label_width}" width="{value_width}" height="{height}" rx="4" fill="{value_fill}"/>\n'
    svg += f'<rect x="{label_width}" width="8" height="{height}" fill="{value_fill}"/>\n'
    svg += f'<rect x="{label_width - 4}" width="8" height="{height}" fill="{NAVY}"/>\n'
    svg += f'<text x="{label_width / 2}" y="19" font-family="{MONO}" font-size="12" fill="{PAPER}" text-anchor="middle">{label}</text>\n'
    svg += f'<text x="{label_width + value_width / 2}" y="19" font-family="{MONO}" font-size="12" font-weight="700" fill="{PAPER}" text-anchor="middle">{value}</text>\n'
    return svg + "</svg>\n"


def sample_exhibit() -> str:
    width, height = 900, 560
    svg = svg_open(width, height, CREAM)
    svg += f'<text x="28" y="34" font-family="{MONO}" font-size="12" fill="{COBALT}" letter-spacing="3">REPORT SAMPLE  |  EXHIBIT ANATOMY  |  BHIL RECONSTRUCTION</text>\n'
    card_x, card_y, card_w, card_h = 190, 60, 560, 400
    svg += f'<rect x="{card_x}" y="{card_y}" width="{card_w}" height="{card_h}" rx="10" fill="{PAPER}" stroke="#E2DCCB"/>\n'
    svg += f'<text x="{card_x + 28}" y="{card_y + 44}" font-size="19" font-weight="700" fill="{NAVY}">Gen AI adoption grows, but measured</text>\n'
    svg += f'<text x="{card_x + 28}" y="{card_y + 68}" font-size="19" font-weight="700" fill="{NAVY}">impact remains limited</text>\n'
    svg += f'<text x="{card_x + 28}" y="{card_y + 90}" font-size="12" font-style="italic" fill="{STONE}">Share of respondents, illustrative reconstruction</text>\n'
    svg += f'<line x1="{card_x + 28}" y1="{card_y + 102}" x2="{card_x + card_w - 28}" y2="{card_y + 102}" stroke="{NAVY}" stroke-width="1.5"/>\n'
    rows = [
        ("Using gen AI regularly", 89, 37),
        ("Seeing material P and L impact", 34, 12),
        ("Scaling across functions", 28, 8),
    ]
    base_y = card_y + 140
    for i, (label, adoption, impact) in enumerate(rows):
        y = base_y + i * 72
        svg += f'<text x="{card_x + 180}" y="{y + 12}" font-size="12" fill="{NAVY}" text-anchor="end">{label}</text>\n'
        svg += f'<rect x="{card_x + 192}" y="{y}" width="{adoption * 2.6}" height="16" fill="{STONE}" opacity="0.75"/>\n'
        svg += f'<text x="{card_x + 200 + adoption * 2.6}" y="{y + 13}" font-family="{MONO}" font-size="12" fill="{STONE}">{adoption}%</text>\n'
        svg += f'<rect x="{card_x + 192}" y="{y + 22}" width="{impact * 2.6}" height="16" fill="{CLARET}"/>\n'
        svg += f'<text x="{card_x + 200 + impact * 2.6}" y="{y + 35}" font-family="{MONO}" font-size="12" fill="{CLARET}">{impact}%</text>\n'
    svg += f'<line x1="{card_x + 28}" y1="{card_y + card_h - 46}" x2="{card_x + card_w - 28}" y2="{card_y + card_h - 46}" stroke="#E2DCCB"/>\n'
    svg += f'<text x="{card_x + 28}" y="{card_y + card_h - 26}" font-family="{MONO}" font-size="10" fill="{STONE}">SOURCE  BHIL STENCIL STUDY  |  PUBLIC-SOURCE PATTERN RECONSTRUCTION</text>\n'

    callouts = [
        (1, 40, 120, "Full-sentence", "conclusion title", card_x + 30, card_y + 50),
        (2, 40, 250, "Single dominant", "comparison", card_x + 195, base_y + 80),
        (4, 40, 380, "Disciplined", "source line", card_x + 30, card_y + card_h - 30),
        (3, 800, 190, "Direct labels,", "no legend hunt", card_x + card_w - 40, base_y + 8),
        (5, 800, 330, "Method note", "when needed", card_x + card_w - 40, base_y + 160),
    ]
    for num, x, y, line1, line2, tx, ty in callouts:
        anchor = "start" if x < 400 else "end"
        label_x = x + 34 if x < 400 else x - 34
        svg += f'<circle cx="{x}" cy="{y}" r="14" fill="{COBALT}"/>\n'
        svg += f'<text x="{x}" y="{y + 5}" font-size="13" font-weight="700" fill="{PAPER}" text-anchor="middle">{num}</text>\n'
        svg += f'<text x="{label_x}" y="{y - 2}" font-size="12.5" font-weight="600" fill="{NAVY}" text-anchor="{anchor}">{line1}</text>\n'
        svg += f'<text x="{label_x}" y="{y + 14}" font-size="12.5" font-weight="600" fill="{NAVY}" text-anchor="{anchor}">{line2}</text>\n'
        svg += f'<line x1="{x + (18 if x < 400 else -18)}" y1="{y}" x2="{tx}" y2="{ty}" stroke="{ACCENT}" stroke-width="1.4" stroke-dasharray="4 3"/>\n'
    svg += f'<text x="28" y="{height - 40}" font-size="13" fill="{NAVY}">The exhibit is the atomic unit: one idea, one conclusion, one proof.</text>\n'
    svg += f'<text x="28" y="{height - 18}" font-family="{MONO}" font-size="10" fill="{STONE}">BHIL INSIDE QUANTUMBLACK STUDY  |  {TAGLINE}</text>\n'
    return svg + "</svg>\n"


def page_wireframe() -> str:
    width, height = 900, 620
    svg = svg_open(width, height)
    svg += f'<text x="28" y="34" font-family="{MONO}" font-size="12" fill="{COBALT}" letter-spacing="3">REPORT SAMPLE  |  PAGE ARCHITECTURE WIREFRAME</text>\n'
    px, py, pw, ph = 90, 60, 430, 500
    svg += f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="8" fill="{PAPER}" stroke="{STONE}"/>\n'
    zones = [
        ("kicker", py + 24, 14, COBALT_LIGHT, "PRACTICE / TOPIC KICKER"),
        ("headline", py + 56, 46, NAVY, ""),
        ("dek", py + 112, 18, "#D5DCF2", ""),
        ("takeaways", py + 146, 70, COBALT_LIGHT, "KEY TAKEAWAYS  |  3 to 5 bullets"),
        ("exhibit", py + 232, 200, CREAM, "EXHIBIT 1  |  title states the result"),
        ("source", py + 448, 16, "#EFEFEF", "SOURCE  dataset, sample, dates, notes"),
    ]
    labels = [
        (1, "Headline carries the answer", py + 79),
        (2, "Deck adds scope, not a second thesis", py + 121),
        (3, "Takeaways compress the page into decisions", py + 181),
        (4, "Exhibit title states the result", py + 332),
        (5, "Source and method easy to find", py + 456),
    ]
    for _, y, zone_height, fill, caption in zones:
        svg += f'<rect x="{px + 22}" y="{y}" width="{pw - 44}" height="{zone_height}" rx="4" fill="{fill}"/>\n'
        if caption:
            text_fill = STONE if fill != NAVY else PAPER
            caption_y = y + 18 if zone_height > 80 else y + zone_height / 2 + 4
            svg += f'<text x="{px + 34}" y="{caption_y}" font-family="{MONO}" font-size="10.5" fill="{text_fill}">{caption}</text>\n'
    svg += f'<text x="{px + 34}" y="{py + 86}" font-size="17" font-weight="700" fill="{PAPER}">A conclusion written as a headline</text>\n'
    bar_y = py + 300
    for i, (value, color) in enumerate([(150, COBALT), (100, STONE), (60, STONE)]):
        svg += f'<rect x="{px + 120}" y="{bar_y + i * 30}" width="{value}" height="14" fill="{color}"/>\n'
        svg += f'<text x="{px + 100}" y="{bar_y + i * 30 + 11}" font-size="10" fill="{NAVY}" text-anchor="end">{chr(65 + i)}</text>\n'
    for num, text, y in labels:
        svg += f'<circle cx="{px + pw + 60}" cy="{y}" r="13" fill="{COBALT if num % 2 else NAVY}"/>\n'
        svg += f'<text x="{px + pw + 60}" y="{y + 4}" font-size="12" font-weight="700" fill="{PAPER}" text-anchor="middle">{num}</text>\n'
        svg += f'<text x="{px + pw + 84}" y="{y + 4}" font-size="13" fill="{NAVY}">{text}</text>\n'
        svg += f'<line x1="{px + pw - 18}" y1="{y}" x2="{px + pw + 44}" y2="{y}" stroke="{ACCENT}" stroke-width="1.3" stroke-dasharray="4 3"/>\n'
    svg += f'<text x="28" y="{height - 40}" font-size="13" fill="{NAVY}">Reading order: headline, takeaway, evidence, implication, source.</text>\n'
    svg += f'<text x="28" y="{height - 18}" font-family="{MONO}" font-size="10" fill="{STONE}">BHIL INSIDE QUANTUMBLACK STUDY  |  {TAGLINE}</text>\n'
    return svg + "</svg>\n"


def evidence_waffle() -> str:
    width, height = 900, 320
    tiers = [("VERIFIED", 13, MOSS), ("CORROBORATED", 15, COBALT), ("UNCORROBORATED", 3, GOLD), ("STATED, QUARANTINED", 1, CLARET)]
    svg = svg_open(width, height)
    svg += f'<text x="28" y="36" font-size="18" font-weight="600" fill="{NAVY}">Every register row carries an evidence tier</text>\n'
    svg += f'<text x="28" y="58" font-size="12" font-style="italic" fill="{STONE}">One square per artifact, 32 total, row-level ledger</text>\n'
    cells: list[str] = []
    for _, count, color in tiers:
        cells.extend([color] * count)
    for index, color in enumerate(cells):
        row, col = divmod(index, 8)
        svg += f'<rect x="{28 + col * 52}" y="{86 + row * 52}" width="44" height="44" rx="5" fill="{color}"/>\n'
    legend_y = 100
    for name, count, color in tiers:
        svg += f'<rect x="500" y="{legend_y - 12}" width="16" height="16" rx="3" fill="{color}"/>\n'
        svg += f'<text x="526" y="{legend_y + 1}" font-family="{MONO}" font-size="12" fill="{NAVY}">{name}</text>\n'
        svg += f'<text x="{width - 40}" y="{legend_y + 1}" font-family="{MONO}" font-size="13" font-weight="700" fill="{color}" text-anchor="end">{count}</text>\n'
        legend_y += 36
    svg += f'<text x="500" y="{legend_y + 6}" font-size="12" font-style="italic" fill="{STONE}">Firm self-claims are STATED and never promoted.</text>\n'
    svg += f'<text x="500" y="{legend_y + 24}" font-size="12" font-style="italic" fill="{STONE}">No tool here reports CLEAN; absence of anomaly</text>\n'
    svg += f'<text x="500" y="{legend_y + 42}" font-size="12" font-style="italic" fill="{STONE}">is INCONCLUSIVE.</text>\n'
    svg += f'<text x="28" y="{height - 14}" font-family="{MONO}" font-size="10" fill="{STONE}">BHIL INSIDE QUANTUMBLACK STUDY  |  {TAGLINE}</text>\n'
    return svg + "</svg>\n"


def artifact_mix() -> str:
    width, height = 900, 300
    rows = [
        ("T1 Thought leadership", 15, COBALT),
        ("T2 Case studies", 5, NAVY),
        ("T4 Frameworks and models", 4, NAVY),
        ("T5 Procurement records", 4, NAVY),
        ("T3 Presentations", 2, STONE),
        ("T6 Data visualizations", 2, STONE),
    ]
    svg = svg_open(width, height)
    svg += f'<text x="28" y="36" font-size="18" font-weight="600" fill="{NAVY}">Thought leadership carries the corpus</text>\n'
    svg += f'<text x="28" y="58" font-size="12" font-style="italic" fill="{STONE}">Cataloged artifacts by STENCIL taxonomy category, 32 total</text>\n'
    for i, (label, value, color) in enumerate(rows):
        y = 92 + i * 32
        svg += f'<text x="248" y="{y + 12}" font-size="13" fill="{NAVY}" text-anchor="end">{label}</text>\n'
        svg += f'<rect x="262" y="{y}" width="{value * 36}" height="17" rx="3" fill="{color}"/>\n'
        svg += f'<text x="{272 + value * 36}" y="{y + 13}" font-family="{MONO}" font-size="12" fill="{color}">{value}</text>\n'
    svg += f'<text x="28" y="{height - 14}" font-family="{MONO}" font-size="10" fill="{STONE}">BHIL INSIDE QUANTUMBLACK STUDY  |  {TAGLINE}</text>\n'
    return svg + "</svg>\n"


def stencil_pipeline() -> str:
    width, height = 1200, 150
    stages = ["SP-1 SCOPE", "SP-2 SWEEP", "SP-3 LIBRARY", "SP-4 NARRATIVE", "SP-5 FRAMEWORKS", "SP-6 VISUAL", "SP-7 LEXICON", "SP-8 RECIPES", "SP-10 GATE"]
    svg = svg_open(width, height, NAVY)
    svg += f'<text x="28" y="34" font-family="{MONO}" font-size="12" fill="{ACCENT}" letter-spacing="3">THE STENCIL PIPELINE BEHIND THIS REPO</text>\n'
    x = 28
    for i, stage in enumerate(stages):
        box_w = 112
        fill = COBALT if stage != "SP-10 GATE" else MOSS
        svg += f'<rect x="{x}" y="58" width="{box_w}" height="40" rx="6" fill="{fill}"/>\n'
        svg += f'<text x="{x + box_w / 2}" y="82" font-family="{MONO}" font-size="10.5" fill="{PAPER}" text-anchor="middle">{stage}</text>\n'
        if i < len(stages) - 1:
            svg += f'<path d="M {x + box_w + 3} 78 l 10 0 m -4 -4 l 4 4 l -4 4" stroke="{ACCENT}" stroke-width="2" fill="none"/>\n'
        x += box_w + 18
    svg += f'<text x="28" y="128" font-family="{MONO}" font-size="10" fill="{STONE}">DISPOSITION: SHIP  |  32 ARTIFACTS AGAINST A 20 MINIMUM  |  INFERENCE SHARE 22 PERCENT AGAINST A 40 PERCENT HOLD TRIGGER</text>\n'
    return svg + "</svg>\n"


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    assets = root / "docs" / "assets"
    assets.mkdir(parents=True, exist_ok=True)
    outputs = {
        "readme-banner.svg": banner(),
        "readme-badge-gates.svg": badge("GATES", "4 PASSING", MOSS, 70, 100),
        "readme-badge-license.svg": badge("LICENSE", "MIT + CC BY 4.0", COBALT, 84, 140),
        "readme-badge-artifacts.svg": badge("CORPUS", "32 ARTIFACTS", NAVY if False else COBALT_DARK, 80, 120),
        "readme-badge-python.svg": badge("PYTHON", "STDLIB ONLY", "#4B5563", 80, 116),
        "readme-sample-exhibit.svg": sample_exhibit(),
        "readme-page-wireframe.svg": page_wireframe(),
        "readme-evidence-waffle.svg": evidence_waffle(),
        "readme-artifact-mix.svg": artifact_mix(),
        "readme-stencil-pipeline.svg": stencil_pipeline(),
    }
    for name, content in outputs.items():
        (assets / name).write_text(content, encoding="utf-8")
        print(f"wrote docs/assets/{name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

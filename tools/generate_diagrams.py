#!/usr/bin/env python3
"""Generate the repo's SVG diagrams programmatically with BHIL brand tokens.

Derived artifacts: docs/assets/*.svg. Do not hand-edit; edit this tool and
re-run, then refresh the drift manifest. stdlib only.
"""
from __future__ import annotations

from pathlib import Path

COBALT = "#1B4FD8"
COBALT_DARK = "#0F2F8A"
COBALT_LIGHT = "#E8EEFF"
NAVY = "#1C1C2E"
ACCENT = "#6B9EFF"
PAPER = "#FFFFFF"
STONE = "#6B7280"
FONT = "IBM Plex Sans, Arial, sans-serif"
MONO = "IBM Plex Mono, Consolas, monospace"


def header(width: int, height: int) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'font-family="{FONT}">\n'
        f'<rect width="{width}" height="{height}" fill="{PAPER}"/>\n'
    )


def footer_block(width: int, height: int) -> str:
    return (
        f'<text x="24" y="{height - 16}" font-family="{MONO}" font-size="10" fill="{STONE}">'
        "BHIL INSIDE QUANTUMBLACK STUDY</text>\n"
        f'<text x="{width - 24}" y="{height - 16}" font-family="{MONO}" font-size="10" '
        f'fill="{STONE}" text-anchor="end">HUMAN-DIRECTED. AI-ENABLED. COMMERCIALLY TESTED.</text>\n'
        "</svg>\n"
    )


def narrative_flow() -> str:
    steps = [
        ("1", "Quantified tension", "Measurable problem or paradox"),
        ("2", "Answer first", "Conclusion before detail"),
        ("3", "Exhibit cascade", "Evidence in numbered layers"),
        ("4", "Cohort or framework", "Pattern named after proof"),
        ("5", "Playbook close", "A short set of actions"),
        ("6", "Method and byline", "Scope, source, ownership"),
    ]
    width, height = 960, 220
    svg = header(width, height)
    svg += f'<text x="24" y="36" font-size="18" font-weight="600" fill="{NAVY}">The six-step narrative flow</text>\n'
    x0, step_w = 24, 152
    for index, (num, title, sub) in enumerate(steps):
        x = x0 + index * step_w
        fill = COBALT if index % 2 == 0 else COBALT_DARK
        svg += f'<circle cx="{x + 16}" cy="78" r="14" fill="{fill}"/>\n'
        svg += (
            f'<text x="{x + 16}" y="83" font-size="13" font-weight="700" fill="{PAPER}" '
            f'text-anchor="middle">{num}</text>\n'
        )
        svg += f'<text x="{x}" y="116" font-size="13" font-weight="600" fill="{NAVY}">{title}</text>\n'
        words = sub.split()
        mid = len(words) // 2 + len(words) % 2
        svg += f'<text x="{x}" y="134" font-size="10.5" fill="{STONE}">{" ".join(words[:mid])}</text>\n'
        svg += f'<text x="{x}" y="148" font-size="10.5" fill="{STONE}">{" ".join(words[mid:])}</text>\n'
        if index < len(steps) - 1:
            ax = x + step_w - 18
            svg += f'<path d="M {ax} 78 l 10 0 m -4 -4 l 4 4 l -4 4" stroke="{ACCENT}" stroke-width="2" fill="none"/>\n'
    return svg + footer_block(width, height)


def framework_placement() -> str:
    width, height = 760, 480
    left, top, right, bottom = 90, 70, 700, 380
    cx, cy = (left + right) // 2, (top + bottom) // 2
    points = [
        ("Paradox statement", 180, 130, COBALT),
        ("2-axis arena model", 320, 120, ACCENT),
        ("Trend scoring", 260, 190, ACCENT),
        ("Capability concept", 470, 140, NAVY),
        ("Agent architecture", 480, 250, NAVY),
        ("Factory tooling", 610, 270, NAVY),
        ("High-performer cohort", 450, 330, NAVY),
        ("Roadmap", 590, 330, NAVY),
    ]
    svg = header(width, height)
    svg += f'<text x="24" y="36" font-size="18" font-weight="600" fill="{NAVY}">Framework placement: intent by position</text>\n'
    svg += f'<rect x="{left}" y="{top}" width="{right - left}" height="{bottom - top}" fill="{COBALT_LIGHT}" opacity="0.35"/>\n'
    svg += f'<line x1="{cx}" y1="{top}" x2="{cx}" y2="{bottom}" stroke="{STONE}" stroke-width="1"/>\n'
    svg += f'<line x1="{left}" y1="{cy}" x2="{right}" y2="{cy}" stroke="{STONE}" stroke-width="1"/>\n'
    for name, x, y, color in points:
        svg += f'<circle cx="{x}" cy="{y}" r="7" fill="{color}"/>\n'
        svg += f'<text x="{x}" y="{y + 22}" font-size="11.5" fill="{NAVY}" text-anchor="middle">{name}</text>\n'
    svg += f'<text x="{left}" y="{top - 12}" font-family="{MONO}" font-size="11" fill="{STONE}">FRONT-LOADED (lede / title)</text>\n'
    svg += f'<text x="{left}" y="{bottom + 24}" font-family="{MONO}" font-size="11" fill="{STONE}">BACK-LOADED (reveal / playbook)</text>\n'
    svg += f'<text x="{left + 70}" y="{bottom + 44}" font-family="{MONO}" font-size="11" fill="{STONE}">DIAGNOSTIC</text>\n'
    svg += f'<text x="{right - 70}" y="{bottom + 44}" font-family="{MONO}" font-size="11" fill="{STONE}" text-anchor="end">PRESCRIPTIVE</text>\n'
    return svg + footer_block(width, height)


def vocabulary_migration() -> str:
    width, height = 760, 400
    years = [2023, 2024, 2025, 2026]
    series = {
        "Gen AI / use cases": ([1, 1, 3, 4], STONE),
        "Rewiring / redesign": ([3, 2, 2, 3], STONE),
        "Agentic AI / agents": ([4, 4, 1, 2], STONE),
        "ROI / tokenomics": ([2, 3, 4, 1], COBALT),
    }
    left, top, right, bottom = 90, 80, 560, 320
    xs = {year: left + i * (right - left) / 3 for i, year in enumerate(years)}
    ys = {rank: top + (rank - 1) * (bottom - top) / 3 for rank in (1, 2, 3, 4)}
    svg = header(width, height)
    svg += f'<text x="24" y="36" font-size="18" font-weight="600" fill="{NAVY}">Four vocabularies in four years</text>\n'
    for rank in (1, 2, 3, 4):
        svg += f'<line x1="{left}" y1="{ys[rank]}" x2="{right}" y2="{ys[rank]}" stroke="{COBALT_LIGHT}" stroke-width="1"/>\n'
        svg += f'<text x="{left - 12}" y="{ys[rank] + 4}" font-family="{MONO}" font-size="10" fill="{STONE}" text-anchor="end">RANK {rank}</text>\n'
    for year in years:
        svg += f'<text x="{xs[year]}" y="{bottom + 26}" font-family="{MONO}" font-size="11" fill="{STONE}" text-anchor="middle">{year}</text>\n'
    for name, (ranks, color) in series.items():
        pts = " ".join(f"{xs[year]},{ys[rank]}" for year, rank in zip(years, ranks))
        stroke_width = 3 if color == COBALT else 1.5
        svg += f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="{stroke_width}"/>\n'
        for year, rank in zip(years, ranks):
            svg += f'<circle cx="{xs[year]}" cy="{ys[rank]}" r="4" fill="{color}"/>\n'
        label_fill = COBALT if color == COBALT else STONE
        svg += f'<text x="{right + 14}" y="{ys[ranks[-1]] + 4}" font-size="11.5" fill="{label_fill}">{name}</text>\n'
    return svg + footer_block(width, height)


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    assets = root / "docs" / "assets"
    assets.mkdir(parents=True, exist_ok=True)
    outputs = {
        "narrative-flow.svg": narrative_flow(),
        "framework-placement.svg": framework_placement(),
        "vocabulary-migration.svg": vocabulary_migration(),
    }
    for name, content in outputs.items():
        (assets / name).write_text(content, encoding="utf-8")
        print(f"wrote docs/assets/{name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Genere trace-light.svg et trace-dark.svg : le parcours en waterfall de spans.

Palette issue de references/palette.md (slots categoriels 1-3), validee par
scripts/validate_palette.js en light et dark, --pairs all : tous les checks PASS.
EPITA est en gris neutre : c'est le decor, pas une serie.
"""

MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"

THEMES = {
    "light": dict(
        surface="#fcfcfb", stroke="#e5e4df",
        ink="#0b0b0b", ink2="#52514e", ink3="#8a8984",
        base="#d6d5ce",                       # EPITA, neutre
        series=["#2a78d6", "#008300", "#e87ba4"],
        prompt="#8a8984",
    ),
    "dark": dict(
        surface="#1a1a19", stroke="#33322f",
        ink="#ffffff", ink2="#c3c2b7", ink3="#8a8984",
        base="#3d3c38",
        series=["#3987e5", "#008300", "#d55181"],
        prompt="#8a8984",
    ),
}

# (libelle, duree, debut, fin, index de couleur ; None = neutre)
# La techno est portee par le libelle : pas de note a droite, donc pas de
# debordement hors du cadre (le rendu precedent coupait "K8s AIOps").
# Annee decimale : debut du mois m = annee + (m-1)/12.
# McKay sept 2024 -> fin fev 2025 = 2024.667..2025.167 = 6 mois pleins.
# MinArm fev 2025 -> janv 2026, Devoteam fev 2026 -> aout 2026 : la chaine
# est continue, ce qui est le point du dessin.
SPANS = [
    ("EPITA · MSc AI & ML",        "",      2021.667, 2026.500, None),
    ("McKay Brothers · Rust, HFT", "6 mo",  2024.667, 2025.167, 0),
    ("Ministère des Armées · RAG", "11 mo", 2025.083, 2026.000, 1),
    ("Devoteam · K8s AIOps",       "7 mo",  2026.083, 2026.667, 2),
]

W, H = 780, 268
X0, X1 = 252, 700          # zone des barres, marge a droite pour les durees
T0, T1 = 2021.67, 2026.83
ROW0, ROWH, BARH = 76, 30, 13


def x(t):
    return X0 + (t - T0) / (T1 - T0) * (X1 - X0)


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def build(mode):
    t = THEMES[mode]
    o = []
    o.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
        f'viewBox="0 0 {W} {H}" font-family="{MONO}" role="img" '
        f'aria-label="Career timeline of Wassim Badraoui rendered as a distributed trace: '
        f'EPITA MSc AI and ML 2021 to 2026, McKay Brothers 2024 to 2025, '
        f'Ministere des Armees 2025 to 2026, Devoteam 2026.">'
    )
    o.append(f'<rect width="{W}" height="{H}" rx="8" fill="{t["surface"]}" stroke="{t["stroke"]}"/>')

    # ligne de commande
    o.append(f'<text x="24" y="36" font-size="13" fill="{t["prompt"]}">$</text>')
    o.append(
        f'<text x="38" y="36" font-size="13" fill="{t["ink2"]}">'
        f'otel trace <tspan fill="{t["ink3"]}">--service</tspan> wassim-badraoui</text>'
    )

    # graduations d'annees, en retrait
    for year in (2022, 2023, 2024, 2025, 2026):
        gx = x(year)
        o.append(
            f'<line x1="{gx:.1f}" y1="58" x2="{gx:.1f}" y2="{ROW0 + 4 * ROWH - 12}" '
            f'stroke="{t["stroke"]}" stroke-width="1"/>'
        )
        o.append(
            f'<text x="{gx:.1f}" y="{ROW0 + 4 * ROWH + 4}" font-size="10" '
            f'fill="{t["ink3"]}" text-anchor="middle">{year}</text>'
        )

    # spans
    for i, (label, dur, a, b, ci) in enumerate(SPANS):
        y = ROW0 + i * ROWH
        fill = t["base"] if ci is None else t["series"][ci]
        bx, bw = x(a), max(4, x(b) - x(a))
        # le libelle est adjacent a sa barre : l'identite n'est jamais portee
        # par la couleur seule, ce qui satisfait la relief rule.
        o.append(
            f'<text x="24" y="{y + 4}" font-size="12.5" fill="{t["ink"]}">{esc(label)}</text>'
        )
        o.append(
            f'<rect x="{bx:.1f}" y="{y - BARH + 4:.1f}" width="{bw:.1f}" height="{BARH}" '
            f'rx="3.5" fill="{fill}"/>'
        )
        if dur:
            o.append(
                f'<text x="{bx + bw + 8:.1f}" y="{y + 4}" font-size="10.5" '
                f'fill="{t["ink3"]}">{esc(dur)}</text>'
            )

    # pied
    fy = H - 34
    o.append(
        f'<text x="24" y="{fy}" font-size="12.5" fill="{t["ink"]}">'
        f'wassim badraoui <tspan fill="{t["ink3"]}">·</tspan> '
        f'machine learning engineer <tspan fill="{t["ink3"]}">·</tspan> paris</text>'
    )
    o.append(
        f'<text x="24" y="{fy + 17}" font-size="11.5" fill="{t["ink2"]}">'
        f'three roles back to back since 2024. next span opens october 2026.</text>'
    )
    o.append("</svg>")
    return "\n".join(o)


for mode in ("light", "dark"):
    p = f"trace-{mode}.svg"
    open(p, "w").write(build(mode))
    print(f"ecrit {p}")

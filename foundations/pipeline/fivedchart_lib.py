# -*- coding: utf-8 -*-
"""
BIBLIOTECA-PADRÃO 5DCHART (esferas 3D glossy com degradê + cores sólidas).
Renderizador oficial para TODAS as análises 5D (atuais e futuras).

Cada bolha codifica 5 dimensões: X, Y, Z (eixos espaciais), tamanho (4ª) e cor (5ª).
Estilo fiel aos templates de \\5dchart: esfera glossy (degradê difuso + brilho especular),
caixa wireframe, sombras e linhas de projeção no piso, 3 eixos coloridos.

Uso:
    from fivedchart_lib import render_5d
    items = [dict(x=.., y=.., z=.., s=.., c=.., lbl='..'), ...]   # c = categoria (str) ou valor (num)
    render_5d(items, ['rótulo X','rótulo Y','rótulo Z'], 'Título', '/caminho/saida.png',
              color_mode='cat'|'value', cmap='viridis', legend_title='...', color_label='...', note='...')
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, FancyArrowPatch
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize
from matplotlib.lines import Line2D
import matplotlib.patheffects as pe

plt.rcParams['font.family'] = 'DejaVu Sans'
_L = 10.0; _ORIG = np.array([0.0, 0.0])
_EX = np.array([0.95, -0.30]); _EY = np.array([0.62, 0.46]); _EZ = np.array([0.0, 1.0])
def _proj(xn, yn, zn): return _ORIG + xn*_EX*_L + yn*_EY*_L + zn*_EZ*_L

def sphere_rgba(n, base_rgb, light=(-0.45, 0.55)):
    """Esfera glossy com degradê (cor sólida + brilho especular)."""
    gg = np.linspace(-1, 1, n); xx, yy = np.meshgrid(gg, gg)
    r2 = xx**2 + yy**2; mask = r2 <= 1.0; z = np.sqrt(np.clip(1-r2, 0, 1))
    lx, ly, lz = light[0], light[1], 0.72
    ln = (lx*lx+ly*ly+lz*lz)**0.5; lx, ly, lz = lx/ln, ly/ln, lz/ln
    diff = np.clip(xx*lx+yy*ly+z*lz, 0, 1)
    shade = 0.22 + 0.78*diff
    spec = np.clip(xx*lx+yy*ly+z*lz, 0, 1)**45
    rim = np.clip(1-z, 0, 1)**2*0.20
    base = np.array(base_rgb, float); rgba = np.zeros((n, n, 4))
    for i in range(3):
        rgba[..., i] = np.clip(base[i]*shade - rim + spec*0.95, 0, 1)
    a = mask.astype(float); edge = (r2 > 0.86) & mask
    a[edge] = np.clip((1-r2[edge])/(1-0.86), 0, 1); rgba[..., 3] = a
    return rgba

def _short(s, n=16): return s if len(str(s)) <= n else str(s)[:n-1]+'…'

def render_5d(items, axis_labels, title, out_path, color_mode='cat', cmap='viridis',
              color_label='', legend_title='', note='', size_label='tamanho = dimensão 4\n(bolha maior = maior)',
              dpi=115, dim_prefix=True, size_legend_title='Dim.4 — Faturamento (tamanho)',
              size_fmt=lambda v: f'~R$ {v/1000:.0f}k', show_ticks=True):
    xs = np.array([it['x'] for it in items], float); ys = np.array([it['y'] for it in items], float)
    zs = np.array([it['z'] for it in items], float); ss = np.array([it['s'] for it in items], float)
    def nrm(a):
        lo, hi = a.min(), a.max()
        return ((a-lo)/(hi-lo) if hi > lo else np.full_like(a, .5)), lo, hi
    xn, xlo, xhi = nrm(xs); yn, ylo, yhi = nrm(ys); zn, zlo, zhi = nrm(zs)
    sn = (ss-ss.min())/(ss.max()-ss.min()) if ss.max() > ss.min() else np.full_like(ss, .5)
    rad = 0.78 + 1.70*np.sqrt(sn)   # esferas maiores/mais visíveis (vendorizado p/ o Framework)
    if color_mode == 'cat':
        cats = []
        for it in items:
            if it['c'] not in cats: cats.append(it['c'])
        pal = plt.get_cmap('tab10'); cmap_cat = {c: pal(i % 10)[:3] for i, c in enumerate(cats)}
        colors = [cmap_cat[it['c']] for it in items]; norm = None
    else:
        cv = np.array([it['c'] for it in items], float)
        norm = Normalize(cv.min(), cv.max()); cm = plt.get_cmap(cmap)
        colors = [cm(norm(v))[:3] for v in cv]

    fig = plt.figure(figsize=(13, 9), facecolor='white')
    ax = fig.add_axes([0.02, 0.10, 0.80, 0.84]); ax.set_aspect('equal'); ax.axis('off')
    corners = {(a, b, c): _proj(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)}
    edges = [((0,0,0),(1,0,0)),((0,0,0),(0,1,0)),((0,0,0),(0,0,1)),((1,0,0),(1,1,0)),
             ((1,0,0),(1,0,1)),((0,1,0),(1,1,0)),((0,1,0),(0,1,1)),((0,0,1),(1,0,1)),
             ((0,0,1),(0,1,1)),((1,1,0),(1,1,1)),((1,0,1),(1,1,1)),((0,1,1),(1,1,1))]
    for p, q in edges:
        a, b = corners[p], corners[q]; ax.plot([a[0], b[0]], [a[1], b[1]], color='#C9C9D2', lw=0.8, zorder=1)
    GC = '#E3E3EA'
    for t in np.linspace(0, 1, 6):
        # piso (z=0)
        a, b = _proj(t, 0, 0), _proj(t, 1, 0); ax.plot([a[0], b[0]], [a[1], b[1]], color=GC, lw=0.6, zorder=1)
        a, b = _proj(0, t, 0), _proj(1, t, 0); ax.plot([a[0], b[0]], [a[1], b[1]], color=GC, lw=0.6, zorder=1)
        # parede de fundo (y=1) — GRID interno
        a, b = _proj(t, 1, 0), _proj(t, 1, 1); ax.plot([a[0], b[0]], [a[1], b[1]], color=GC, lw=0.5, zorder=1)
        a, b = _proj(0, 1, t), _proj(1, 1, t); ax.plot([a[0], b[0]], [a[1], b[1]], color=GC, lw=0.5, zorder=1)
        # parede esquerda (x=0) — GRID interno
        a, b = _proj(0, t, 0), _proj(0, t, 1); ax.plot([a[0], b[0]], [a[1], b[1]], color=GC, lw=0.5, zorder=1)
        a, b = _proj(0, 0, t), _proj(0, 1, t); ax.plot([a[0], b[0]], [a[1], b[1]], color=GC, lw=0.5, zorder=1)
    # eixos + rótulos "Dim.N —" + valores numéricos (ticks)
    axinfo = [(_EX, '#1F77B4', axis_labels[0], xlo, xhi, 'x', (0, -0.42)),
              (_EY, '#D62728', axis_labels[1], ylo, yhi, 'y', (0.22, 0.0)),
              (_EZ, '#2CA02C', axis_labels[2], zlo, zhi, 'z', (-0.45, 0.0))]
    _center = _proj(0.5, 0.5, 0.5)
    for k, (vec, col, lab, lo, hi, axn, toff) in enumerate(axinfo, 1):
        end = _ORIG+vec*_L*1.06
        ax.add_patch(FancyArrowPatch(_ORIG, end, arrowstyle='-|>', mutation_scale=18, color=col, lw=2.2, zorder=2))
        # rótulo "Dim.N —" posicionado FORA do cubo (retângulos de referência), alinhado ao eixo
        full = (f'Dim.{k} — ' if dim_prefix else '') + lab
        rot = np.degrees(np.arctan2(vec[1], vec[0]))
        if rot > 90: rot -= 180
        if rot < -90: rot += 180
        if axn == 'x':      # base, abaixo do cubo (centro)
            lab_pos = _proj(0.55, 0, 0) + np.array([0.0, -2.7])
        elif axn == 'y':    # canto inferior-esquerdo, fora (diagonal)
            lab_pos = _ORIG + np.array([-1.9, -2.4])
        else:               # à esquerda do eixo Z, fora (vertical)
            lab_pos = _proj(0, 0, 0.5) + np.array([-2.4, 0.0])
        ax.text(lab_pos[0], lab_pos[1], full, color=col, fontsize=10.5, fontweight='bold',
                ha='center', va='center', rotation=rot, rotation_mode='anchor', zorder=26,
                bbox=dict(boxstyle='round,pad=0.25', fc='white', ec=col, lw=0.8, alpha=0.95))
        if show_ticks:
            for t in (0.0, 0.25, 0.5, 0.75, 1.0):
                pt = _proj(*((t, 0, 0) if axn == 'x' else (0, t, 0) if axn == 'y' else (0, 0, t)))
                tick_to = pt + np.array(toff)*0.5
                ax.plot([pt[0], tick_to[0]], [pt[1], tick_to[1]], color=col, lw=0.9, zorder=6)
                val = lo + t*(hi-lo)
                ax.text(pt[0]+toff[0], pt[1]+toff[1], f'{val:g}', color=col, fontsize=6.5, ha='center', va='center',
                        zorder=26, bbox=dict(boxstyle='round,pad=0.05', fc='white', ec='none', alpha=0.7))
    order = sorted(range(len(items)), key=lambda i: (yn[i]-xn[i]*0.3-zn[i]*0.15), reverse=True)
    for i in order:
        cx, cy = _proj(xn[i], yn[i], zn[i]); fx, fy = _proj(xn[i], yn[i], 0.0)
        ax.plot([fx, cx], [fy, cy], color='#9A9AA6', lw=0.8, alpha=0.7, zorder=3)
        ax.add_patch(Ellipse((fx, fy), rad[i]*1.7, rad[i]*0.62, facecolor=colors[i], alpha=0.22, edgecolor='none', zorder=2))
        rr = rad[i]
        ax.imshow(sphere_rgba(140, colors[i]), extent=[cx-rr, cx+rr, cy-rr, cy+rr], zorder=5+0.001*i, interpolation='bilinear')
        lbl = it_lbl(items[i])
        if lbl:
            ax.text(cx, cy, _short(lbl, 18), ha='center', va='center', fontsize=8, fontweight='bold',
                    color='white', zorder=20, path_effects=[pe.withStroke(linewidth=2.2, foreground='#00000088')])
    allp = [_proj(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)]
    ax.set_xlim(min(p[0] for p in allp)-3.4, max(p[0] for p in allp)+2.2)
    ax.set_ylim(min(p[1] for p in allp)-2.4, max(p[1] for p in allp)+1.6)
    fig.suptitle(title, fontsize=15, fontweight='bold', color='#1F3864', y=0.975)
    lax = fig.add_axes([0.83, 0.12, 0.15, 0.76]); lax.axis('off')
    if color_mode == 'cat':
        h = [Line2D([0], [0], marker='o', color='w', markerfacecolor=cmap_cat[c], markeredgecolor='k',
                    markersize=11, label=c) for c in cats]
        lax.legend(handles=h, title=legend_title or 'Cor', loc='upper center', fontsize=8.5, title_fontsize=9.5, framealpha=.95)
    else:
        sm = ScalarMappable(norm=norm, cmap=plt.get_cmap(cmap)); sm.set_array([])
        cb = fig.colorbar(sm, ax=lax, fraction=0.5, pad=0.0, aspect=16); cb.set_label(color_label, fontsize=9)
    # legenda de TAMANHO (diâmetro -> 4ª dimensão, ex.: faturamento) com bolhas de referência
    smin, smax = ss.min(), ss.max()
    refs = [0.12, 0.45, 1.0]
    sh = [Line2D([0], [0], marker='o', color='w', markerfacecolor='#9AA0AA', markeredgecolor='#555',
                 markersize=(0.42+1.05*np.sqrt(f))*13, label=size_fmt(smin+f*(smax-smin))) for f in refs]
    leg = ax.legend(handles=sh, title=size_legend_title, loc='upper left', fontsize=8,
                    title_fontsize=8.5, labelspacing=1.7, borderpad=1.0, handletextpad=1.2, framealpha=0.95)
    leg.set_zorder(30)
    if note:
        fig.text(0.5, 0.035, note, ha='center', fontsize=9, color='#595959')
    fig.savefig(out_path, dpi=dpi, bbox_inches='tight', pad_inches=0.3); plt.close()
    return out_path

def it_lbl(it): return it.get('lbl', it.get('name', ''))

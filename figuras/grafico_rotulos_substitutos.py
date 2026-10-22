import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.family': 'serif', 'font.size': 9})

GRUPOS = [
  ('Sinal, sem rótulos clínicos', [
    ('ResNet-18 treinada para MSC', .508, .431, .588),
    ('Extrator aleatório (controle)', .529, .437, .615),
    ('Autoencoder', .494, .413, .576),
    ('Mascarado', .555, .476, .649),
    ('Contrastivo', .590, .501, .677)]),
  ('Sinal, orientado por conhecimento clínico', [
    ('Dois marcadores pré-especificados', .647, .563, .726),
    ('Rede multitarefa (representação)', .682, .600, .763)]),
  ('Variáveis do estudo MUSIC', [
    ('Seis variáveis clínicas', .661, .580, .743),
    ('Pro-BNP', .682, .605, .753),
    ('Ecocardiograma', .714, .641, .774),
    ('Todos os exames', .738, .666, .809)]),
  ('Combinações com as seis variáveis clínicas', [
    ('+ dois marcadores', .679, .599, .757),
    ('+ rede multitarefa', .702, .621, .780),
    ('+ ecocardiograma', .720, .640, .789),
    ('+ todos os exames', .733, .656, .804),
    ('+ todos os exames + rede', .728, .652, .798)]),
]
TINTA, SEC, COR = '#1f1f1f', '#5c5c5c', '#2b5c8a'
linhas, y, rot, cab = [], 0, [], []
for g, itens in GRUPOS:
    cab.append((y, g)); y += 1
    for n, a, lo, hi in itens:
        linhas.append((y, a, lo, hi)); rot.append((y, n)); y += 1
    y += 0.4
fig, ax = plt.subplots(figsize=(6.3, 0.27 * y + 0.6))
for yy, a, lo, hi in linhas:
    ax.plot([lo, hi], [yy, yy], color=COR, lw=1.6, solid_capstyle='round')
    ax.plot(a, yy, 'o', color=COR, ms=5.5, mec='white', mew=1)
    ax.text(0.865, yy, f'{a:.3f}'.replace('.', ','), va='center', ha='right', fontsize=8, color=SEC)
ax.axvline(0.5, color=SEC, ls='--', lw=0.8)
ax.axvline(0.661, color=SEC, ls=':', lw=1)
ax.set_yticks([r[0] for r in rot]); ax.set_yticklabels([r[1] for r in rot], color=TINTA)
for yy, g in cab:
    ax.text(0.36, yy, g, fontweight='bold', va='center', ha='left', color=TINTA, fontsize=8.5, bbox=dict(facecolor='white', edgecolor='none', pad=1.5),
            transform=ax.get_yaxis_transform() if False else ax.transData)
ax.set_xlim(0.36, 0.87); ax.set_ylim(y - 0.2, -0.8)
ax.set_xlabel('AUC fora da partição (IC 95%)', color=TINTA)
ax.xaxis.set_major_formatter(lambda v, _: f'{v:.2f}'.replace('.', ','))
ax.set_xticks([0.4, 0.5, 0.6, 0.7, 0.8])
ax.grid(axis='x', color='#e6e6e6', lw=0.6); ax.set_axisbelow(True)
for s in ('top', 'right', 'left'): ax.spines[s].set_visible(False)
ax.tick_params(axis='y', length=0)
ax.text(0.5, -0.75, 'acaso', ha='center', va='bottom', fontsize=7.5, color=SEC)
ax.text(0.661, -0.75, 'clínicas', ha='center', va='bottom', fontsize=7.5, color=SEC)
plt.tight_layout()
plt.savefig('resultados_rotulos_substitutos.pdf', bbox_inches='tight')
plt.savefig('resultados_rotulos_substitutos.png', dpi=200, bbox_inches='tight')

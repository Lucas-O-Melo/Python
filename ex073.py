times = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Mirassol',
         'Botafogo', 'Bahia', 'Fluminense', 'Vasco',
         'São Paulo', 'Bragantino', 'Corinthians', 'Grêmio',
         'Ceará SC', 'Internacional', 'Atlético-MG', 'Santos',
         'Vitória', 'Juventude', 'Fortaleza', 'Sport', 'Recife')
print('-=' * 15)
print(f'Lista de Times: {times}')
print('-=' * 15)
print(f'Os cinco primeiros são: {times[:5]}')
print('-=' * 15)
print(f'Os ultimos 4 colocados são: {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Grande Corinthians está na {times.index("Corinthians")+1}ª posição')
#print(f'O Grande {times[10]} esta em 11° lugar')
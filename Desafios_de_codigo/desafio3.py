# desafio 3

valores = [10, 85]
COSUMO_MEDIO = 12

tempo_de_viagen = float(valores[0])
velocidade_media = float(valores[1])

distancia_percorrida = float(tempo_de_viagen * velocidade_media)
consumo_total = distancia_percorrida / COSUMO_MEDIO

print(f'{consumo_total:.3f}')
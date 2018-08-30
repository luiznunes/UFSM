"""
Luiz G.
Marcelo M.
"""

import time
from math import log10
import numpy as np
import matplotlib.pyplot as plt


def expressao(exponencial):
    for exp in range(0, exponencial):
        resultado = 0
        start_time = time.time()
        n = pow(10, exp)
        for k in range(1, n + 1):
            resultado += 1 / (k * (k + 1))

        print("N: 10^" + str(exp))
        print(str(resultado))
        print("--- %s seconds ---" % (time.time() - start_time))
        print('')


"""Funcao utilizada na map retorna apenas o log de cada item da lista"""


def calculolog(n):
    return log10(n)


def calculoformula(exp):
    return pow(10, exp)


def formula(n):
    start_time = time.time()
    calc = (n * (n + 1)) / 2
    tempo = time.time() - start_time
    print('Resultado:', calc)
    print('Tempo:', tempo, end="\n\n")
    return (tempo)


# tempos da ultima execução
tempo = [
    0.00004124641418457031,
    0.00002765655517578125,
    0.00005245208740234375,
    0.00026345252990722656,
    0.0021965503692626953,
    0.021300554275512695,
    0.20853614807128906,
    2.016371250152588,
    22.192879915237427,
    368.6107008457184,
    4345.233531236649
]
y_data_tempo = list(map(calculolog, tempo))
x = []
for c in range(0, len(tempo)):
    x.append(c)

m = list(map(lambda exp: pow(10, exp), range(0, len(y_data_tempo))))
y_data_formula = list(map(formula, m))
y_data_formula = list(map(calculolog, y_data_formula))

plt.plot(x, y_data_tempo, 'go')
plt.plot(x, y_data_tempo, 'k:', color="green")

plt.plot(x, y_data_formula, 'r^')
plt.plot(x, y_data_formula, 'k:', color='orange')  # linha tracejada azul

plt.axis([-1, 11, (min(y_data_tempo) - 5), (max(y_data_tempo) + 5)])

plt.grid(True)
plt.xlabel("Log(n)")
plt.ylabel("Log(Tempo)")
plt.show()

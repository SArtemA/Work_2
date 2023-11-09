# подключаем библиотеки
import json
import numpy as np

matrix = np.load('matrix_78.npy')

size = len(matrix)

m_stat = dict()
m_stat['sum'] = 0
m_stat['avr'] = 0
m_stat['sumMD'] = 0
m_stat['avrMD'] = 0
m_stat['sumSD'] = 0
m_stat['avrSD'] = 0
m_stat['max'] = matrix[0][0]
m_stat['min'] = matrix[0][0]

for i in range(0, size):
    for j in range(0, size):
        m_stat['sum'] += matrix[i][j]

        if i == j:
            m_stat['sumMD'] += matrix[i][j]

        if i + j == (size - 1):
            m_stat['sumSD'] += matrix[j][j]

        m_stat['max'] = max(m_stat['max'], matrix[i][j])
        m_stat['min'] = max(m_stat['min'], matrix[i][j])

m_stat['avr'] = m_stat['sum'] / (size ** 2)
m_stat['avrMD'] = m_stat['sumMD'] / size
m_stat['avrSD'] = m_stat['sumSD'] / size

for key in m_stat.keys():
    m_stat[key] = float(m_stat[key])

with open('matrix_stat.json', 'w') as file:
    file.write((json.dumps(m_stat)))

norm_matrix = np.ndarray((size, size), dtype=float)

for i in range(0, size):
    for j in range(0, size):
        norm_matrix[i][j] = matrix[i][j] / m_stat['sum']


perem = 0
for i in norm_matrix:
    perem+=sum(i)

np.save('norm_matrix', norm_matrix)

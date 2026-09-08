# ATIVIDADE - ESTRUTURAS DE DADOS
# Ordenação: Bubble Sort x Quick Sort
import random

def bubble_sort(v):
    v = v[:]; comp = troc = 0
    for i in range(len(v) - 1):
        troca = False
        for j in range(len(v) - 1 - i):
            comp += 1
            if v[j] > v[j + 1]:
                v[j], v[j + 1] = v[j + 1], v[j]
                troc += 1; troca = True
        if not troca: break
    return comp, troc

def quick_sort(v):
    if len(v) <= 1: return v, 0, 0
    pivo, resto = v[-1], v[:-1]
    menores = [x for x in resto if x <= pivo]
    maiores = [x for x in resto if x > pivo]
    comp = len(resto)
    e, ce, me = quick_sort(menores)
    d, cd, md = quick_sort(maiores)
    return e + [pivo] + d, comp + ce + cd, len(v) + me + md

print(f"Tam | Bubble(comp,troca) | Quick(comp,mov)")
for n in (10, 20, 1000):
    random.seed(42)
    dados = [random.randint(0, 99999) for _ in range(n)]
    cb, tb = bubble_sort(dados)
    _, cq, mq = quick_sort(dados)
    print(n, "|", cb, tb, "|", cq, mq)

# Busca sequencial em matriz
def busca(m, valor):
    comp = 0
    for i, linha in enumerate(m):
        for j, x in enumerate(linha):
            comp += 1
            if x == valor: return i, j, comp
    return -1, -1, comp

print("Matriz | Início | Final | Inexistente")
for lin, col in ((2, 2), (10, 10), (100, 100)):
    m = [[i * col + j + 1 for j in range(col)] for i in range(lin)]
    tot = lin * col
    _, _, c1 = busca(m, m[0][0])
    _, _, c2 = busca(m, m[-1][-1])
    _, _, c3 = busca(m, tot + 999)
    print(f"{lin}x{col} | {c1} | {c2} | {c3}")

# Hands On 1: array de temperaturas
temp = [float(input(f"Temperatura {i}: ")) for i in range(10)]
media = sum(temp) / 10

print("Temperaturas:", temp)
print("Média:", round(media, 2))
print("Maior:", max(temp), "índice", temp.index(max(temp)))
print("Menor:", min(temp), "índice", temp.index(min(temp)))
print("Acima da média:", sum(1 for t in temp if t > media))

# Hands On 2: matriz de sensores (5x24)
sensores = [
    [18,18,17,17,16,16,17,19,21,23,25,27,28,29,29,28,27,25,23,21,20,19,18,18],
    [20,19,19,18,18,19,21,23,25,27,29,31,32,33,33,32,31,29,27,25,23,22,21,20],
    [15,15,14,14,14,15,16,18,20,22,24,26,27,28,28,27,26,24,22,20,18,17,16,15],
    [22,21,21,20,20,21,23,25,27,29,31,33,34,35,35,34,33,31,29,27,25,24,23,22],
    [17,16,16,15,15,16,18,20,22,24,26,28,29,30,30,29,28,26,24,22,20,19,18,17],
]
limite = float(input("Limite de temperatura: "))
todas = [v for linha in sensores for v in linha]
maior = max(todas)
si, hi = next((i, j) for i, l in enumerate(sensores) for j, v in enumerate(l) if v == maior)

print("Médias:", [round(sum(l) / 24, 2) for l in sensores])
print("Maior:", maior, f"(sensor {si}, hora {hi}h)")
print("Média geral:", round(sum(todas) / 120, 2))
print("Acima do limite:", sum(1 for v in todas if v > limite))

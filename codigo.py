# ATIVIDADE - CENTRAL DE DISTRIBUIÇÃO DE PEDIDOS
# Bubble, Insertion, Selection e Quick Sort
import sys, random
sys.setrecursionlimit(5000)

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

def insertion_sort(v):
    v = v[:]; comp = mov = 0
    for i in range(1, len(v)):
        chave = v[i]
        j = i - 1
        while j >= 0:
            comp += 1
            if v[j] > chave:
                v[j + 1] = v[j]
                mov += 1
                j -= 1
            else:
                break
        v[j + 1] = chave
    return comp, mov

def selection_sort(v):
    v = v[:]; comp = troc = 0
    n = len(v)
    for i in range(n - 1):
        idx_min = i
        for j in range(i + 1, n):
            comp += 1
            if v[j] < v[idx_min]:
                idx_min = j
        if idx_min != i:
            v[i], v[idx_min] = v[idx_min], v[i]
            troc += 1
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

print("Tam | Bubble(c,t) | Insertion(c,m) | Selection(c,t) | Quick(c,m)")
for n in (10, 20, 1000):
    random.seed(42)
    vetor_bubble = [random.randint(0, 99999) for _ in range(n)]
    vetor_insertion = vetor_bubble.copy()
    vetor_selection = vetor_bubble.copy()
    vetor_quick = vetor_bubble.copy()

    cb, tb = bubble_sort(vetor_bubble)
    ci, mi = insertion_sort(vetor_insertion)
    cs, ts = selection_sort(vetor_selection)
    _, cq, mq = quick_sort(vetor_quick)

  # Desafio adicional: aleatório x ordenado x invertido (n = 1000)
n = 1000
random.seed(42)
aleatorio = [random.randint(0, 99999) for _ in range(n)]
ordenado = sorted(aleatorio)
invertido = sorted(aleatorio, reverse=True)

casos = {"Aleatório": aleatorio, "Ordenado": ordenado, "Invertido": invertido}
print(f"{'Caso':<12}{'Bubble(c,t)':<16}{'Insertion(c,m)':<18}{'Selection(c,t)':<18}{'Quick(c,m)'}")
for nome, dados in casos.items():
    cb, tb = bubble_sort(dados)
    ci, mi = insertion_sort(dados)
    cs, ts = selection_sort(dados)
    _, cq, mq = quick_sort(dados)
    print(f"{nome:<12}{str((cb,tb)):<16}{str((ci,mi)):<18}{str((cs,ts)):<18}{(cq,mq)}")







  
    print(n, "|", cb, tb, "|", ci, mi, "|", cs, ts, "|", cq, mq)

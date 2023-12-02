# 63 Fibonnaci  nao consegui
n = int(input('Diginte um numero para sua sequência de fibonacci: '))
t1 = 0
t2 = 1
print(f'- {t1}\n- {t2}')

for _ in range(3, n + 1):
    t3 = t1 + t2
    print(f'- {t3}')
    t1 = t2
    t2 = t3 
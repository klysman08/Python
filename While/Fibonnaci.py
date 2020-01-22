# 63 Fibonnaci  nao consegui
n = int(input('Diginte um numero para sua sequência de fibonacci: '))
t1 = 0
t2 = 1
i = 3
print('- {}\n- {}'.format(t1, t2))

while (i <= n):
    t3 = t1 + t2
    print('- {}'.format(t3))
    t1 = t2
    t2 = t3
    i += 1 
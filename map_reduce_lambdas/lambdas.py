from functools import reduce

alunos = [
    {'nome': 'João', 'nota': 5.0},
    {'nome': 'Maria', 'nota': 7.0},
    {'nome': 'José', 'nota': 8.0},
    {'nome': 'Ana', 'nota': 9.0},
    {'nome': 'Pedro', 'nota': 10.0}
]

aluno_aprovado = lambda aluno: aluno['nota'] >= 7.0

alunos_aprovados = filter(aluno_aprovado, alunos)
print(list(alunos_aprovados))
from functools import reduce

# List of students with their names and grades
alunos = [
    {'nome': 'João', 'nota': 5.0},
    {'nome': 'Maria', 'nota': 7.0},
    {'nome': 'José', 'nota': 8.0},
    {'nome': 'Ana', 'nota': 9.0},
    {'nome': 'Pedro', 'nota': 10.0}
]

alunos_aprovados = [aluno for aluno in alunos if aluno['nota'] >= 7.0]

notas_alunos_aprovados = [aluno['nota'] for aluno in alunos_aprovados]

print(notas_alunos_aprovados)
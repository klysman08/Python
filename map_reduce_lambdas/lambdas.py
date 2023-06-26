from functools import reduce

# List of students with their names and grades
alunos = [
    {'nome': 'João', 'nota': 5.0},
    {'nome': 'Maria', 'nota': 7.0},
    {'nome': 'José', 'nota': 8.0},
    {'nome': 'Ana', 'nota': 9.0},
    {'nome': 'Pedro', 'nota': 10.0}
]

# Lambda function to check if a student's grade is greater than or equal to 7.0
aluno_aprovado = lambda aluno: aluno['nota'] >= 7.0

# Filter the list of students to only include those who passed
alunos_aprovados = filter(aluno_aprovado, alunos)

# Print the list of students who passed
print(list(alunos_aprovados))
# Entrada de dados
# Apresenta erros nos dias

entrada = int(input(""))

ano = 0
dia = 0
mes = 0

# Verificao ano
ano = int(entrada/365)

# Verifica mes

mes = int((entrada % 365) / 30)

# Verifica dias

dias = int((entrada % 365) % 30)

print(ano, " ano(s)")
print(mes, " mes(es)")
print(dia, " dia(s)")

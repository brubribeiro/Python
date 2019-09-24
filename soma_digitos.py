n = int(input("Digite um número inteiro: "))
soma = 0
aux = n
while (aux > 0):
	soma = soma + aux % 10
	aux = int(aux/10)
print(soma)

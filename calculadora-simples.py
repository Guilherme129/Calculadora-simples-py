#Função para a operação matemática após a escolha de qual vai ser feita.
#Essa função utiliza de 3 valores de variáveis, sendo elas a "operação", "x" e "y".
def matematica(operacao, x, y):
	if operacao == 1:
		resultado = x + y
	elif operacao == 2:
		resultado = x - y
	elif operacao == 3:
		resultado = x / y
	elif operacao == 4:
		resultado = x * y
	else:
		return "ESCREVA UMA OPÇÃO VÁLIDA!"
	return resultado
#Este código faz com que as opções a serem escolhidas sempre fiquem aparentes
while True:
	print("1 = soma")
	print("2 = subtração")
	print("3 = divisão")
	print("4 = multiplicação")

	operacao = int(input("Escolha o tipo de operação que deseja usar: "))
	
#Este código identifica se o número digitado na variável "operação" é válido.
#Se for ele pede os inputs dos valores que seram utilizados.
	if operacao not in [1, 2, 3, 4]:
		print("ESCREVA UMA OPÇÃO VÁLIDA!")
		continue
	x = int(input("Escreva o primeiro número: "))
	y = int(input("Escreva o segundo número: "))

#Aqui é onde a função feita anteriormente é chamada, já com os valores digitados pelo usuário	
	resultado = matematica(operacao, x, y)
	print(f"O resultado é: {resultado}")
	
#Nesta parte é para caso o usuário deseje continuar usando a calculadora
	continuar = int(input("Se deseja fazer mais calculos digite o número 1, se não número 2: "))
	
	if continuar != 1:
		break

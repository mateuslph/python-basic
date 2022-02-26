# 1, printar Brasil 3 vezes
print("Brasil  " *3)

# 2, imprima a primeira letra
print("Brasil"[0])

# 3, imprima o trecho "rasi"
print("Brasil"[1:5])

# 4, imprima do "r" endiante
print("Brasil"[1:])

# 5, imprima a quantidade de letras
print(len("Brasil"))

# 6, verificar se existe a letra "i"
print("i" in "Brasil")
# 7, tem "f" em "Brasil"
print("f" in "Brasil")

# 8, imprimir o nome dos paises separado por duas barras (Brasil, Argentina, Italia, Equador, Uruguai, Espanha, Nigeria)
print("Brasil", "Argentina", "Italia", "Equador", "Uruguai", "Espanha", "Nigéria", sep="//")

# 9, imprimir o exercicio anterior, mas com a substituicao de imprimir um em cada linha
print("Brasil", "Argentina", "Italia", "Equador", "Uruguai", "Espanha", "Nigéria", sep="\n")

# 9.1, extra, imprimir um triangulo (pode ser com asterisco)
print("      *      ", "    *   *    ", "  *       *  ", " * * * * * * ", sep="\n")
# ou:
print("     /\     ", "    /  \    ", "   /    \   ", "  /      \  ", " /________\ ", sep="\n")
# obs do exercicio anterior: deve ser feito com menas linhas possível, para esse exemplo nao foi usado funcao

# extra de Alonso, a escada ficou assim:
def stair(n):
    if n >= 1:
        for i in range(1, n + 1):
            output = ' ' * (n - i) + '*' * i
            print(output)
                
    else:
        raise ValueError("Por favor, digite um número inteiro maior ou igual a 1!")

stair(6)

# 10, em uma lista com todos paises deve-se imprimir apenas Uruguai
lista = ["Brasil", "Argentina", "Italia", "Equador", "Uruguai", "Espanha", "Nigéria"]
print(lista[4])

# 11, em uma lista com todos paises deve-se imprimir apenas Argentina e Uruguai
lista = ["Brasil", "Argentina", "Italia", "Equador", "Uruguai", "Espanha", "Nigéria"]
print(lista[1], lista[3])

# 12, em uma lista com todos paises deve-se imprimir apenas Argentina ate Espanha
lista = ["Brasil", "Argentina", "Italia", "Equador", "Uruguai", "Espanha", "Nigéria"]
print(lista[1:6])

# 13, imprimir o nome do pais uruguai e a segunda, terceira e a quarta letra de uruguai ("ugu")
lista = ["Brasil", "Argentina", "Italia", "Equador", "Uruguai", "Espanha", "Nigéria"]
print(lista[4])
print(lista[4][2:5])

# extra, atividade do professor, usuario informar o nome do carro e imprimir o nome do carro que esse cliente escolheu
carro = input("Informe o nome de um carro")
print("O carro é um ", carro)

# 14, imprima uma vez para o usuario um modelo de carro e em seguida o modelo de ma moto
carro = input("Informe o nome de um carro \n")
moto = input("Informe o nome de um moto \n")
print("O carro é um ", carro)
print("O moto é uma ", moto)

# 15, imprima o nome de um carro quantas vezes o usuario quiser
carro = input("Informe o nome de um carro \n")
qnt = int(input("Quantas vezes quer imprimir \n"))
print(carro*qnt)

# 16, imprima o numero de letras do carro que o usuario passar
carro = input("Informe o nome de um carro \n")
# tem varias maneiras de consilhar strings, com atencao para algumas particularidades:
# usando "f" e "chaves"
print(f"O carro {carro} contém {len(carro)} letras")
# ou usar "virgula"
print("O carro", carro, "contém", len(carro), "letras")
# ou usar ".format()"
print("O carro {} contém {} letras".format(carro, len(carro)))
# ou usar "+", nesse caso existem algumas excecoes, como se for seguido de um numero vai somar
print("O carro" + carro, "contém" + len(carro), "letras")

# 17, imprima o nome do carro escolhido pelo usuario, depois imprima uma letra desse carro conforme posicao informada
# tambem pelo usuario
carro = ["Sandero", "Gol", "Ecosport", "Cruze"]
escolhido = str(input("Digite exatamente uma marca de carro dentre as asseguir: Sandero, Gol, Ecosport, Cruze \n"))
if escolhido in carro:
    posicao = int(input("Informe qual posicao que você quer ver, contado a partir de 0 (zero) \n"))
    if (posicao <= len(escolhido)-1 and (posicao >= 0)):
        print(escolhido, " - Letra ", posicao, '- "', escolhido[posicao], '"')
    else:
        print("Essa posição não existe!")
else:
    print("O nome digitado não corresponde.")

# 18, imprima o nome de dois veiculos escolhidos pelo usuario e separe a impressao deles conforme o separador da 
# preferencia do usuario, sendo "//, **, $$, &&, \"
carro1 = input("Informe a marca do primeiro carro \n")
carro2 = input("Informe a marca do segundo carro \n")
separador = input("Escolha um separador desses (**, //, $$, &&, \)")
print(carro1, carro2, sep=separador)

# 19, imprima o nome informado de dois veiculos, um em cada linha com um unico print
carro1 = input("Informe a marca do primeiro carro 1 \n")
carro2 = input("Informe a marca do segundo carro 2 \n")
print(carro1, carro2, sep="\n")

# 20, o usuario deve inserir na lista tres nomes de carro, depois deve escolher qual a posicao e imprimir na tela, em seguida escolher 
# qual posicao da letra do carro que quer imprimir
nCarros = []
while len(nCarros) < 3:
    print(nCarros)
    tmp = input("Insira o nome do carro: ")
    nCarros.append(tmp)
print("\n", nCarros)
escolhaCarro = int(input("Digite o número do carro: "))
print(nCarros[escolhaCarro -1])
escolhaLetra = int(input("Digite o número da letra: "))
print(nCarros[escolhaCarro -1][escolhaLetra -1])
# outro metodo soh com o que foi ja aprendido
carroA = input("Informe o nome do carro A: ")
carroB = input("Informe o nome do carro B: ")
carroC = input("Informe o nome do carro C: ")
lista = carroA, carroB, carroC
posicao = int(input("Informe a posicao do carro, se é: 1, 2, ou 3: "))
print(lista[posicao-1])  # "-1" eh uma simples subtracao da "posicao", para a numeracao visual equivaler a posicao de indices da lista
letra = int(input("Informe a posicao da letra do carro escolhido: "))
print(lista[posicao-1] [letra-1])

# 21, operacoes basicas matematicas - Imprima na tela a soma, subtracao, divisao e moltiplicacao de dois numeros informados pelo 
# usuario, adicional fazer resto e o cociente da divisao
num1 = float(input("Digite o primeiro numero"))
num2 = float(input("Digite o primeiro numero"))
soma = (num1+num2)
subtracao = (num1-num2)
multiplicacao = (num1*num2)
divisao = (num1/num2)
restoDaDivisao = (num1%num2)
cocienteDaDivisao = (num1//num2)
print("Soma: {} Subtracao: {} Divisão: {} Multiplicação: {} \nResto da divisao {} Cociente da divisao {} ".format(soma, subtracao, "%.2f%", divisao, multiplicacao, restoDaDivisao, cocienteDaDivisao))

# 22, construa uma condicao "if"
from turtle import up


numero = int(input("Digite um numero inteiro"))
if (numero > 0):
    print("Número positivo")
elif (numero < 0):
    print("Número negativo")
else:
    print("O número nulo")

# 23, deixe a frase do usuario em letra 
frase = input("Escreva sua frase")
formato = input("Digite 'AZ' para maiusculas, ou 'az' para minúsculas, ou AzA, para as primeira letras de cada palavra em maiúsculas")
if (formato == "AZ"):
    print(frase.upper())
elif (formato == "az"):
    print(frase.lower())
elif (formato == "AzA"):
    print(frase.title())
else:
    print("Formato inválido")

# 24, imprima na tela o maior numero, o menor numero da lista de tres numero inteiros informado pelo usuario, o tamanho, soma,
# ordem crescente e decrescente
numero1 = int(input("Informe o primeiro número em inteiro"))
numero2 = int(input("Informe o segundo número em inteiro"))
numero3 = int(input("Informe o terceiro número em inteiro"))
lista = [numero1, numero2, numero3]
print("Comprimento da lista: ", len(lista))
print("Maior valor: ", max(lista))
print("Menor valor: ", min(lista))
print("A soma dos números da lista : ", sum(lista))
lista.sort()
print("Lista em forma crescente: ", lista)
lista.reverse()
print("Lista em forma decrescente: ", lista)
# ou
print(f'A lista em ordem decrescente é: {sorted(lista, reverse=True)}') 

# 25, faca um programa qiue verifique se o estudante foi aprovado ou reprovado, onde para ser aprovado o aluno precisa nota 6
# em portugues e matematica
matematica = int(input("Digite a nota em Matemática"))
portugues = int(input("Digite a nota em Português"))
if (matematica >= 6) and (portugues >= 6):
    print("O aluno foi aprovado")
else:
    print("O aluno foi reprovado")

# 26, faca um programa que leia a idade de seis empregados, ou seja, tem que inserir 6 idades
cont = 0
while (cont < 6):
    idade = int(input("Digite a idade"))
    cont +=1

# 26, faca um programa que leia a idade de seis empregados, ou seja, tem que inserir 6 idades, somar as idades
cont = 0
total = 0
while (cont < 3):
    idade = int(input("Digite a idade"))
    total = total + idade
    cont +=1
print("A soma é: ", total)

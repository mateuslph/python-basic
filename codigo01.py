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

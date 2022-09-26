# Atualização organizando o projeto com POO
# Refactoring Guru 
import Extra, Cifra_Cesar_Cifrar, Cifra_Cesar_Descifrar

#regra = int(input("Escolha um dos modelos de regra abaixo:\n[1] - "))

# Regras Simples:
# Regra 01: Substituição 3x4 
# Regra 02: Substituição 3x4 + Palavra Normal com Inicial Maiuscula provavelmente
# Regra 03: Substituição 3x4 + Palavra Normal com Inicial Maiuscula provavelmente + Uma palavra ou uma Sigla toda maiuscula
# Regra 04: Substituição 3x4 + Palavra Cifrada(Cesar) com inicial Maiuscula + Uma palavra ou uma Sigla toda maiuscula

# Regras Medianas:
# Regra 03: Primeira e Terceira letra da primeira palavra maiuscula, caso a primeira letra tenha no minimo tres letras, caso contrario primeira e segunda, as outras palavras seram alteradas em Primeira e terceira somente se a primeira palavra originalmente for maiuscula, se for minuscula a segunda e a terceira seram alteradas, os espaços seram substituidos por [_] [-] [ ]
# Regra 04: 
# Regra 05: 

# Regras Complexas:
# Regra 06:

regra = 0

opcao = int(input("Escolha uma das opções abaixo:\n[1] - Cifra de César (Cifrar)\n[2] - Cifra de César (Descifrar)\nInsira sua escolha: "))

if(opcao >= 1) and (opcao <= 2):
  p01 = input("Insira a palavra principal: ")
  p02 = input("Insira a palavra secundaria: ")
  
  if(opcao == 1):
    marcacao = Extra.Extra(p01, 0)
    marcacao.registrar()
    marcacao.igualar(p02)
    
    cifra_cesar = Cifra_Cesar_Cifrar.Cifra_Cesar_Cifrar(p01, marcacao.list_Str())
    cifra_cesar.conversao_Letra()
    cifra_cesar.lista_Str_Int()
    cifra_cesar.somar()
    cifra_cesar.lista_Int_Str()
    cifra_cesar.conversao_Numero()
    
    marcacao.listaResultado = cifra_cesar.resultadoStr[0]
    marcacao.formatar(marcacao.list_Str())
    marcacao.gravar()
    print(f"Resultado: {marcacao.palavraResultado}\nUm arquivo com o resultado foi criado.")
    
  elif(opcao == 2):
    marcacao = Extra.Extra(p01, 0)
    marcacao.registrar()
    marcacao.igualar(p02)

    cifra_cesar = Cifra_Cesar_Descifrar.Cifra_Cesar_Descifrar(p01, marcacao.list_Str())
    cifra_cesar.conversao_Letra()
    cifra_cesar.lista_Str_Int()
    cifra_cesar.subtrair()
    cifra_cesar.lista_Int_Str()
    cifra_cesar.conversao_Numero()
    
    marcacao.listaResultado = cifra_cesar.resultadoStr[0]
    marcacao.formatar(marcacao.list_Str())
    marcacao.gravar()
    print(f"Resultado: {marcacao.palavraResultado}\nUm arquivo com o resultado foi criado.")

elif(opcao >= 3) and (opcao <= 3):
  pass
else:
  print("ERRO, Opcao inexistente")
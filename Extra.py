# É necessario um registro?
class Extra:
  def __init__(self, palavra: str, regra: int):
    self.palavra = palavra
    self.regra = regra
    self.palavraResultado = ""
    self.lista = []
    self.listaResultado = []
    self.contador = 0
    
  def registrar(self):
    """ Recebe uma string e retorna a marcação de letras minusculas, maiusculas e espaços em uma lista """
      
    for i in range(len(self.palavra)):
      if(self.palavra[i] == " "):
        self.lista.append(0)
      elif(self.palavra[i] != self.palavra[i].upper()):
        self.lista.append(1)
      elif(self.palavra[i] == self.palavra[i].upper()):
        self.lista.append(2)
        	
  def formatar(self, palavra: str):
    """ Recebe uma lista e uma string, formata conforme as marcações da lista """
    self.listaResultado = []
    for i in range(len(self.palavra)):
      if(self.lista[i] == 0):
        self.listaResultado.append(" ")
      elif(self.lista[i] == 1):
        self.listaResultado.append(palavra[i].lower())
      elif(self.lista[i] == 2):
        self.listaResultado.append(palavra[i].upper())
    self.palavraResultado = "".join(self.listaResultado)

  def list_Str(self):
    """ Um [for] comprimido que converte a lista em uma string encapsulada em um [join] que pega cada caractere individualmente """
    return "".join([str(x) for x in self.listaResultado])

  def igualar(self, palavra: str):
    """ Recebe duas palavras e iguala os tamanhos """
    if(len(self.palavra) > len(palavra)):
      palavra = palavra.replace(" ", "")
      self.contador = 0
      for i in range(len(self.palavra)):
        if(len(palavra) == (i - self.contador)):
          self.contador = len(palavra) + self.contador
        if(self.palavra[i] == " "):
          self.listaResultado.append(" ")
          self.contador += 1
        else:
          self.listaResultado.append(palavra[i - self.contador])
    elif(len(self.palavra) < len(palavra)):
      palavra = palavra.replace(" ", "")
      self.contador = 0
      for i in range(len(self.palavra)):
        if(self.palavra[i] == " "):
          self.listaResultado.append(" ")
          self.contador += 1
        else:
          self.listaResultado.append(palavra[i - self.contador]) 
    elif(len(self.palavra) == len(palavra)):
      pass
    else:
      print("ERRO NA FUNÇÃO IGUALAR")

  def regrar(self):
    if(self.regra == 0):
      pass
    elif(self.regra == 1):
      pass
    else:
      print("ERRO, Regra inexistente.")

  def gravar(self):
    with open("Resultado", "w") as d:
      d.write(self.palavraResultado)
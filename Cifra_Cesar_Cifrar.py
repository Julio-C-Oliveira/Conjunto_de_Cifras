#Verificar  se é necesario manter duas listas Str e Int ou só uma
class Cifra_Cesar_Cifrar:
  def __init__(self, frase: str, senha: str):
    self.frase = frase
    self.senha = senha
    self.listaStr = []
    self.listaInt = []
    self.resultadoInt = []
    self.resultadoStr = []
    
  def conversao_Letra(self):
    """ Recebe letras e converte para numeros """
    for i in [self.frase, self.senha]:
      i = i.upper()
      i = i.replace(" ", "0 ")
      i = i.replace('A','1 ')
      i = i.replace('B','2 ')
      i = i.replace('C','3 ')
      i = i.replace('D','4 ')
      i = i.replace('E','5 ')
      i = i.replace('F','6 ')
      i = i.replace('G','7 ')
      i = i.replace('H','8 ')
      i = i.replace('I','9 ')
      i = i.replace('J','10 ')
      i = i.replace('K','11 ')
      i = i.replace('L','12 ')
      i = i.replace('M','13 ')
      i = i.replace('N','14 ')
      i = i.replace('O','15 ')
      i = i.replace('P','16 ')
      i = i.replace('Q','17 ')
      i = i.replace('R','18 ')
      i = i.replace('S','19 ')
      i = i.replace('T','20 ')
      i = i.replace('U','21 ')
      i = i.replace('V','22 ')
      i = i.replace('W','23 ')
      i = i.replace('X','24 ')
      i = i.replace('Y','25 ')
      i = i.replace('Z','26 ')
      i = i.split()
      self.listaStr.append(i)
      
  def conversao_Numero(self):
    """ Recebe numeros e transforma em palavras """
    for i in range(len(self.resultadoStr[0])):
      if(self.resultadoInt[i] >= 0) and (self.resultadoInt[i] <= 9):
        self.resultadoStr[0][i] = self.resultadoStr[0][i].replace('0',' ')
        self.resultadoStr[0][i] = self.resultadoStr[0][i].replace('1','A')
        self.resultadoStr[0][i] = self.resultadoStr[0][i].replace('2','B')
        self.resultadoStr[0][i] = self.resultadoStr[0][i].replace('3','C')
        self.resultadoStr[0][i] = self.resultadoStr[0][i].replace('4','D')
        self.resultadoStr[0][i] = self.resultadoStr[0][i].replace('5','E')
        self.resultadoStr[0][i] = self.resultadoStr[0][i].replace('6','F')
        self.resultadoStr[0][i] = self.resultadoStr[0][i].replace('7','G')
        self.resultadoStr[0][i] = self.resultadoStr[0][i].replace('8','H')
        self.resultadoStr[0][i] = self.resultadoStr[0][i].replace('9','I')
      elif(self.resultadoInt[i] >= 10) and (self.resultadoInt[i] <= 26):
        self.resultadoStr[0][i] = self.resultadoStr[0][i].replace('10','J')
        self.resultadoStr[0][i] = self.resultadoStr[0][i].replace('11','K')
        self.resultadoStr[0][i] = self.resultadoStr[0][i].replace('12','L')
        self.resultadoStr[0][i] = self.resultadoStr[0][i].replace('13','M')
        self.resultadoStr[0][i] = self.resultadoStr[0][i].replace('14','N')
        self.resultadoStr[0][i] = self.resultadoStr[0][i].replace('15','O')
        self.resultadoStr[0][i] = self.resultadoStr[0][i].replace('16','P')
        self.resultadoStr[0][i] = self.resultadoStr[0][i].replace('17','Q')
        self.resultadoStr[0][i] = self.resultadoStr[0][i].replace('18','R')
        self.resultadoStr[0][i] = self.resultadoStr[0][i].replace('19','S')
        self.resultadoStr[0][i] = self.resultadoStr[0][i].replace('20','T')
        self.resultadoStr[0][i] = self.resultadoStr[0][i].replace('21','U')
        self.resultadoStr[0][i] = self.resultadoStr[0][i].replace('22','V')
        self.resultadoStr[0][i] = self.resultadoStr[0][i].replace('23','W')
        self.resultadoStr[0][i] = self.resultadoStr[0][i].replace('24','X')
        self.resultadoStr[0][i] = self.resultadoStr[0][i].replace('25','Y')
        self.resultadoStr[0][i] = self.resultadoStr[0][i].replace('26','Z')
        
  def lista_Str_Int(self):
    """ Converte uma lista de strings em uma lista de int """
    for j in self.listaStr:
      j = [int(i) for i in j]
      self.listaInt.append(j)

  def lista_Int_Str(self):
    """ Converte uma lista de Int para String """
    self.resultadoStr.append([str(i) for i in self.resultadoInt])

  def somar(self):
    """ Soma os numeros os deixando abaixo de 26 """
    for i in range(len(self.listaInt[0])):
      if((self.listaInt[0][i] + self.listaInt[1][i]) > 26):
        self.resultadoInt.append((self.listaInt[0][i] + self.listaInt[1][i]) - 26)
      else:
        self.resultadoInt.append((self.listaInt[0][i] + self.listaInt[1][i]))
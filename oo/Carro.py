"""Você deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classes:

Motor
Direção
O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:

Atributo de dado velocidade
Método acelerar, que deverá incremetar a velocidade de uma unidade
Método frear que deverá decrementar a velocidade em duas unidades
A Direção terá a responsabilidade de controlar a direção. Ela oferece
os seguintes atributos:

Valor de diração com valores possíveis: Norte, Sul, Leste, Oeste.
Método girar_a_direita
Método girar_a_esquerda

       N
    O     L
       S

Exemplo:
    >>> # Testando motor
    >>> motor = motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # Testando Direcao
    >>> Direcao = Direcao()
    >>> Direcao.valor
    'Norte'
    >>> Direcao.girar_a_direita()
    >>> Direcao.valor
    'Leste'
    >>> Direcao.girar_a_direita()
    >>> Direcao.valor
    'Sul'
    >>> Direcao.girar_a_direita()
    >>> Direcao.valor
    'Oeste'
    >>> Direcao.girar_a_direita()
    >>> Direcao.valor
    'Norte'
    >>> Direcao.girar_a_esquerda()
    >>> Direcao.valor
    'Oeste'
    >>> Direcao.girar_a_esquerda()
    >>> Direcao.valor
    'Sul'
    >>> Direcao.girar_a_esquerda()
    >>> Direcao.valor
    'Leste'
    >>> Direcao.girar_a_esquerda()
    >>> Direcao.valor
    'Norte'
    >>> carro = Carro(Direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'
"""

class Carro:
  def __init__(self,Direcao, motor):
    self.Direcao = Direcao
    self.motor = motor

  def calcular_velocidade(self):
    return self.motor.velocidade

  def acelerar(self):
    self.motor.acelerar()

  def frear(self):
    self.motor.frear()

  def calcular_direcao(self):
    return self.Direcao.valor

  def girar_a_direita(self):
    self.Direcao.girar_a_direita()

  def girar_a_esquerda(self):
    self.Direcao.girar_a_esquerda()

class motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        if self.velocidade <= 0:
            self.velocidade = 0



direcoes = ('Norte', 'Leste', 'Sul', 'Oeste')


class Direcao:

  def __init__(self):
    self.valor = 'Norte'
    self.referencia = 0

  def girar_a_direita(self):
    self.referencia += 1
    if self.referencia >= 4:
      self.referencia = 0
    self.valor = (direcoes[self.referencia])

  def girar_a_esquerda(self):
     self.referencia -= 1
     if self.referencia < 0:
       self.referencia = 3
     self.valor = (direcoes[self.referencia])


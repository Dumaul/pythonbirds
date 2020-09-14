from unittest import TestCase

from oo.Carro import motor

class carroTestCase(TestCase):
    def teste_velocidade_inicial(self):
        Motor = motor()
        self.assertEqual(0, Motor.velocidade)

    def teste_acelerar(self):
        Motor = motor()
        Motor.acelerar()
        self.assertEqual(1, Motor.velocidade)
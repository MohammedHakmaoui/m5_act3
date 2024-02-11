import unittest
from CompteCorrent import CompteCorrent

class TestCompteCorrent(unittest.TestCase):

    def setUp(self):
        # Crear una instancia de CompteCorrent para usar en las pruebas
        self.compte = CompteCorrent(saldoInicial=1000.0, cs="contrasenya123")

    def test_dipositar(self):
        # Prueba dipositar
        resultado = self.compte.dipositar(500.0)
        self.assertEqual(resultado, 1500.0)

    def test_retirar_con_contrasenya_correcta_y_saldo_suficiente(self):
        # Prueba retirar con contraseña correcta y saldo suficiente
        resultado = self.compte.retirar(200.0, "contrasenya123")
        self.assertEqual(resultado, 800.0)

    def test_retirar_con_contrasenya_incorrecta(self):
        # Prueba retirar con contraseña incorrecta
        resultado = self.compte.retirar(200.0, "contrasenyaIncorrecta")
        self.assertEqual(resultado, -2)

    def test_retirar_con_contrasenya_correcta_y_saldo_insuficiente(self):
        # Prueba retirar con contraseña correcta y saldo insuficiente
        resultado = self.compte.retirar(1200.0, "contrasenya123")
        self.assertEqual(resultado, -1)

    def test_getSaldo_con_contrasenya_correcta(self):
        # Prueba getSaldo con contraseña correcta
        resultado = self.compte.getSaldo("contrasenya123")
        self.assertEqual(resultado, 1000.0)

    def test_getSaldo_con_contrasenya_incorrecta(self):
        # Prueba getSaldo con contraseña incorrecta
        resultado = self.compte.getSaldo("contrasenyaIncorrecta")
        self.assertEqual(resultado, -2)

    def test_setContrasenya_con_contrasenya_correcta(self):
        # Prueba setContrasenya con contraseña correcta
        resultado = self.compte.setContrasenya("contrasenya123", "nuevaContrasenya")
        self.assertEqual(resultado, 0)
        # Verificar que la contraseña se haya actualizado
        self.assertEqual(self.compte.contrasenya, "nuevaContrasenya")

    def test_setContrasenya_con_contrasenya_incorrecta(self):
        # Prueba setContrasenya con contraseña incorrecta
        resultado = self.compte.setContrasenya("contrasenyaIncorrecta", "nuevaContrasenya")
        self.assertEqual(resultado, -2)
        # Verificar que la contraseña no se haya actualizado
        self.assertEqual(self.compte.contrasenya, "contrasenya123")


if __name__ == '__main__':
    unittest.main()

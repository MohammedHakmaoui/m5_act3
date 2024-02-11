import unittest
import costPersonal
import  Treballador as Treballador


class TestCalculaCostDelPersonal(unittest.TestCase):

    def test_calculaCostDelPersonal(self):
        # Crea instancies de Treballador per les proves
        director = Treballador(nom="Director", tipus=Treballador.DIRECTOR, nomina=5000.0)
        subdirector = Treballador(nom="Subdirector", tipus=Treballador.SUBDIRECTOR, nomina=4000.0)
        base_worker = Treballador(nom="Trabajador Base", tipus=Treballador.BASE, nomina=3000.0, hores=10)

        # crida a la funccio i verifica el resultat

if __name__ == '__main__':
    unittest.main()

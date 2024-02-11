

''' from Treballador import Treballador

def calculaCostDelPersonal(treballadors: list):
    costFinal = 0
    for treballador in treballadors:
        if treballador.getTipusTreballador() in [Treballador.DIRECTOR,Treballador.SUBDIRECTOR]:
            costFinal += treballador.getNomina()
        else: 
            costFinal += treballador.getNomina() + (treballador.getHoresExtres()*20)
    return costFinal

'''

from Treballador import Treballador

def calculaCostDelPersonal(treballadors: list):
    return sum(t.getNomina() if t.getTipusTreballador() in [Treballador.DIRECTOR, Treballador.SUBDIRECTOR]
               else t.getNomina() + t.getHoresExtres() * 20
               for t in treballadors)


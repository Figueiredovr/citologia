#================================================
#          VICTOR FIGUEIREDO
#================================================

class Laudo(object):
    """docstring for laudo."""
    def __init__(self, nome, idade , num, conven, um, queixa, paridade):
        super(Laudo, self).__init__()
        self.nome = nome
        self.idade = idade
        self.num = num
        self.conven = conven
        self.um = um
        self.queixa = queixa
        self.paridade = paridade
        self.tipo = ""
        self.amostra_rej =""
        self.adequabilidade = ""
        self.diag = ""
        self.micro = ""
        self.atipicas = ""
        self.atipias_escamosas = ""
        self.atipias_glandulares = ""

# encoding: utf-8
#================================================
#          VICTOR FIGUEIREDO
#================================================

from laudo import Laudo




def novo_laudo():
    info = ""
    nome = raw_input("\n\nNome: ")
    idade = raw_input("\n\nIdade: ")
    num = raw_input("\n\nNumero: ")
    conven = raw_input("\n\nConvenio: ")
    um = raw_input("\n\nUM: ")
    queixa = raw_input("\n\nQueixa Principal: ")
    paridade = raw_input("\n\nParidade: ")

    n_laudo = Laudo(nome, idade , num, conven, um, queixa, paridade)

    tipo = raw_input("TIPO DA AMOSTRA\n\n 1-Convencional\n2-Em meio liquido\n\n")
    tipo = int(tipo)
    if tipo==1:
        tipo = "Convencional"
    elif tipo==2:
        tipo = "Em meio liquido"
    n_laudo.tipo = tipo

    # AMOSTRA  REJEITADA POR ----------------------------------------------------------------
    while True:

        print("Marcados: {}\n\n\n").format(info)
        a = raw_input("        -AVALIACAO PRE ANALITICA\n AMOSTRA  REJEITADA POR: \n\n        1-Ausencia ou erro na identificacao da lamina, frasco ou formulario \n        2-Lamina danificada ou ausente\n        3- Causas alheias ao laboratorio\n        4-Outras causas\n\n\n        9- LIMPAR SELECIONADOS        0- PROXIMO        ")

        a = int(a)
        if (a==1):
            info = info +  " Ausencia ou erro na identificacao da lamina, frasco ou formulario"
        elif (2==a):
            info = info + " Lamina danificada ou ausente"
        elif (3==a):
            info = info + "Causas alheias ao laboratorio: "
            info = info + "Causas alheias ao laboratorio, " + raw_input("Causas alheias ao laboratorio, detalhes: ")
        elif (4==a):
            info = info + "Outras causas, " + raw_input("Outras causas, detalhes: ")
        elif (9==a):
            info = ""
        elif(0==a):
            break

    n_laudo.amostra_rej = info
    info = ""
    return n_laudo

l = novo_laudo()
print(l)


#EPITELIOS REPRESENTADOS NA AMOSTRA -----------------------------------------------
    # while True:
    #     print("Marcados: {}\n\n\n").format(info)
    #     a = raw_input("

    #
    #     ")
    #     pass

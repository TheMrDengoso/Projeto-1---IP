def lerArquivo(fileName="agendasuspeitos.txt"):
    file = open(fileName,"r")
    conteudo = file.readlines()
    for i in range(len(conteudo)):
        conteudo[i] = conteudo[i].replace("\n","")
    return conteudo
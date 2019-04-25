from FileHelper import lerArquivo
conteudo = lerArquivo()
nomes = []
for i,e in enumerate(conteudo):
    if e != 'agenda' and e != 'chamadas':
        d_ponto = str(conteudo[i]).split(":")
        p = str(d_ponto[0]).split('-')
        nomes.append(p[0])
        print(p)
    if e == 'chamadas':
        break
print(nomes)


while True:
    print("Menu: \n1 - Ver agenda de um suspeito \n2 - Listar agendas apenas com suspeitos incluídos \n3 - Visualizar reciprocidades \n4 - Visualizar contatos com alto nível de suspeição \n5 - Sair")
    opcao = int(input("Digite a opção deseja: "))
    if opcao == 5:
        break

    if opcao == 1:
        nome = str(input("Informe o nome do suspeito que deseja saber a agenda dele: "))
        if nome == "joao":
            print(conteudo[1])
        elif nome == "pedro":
            print(conteudo[2])
        elif nome == "antonio":
            print(conteudo[3])
        else:
            print("Nome invalido!")

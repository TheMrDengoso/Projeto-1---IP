from FileHelper import lerArquivo
conteudo = lerArquivo()
nomes = []
numeros = []
agendas = []
for i,e in enumerate(conteudo):
    if e != 'agenda' and e != 'chamadas':
        d_ponto = str(conteudo[i]).split(":")
        p = str(d_ponto[0]).split('-')
        agenda = str(d_ponto[1]).split(",")
        nomes.append(p[0])
        numeros.append(p[1])
        agendas.append(agenda)
    if e == 'chamadas':
        break
print(agendas)


while True:
    print("Menu: \n1 - Ver agenda de um suspeito \n2 - Listar agendas apenas com suspeitos incluídos \n3 - Visualizar reciprocidades \n4 - Visualizar contatos com alto nível de suspeição \n5 - Sair")
    opcao = int(input("Digite a opção deseja: "))
    if opcao > 5 or opcao <= 0:
      print("Valor inválido, tente o que está no menu!")
      continue
    if opcao == 5:
        break

    if opcao == 1:
        nome = str(input("Informe o nome do suspeito que deseja saber a agenda dele: "))
        if nome == "joao" or nome=="Joao" or nome =="JOAO":
          print("Agenda do suspeito {}:".format(nome))
          for i in agendas[0]:
            print(i)
        elif nome == "pedro" or nome == "Pedro" or nome== "PEDRO":
            print("Agenda do suspeito {}:".format(nome))
            for i in agenda[1]:
              print(i)
        elif nome == "antonio" or nome=="Antonio" or nome =="ANTONIO":
            print("Agenda do suspeito {}:".format(nome))
            for i in agenda[2]:
              print(i)
        else:
            print("Nome invalido!")

from FileHelper import lerArquivo
conteudo = lerArquivo()

###variaveis
nomes = []
numeros = []
agendas = []
opcao2 = []
suspeitos_j =[]
suspeitos_p =[]
suspeitos_a = []
ag_j= []
ag_p= []
ag_a= []
rec_j = []
rec_p =[]
rec_a = []
t = []

###opcao 1
for i,e in enumerate(conteudo):
    if e != 'agenda' and e != 'chamadas':
        d_ponto = str(conteudo[i]).split(":")
        p = str(d_ponto[0]).split('-')
        agenda = str(d_ponto[1]).split(',')
        nomes.append(p[0])
        numeros.append(p[1])
        agendas.append(agenda)
        
    if e == 'chamadas':
        break

###opcao 2
for i,e in enumerate(agendas[0]):     
  if(e == numeros[1]):
    suspeitos_j.append(nomes[1])
  elif(e == numeros[2]):
    suspeitos_j.append(nomes[2])


for i,e in enumerate(agendas[1]):
  if(e == numeros[0]):
    suspeitos_p.append(nomes[0])
  elif(e == numeros[2]):
    suspeitos_p.append(nomes[2])


for i,e in enumerate(agendas[2]):
  if(e==numeros[0]):
    suspeitos_a.append(nomes[0])
  elif(e==numeros[1]):
    suspeitos_a.append(nomes[1])

###opcao 3
for i,e in enumerate(agendas[0]):  
  if i<len(numeros):
    if agendas[0].count(str(numeros[i]))==True:
      ag_j.append(numeros[i])
    
  if i>len(numeros):
    break
for i,e in enumerate(agendas[1]):  
  if i<len(numeros):
    if agendas[1].count(str(numeros[i]))==True:
      ag_p.append(numeros[i])
    
  if i>len(numeros):
    break
for i,e in enumerate(agendas[2]):  
  if i<len(numeros):
    if agendas[2].count(str(numeros[i]))==True:
      ag_a.append(numeros[i])
    
  if i>len(numeros):
    break

for i in range (len(nomes)):
  if(nomes[i] in suspeitos_p):
    rec_p.append(nomes[i])
  if(nomes[i] in suspeitos_a):
    rec_a.append(nomes[i])
  if(nomes[i] in suspeitos_j):
    rec_j.append(nomes[i])

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
            for i in agendas[1]:
              print(i)
        elif nome == "antonio" or nome=="Antonio" or nome =="ANTONIO":
            print("Agenda do suspeito {}:".format(nome))
            for i in agendas[2]:
              print(i)
        else:
            print("Nome invalido!\nO nome dos suspeitos: 'joao' ou 'pedro' ou 'antonio'.\n")
    elif opcao == 2:
      suspeitos_j = ",".join(suspeitos_j)
      suspeitos_a = ",".join(suspeitos_a)
      suspeitos_p = ",".join(suspeitos_p)
      print("joao: {}".format(suspeitos_j))
      print("pedro: {}".format(suspeitos_p))
      print("antonio: {}".format(suspeitos_a))
    
    elif opcao == 3:
      if(nomes[0]in rec_p and nomes[1]in rec_j):
        print("{}<->{}".format(nomes[0],nomes[1]))
      if(nomes[0]in rec_a and nomes[2]in rec_j):
        print("{}<->{}".format(nomes[0],nomes[2]))
      if(nomes[1] in rec_a and nomes[2] in rec_p):
        print("{}<->{}".format(nomes[1],nomes[2]))
      

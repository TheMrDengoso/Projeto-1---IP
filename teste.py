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
pos_op2_1 = []
pos_op2_2 = []
chamadas = []
qtd_cha = []
num = []
cha = []
r =0
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

### chamada
for i,e in enumerate(conteudo):
    if e != 'agenda' and e != 'chamadas':
        d = str(conteudo[i]).split(":")
        for i in range(len(nomes)):

          if(nomes[i]==d[0]):
            chamada = str(d[1].split(","))
            chamadas.append(chamada)

###opcao 2
for i in range (len(agendas)):
  nomes1_op_2 = nomes[i]
  nomes2_op_2 = []
  for e in range(len(agendas[i])):
    for j in numeros:
      if j in agendas[i][e]:
        pos_op2_1.append(i)
        pos_op2_2.append(j)
        x = numeros.index(j)
        nomes2_op_2.append(nomes[x])
  print("{}: {}".format(nomes1_op_2,",".join(nomes2_op_2)))
        

print(pos_op2_1)
print(pos_op2_2)
print(nomes2_op_2)
    

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

###opcao 4
msg = "(nível alto de suspeição)"

for i in numeros:
  
  if i in chamadas[0]:
    x = chamadas[0].count(i)
    num.append(i)
    cha.append(x)


###algoritmo
while True:
    print("Menu: \n1 - Ver agenda de um suspeito \n2 - Listar agendas apenas com suspeitos incluídos \n3 - Visualizar reciprocidades \n4 - Visualizar contatos com alto nível de suspeição \n5 - Sair")
    opcao = int(input("Digite a opção deseja: "))
    if opcao > 5 or opcao <= 0:
      print("Valor inválido, tente o que está no menu!")
      continue
    if opcao == 5:
        break

    if opcao == 1:
        nome = str(input("Informe o nome do suspeito que deseja saber a agenda dele: ").lower())
        
        for i in range (len(nomes)):
        

            if nome == nomes[i]:
              print("Agenda do suspeito {}:".format(nomes[i]))
              for i in agendas[i]:
                print(i)
          
            if nome not in nomes:
              print("\nNome não encontrado na agenda!\n")
              break
                
            
        
          
        
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
    
    elif opcao == 4:
      
      qtd = int(input("Informe a quantidade de chamadas desejadas: "))
      

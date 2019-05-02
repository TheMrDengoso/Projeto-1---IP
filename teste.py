from FileHelper import lerArquivo
conteudo = lerArquivo()

###variaveis
nomes = []
numeros = []
agendas = []
chamadas = []
pos_op2_1 = []
pos_op2_2 = []
num_op = []
cha = []
t =[]
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


###algoritmo
while True:
  try:
    print("Menu: \n1 - Ver agenda de um suspeito \n2 - Listar agendas apenas com suspeitos incluídos \n3 - Visualizar reciprocidades \n4 - Visualizar contatos com alto nível de suspeição \n5 - Sair")
    opcao = int(input("Digite a opção deseja: "))
    
    if opcao > 5 or opcao <= 0:
      print("\nValor inválido, tente o que está no menu!\n")
      continue
    if opcao == 5:
        break

    ###Opçao1
    if opcao == 1:
        nome = str(input("Informe o nome do suspeito que deseja saber a agenda dele: ").lower())
        
        for i in range (len(nomes)):
        

            if nome == nomes[i]:
              print("\nAgenda do suspeito {}:".format(nomes[i]))
              for i in agendas[i]:
                print(i)
          
            if nome not in nomes:
              print("\nNome não encontrado na agenda!\n")
              break
                       
    ###Opçao2    
    elif opcao == 2:
      for i in range (len(agendas)):
        nomes1_op_2 = nomes[i]
        nomes2_op_2 = []
        for e in range(len(agendas[i])):
          for j in numeros:
            if j in agendas[i][e]:
              pos_op2_1.append(i)
              t.append(e)
              pos_op2_2.append(j)
              x = numeros.index(j)
              nomes2_op_2.append(nomes[x])
              
        print("{}: {}".format(nomes1_op_2,",".join(nomes2_op_2)))

    ###Opçao3
    elif opcao == 3:
      for i in range (len(agendas)):
        nomes1_op_2 = nomes[i]
        nomes2_op_2 = []
        rec_1 = []
        rec_2 =[]
        w = []
        for e in range(len(agendas[i])):
          for j in numeros:
            if j in agendas[i][e]:
              pos_op2_1.append(i)
              t.append(e)
              pos_op2_2.append(j)
              x = numeros.index(j)
              nomes2_op_2.append(nomes[x])
              num_op.append(nomes[x])
              ###reciprocidade
              if numeros[x] in agendas[i]:
                if(numeros[i] in agendas[x]):
                  
                  rec_1.append(nomes[i])
                  rec_2.append(nomes[x])
                  w = rec_1
                  w.extend(rec_2)
                  y = sorted(w)
                  if w == y:
                    w = ",".join(w)
                    w = w.replace(",","<->")
                    print("{}".format(w))
                          
    ###Opçao4
    elif opcao == 4:
      msg = "(nível alto de suspeição)"
      qtd_cha = int(input("Informe a quantidade de chamadas desejadas: "))
      print("\nLista de reciprocidades com chamadas:\n--------------------------")
      if(qtd_cha<0):
        print("\nInforme um valor acima de 0.\nPara realizar uma busca mais complexa.\n")
        
      for i in range (len(agendas)):
        nomes1_op_2 = nomes[i]
        nomes2_op_2 = []
        rec_1 = []
        rec_2 =[]
        w = []
        qtd = 0
        for e in range(len(agendas[i])):
          for j in numeros:
            if j in agendas[i][e]:
              pos_op2_1.append(i)
              t.append(e)
              pos_op2_2.append(j)
              x = numeros.index(j)
              nomes2_op_2.append(nomes[x])
              num_op.append(nomes[x])
              
              ###reciprocidade
              if numeros[x] in agendas[i]:
                if(numeros[i] in agendas[x]):
                  ###chamadas
                  if numeros[x] in chamadas[i]:
                    a = chamadas[i].count(numeros[x])
                    b = chamadas[x].count(numeros[i])
                                      
                  rec_1.append(nomes[i])
                  rec_2.append(nomes[x])
                  w = rec_1
                  w.extend(rec_2)
                  y = sorted(w)
                  if w == y:
                    if a > b:
                      k = a
                    else:
                      k = b
                    
                    if k>= qtd_cha:
                      w = ",".join(w)
                      w = w.replace(",","<->")
                      print("{} {}".format(w,msg))
                    else:
                      w = ",".join(w)
                      w = w.replace(",","<->")
                      print("{}".format(w))
      ### Coloca um contador

  except ValueError:
    print("\nValor inválido, tente o que está no menu!\n")
      

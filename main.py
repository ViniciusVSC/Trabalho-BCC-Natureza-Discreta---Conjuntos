#Vinícius Silva Camargo BCC Manhã

#Para  obter  os  pontos  relativos  a  este  trabalho,  você  deverá  criar  um  programa,  utilizando  a 
#linguagem  Python, C, ou C++.  Este  programa,  quando  executado,  irá  apresentar  os  resultados  de 
#operações que serão realizadas entre dois conjuntos de dados.  
#O  programa  que  você  desenvolverá  irá  receber  como  entrada um arquivo de texto  (.txt) 
#contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão representadas 
#em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas 
#segundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de 
#operações  que  estão  descritas  no  arquivo,  este  número  de  operações  será  um  inteiro;  as  linhas 
#seguintes  seguirão  sempre  o  mesmo  padrão  de  três  linhas:  a  primeira  linha  apresenta  o  código  da 
#operação  (U para união, I para interseção, D para diferença e C produto cartesiano),  a  segunda  e 
#terceira linhas conterão os elementos dos conjuntos separados por virgulas. A seguir está um exemplo 
#das linhas que podem existir em um arquivo de testes para o programa que você irá desenvolver: 
#4 
#U 
#3, 5, 67, 7 
#1, 2, 3, 4  
#I 
#1, 2, 3, 4, 5 
#4, 5 
#D 
#1, A, C, 34 
#A, C, D, 23 
#C 
#3, 4, 5, 5, A, B, R 
#1, B, C, D, 1 
#Neste exemplo temos 4 operações uma união (U), uma interseção (I), um diferença (D) e um 
#produto cartesiano (C). A união, definida por U, deverá ser executada sobre os conjuntos {𝟑,𝟓,𝟔𝟕,𝟕} e 
#{𝟏,𝟐,𝟑,𝟒}, cujos elementos estão explicitados nas linhas posteriores a definição da operção (U).  
#A resposta do seu programa deverá conter a operação realizada, descrita por extenso, os dados 
#dos conjuntos identificados, e o resultado da operação. No caso da união a linha de saída deverá conter 
#a informação e a formatação mostrada a seguir:    
#União: conjunto 1 {3,5,67,7}, conjunto 2 {1,2,3,4}. Resultado: {3,5,67,7,1,2,4}   
#Seu programa deverá mostrar a saída no terminal, ou em um arquivo de textos. Em qualquer 
#um dos casos, a saída será composta por uma linha de saída para cada operação constante no arquivo 
#de  textos  de  entrada  formatada  segundo  o  exemplo  de  saída  acima.  Observe  as  letras  maiúsculas  e 
#minúsculas, e os pontos utilizados na formatação da linha de saída apresenta acima.  
#No  caso  do  texto  de  exemplo,  teremos  4  linhas,  e  apenas  4  linhas  de  saída,  formatadas  e 
#pontuadas conforme o exemplo de saída acima. O uso de linhas extras na saída, ou erros de formatação, 
#implicam em perda de pontos como pode ser visto na rubrica de avaliação constante neste documento. 
#Para que seu programa possa ser testado você deve criar, no mínimo, três arquivos de entrada 
#contendo um número diferente de operações, operações com dados diferentes, e operações em ordem
#diferentes.  Os  arquivos  de  entrada  criados  para  os  seus  testes  devem  estar  disponíveis  tanto  no 
#ambiente repl.it quanto no ambiente Github.  
#Observe que o professor irá testar seu programa com os arquivos de testes que você criar e com, 
#no mínimo um arquivo de testes criado pelo próprio professor. 


v = ","                                     #criei uma variável pra remover vírgulas que apareciam na saída
letras = ["U","I","D","C"]                  #criei uma variável para reconhecer a operação requisitada
file = open("lista1.txt", "r")               #essa parte do código ira abrir o arquivo txt
linha = file.readlines()
linha = [x.rstrip("\n") for x in linha]


for i in range(len(linha)):                        #esse código irá ler todo o arquivo txt
    if linha[i][0] in letras:
        tarefa = linha[i][0]
        if tarefa == "U":                          #usei if para identificar a primeira operação enquanto os outros usei elif
            n1 = []                                #criei 2 vetores para armazenar a lista de caracteres
            n2 = []                                           
            ru = []                                #vetor onde será armazenado o resultado
            for item in linha[i+1].split(","):     #codigo que irá fazer a união das duas listas
                n1.append(item)
                if item not in ru:
                    ru.append(item) 
            for item in linha[i+2].split(","):
                n2.append(item)
                if item not in ru:
                    ru.append(item)    
            while v in ru:
                ru.remove(v)
            print(f"União: conjunto 1:{n1} conjunto 2:{n2} Resultado:{ru}")
            

        elif tarefa == "I":                         #a mesma lógica do primeiro códico
            n3 = []
            n4 = []
            ri = []
            rii = []                               #unica diferença foi que criei um vetor a mais
            for item in linha[i+1].split(","):
                n3.append(item)
                if item not in ri:
                    ri.append(item)
                else:
                    rii.append(item)
            for item in linha[i+2].split(","):
                n4.append(item)
                if item not in ri:
                    ri.append(item)
                else:
                    rii.append(item)               
            while v in rii:
                rii.remove(v)                  
            print(f"Interseção: conjunto 1:{n3} conjunto 2:{n4} Resultado:{rii}")  #para no final poder escolher para imprimir
                


        elif tarefa == "D":                     #mesma lógica dos outros
            n5 = []
            n6 = []
            rd = []
            for item in linha[i+1].split(","):
                n5.append(item)
                if item in linha[i+1] and item not in linha[i+2] and item not in rd:        #aqui irá comparar mais de uma vez as listas
                    rd.append(item)
            for item in linha[i+2].split(","):
                n6.append(item)
                if item in linha[i+2] and item not in linha[i+1] and item not in rd:
                    rd.append(item)
            while v in rd:
                rd.remove(v)
            print(f"Diferença: conjunto 1:{n5} conjunto 2:{n6} Resultado:{rd}")
            
                

        elif tarefa == "C":                       #mesma lógica dos outros
            n7 = []
            n8 = []
            rc = []
            for item in linha[i+1].split(","):
                n7.append(item)
            for item in linha[i+2].split(","):
                n8.append(item)
            while v in n7:
                n7.remove(v)
            while v in n8:
                n8.remove(v)
            for l in range(0,len(n7)):              #nesta parte, faço o código criar uma matriz com os resutados
                rc.append([])
                for c in range(0,len(n8)):
                    n = n7[l], n8[c]
                    rc[l].append(n)
            while v in rc:
                rc.remove(v)
            print(f"Carteziano: conjunto 1:{n7} conjunto 2:{n8} Resultado{rc}")
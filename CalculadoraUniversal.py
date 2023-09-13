import os

menu_Principal = 0
while menu_Principal != 4:
  print('''Calculadora Do Juan Nacif
  
Bem-Vindo a Calculadora Universal.
Preciso que você escolha a Disciplina que você queira calcular:

[ 1 ] Matemática
[ 2 ] Física 
[ 3 ] Química (EM BREVE)
[ 4 ] Medicina (EM BREVE)
  ''')
  menu_Principal = int(input('''Escolha uma Disciplina: '''))
  menu_Principal != 4
  os.system('clear')
  
  #MATEMÁTICA
  if menu_Principal == 1:
    
    opcao = 0 
    while opcao != 8:  
      print('''
Bem-Vindo a Calculadora para Disciplina de Matemática 

Escolha a Operação:

[ 1 ] Soma
[ 2 ] Subtração 
[ 3 ] Multiplicação
[ 4 ] Divisão
[ 5 ] Algoritmo de Divisão
[ 6 ] Área (Geometria)
[ 7 ] Volume (Geometria)
[ 8 ] Voltar para o menu anterior
    ''')
      opcao = int(input('''Escolha a Operação: '''))
      opcao != 7
      os.system('clear')
      
    #SOMA
      if opcao == 1:
        a = int(input('Digite o 1 Numéro inteiro: '))
        b = int(input('Digite o 2 Numéro inteiro: '))
        soma = a + b
        print('')
        print(f'A soma entre {a} + {b} = {soma}')
    
    #SUBTRAÇÃO
      elif opcao == 2:
        a = int(input('Digite o 1 Numéro inteiro: '))
        b = int(input('Digite o 2 Numéro inteiro: '))
        subtracao = a - b
        print('')
        print(f'A Subtração entre {a} + {b} = {subtracao}')
    
    #MULTIPLICAÇÃO
      elif opcao == 3:
        a = int(input('Digite o 1 Numéro inteiro: '))
        b = int(input('Digite o 2 Numéro inteiro: '))
        multiplicacao = a * b
        print('')
        print(f'A Multiplicação entre {a} x {b} = {multiplicacao}')
    
    
    
    #DIVISÃO 
      elif opcao == 4:
        a = int(input('Digite o 1 Numéro inteiro: '))
        b = int(input('Digite o 2 Numéro inteiro: '))
        divisao = a / b
        print('')
        print(f'A Divisão entre {a} / {b} = {divisao}')


    #ALGORITMO DE DIVISÃO 
      elif opcao == 5:
    
                a = float(input('''
*Substitua a Vírgula por Ponto*
    
Escreva o Divindendo: '''))
                b = float(input('''
Escreva o Divisor: '''))
        
                resto_algorit_divisao = a % b
                divisao_inteira = a // b
              
        
                print(f'''
O Calculo do Algoritmo de Divisão --> {a} = {b} x {divisao_inteira} + {resto_algorit_divisao} 
''')
    
    
    #Calculore de Area
      elif opcao == 6:
        opcaoAREA = 0
        while opcaoAREA != 13:
    
          print('''
Calculadora de Área Geompetrica do Nacif
        
[ 1 ] Retângulo
[ 2 ] Quadrado
[ 3 ] Triângulo
[ 4 ] Círculo
[ 5 ] Paralelepípedo
[ 6 ] Trapézio
[ 7 ] Esfera
[ 8 ] Triângulo Equilátero
[ 9 ] Cone
[ 10 ] Pirâmide Quadrada
[ 11 ] Cilindro
[ 12 ] Cubo
[ 13 ] Voltar ao Inicio
    ''')
          
      
  
          opcaoAREA = int(input('Escolha uma Opção: '))
          opcaoAREA != 12
          os.system('clear')
    
          #RETANGULO
          if opcaoAREA == 1:
            print('Substitua a VÍRGULA por PONTO, caso o número seja Décimal')
            a = float(input('Digite o valor da Altura: '))
            b = float(input('Digite o valor do Compremento: '))
            retanguloarea = a * b
            print(f'A Área do Retângulo com altura {a} e Compremento {b} = {retanguloarea}')
    
          #QUADRADO
          if opcaoAREA == 2:
            print('Substitua a VÍRGULA por PONTO, caso o número seja Décimal')
            a = float(input('Digite o valor do Lado: '))
            quadradoarea = a ** a
            print(f'A Área do Quadrado com Lado {a} = {quadradoarea}')
            
          #TRIANGULO
          if opcaoAREA == 3:
            print('Substitua a VÍRGULA por PONTO, caso o número seja Décimal')
            a = float(input('Digite o valor da Altura: '))
            b = float(input('Digite o valor do Base: '))
            trianguloarea = a * b / 2
            print(f'A Área do Retângulo com Altura {a} e Base {b} = {trianguloarea}')
            
          #CIRCULO
          if opcaoAREA == 4:
            print('Substitua a VÍRGULA por PONTO, caso o número seja Décimal')
            a = float(input('Digite o valor da Raio: '))
            b = 3.14159
            circuloarea = b * a ** 2
            print(f'A Área do Círculo com Raio {a} = {circuloarea}')
            
          #PARALELEPÍPEDO
          if opcaoAREA == 5:
            print('Substitua a VÍRGULA por PONTO, caso o número seja Décimal')
            a = float(input('Digite o valor da Altura: '))
            b = float(input('Digite o valor do Compremento: '))
            c = float(input('Digite o valor do Largura: '))
            retanguloarea = 2 * a * b + 2 * a * c + 2 * b * c
            print(f'A Área do Paralelepípedo com altura {a}, Compremento {b} e Largura {c} = {retanguloarea}')
            
          #TRAPÉZIO
          if opcaoAREA == 6:
            print('Substitua a VÍRGULA por PONTO, caso o número seja Décimal')
            a = float(input('Digite o valor da Altura: '))
            b = float(input('Digite o valor do Base: '))
            trapezioarea = ((b + b) * a) / 2
            print(f'A Área do Trapézio com Altura {a} e Base {b} = {trapezioarea}')
            
          #ESFERA
          if opcaoAREA == 7:
            print('Substitua a VÍRGULA por PONTO, caso o número seja Décimal')
            a = float(input('Digite o valor do Raio: '))
            b = 3.14159
            esferaarea = 4 * b * a ** 2
            print(f'A Área Superficial da Esfera com Raio {a} = {esferaarea}')
            
          #TRIANGULO EQUILÁTERO
          if opcaoAREA == 8:
            print('Substitua a VÍRGULA por PONTO, caso o número seja Décimal')
            a = float(input('Digite o valor da Lado: '))
            trianguloequi_area = (a ** 2 * 1.73205) / 4 
            print(f'A Área do Triângulo Equilátero com Lado {a} = {trianguloequi_area}')
            
          #CONE
          if opcaoAREA == 9:
            print('Substitua a VÍRGULA por PONTO, caso o número seja Décimal')
            a = float(input('Digite o valor do Raio: '))
            b = float(input('Digite o valor da Lateral: '))
            c = 3.14159
            conearea = (c * a * b) + (c * a ** 2)
            print(f'A Área do Cone com Raio {a} e Lateral {b} = {conearea}')
            
          #PIRÂMIDE QUADRADA
          if opcaoAREA == 10:
            print('Substitua a VÍRGULA por PONTO, caso o número seja Décimal')
            a = float(input('Digite o valor do Lado da Base: '))
            b = float(input('Digite o valor do Altura: '))
            c = int(input('Informe a quantidade de Lados existente na Pirâmede: '))
            piramidearea = ((a * b / 2) * c) + (a ** 2)
            print(f'A Área do Pirâmide com altura {a} e Compremento {b} = {piramidearea}') 
            
          #CILINDRO
          if opcaoAREA == 11:
            print('Substitua a VÍRGULA por PONTO, caso o número seja Décimal')
            a = float(input('Digite o valor do Raio: '))
            b = float(input('Digite o valor da Altura: '))
            cilindroarea = (pi * a ** 2) + 2 * pi * a * b
            print(f'A Área do Cilindro com Raio {a} e Altura {b} = {cilindroarea}')
    
          #Cubo
          if opcaoAREA == 12:
            print('Substitua a VÍRGULA por PONTO, caso o número seja Décimal')
            a = float(input('Digite o valor do Lado: '))
            
            cuboarea = a * a * a
            print(f'A Área do Cubo com Lado {a} = {cuboarea}')
            
    #VOLUMEEEEEE
    
      elif opcao == 7:        
        opcaoVOLUME = 0
        while opcaoVOLUME != 7:
          print(''' 
Calculadora de VOLUME Geompetrica do Juan Nacif

[ 1 ] Paralelepípedo
[ 2 ] Tronco
[ 3 ] Esfera
[ 4 ] Cone
[ 5 ] Pirâmide Quadrada
[ 6 ] Cilindro
[ 7 ] Voltar ao Inicio''')
          opcaoVOLUME = int(input('''
Escolha uma Opção: '''))
          opcaoVOLUME != 6
          os.system('clear')
          
          #PRALELEPIPEDO
          if opcaoVOLUME == 1:
            print('Substitua a VÍRGULA por PONTO, caso o número seja Décimal')
            a = float(input('Digite o valor da Altura: '))
            b = float(input('Digite o valor do Compremento: '))
            c = float(input('Digite o valor do Largura: '))
            retangulovolume = a * b * c
            print(f'''A Volume do Paralelepípedo com altura {a}, Compremento {b} e Largura {c} = {retangulovolume}
            ''')
            
          #TRONCO
          if opcaoVOLUME == 2:
            print('Substitua a VÍRGULA por PONTO, caso o número seja Décimal')
            a = float(input('Digite o valor do Raio Maior: '))
            b = float(input('Digite o valor do Raio Menor: '))
            c = float(input('Digite o valor do Altura: '))
            pi = 3.14159
            troncovolume = (pi * c * (b ** 2 + b) * (a + a ** 2)) / 3
            print(f'A Volume do Tronco = {troncovolume}')      
            
          #ESFERA
          if opcaoVOLUME == 3:
            print('Substitua a VÍRGULA por PONTO, caso o número seja Décimal')
            a = float(input('Digite o valor do Raio: '))
            b = 3.14159
            esferaarea = 4 * b * a ** 2
            print(f'A Área Superficial da Esfera com Raio {a} = {esferaarea}')      
            
          #CONE
          if opcaoVOLUME == 4:
            print('Substitua a VÍRGULA por PONTO, caso o número seja Décimal')
            a = float(input('Digite o valor do Raio: '))
            b = float(input('Digite o valor da Altura '))
            pi = 3.14159
            conevolume = (pi * a ** 2 * b) / 3
            print(f'A Volume Cone com Raio {a} e Altura {b} = {conevolume}')
    
          #PIRAMIDE QUADRADA
          if opcaoVOLUME == 5:
            print('Substitua a VÍRGULA por PONTO, caso o número seja Décimal')
            a = float(input('Digite o valor do Lado: '))
            b = float(input('Digute o valor da Altura'))
            piramidequadradavolume = a ** 2 * b / 3
            print(f'O Volume da Pirâmide = {piramidequadradavolume}')
    
          #CILINDRO
          if opcaoVOLUME == 6:
            print('Substitua a VÍRGULA por PONTO, caso o número seja Décimal')
            a = float(input('Digite o valor do Raio: '))
            b = float(input('Digite o valor da Altura: '))
            pi = 3.14159
            cilindrovolume = (pi * a ** 2 * b) / 3 
            print(f'O Volume do Ciilindro com Raio {a} = {cilindrovolume}')
    
      
          
            
  #FÍSICA  
  if menu_Principal == 2:
    
    opcao_fisica = 0 
    while opcao_fisica != 2:  
      print('''
Bem-Vindo a Calculadora para Disciplina de Física 

Escolha a Operação:

[ 1 ] Cinemática (Movimento)
[ 2 ] Voltar para o Menu Inicial
    ''')
      opcao_fisica = int(input('''Escolha a Operação: '''))
      opcao_fisica != 1
      os.system('clear')

      #CINEMÁTICA (MOVIMENTO)'
      if opcao_fisica == 1:
        opcao_cinematica = 0 
        while opcao_cinematica != 9:  
          print('''
Calculo de Cimemática: 

[ 1 ] M/s --> Km/h
[ 2 ] Km/h --> M/s 
[ 3 ] Aceleração
[ 4 ] Movimento Uniforme (MU)
[ 5 ] Movimento Uniformente Variado (MUV)
[ 6 ] Equação de Torricelli
[ 7 ] Movimento Vertical
[ 8 ] Movimento Circular
[ 9 ] Voltar para o Menu Anterior
''')
          opcao_cinematica = int(input('''Escolha a Operação: '''))
          opcao_cinematica != 8
          os.system('clear')

          
          #M/s --> Km/h 
          if opcao_cinematica == 1:
            a = float(input('''
*Substitua a Vírgula por Ponto*
Escreva o M/s: '''))
            convertendoKm = a * 3.6
            print(f'''{a} M/s = {convertendoKm} Km/h''')



          #Km/h --> M/s 
          if opcao_cinematica == 2:
            a = float(input('''
*Substitua a Vírgula por Ponto*

Escreva o Km/h: '''))
            convertendoMs = a / 3.6
            print(f'''{a} Km/h = {convertendoMs} M/s''')

          #ACELERAÇÃO
          if opcao_cinematica == 3:
            a = float(input('''
*Substitua a Vírgula por Ponto*

Escreva a Variação da Velocidade em M/s: '''))
            b = float(input('''
Escreva a Variação do Tempo: '''))
            aceleracaosimples = a / b
            print(f'''
A Aceleração = {acelecaosimples} M/s2 ''')

          #MOVIMENTO UNIFORME (MU)         
          #Função horária do deslocamento
          if opcao_cinematica == 4:  
            a = float(input('''
*Substitua a Vírgula por Ponto*

Escreva a Posição Inicial em M: '''))
            b = float(input('''
Escreva a Variação do Tempo: '''))
            c = float(input('''
Escreva a Velocidade em M/s: '''))
            funcao_horaria_deslocamento = a + c * b
            print(f'''
A Posição Final = {funcao_horaria_deslocamento} M ''')

          #MOVIMENTO UNIFORMENTE VARIADO (MUV)

          if opcao_cinematica == 5:
            opcao_MUV = 0 
            while opcao_MUV != 4:  
              print('''
Calculo de Movimento Vetical: 
    
[ 1 ] Função Horário da Velocidade
[ 2 ] Função Horário da Posição
[ 3 ] Equação de Torriceli
[ 4 ] Voltar para o Menu Anterior
    ''')
              opcao_MUV = int(input('''Escolha a Operação: '''))
              opcao_MUV != 3
              os.system('clear')
  
              #Função horária da velocidade
              if opcao_MUV == 1:
                a = float(input('''
*Substitua a Vírgula por Ponto*
    
Escreva a Velocidade Inicial em M/s: '''))
                b = float(input('''
Escreva a Aceleração em M/s2: '''))
                c = float(input('''
Escreva Tempo em Segundos: '''))
                funcao_horaria_velocidade = a + b * c
                print(f'''
    A Funão Horária da Velocidade = {funcao_horaria_velocidade} M/s ''')              
    
                #Função horária da posição
              
              elif opcao_MUV == 2:
                a = float(input('''
*Substitua a Vírgula por Ponto*
    
Escreva a Velocidade Inicial em M/s: '''))
                b = float(input('''
Escreva a Aceleração em M/s2: '''))
                c = float(input('''
Escreva Tempo em Segundos: '''))
                funcao_horaria_velocidade = a + b * c
                print(f'''
    A Funão Horária da Velocidade = {funcao_horaria_velocidade} M/s ''')
    
                #Torricelli
              elif opcao_MUV == 3:
    
                a = float(input('''
*Substitua a Vírgula por Ponto*
    
Escreva a Velocidade Inicial em M/s: '''))
                b = float(input('''
Escreva a Aceleração em M/s2: '''))
                c = float(input('''Escreva o Deslocamento em M: '''))
                torricelli = a ** 2 + 2 * b * c
                print(f'''
A Velocidade Final = {torricelli} M/s ''')



          #EQUAÇÃO DE TORRICELI
          if opcao_cinematica == 6:
            a = float(input('''
*Substitua a Vírgula por Ponto*

Escreva a Velocidade Inicial em M/s: '''))
            b = float(input('''
Escreva a Aceleração em M/s2: '''))
            c = float(input('''Escreva o Deslocamento em M: '''))
            torricelli = a ** 2 + 2 * b * c
            print(f'''
A Velocidade Final = {torricelli} M/s ''')

################ Vertical ###################
          if opcao_cinematica == 7:
            opcao_vertical = 0 
            while opcao_vertical != 4:  
              print('''
Calculo de Movimento Vetical: 
    
[ 1 ] Equação de Torricelli para lançamento vertical
[ 2 ] Velocidade vertical em função do tempo
[ 3 ] Posição vertical em função do tempo
[ 4 ] Voltar para o Menu Anterior
    ''')
              opcao_vertical = int(input('''Escolha a Operação: '''))
              opcao_vertical != 3
              os.system('clear')

              #Equação de Torricelli para lançamento vertical
              if opcao_vertical == 1:
                a = float(input('''
*Substitua a Vírgula por Ponto*
    
Escreva a Velocidade Inicial em M/s: '''))
                b = float(input('''
Escreva a Aceleração da Gravidade em M/s2: '''))
                c = float(input('''
Escreva Altura em M: '''))
                torricelli_vertical_subindo = (a ** 2) + 2 * b * c
                torricelli_vertical_descendo = (a ** 2) - 2 * b * c
                print(f'''
A Equação de Torricelli para lançamento vertical SUBINDO a Velocidade final = {torricelli_vertical_subindo} M/s ''') 
                print(f'''
A Equação de Torricelli para lançamento vertical DESCENDO a Velocidade final = {torricelli_vertical_descendo} M/s 
    ''') 
                

                #Velocidade vertical em função do tempo
              if opcao_vertical == 2:
                a = float(input('''
*Substitua a Vírgula por Ponto*
    
Escreva a Velocidade Inicial em M/s: '''))
                b = float(input('''
Escreva a Aceleração da Gravidade em M/s2: '''))
                c = float(input('''
Escreva Tempo em Segundos: '''))
                velocidade_vertical_tempo_subindo = a + b * c
                velocidade_vertical_tempo_descendo = a - b * c
                print(f'''
A Velocidade Vertical em Função do Tempo SUBINDO a Velocidade final = {torricelli_vertical_subindo} M/s ''') 
                print(f'''
A Velocidade Vertical em Função do Tempo DESCENDO a Velocidade final = {torricelli_vertical_descendo} M/s 
    ''') 
          

                #Posição vertical em função do tempo
              if opcao_vertical == 3:
                inicial_posicao = float(input('''  
Escreva a Posição Inicial em M/s: '''))
                a = float(input('''
*Substitua a Vírgula por Ponto*
    
Escreva a Velocidade Inicial em M/s: '''))
                b = float(input('''
Escreva a Aceleração da Gravidade em M/s2: '''))
                c = float(input('''
Escreva Tempo em Segundos: '''))
                posicao_vertical_func_tempo_subindo = (inicial_posicao + a * c + b * t ** 2) / 2
                posicao_vertical_func_tempo_descendo = (inicial_posicao + a * c - b * t ** 2) / 2
                print(f'''
Posição Vertical em Função do Tempo SUBINDO a Velocidade final = {posicao_vertical_func_tempo_subindo} M/s ''') 
                print(f'''
A Posição Vertical em Função do Tempo DESCENDO a Velocidade final = {posicao_vertical_func_tempo_descendo} M/s 
    ''') 
    
################################# MOVIMENTO CIRCULAR ############################
          if opcao_cinematica == 8:
            opcao_circular = 0 
            while opcao_circular != 6:  
              print('''
Calculo de Cimemática: 
    
[ 1 ] Posição Angular
[ 2 ] Deslocamento Angular
[ 3 ] Velocidade Angular Média
[ 4 ] Aceleração Centripéta
[ 5 ] Aceleração Angular Média
[ 6 ] Voltar para o Menu Anterior
    ''')
              opcao_circular = int(input('''Escolha a Operação: '''))
              opcao_circular != 5
              os.system('clear')
  
            #Posição angular
              if opcao_circular == 1:
                a = float(input('''
*Substitua a Vírgula por Ponto*
    
Escreva a Posição em M: '''))
                b = float(input('''
Escreva o Raio em M: '''))
                posicao_angular = a / b
                print(f'''
A Posição Angular = {posicao_angular} Rad 
    ''')
    
              #DESLOCAMENTO ANGULAR
              if opcao_circular == 2:
                a = float(input('''
*Substitua a Vírgula por Ponto*
    
Escreva a Variação da Posição em M: '''))
                b = float(input('''
Escreva o Raio em M: '''))
                deslocamento_angular = a / b
                print(f'''
O Deslocamento Angular = {deslocamento_angular} Rad/s
    ''')
    
              #Velocidade Angular Media
              if opcao_circular == 3:
                a = float(input('''
*Substitua a Vírgula por Ponto*
    
Escreva o Deslocamento Angular em Rad: '''))
                b = float(input('''
Escreva a Variação do Tempo em Segundos: '''))
                vel_agular_media = a / b
                print(f'''
A Velocidade Angular Média = {vel_agular_media} Rad/s 
    ''')            
    
              #ACELERAÇÃO CENTRÍPETA  
              if opcao_circular == 4:
                a = float(input('''
*Substitua a Vírgula por Ponto*
    
Escreva a Velocidade em M/s: '''))
                b = float(input('''
Escreva o Raio da Circunferência em M: '''))
                aceleracao_centripeta = (a ** 2) / b
                print(f'''
A Aceleração Centrípeta = {aceleracao_centripeta} Rad 
    ''')    
    
    
              #ACELERAÇÃO Angular media
              if opcao_circular == 5:
                a = float(input('''
*Substitua a Vírgula por Ponto*
    
Escreva o Velocidade Angular em Rad/s: '''))
                b = float(input('''
Escreva a Variação do Tempo em Segundos: '''))
                aceleracao_agular_media = a / b
                print(f'''
A Aceleração Angular Média = {aceleracao_agular_media} Rad/s2
    ''')   

          #VOLTAR PARA O MENU ANTERIOR





#####################################################################################################
#QUIMICA
  if menu_Principal == 3:
    print(f'''Estamos em Desenvolvimento.
''')




#MEDICINA
  if menu_Principal == 4:
    print(f'''Estamos em Desenvolvimento.
''')

  else:
    print('Opção Inválida. Tente Novamente')  
    print('Até daqui a pouco :)')


import random

#variaveis players (modo 1)
pontos_player1 = 0 # contador para o jogador 1
pontos_player2 = 0 # contador para o jogador 2

#variaveis player e maquina (modo 2)
pontosComputador = 0
pontos_player1 = 0

#variaveis de pontos computador x computador (modo 3)
pontosComputador1 = 0
pontosComputador2 = 0


# Menu onde o usuário pode escolher entre jogar ou sair.
# Usei o \033["numero da cor" "texto" \033[0m para mudar a cor do texto. e para fazer as bordas usei os + para as bordas, o - para o meio e | para as laterais.
print("\033[1;34m+" + "-" * 38 + "+\033[0m")
print("\033[1;34m|\033[0m     \033[1;31m*** BEM VINDO AO JOKEMPO ***\033[0m     \033[1;34m|\033[0m")
print("\033[1;34m|" + " " * 38 + "|\033[0m")
print("\033[1;34m|\033[0m   \033[1;34mEscolha um modo de jogar:\033[0m          \033[1;34m|\033[0m")
print("\033[1;34m|" + " " * 38 + "|\033[0m")
print("\033[1;34m|\033[0m   \033[36m1. Player vs Player\033[0m                \033[1;34m|\033[0m")
print("\033[1;34m|\033[0m   \033[36m2. Player vs Computador\033[0m            \033[1;34m|\033[0m")
print("\033[1;34m|\033[0m   \033[36m3. Computador vs Computador\033[0m        \033[1;34m|\033[0m")
print("\033[1;34m|\033[0m   \033[36m4. Sair do jogo\033[0m                    \033[1;34m|\033[0m")
print("\033[1;34m+" + "-" * 38 + "+\033[0m")

while True:
        modo = input("\033[1;37mResposta:\033[0m ")
        if modo.isdigit(): # ele verifica se o usuário digitou apenas números.
                modo = int(modo) # se for numero ele converte para int.
                
        else:
                print("\nOpção inválida! Digite novamente ")
                modo = int(input("\033[1;37mResposta:\033[0m "))
                
        if modo <= 0 or modo >= 5: # esse serve para caso a pessoa escoha uma opção nao valida ele tente novamente.
                print("\n Opção inválida, digite um número de 1 a 4: ")
        
        else:
                while True:
                        if modo == 1: # caso a pessoa escoha o modo 1
                                print("\n--------------------------------------------")
                                print("          \033[1;35mModo Player vs Player\033[0m ")
                                print("--------------------------------------------")

                                escolha = input("\n\033[32mPlayer 1 escolha: Pedra, Papel ou Tesoura:\033[0m ").lower() # jogador 1 escolhe sua jogada.
                                
                                #verifica se a resposta do player 1 é valida
                                if escolha != "pedra" and escolha != "papel" and escolha != "tesoura":
                                        print("\n\033[1;37mOpção inválida! Digite novamente: \033[0m")
                                        escolha = input("\n\033[32mPlayer 1 escolha: Pedra, Papel ou Tesoura:\033[0m ").lower()
                                
                                #verifica se a resposta do player 2 é valida       
                                escolha2 = input("\n\033[31mPlayer 2 escolha: Pedra, Papel ou Tesoura:\033[0m ").lower() # jogador 2 escolhe sua jogada.
                                if escolha2 != "pedra" and escolha2 != "papel" and escolha2 != "tesoura":
                                        print("\n\033[1;37mOpção inválida! Digite novamente: \033[0m")
                                        escolha2 = input("\n\033[31mPlayer 2 escolha: Pedra, Papel ou Tesoura:\033[0m ").lower()
                                        
                                        
                                if escolha == "pedra" and escolha2 == "papel": # essa parte serve para ver qual jogador ganhou a rodada.
                                        print("\n--------------------------------------------")
                                        print("            \033[1;31mPlayer 2 venceu!\033[0m")
                                        print("--------------------------------------------")
                                        pontos_player2 += 1
                                elif escolha == "pedra" and escolha2 == "tesoura":
                                        print("\n--------------------------------------------")
                                        print("            \033[1;32mPlayer 1 venceu!\033[0m")
                                        print("--------------------------------------------")
                                        pontos_player1 += 1
                                elif escolha == "papel" and escolha2 == "pedra":
                                        print("\n--------------------------------------------")
                                        print("            \033[1;32mPlayer 1 venceu!\033[0m")
                                        print("--------------------------------------------")
                                        pontos_player1 += 1
                                        
                                        
                                #PLAYER 2 VENCENDO
                                elif escolha == "papel" and escolha2 == "tesoura":
                                        print("\n--------------------------------------------")
                                        print("            \033[1;31mPlayer 2 venceu!\033[0m")
                                        print("--------------------------------------------")
                                        pontos_player2 += 1
                                elif escolha == "tesoura" and escolha2 == "pedra":
                                        print("\n--------------------------------------------")
                                        print("            \033[1;31mPlayer 2 venceu!\033[0m")
                                        print("--------------------------------------------")
                                        pontos_player2 += 1
                                elif escolha == "tesoura" and escolha2 == "papel":
                                        print("\n--------------------------------------------")
                                        print("            \033[1;32mPlayer 1 venceu!\033[0m")
                                        print("--------------------------------------------")
                                        pontos_player1 += 1
                                elif escolha == escolha2:
                                        print("\n--------------------------------------------")
                                        print("                \033[1;30mEmpate!\033[0m")
                                        print("--------------------------------------------")
                                
                                print(f"\n\033[1;37mPlacar:\033[0m \033[1;32mPlayer 1 =\033[0m \033[1;37m{pontos_player1}\033[0m | \033[1;31mPlayer 2 =\033[0m \033[1;37m{pontos_player2}\033[0m") # imprime o placar atual do jogo.
                                
                                # Essa parte serve para perguntar se ele quer jogar novamente quando uma partida termina
                                jogar_novamente = input("\n\033[1;37mDeseja jogar novamente? (s/n):\033[0m ").lower()
                                
                                while jogar_novamente != "s" and jogar_novamente != "n":
                                        print("\n\033[1;37mOpção inválida\033[0m")
                                        jogar_novamente = input("\033[1;37mDeseja jogar novamente? (s/n):\033[0m ").lower()
                                if jogar_novamente == "s":
                                        continue
                                elif jogar_novamente == "n":
                                        print("\n\033[1;37mObrigado por jogar! Estudantes: Felipe Bresciani, Pedro Henrique Junqueira e Rafael Eliezer.\033[0m")
                                        break

                        elif modo == 2: # caso a pessoa escoha o modo 2
                                print("\n--------------------------------------------")
                                print("          \033[1;35mModo Player vs Computador\033[0m ")
                                print("--------------------------------------------")

                                escolha = input("\n\033[32mPlayer 1 escolha: Pedra, Papel ou Tesoura:\033[0m ").lower() # jogador 1 escolhe sua jogada.
                                
                                #verifica se a resposta do player 1 é valida
                                if escolha != "pedra" and escolha != "papel" and escolha != "tesoura":
                                        print("\n\033[1;37mOpção inválida! Digite novamente: \033[0m")
                                        escolha = input("\n\033[32mPlayer 1 escolha: Pedra, Papel ou Tesoura:\033[0m ").lower()
                                
                                #Criando e exibindo a resposta do computador
                                respostaComputador = random.randint(1,3)
                                if respostaComputador == 1:
                                        respostaComputador = "pedra"
                                elif respostaComputador == 2:
                                        respostaComputador = "papel"
                                elif respostaComputador == 3:
                                        respostaComputador = "tesoura"
                                print("\033[31mMáquina - Aqui está a resposta da máquina:\033[0m", respostaComputador)
                                        
                                #Computador ganhando      
                                if escolha == "pedra" and respostaComputador == "papel":
                                        print("\n--------------------------------------------")
                                        print("            \033[1;31mA Máquina venceu!\033[0m")
                                        print("--------------------------------------------")
                                        pontosComputador += 1
                                elif escolha == "papel" and respostaComputador == "tesoura":
                                        print("\n--------------------------------------------")
                                        print("            \033[1;32mA Máquina venceu!\033[0m")
                                        print("--------------------------------------------")
                                        pontosComputador += 1
                                elif escolha == "tesoura" and respostaComputador == "pedra":
                                        print("\n--------------------------------------------")
                                        print("            \033[1;32mA Máquina venceu!\033[0m")
                                        print("--------------------------------------------")
                                        pontosComputador += 1
                                        
                                        
                                #PLAYER 1 VENCENDO
                                elif escolha == "pedra" and respostaComputador == "tesoura":
                                        print("\n--------------------------------------------")
                                        print("            \033[1;31mPlayer 1 venceu!\033[0m")
                                        print("--------------------------------------------")
                                        pontos_player1 += 1
                                elif escolha == "papel" and respostaComputador == "pedra":
                                        print("\n--------------------------------------------")
                                        print("            \033[1;31mPlayer 1 venceu!\033[0m")
                                        print("--------------------------------------------")
                                        pontos_player1 += 1
                                elif escolha == "tesoura" and respostaComputador == "papel":
                                        print("\n--------------------------------------------")
                                        print("            \033[1;32mPlayer 1 venceu!\033[0m")
                                        print("--------------------------------------------")
                                        pontos_player1 += 1
                                elif escolha == respostaComputador:
                                        print("\n--------------------------------------------")
                                        print("                \033[1;30mEmpate!\033[0m")
                                        print("--------------------------------------------")
                                
                                print(f"\n\033[1;37mPlacar:\033[0m \033[1;32mPlayer 1 =\033[0m \033[1;37m{pontos_player1}\033[0m | \033[1;31mPlayer 2 =\033[0m \033[1;37m{pontosComputador}\033[0m") # imprime o placar atual do jogo.

                                
                                # Essa parte serve para perguntar se ele quer jogar novamente quando uma partida termina
                                jogar_novamente = input("\n\033[1;37mDeseja jogar novamente? (s/n):\033[0m ").lower()
                                
                                while jogar_novamente != "s" and jogar_novamente != "n":
                                        print("\n\033[1;37mOpção inválida\033[0m")
                                        jogar_novamente = input("\033[1;37mDeseja jogar novamente? (s/n):\033[0m ").lower()
                                if jogar_novamente == "s":
                                        continue
                                elif jogar_novamente == "n":
                                        print("\n\033[1;37mObrigado por jogar! Estudantes: Felipe Bresciani, Pedro Henrique Junqueira e Rafael Eliezer.\033[0m")
                                        break
                                
                        elif modo == 3: # caso a pessoa escoha o modo 3
                                print("\n--------------------------------------------")
                                print("          \033[1;35mModo Computador vs Computador\033[0m ")
                                print("--------------------------------------------")
                                
                                #Criando e exibindo a resposta do computador 1
                                respostaComputador1 = random.randint(1,3)
                                if respostaComputador1 == 1:
                                        respostaComputador1 = "pedra"
                                elif respostaComputador1 == 2:
                                        respostaComputador1 = "papel"
                                elif respostaComputador1 == 3:
                                        respostaComputador1 = "tesoura"
                                print("\033[32mmMáquina 1- Aqui está a resposta da máquina:\033[0m", respostaComputador1)
                                        
                                #Criando e exibindo a resposta do computador 2
                                respostaComputador2 = random.randint(1,3)
                                if respostaComputador2 == 1:
                                        respostaComputador2 = "pedra"
                                elif respostaComputador2 == 2:
                                        respostaComputador2 = "papel"
                                elif respostaComputador2 == 3:
                                        respostaComputador2 = "tesoura"
                                print("\033[31mMáquina 2 - Aqui está a resposta da máquina:\033[0m", respostaComputador2)
                                        
                                #Computador 1 vencendo     
                                if respostaComputador2 == "pedra" and respostaComputador1 == "papel":
                                        print("\n--------------------------------------------")
                                        print("            \033[1;31mA Máquina 1 venceu!\033[0m")
                                        print("--------------------------------------------")
                                        pontosComputador1 += 1
                                elif respostaComputador2 == "papel" and respostaComputador1 == "tesoura":
                                        print("\n--------------------------------------------")
                                        print("            \033[1;32mA Máquina 1 venceu!\033[0m")
                                        print("--------------------------------------------")
                                        pontosComputador1 += 1
                                elif respostaComputador2 == "tesoura" and respostaComputador1 == "pedra":
                                        print("\n--------------------------------------------")
                                        print("            \033[1;32mA Máquina 1 venceu!\033[0m")
                                        print("--------------------------------------------")
                                        pontosComputador1 += 1
                                        
                                        
                                #Computador 2 vencendo
                                if respostaComputador1 == "pedra" and respostaComputador2 == "papel":
                                        print("\n--------------------------------------------")
                                        print("            \033[1;31mA Máquina 2 venceu!\033[0m")
                                        print("--------------------------------------------")
                                        pontosComputador2 += 1
                                elif respostaComputador1 == "papel" and respostaComputador2 == "tesoura":
                                        print("\n--------------------------------------------")
                                        print("            \033[1;32mA Máquina 2 venceu!\033[0m")
                                        print("--------------------------------------------")
                                        pontosComputador2 += 1
                                elif respostaComputador1 == "tesoura" and respostaComputador2 == "pedra":
                                        print("\n--------------------------------------------")
                                        print("            \033[1;32mA Máquina 2 venceu!\033[0m")
                                        print("--------------------------------------------")
                                        pontosComputador2 += 1
                                elif respostaComputador1 == respostaComputador2:
                                        print("\n--------------------------------------------")
                                        print("                \033[1;30mEmpate!\033[0m")
                                        print("--------------------------------------------")
                                
                                print(f"\n\033[1;37mPlacar:\033[0m \033[1;32mPlayer 1 =\033[0m \033[1;37m{pontosComputador1}\033[0m | \033[1;31mPlayer 2 =\033[0m \033[1;37m{pontosComputador2}\033[0m") # imprime o placar atual do jogo.

                                
                                # Essa parte serve para perguntar se ele quer jogar novamente quando uma partida termina
                                jogar_novamente = input("\n\033[1;37mDeseja jogar novamente? (s/n):\033[0m ").lower()
                                
                                while jogar_novamente != "s" and jogar_novamente != "n":
                                        print("\n\033[1;37mOpção inválida\033[0m")
                                        jogar_novamente = input("\033[1;37mDeseja jogar novamente? (s/n):\033[0m ").lower()
                                if jogar_novamente == "s":
                                        continue
                                elif jogar_novamente == "n":
                                        print("\n\033[1;37mObrigado por jogar! Estudantes: Felipe Bresciani, Pedro Henrique Junqueira e Rafael Eliezer.\033[0m")
                                        break
                                
                        elif modo == 4: # caso a pessoa escolha o modo 4
                                print("\n\033[1;37mObrigado por jogar! Estudantes: Felipe Bresciani, Pedro Henrique Junqueira e Rafael Eliezer.\033[0m")
                                break
                                        
                break

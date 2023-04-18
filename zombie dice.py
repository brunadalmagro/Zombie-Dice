#importacao metodo utilizado
from random import randint

#armazenamento jogador
class Jogador:
    def __init__(self, id, nome):
        self.nome = nome
        self.id = id
        self.tiros = 0
        self.cerebros = 0
        self.vitorias = 0
        self.mortes = 0

print("Seja bem-vindo ao jogo Zombie Dice")
# variaveis/objetos
copo = []
Jogadores = []
# identificacao dos dados
# T(tiro) C(cerebro) P(passos)
dadoVerde = 'CTCPTC'
dadoAmarelo = 'TPCTPC'
dadoVermelho = 'TPTCPT'

# lista dados armazenados
# dados vermelhos
for i in range(0, 3):
    copo.append(dadoVermelho)
# dados verdes
for i in range(0, 6):
    copo.append(dadoVerde)
# dados amarelos
for i in range(0, 4):
    copo.append(dadoAmarelo)
print("Dados na mesa")
# quantidade de jogadores
while ('numJogadores'):
    numJogadores = int(input('Informe a quantidade de jogadores:\n'))
    break
#

if numJogadores > 1:

    for i in range(0, numJogadores):
        print("\n")
        nome = input("Qual o nome do {} jogador?\n".format(i + 1))

        player = Jogador(i + 1, nome)
        Jogadores.append(player)
# estrutura dos pontos

while (True):
    for jogador in Jogadores:
        rodadaEncerrada = False
        passos = 0
        dados = 3
        while (True):
            for i in range(dados):
                numSorteado = randint(0, 12)
                print("Dado sorteado {}: {}".format((i + 1), numSorteado))
                # verificando o dado sorteado
                dadoSorteado = copo[numSorteado]
                ladoDado = randint(0, 5)
                if dadoSorteado[ladoDado] == 'C':
                    print("Cééérebrooo!!!")
                    # informar ao jogador as pontuações da rodada
                    print("Nham, Nham! Você comeu um cérebro!\n")
                    # adicionando a variavel
                    jogador.cerebros = jogador.cerebros + 1
                elif dadoSorteado[ladoDado] == "T":
                    print("BANG-BANG")
                    print("Você levou um tiro! \n")
                    jogador.tiros = jogador.tiros + 1
                else:
                    print("Passos...")
                    # informe que a vitima escapou, e o jogador deve jogar novamente
                    print("a vítima escapou! \n")
                    passos = passos + 1

            print("\n")
            if jogador.tiros >= 3:
                print("O Jogador {} morreu!".format(jogador.nome))
                jogador.mortes = jogador.mortes + 1
                break

            if jogador.cerebros >= 13:
                print("O jogador {} venceu essa rodada!".format(jogador.nome))
                jogador.vitorias = jogador.vitorias + 1
                rodadaEncerrada = True
                break

            print("Pontos do Jogador: {} - {}".format((jogador.id), jogador.nome))
            print("Cerebros: {}".format(jogador.cerebros))
            print("Tiros: {}".format(jogador.tiros))
            print("Passos: {}".format(passos))
            segueJogo = input("Continuar ou sair: (s/n): ")
            if segueJogo == "s":
                print("Avante monstrinho!\n")
            else:
                print("Os humanos venceram...")
                break
            # recomeçando a rodada do zero

            dados = 3 + passos
            passos = 0

        if rodadaEncerrada:
            break
    break
# TODO adicionar validação de quem ganhou a rodada (Quem tem mais cérebros ou cerebros = 13)
# TODO adicionar pergunta se deseja começar uma nova rodada
# TODO zerar valores de tiro e cerebros dos jogados para a nova rodada

print(Jogadores)
import time
import random

#Este é o algorítmo Greedy Randomized Adaptive Search Procedure (GRASP), algumas alterações podem ser feitas nas funções para fins de testes:
    #Lista de alterações disponíveis:
        #1. É possível escolher entre a Solução Gulosa e a solução que inclui o parâmetro alfa como parâmetro de randomização do algorítmo.
            #Para isso, basta definir os parâmetros na função BinPacking1DGRASP e remover os comentários (linha 121).
        #2. Na busca local do algorítmo, é possível escolher entre o First Improvement e o Best Improvement como tentativa de melhorar a qualidade da solução.
            #Para isso, basta remover o comentário da função que será utilizada e adicionar na que não será utilizada (linha 104).

def GreedySolution(capacidade, itens):
    #Os candidatos são todos os itens que podem ser inseridos nas caixas
    #O MissItens são a quantidade de itens que não foram alocados
    GSolution = []
    Candidates = itens[:]
    MissItens = len(itens)
    while MissItens:
        #Enquanto Tenho itens a serem alocados
        BinAtt = []
        BinCapacity = capacidade
        Ok = True
        #Enquanto Ok for true, ou seja, quando não existirem itens que caibam na minha caixa o meu while para
        while Ok:
            #Minha lista RCL é formada com os itens que cabem na caixa atual
            RCL = [item for item in Candidates if item <= BinCapacity]
            if len(RCL) == 0:
                Ok = False
                break
            #Escolho um item aleatorio da minha RCL e coloco na caixa
            RandomItem = random.choice(RCL)
            BinAtt.append(RandomItem)
            BinCapacity -= RandomItem
            Candidates.remove(RandomItem)
        GSolution.append(BinAtt)
        MissItens -= len(BinAtt)
    return GSolution, len(GSolution)

def GreedyRandomizedSolution(alfa, seed, capacidade, itens):
    #Os comentários da função acima servem para essa
    random.seed(seed)
    GSolution = []
    Candidates = itens[:]
    MissItens = len(itens)
    while MissItens:
        BinAtt = []
        BinCapacity = capacidade
        Ok = True
        while Ok:
            if len(Candidates) == 0:
                break
            MinCost = min(Candidates)
            MaxCost = max(Candidates)
            #A diferença essencial está na minha lista de candidatos, que agora pode ser gulosa ou aleatoria com base no meu alfa
            RCL = [item for item in Candidates if item <= (MinCost + alfa*(MaxCost-MinCost)) and item <= BinCapacity]
            if len(RCL) == 0:
                Ok = False
                break
            RandomItem = random.choice(RCL)
            BinAtt.append(RandomItem)
            BinCapacity -= RandomItem
            Candidates.remove(RandomItem)
        GSolution.append(BinAtt)
        MissItens -= len(BinAtt)
    return GSolution, len(GSolution)

def FImprovement(Solution, capacidade):
    #Aqui eu paro minha Busca Local se eu encontro uma melhoria
    size = len(Solution)
    for i in range(size):
        for j in range(i + 1, size):
            Box1 = Solution[i]
            Box2 = Solution[j]
            SumBox2 = sum(Box2)
            for item in Box1:
                if SumBox2 + item <= capacidade:
                    NewSolution = [bin[:] for bin in Solution]
                    NewSolution[i].remove(item)
                    NewSolution[j].append(item)
                    SumBox2+= item
                    if not NewSolution[i]:
                        del NewSolution[i]
                    return NewSolution
    return None

def BImprovement(Solution, capacidade):
    #Aqui eu busco todas as melhorias possíveis
    BestSolution = Solution
    BinsSolution = len(Solution)
    for i in range(len(Solution)):
        for j in range(i + 1, len(Solution)):
            Box1 = Solution[i]
            Box2 = Solution[j]
            SumBox2 = sum(Box2)
            for item in Box1:
                if SumBox2 + item <= capacidade:
                    NewSolution = [bin[:] for bin in Solution]
                    NewSolution[i].remove(item)
                    NewSolution[j].append(item)
                    SumBox2+= item
                    if not NewSolution[i]:
                        del NewSolution[i]
                    QtdBins = len(NewSolution)
                    if QtdBins < BinsSolution:
                        BestSolution = NewSolution
                        BinsSolution = QtdBins
    if BestSolution != Solution:
        return BestSolution
    return None

def LocalSearch(Solution, capacidade):
    IsBetter = True
    while IsBetter:
        IsBetter = False
        #NewSolution = BImprovement(Solution, capacidade)
        NewSolution = FImprovement(Solution, capacidade)
        if NewSolution is not None and len(NewSolution) < len(Solution):
            Solution = NewSolution
            IsBetter = True
    return Solution, len(Solution)

def AttSolution(QtdBins, Solution, BestSolution, BinsSolution):
    if QtdBins < BinsSolution:
        BinsSolution = QtdBins
        return Solution, QtdBins
    return BestSolution, BinsSolution

def BinPacking1DGRASP(capacidade, itens):
    start = time.time()
    iteracoes = 100

    #Parâmetros da busca gulosa randomizada:
    
    #seed = int(time.time())
    #alfa = 0.95

    BestSolution = []
    BinsSolution = len(itens)
    for i in range(iteracoes):
        random.shuffle(itens)
        Solution, QtdBins = GreedySolution(capacidade, itens)
        #Solution, QtdBins = GreedyRandomizedSolution(alfa, seed, capacidade, itens)
        Solution, QtdBins = LocalSearch(Solution, capacidade)
        BestSolution, BinsSolution = AttSolution(QtdBins, Solution, BestSolution, BinsSolution)
    end = time.time()
    tempo = end - start
    print(f"Solução inicial encontrada com o GRASP:\n{BestSolution}\nQuantidade de bins: {BinsSolution}\nTempo de execução: {tempo:.4f} segundos\n")
    return BestSolution, BinsSolution

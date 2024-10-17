import random
import math

#Este é o algorítmo Simulated Annealing (SA), algumas alterações podem ser feitas nas funções para fins de testes:
    #Alterações disponíveis:
        #O parâmetro alfa utilizado como critério de aceitação de soluções pode ser alterado, assim como a temperatura inicial, a taxa de resfriamento e a capacidade das caixas(linha 37).

def best_fit_construircaixas(vetor, capacidade):
    caixas = []  # lista para armazenar as caixas
    
    for item in vetor:
        melhor_caixa = None
        menor_espaco = capacidade + 1  # definir inicialmente como maior que a capacidade
        
        for caixa in caixas:
            espaco_livre = capacidade - sum(caixa)
            if espaco_livre >= item and espaco_livre < menor_espaco:
                melhor_caixa = caixa
                menor_espaco = espaco_livre
        
        if melhor_caixa is not None: 
            melhor_caixa.append(item)
        else:
            caixas.append([item])
    
    return caixas
    
def calculacaixas(vetor, capacidade):
    return best_fit_construircaixas(vetor, capacidade)

def perturbarsol(vetor):
    solucao = vetor[:]
    random.shuffle(solucao) 
    return solucao

def simulated_annealing(vetor, todastemperaturas, todososresultadosbins, tdsiteracoes, capacidade):
    tempinicial = 1000
    resfriamento = 0.95

    solucaoatual = vetor
    melhorsolucao = solucaoatual[:]
    melhorcaixas = calculacaixas(solucaoatual,capacidade)
    melhorbins = len(melhorcaixas)
    caixasatual = melhorcaixas
    temperatura = tempinicial
    c=0

    while temperatura > 1:
        novasolucao = perturbarsol(solucaoatual)  
        novascaixas = calculacaixas(novasolucao, capacidade)

        binsnova = len(novascaixas)
        binsatual = len(caixasatual)
        c+=1
        taxavariacao = binsnova - binsatual
        todastemperaturas.append(temperatura)
        todososresultadosbins.append(binsatual)
        tdsiteracoes.append(c)

        if taxavariacao < 0 or random.uniform(0, 1) < math.exp(-taxavariacao / temperatura):
            solucaoatual = novasolucao
            caixasatual = novascaixas

        if binsnova < melhorbins:
            melhorsolucao = novasolucao
            melhorcaixas = novascaixas
            melhorbins = binsnova
		
        temperatura *= resfriamento

    return melhorcaixas, melhorbins, todastemperaturas, todososresultadosbins, tdsiteracoes

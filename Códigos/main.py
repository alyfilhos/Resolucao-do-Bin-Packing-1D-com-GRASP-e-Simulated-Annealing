import matplotlib.pyplot as plt
import time
import SA

#Este é o arquivo que contem a leitura do arquivo com as instancias e os códigos que geram os gráficos utilizados na análise dos algorítmos.
#Obs: os arquivos devem seguir o seguinte formato:
    #A primeira linha deve conter a capacidade, quantidade de itens e melhor solução respectivamente.
    #A partir da segunda linha o arquivo deve ter um item por linha

def ReadInput(arquivo):
    with open(arquivo, 'r') as arquivo:
        primeira_linha = arquivo.readline().strip().split()
        valor1, valor2, valor3 = int(primeira_linha[0]), int(primeira_linha[1]), int(primeira_linha[2])

        vetor = []
        for linha in arquivo:
            vetor.append(int(linha.strip()))

    return valor1, valor2, valor3, vetor

# Exemplo de uso
arquivo = 'C:/Users/Alysson Victor/OneDrive/Documentos/metaheuristica 2024.2/instancia1.txt'
capacidade, qtditens, melhorresposta, vetor = ReadInput(arquivo)

print(f"Capacidade, qtd de ites e melhor resposta: {capacidade}, {qtditens}, {melhorresposta}")
print("\nVetor com os valores restantes:\n", vetor)

todososresultadosbins = []
todastemperaturas =[]
tdsiteracoes =[]

start = time.time()
melhorcaixas, melhorbins, todastemperaturas, todososresultadosbins, tdsiteracoes = SA.simulated_annealing(vetor, todastemperaturas, todososresultadosbins, tdsiteracoes, capacidade)
end = time.time()
tempo = end - start
print(f"Solução final encontrada com o Simulated Annealing:\n{melhorcaixas}\nQuantidade de bins: {melhorbins}\nTempo de execução: {tempo:.4f} segundos")

plt.plot(todastemperaturas, todososresultadosbins)
plt.xlabel('Temperatura')
plt.ylabel('numero de caixas')
plt.title('Evolução do número de caixas durante o Simulated Annealing')
plt.gca().invert_xaxis()
plt.show()

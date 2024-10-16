import matplotlib.pyplot as plt
import time
import SA

#Este é o arquivo que contem a leitura do arquivo com as instancias e os códigos que geram os gráficos utilizados na análise dos algorítmos.
#Obs: os arquivos devem seguir o seguinte formato:
    #Um item por linha
#A quantidade de itens é definida pelo tamanho do vetor formado com as linhas do arquivo.

with open('C:/Users/Alysson Victor/OneDrive/Documentos/metaheuristica 2024.2/instancia3.txt', 'r') as arquivo:
    vetor = [int(linha.strip()) for linha in arquivo]

todososresultadosbins = []
todastemperaturas =[]
tdsiteracoes =[]

start = time.time()
melhorcaixas, melhorbins, todastemperaturas, todososresultadosbins, tdsiteracoes = SA.simulated_annealing(vetor, todastemperaturas, todososresultadosbins, tdsiteracoes)
end = time.time()
tempo = end - start
print(f"Solução final encontrada com a hibridização do GRASP com o Simulated Annealing:\n{melhorcaixas}\nQuantidade de bins: {melhorbins}\nTempo de execução: {tempo:.4f} segundos")

plt.plot(todastemperaturas, todososresultadosbins)
plt.xlabel('Temperatura')
plt.ylabel('numero de caixas')
plt.title('Evolução do número de caixas durante o Simulated Annealing')
plt.gca().invert_xaxis()
plt.show()

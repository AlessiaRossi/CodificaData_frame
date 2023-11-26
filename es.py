import pandas as pd
import math
import json
import numpy as np

# Definisci il percorso e il nome del file Excel
path_del_file = "C:\\Users\\hp\\Downloads\\test3_anonimizzato.xlsx"

# Carica i dati dal file Excel in un DataFrame
df = pd.read_excel(path_del_file, header = [0])

diz = dict(df)
#
# accessi = {}
# # print(diz)
# media = []
# accessi_giornalieri = {}
# for x in diz['data']:
#     valori = x.split(' ')
#     data = valori[0]
#     if data in accessi.keys():
#         accessi[data] = accessi.get(data) + 1
#     else:
#         accessi[data] = 1
# # print(accessi)
#
# for numero in accessi.values():
#     v = numero / 1
#     media.append(v)
# print(media)

#Calcolare il numero di accessi medio giornaliero
df.data=pd.to_datetime(df.data).dt.date # coverte la colonna data in valori numerici di data e ora e poi prendo solo data
num_accessi = df.shape[0] # restituisce n righe e colonne , con zeor chiediamo solo righe
num_giorni = len(df.data.unique()) #lunghezza del nuemro di giorni senza ripetizione

media_giornaliera = (num_accessi/num_giorni)
print(media_giornaliera)

#deviazione standard
numeratore=0
print(df.value_counts('data')) # conta la numerosità delle singole date
# for i in df.value_counts('data'):
#     numeratore += math.pow((i-media_giornaliera),2) #potenza al quadrato della media , con for fai la sommatoria
#
# dev_std=math.sqrt(numeratore/num_giorni)
# print(dev_std)
print(np.std(df.value_counts('data')))

#Determinare quali sono gli eventi del giorno che ha
#avuto più accessi e per ciascuno di essi calcolarne
#la numerosità

#raggruppa le righe che hanno stessa data e evento un una (non fa vedere duplicati)
grouped_by_data_evento = df.groupby(['data', 'evento']).agg({'evento': ['count']})#toglie gli indici , count è una nuova riga
#print(grouped_by_data_evento) # agg conta il numero di eventi
#
# resetto gli indici cosi da far ritornare un dataframe
grouped_by_data_evento = grouped_by_data_evento.reset_index()
print(grouped_by_data_evento)

# # Raggruppo per data e prendo il massimo
max_evento_by_data = grouped_by_data_evento.groupby('data').agg('max') #togli la data che si ripete ma prendi quella con count massimo,
# # used to reset the index of a DataFrame, making the current index into a new column and generating a default numbered index.
#print(max_evento_by_data.reset_index()) # in questo caso mette anche gli indici
print (max_evento_by_data)
# #value_counts() function on a DataFrame (df) to count occurrences of values in a specific column ('evento').
#print('\n', df.value_counts('evento',ascending=False))



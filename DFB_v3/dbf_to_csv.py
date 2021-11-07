import os
import pandas as pd
from simpledbf import Dbf5

for file in os.listdir('dbf'):
    if file.endswith(".dbf"):
        dbf = Dbf5('dbf/' + file, codec='ISO-8859-1')
        print(dbf)
        dbf.to_csv("csv/" + os.path.splitext(file)[0] + ".csv")
        print('Transformando DBF para CSV...relaxa...')
        
lista = []
for file_csv in os.listdir('csv'):
    #print(file_csv)
    #chunks = pd.DataFrame(chunks)
    chunks = pd.read_csv("csv/" + file_csv ,encoding= 'ISO-8859-1', low_memory=False)
    chunks_lista = chunks
    lista.append(chunks_lista)
    df = pd.concat(lista)
df.to_csv("csv_concat/" + os.path.splitext(file)[0] + ".csv",index=False)
print('Finalizado a junção!!')
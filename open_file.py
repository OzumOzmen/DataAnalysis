import numpy as np
import pandas as pd
import random

data = np.genfromtxt('data_set', delimiter = ',' ,  dtype=str ) #text dosyasını olusutur
print(data)
"""
a= data[:, (0)]#0. indeksteki tüm satırları al
x=np.asfarray(a,float)#text dosyaı içinde ollması gerekn type çevir

b= data[:, (1)]

c = data [:,(2)]

d =  data [:,(3)]
y=np.asfarray(d,float)


data  = pd.DataFrame(data,columns=["No","İsim","Cinsiyet","Miktar"])
print(data)

print(df["İsim"])#coloumna göre seriyi göster

print(data.loc[1])#satıra göre seriyi göster

print(data[["İsim","Miktar"]]#multiple colomns get

## Data FrameYeni kolon ekleme
data = pd.DataFrame(data,columns=["No","İsim","Cinsiyet","Miktar"]);

print(data);
data["kredioranı"] = pd.Series(np.random.randn(15))
print(data);
#Dataframe toplama
df["Toplam"]= df["bir"] + df["iki"]
df.drop["İsim"] #Dİsim kolonunu sil

df = pd.DataFrame(data,columns=["No","İsim","Cinsiyet","Miktar"])
print(df)
groupKE= df.groupby(["Cinsiyet"]).count()["No"]#cinsiyete göre sayı
print(groupKE)
"""
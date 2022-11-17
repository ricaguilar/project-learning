import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as wb
import numpy as np

#Descarga los datos del sticker de yahoo
symbol = 'BTC-USD'
data = wb.DataReader(symbol, 'yahoo', '2021-1-1')['Adj Close']

mm_short = 30
mm_long = 200

#Crea un dataframe con una variable Signals
signal = pd.DataFrame(index=data.index)
signal['Signals'] = 0

#Creamos dos columnas donde calculamos las medias moviles
signal['Short'] = data.rolling(mm_short).mean()
signal['Long'] = data.rolling(mm_long).mean()

#Crea variables para las medias moviles simples y exponenciales
#signal['Ema_Short'] = data.ewm(mm_short).mean()
#signal['Ema_Long'] = data.ewm(mm_long).mean()

#A la variable signal creada le decimos que marque con un 1 o 0 cuando la media corta cruce a la larga
signal['Signals'] = np.where(signal['Short'] > signal['Long'], 1, 0)
#signal['Signals'] = np.where(signal['Ema_Short'] > signal['Ema_Long'], 1, 0)

#signal['Short'] = signal['Short'].iloc[mm_long:]

signal['Positions'] = signal['Signals'].diff()
print(signal.tail(50))

#Configuramos el grafico
fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(121, ylabel=symbol) #El parametro 121 significa que queremos mas de un grafico
ax1.set_title("Estrategia cruce de medias con: " + str(symbol))

#Graficamos los datos y las medias moviles
data.plot(ax=ax1, color = 'k', lw = 1.2)
signal[['Short', 'Long']].plot(ax=ax1, lw=1.3)

data.iloc[mm_long:].plot(ax=ax1, color='k', lw=1.9)

ax1.plot(signal['Short'][signal['Positions'] == 1], '^', markersize=8, color='g')
ax1.plot(signal['Short'][signal['Positions'] == -1], 'v', markersize=8, color='r')

plt.show()

#########################################
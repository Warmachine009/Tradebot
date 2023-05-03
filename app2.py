import pandas as pd
import numpy as np
import yfinance as yf

def Aroon(df, period):
    high = df['High'].rolling(window=period+1).apply(np.argmax, raw=True)
    low = df['Low'].rolling(window=period+1).apply(np.argmin, raw=True)
    aroon_up = ((period - high) / period) * 100
    aroon_down = ((period - low) / period) * 100
    return aroon_up, aroon_down

# load data
df = yf.download("AAPL", start="2021-01-01", end="2023-04-30")

# calculate Aroon indicator with period=14
df['aroon_up'], df['aroon_down'] = Aroon(df, 14)

# generate buy and sell signals
df['signal'] = np.where(df['aroon_up'] > df['aroon_down'], 1, -1)

# plot signals
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(16,8))
ax.plot(df.index, df['Close'])
ax.scatter(df[df['signal']==1].index, df[df['signal']==1]['Close'], color='green', label='Buy')
ax.scatter(df[df['signal']==-1].index, df[df['signal']==-1]['Close'], color='red', label='Sell')
plt.legend(loc='upper left')
plt.show()

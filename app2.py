import pandas as pd
import numpy as np
import yfinance as yf
import talib
import datetime

current_time = datetime.datetime.now()

end_dt = current_time.strftime("%Y-%m-%d")

def Aroon(df, period):
    high = df['High'].rolling(window=period+1).apply(np.argmax, raw=True)
    low = df['Low'].rolling(window=period+1).apply(np.argmin, raw=True)
    aroon_up = ((period - high) / period) * 100
    aroon_down = ((period - low) / period) * 100
    return aroon_up, aroon_down
def technical(tkr, strt_dt, inter):
    # load data
    df = yf.download(tkr, start=strt_dt, end=end_dt, interval=inter)

    # calculate Aroon indicator with period=14
    df['aroon_up'], df['aroon_down'] = Aroon(df, 14)

    # calculate RSI
    df['rsi'] = talib.RSI(df['Close'], timeperiod=14)

    # generate buy and sell signals
    df['signal'] = np.where((df['aroon_up'] > df['aroon_down']) & (df['Close'] > df['vwap']), 1,
                            np.where((df['aroon_up'] < df['aroon_down']) & (df['Close'] < df['vwap']), -1, 0))

    # print signals
    for i in range(len(df)):
        if df['signal'][i] == 1:
            sig = "buy"
        elif df['signal'][i] == 0:
            sig = "sell"
    return sig

# plot signals

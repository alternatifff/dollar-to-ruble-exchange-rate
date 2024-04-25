import matplotlib.pyplot as plt
import yfinance as yf
import pandas_datareader.data as web


def plot_rub_usd():
    yf.pdr_override()
    df = web.DataReader("USDRUB=X", datetime.datetime.today() - datetime.timedelta(days=365))
    plt.plot(df.index, df['Close'])
    plt.show()


plot_rub_usd()
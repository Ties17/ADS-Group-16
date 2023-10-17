import rpyc
import yfinance as yf

class StockService(rpyc.Service):

    def on_connect(self, conn):
        print("new connection!")
        # code that runs when a connection is created
        # (to init the service, if needed)
        pass

    def on_disconnect(self, conn):
        # code that runs after the connection has already closed
        # (to finalize the service, if needed)
        pass

    def exposed_get_stock_price(self, ticker):
        try:
            data = self.get_stock_data(ticker)
        except:
            print(f"Ticker: {ticker} does not exist")
            return
        else:
            message = f'{ticker}: {data}'
            print(message)
            return message


    def get_stock_data(self, ticker):
        stock = yf.Ticker(ticker)
        # try:
        #     info = ticker.info
        # except:
        #     print(f"Ticker: {ticker} does not exists")
        #     return None

        return stock.history(period='1d', interval='5m').iloc[-1]['Close']
        

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(StockService, port=18861)
    t.start()

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
        data = self.get_stock_data(ticker)

        message = f'{ticker}: {data}'
        print(message)
        return message


    def get_stock_data(self, ticker):
        return yf.Ticker(ticker).history(period='3m', interval='1m').iloc[-1]['Close']
        

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(StockService, port=18861)
    t.start()

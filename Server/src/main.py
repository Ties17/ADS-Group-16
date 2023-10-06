import rpyc
import requests

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

        if not (data is None):
            message = f'{ticker}: {data["Global Quote"]["05. price"]}'
            print(message)
            return message
        
        return None

    def get_stock_data(self, ticker):
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey=CA5GUM3M825B9QS5'
        r = requests.get(url)
        data = r.json()

        if "Global Quote" in data:
            print(data)
            return data

        return None
        

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(StockService, port=18861)
    t.start()

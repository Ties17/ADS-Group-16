import rpyc
import requests
from alpha_vantage.timeseries import TimeSeries

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

    def exposed_get_answer(self): # this is an exposed method
        return 42

    exposed_the_real_answer_though = 43     # an exposed attribute

    def get_question(self):  # while this method is not exposed
        return "what is the airspeed velocity of an unladen swallow?"
    
    def get_stock_price(self, symbol):
        api_key = "RG6Z56SVLUCAVF4Q"
        base_url = f"https://www.alphavantage.co/query?"

        
        function = "GLOBAL_QUOTE"
        final_url = f"{base_url}function={function}&symbol={symbol}&apikey={api_key}"
        response = requests.get(final_url)
        if response.status_code == 200:
            data = response.json()
            if "Global Quote" in data and "05. price" in data["Global Quote"]:
                return float(data["Global Quote"]["05. price"])
            else:
                raise ValueError(f"Unexpected data format: {data}")
        else:
            raise ConnectionError(f"Failed to retrieve data: {response.status_code}")


if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(StockService, port=18861)
    t.start()

import rpyc, sched, time, random, sys

time.sleep(2)

def read_tickers():
    file = open("/app/src/tickers.txt")
    for line in file:
        tickers.append(line[:-1])

interval = int(sys.argv[1])
ip_address = sys.argv[2]
print(f"Trying to connect to {ip_address}")

tickers = []
read_tickers()

start_time = time.time()

for i in range(100):
    c = rpyc.connect(ip_address, port=18861)
    print(c.root.get_stock_price(tickers[i]))

print(f"took {time.time() - start_time} seconds")
import rpyc, sched, time, random, sys

time.sleep(2)

def read_tickers():
    file = open("/app/src/tickers.txt")
    for line in file:
        tickers.append(line[:-1])

def print_result(req):
    # print(req.value)
    pass

def check_reqs(reqs):
    for req in reqs:
        if not req.ready:
            return False
    
    return True

interval = int(sys.argv[1])
ip_address = sys.argv[2]
print(f"Trying to connect to {ip_address}")

tickers = []
read_tickers()

start_time = time.time()

reqs = []
for i in range(100):
    c = rpyc.connect(ip_address, port=18861)
    async_request = rpyc.async_(c.root.get_stock_price)
    res = async_request(tickers[i])
    res.add_callback(print_result)
    reqs.append(res)
    # print(res.value)

while not check_reqs(reqs):
    pass
print(f"took {time.time() - start_time} seconds")
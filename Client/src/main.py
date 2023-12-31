import rpyc, sched, time, random, sys

def read_tickers():
    # file = open("./tickers.txt")
    file = open("/app/src/tickers.txt")

    for line in file:
        tickers.append(line.strip())

def get_random_stock_ticker():
    index = random.randint(0, len(tickers) - 1)
    return tickers[index]

time.sleep(3)

interval = int(sys.argv[1])
ip_address = sys.argv[2]
# print(f"Trying to connect to {ip_address}")

tickers = []
read_tickers()

scheduler = sched.scheduler(time.monotonic, time.sleep)

def print_result(req):
    print(req.value)

def do_request():
    try:
        c = rpyc.connect(ip_address, port=18861)
        # c._config['sync_request_timeout'] = 3
        timed_get_stock = rpyc.timed(c.root.get_stock_price, 3)
        # timed_get_stock.add_callback(print_result)
        req = timed_get_stock(get_random_stock_ticker())
        print(req.value)
        # print(c.root.get_stock_price())
    except:
        print("request timed out, continue")
        pass     

    scheduler.enter(1, 1, do_request)

scheduler.enter(1, 1, do_request)
scheduler.run()

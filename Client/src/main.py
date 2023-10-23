import rpyc, sched, time, random, sys

def read_tickers():
    file = open("/app/src/tickers.txt")
    for line in file:
        tickers.append(line[:-1])

def get_random_stock_ticker():
    index = random.randint(0, len(tickers) - 1)
    return tickers[index]

interval = int(sys.argv[1])

tickers = []
read_tickers()

scheduler = sched.scheduler(time.monotonic, time.sleep)
c = rpyc.connect("172.17.0.2", port=18861)
def do_request():
    print(c.root.get_stock_price(get_random_stock_ticker()))

    scheduler.enter(interval, 1, do_request)

scheduler.enter(1, 1, do_request)
scheduler.run()
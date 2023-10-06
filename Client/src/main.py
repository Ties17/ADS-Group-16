import rpyc, sched, time

scheduler = sched.scheduler(time.monotonic, time.sleep)

c = rpyc.connect("172.17.0.2", port=18861)

def do_request():
    print(c.root.get_stock_price("AAPL"))

    scheduler.enter(3, 1, do_request)

scheduler.enter(1, 1, do_request)
scheduler.run()
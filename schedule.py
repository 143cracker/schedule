import schedule
import time
def do_some_thing():
    print("give time we are updating in formation")
#schedule.every().day().do(do_some_thing)
schedule.every(10).minutes.do(do_some_thing)
schedule.every().hour.do(do_some_thing)
schedule.every(1).to(10).minutes.do(do_some_thing)
schedule.every().wendnesday.at("13:45").do(do_some_thing)
schedule.every().minute.at(":17").do(do_some_thing)
schedule.every(10).seconds.do(do_some_thing)
while 1:
    schedule.run_pending()
    time.sleep(1)
    

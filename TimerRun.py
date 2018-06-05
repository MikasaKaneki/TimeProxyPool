import datetime, time


def timer():
    sched_time = datetime.datetime(2018, 6, 5, 22, 45, 00)
    timedelta = datetime.timedelta(minutes=1)
    now_timer = datetime.datetime.now()
    if str(sched_time - now_timer)[0] == '-':
        print('现在的时间大于开始的时间，请重新调整')
        sched_time = str(datetime.datetime.now() + timedelta)[:-7]

    while True:
        now_timer = str(datetime.datetime.now())[:-7]
        if now_timer == str(sched_time):
            sched_time = str(datetime.datetime.now() + timedelta)[:-7]
            print(sched_time)
        time.sleep(1)
        print('现在的时间是' + str((datetime.datetime.now())))


if __name__ == "__main__":
    timer()

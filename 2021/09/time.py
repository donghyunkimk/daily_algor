import timeit
start_time = timeit.default_timer()  # 시작 시간 체크

number = [_ for _ in range(3,1000001,2)]

print(number)


terminate_time = timeit.default_timer()  # 종료 시간 체크

print("%f초 걸렸습니다." % (terminate_time - start_time))
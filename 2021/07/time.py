import timeit
start_time = timeit.default_timer()  # 시작 시간 체크

a = '0123456'

b = {}
b[a] = a
c = b.get('d')

print(b)
print(c)


terminate_time = timeit.default_timer()  # 종료 시간 체크

print("%f초 걸렸습니다." % (terminate_time - start_time))
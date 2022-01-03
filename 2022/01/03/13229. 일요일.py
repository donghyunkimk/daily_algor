days = ['SUN','MON','TUE','WED','THU','FRI','SAT']

T = int(input())

for tc in range(1,1+T):
    day = str(input())
    ans = 7 - days.index(day)

    print('#{} {}'.format(tc,ans))
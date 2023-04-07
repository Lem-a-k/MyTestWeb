import sys
# строки
# множества
# потоковый ввод
# списочные выражения

line_1 = sys.stdin.readline().rstrip('\n')  # good
line_2 = sys.stdin.readline().rstrip('\n')  # bad
line_3 = sys.stdin.readline().rstrip('\n')
for line in sys.stdin:
    line = line.rstrip('\n')
    # переберём все подстроки
    ans = 0
    s = ''
    short_ans = None
    short_s = None
    for i in range(len(line)):
        for j in range(i + 1, len(line) + 1):
            # количество "хороших" букв в подстроке
            good = sum(1 for x in line[i:j] if x in line_1)
            # количество различных "плохих" букв
            bad = len({x for x in line[i:j] if x in line_2})
            # print(i, j, line[i:j], good, bad)
            if bad == 0 and good >= ans:
                ans = good
                s = line[i:j]
            if all(x in line[i:j] for x in line_3):
                print(line[i:j])
                if short_ans is None or short_ans > len(line[i:j]):
                    short_ans = len(line[i:j])
                    short_s = line[i:j]
    # print(ans, s)
    print(short_ans, short_s)
    ans = 0
    cur = 0
    for x in line:
        if x in line_2:
            cur = 0
        if x in line_1:
            cur += 1
        if ans < cur:
            ans = cur
    # print(ans)

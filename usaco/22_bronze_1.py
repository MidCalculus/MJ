num = int(input())
tuition = list(map(int, input().split()))

t_max = max(tuition)
t_min = min(tuition)

ans = 0

for i in range(t_max, t_min-1, -1):
    temp_ans = 0
    for j in tuition:
        if i <= j:
            temp_ans += i
    if ans < temp_ans:
        ans = temp_ans

print(ans, t_min*num)


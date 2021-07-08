from collections import Counter
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
n = int(input())
a = list(map(int,input().split()))
a = sorted(a)
c = Counter(a)
ans = 0
d=[0]*(10**6+1)
for i in a: 
    if d[i] != 0:
        d[i] = 2
        continue
    for j in range(i,10**6 + 1,i):
        d[j] += 1
ans = 0
for i in a:
    if d[i] == 1:
        ans += 1
print(ans)
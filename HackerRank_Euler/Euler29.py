N=int(input())

memo = [True] * (N+1)
ans = 0

for i in range(2, N+1):
    if memo[i]:
        power = 2
        answers=[]
        
        while i**power<=N:
            memo[i**power] = False
            answers+=[n for n in range(2*power, N*power+1, power) if n > N]
            power+=1
        ans += len(set(answers)) + (N-1)
        
print(ans)
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations, product
from decimal import Decimal, getcontext
getcontext().prec = 20

M = int(input())
S = list(map(Decimal, input().split()))


A = ['+','-','*','/']

def all_comb(S):
    ans = set()
    if len(S) == 1:
        try:
            ans.add(S[0])
        except:
            pass
    elif len(S) == 2:
        try:

            S_comb = list(permutations(S))
            for s in S_comb:
                a,b = s
                for ar in A:
                    try:
                        string = "a" + ar[0] + "b"
                        ans.add(eval(string))
                    except:
                        pass
        except:
            pass
            

    elif len(S) == 3:
        try:
            S_comb = list(permutations(S))
            A_comb = list(product(A, repeat=2))
            for s in S_comb:
                a,b,c = s
                for ar in A_comb:
                    try:
                        string = "(a" + ar[0] + "b)" + ar[1] + "c"
                        ans.add(eval(string))
                    except:
                        pass
                    try:
                        string = "a" + ar[0] + "(b" + ar[1] + "c)"
                        ans.add(eval(string))
                    except:
                        pass
        except:
            pass
    elif len(S) == 4:
        try:
            S_comb = list(permutations(S))
            A_comb = list(product(A, repeat=3 ))
            for s in S_comb:
                a,b,c,d = s
                for ar in A_comb:
                    try:
                        string = "(a" + ar[0] + "b)" + ar[1] + "c" + ar[2] + "d"
                        ans.add(eval(string))
                    except:
                        pass
                    try:
                        string = "(a" + ar[0] + "b)" + ar[1] + "(c" + ar[2] + "d)"
                        ans.add(eval(string))
                    except:
                        pass
                    try:
                        string = "(a" + ar[0] + "(b" + ar[1] + "c))" + ar[2] + "d"
                        ans.add(eval(string))
                    except:
                        pass
                    try:
                        string = "a" + ar[0] + "((b" + ar[1] + "c)" + ar[2] + "d)"
                        ans.add(eval(string))
                    except:
                        pass
                    try:
                        string = "a" + ar[0] + "(b" + ar[1] + "(c" + ar[2] + "d))"
                        ans.add(eval(string))
                    except:
                        pass
        except:
            pass

    elif len(S) == 5:
        try:
            S_comb = list(permutations(S))
            A_comb = list(product(A, repeat=4))

            for s in S_comb:
                a,b,c,d,e = s
                for ar in A_comb:
                    strings = ["(a"  + ar[0] +  "b)" + ar[1] + " c" + ar[2] + " d" + ar[3] + " e",
                        "a" + ar[0] +  "b" + ar[1] + " (c" + ar[2] + " d)" + ar[3] + " e",
                        "a"  + ar[0] + "(b" + ar[1] + " c)" + ar[2] + " d" + ar[3] + " e",
                        "(a" + ar[0] +  "b)" + ar[1] + " (c" + ar[2] + " d)" + ar[3] + " e",
                        "(a" + ar[0] +  "b)" + ar[1] + " c" + ar[2] + " (d" + ar[3] + " e)",
                        "a" + ar[0] +  "(b" + ar[1] + " c)" + ar[2] + " (d" + ar[3] + " e)",           
                        "((a" + ar[0] +  "b)" + ar[1] + " c)" + ar[2] + " d" + ar[3] + " e",
                        "((a" + ar[0] +  "b)" + ar[1] + " c" + ar[2] + " d)" + ar[3] + " e",
                        "(a" + ar[0] +  "(b" + ar[1] + " c))" + ar[2] + " d" + ar[3] + " e",
                        "(a" + ar[0] +  "(b" + ar[1] + " c)" + ar[2] + " d)" + ar[3] + " e",
                        "(a" + ar[0] +  "(b" + ar[1] + " c)" + ar[2] + " d" + ar[3] + " e)",
                        "a" + ar[0] +  "((b" + ar[1] + " c)" + ar[2] + " d)" + ar[3] + " e",
                        "a" + ar[0] +  "((b" + ar[1] + " c)" + ar[2] + " d" + ar[3] + " e)",
                        "a" + ar[0] +  "(b " + ar[1] + "(c" + ar[2] + " d)" + ar[3] + " e)",
                        "a" + ar[0] +  "(b" + ar[1] + " c" + ar[2] + " (d" + ar[3] + " e))",
                        "a" + ar[0] +  "(b" + ar[1] + " (c" + ar[2] + " (d" + ar[3] + " e)))"]
                    for string in strings:
                        try:
                            ans.add(eval(string))
                        except:
                            pass
        except:
            pass
    ans = sorted([int(item) for item in ans if item==int(item) and item > 0])
    return ans

ans_set = all_comb(S)
ans = 0
for i in range(len(ans_set)):
    if ans_set[i] == i+1:
        ans = i + 1

print(ans)

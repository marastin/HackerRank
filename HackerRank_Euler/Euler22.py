n = int(input())
names = [input() for _ in range(n)]
q = int(input())
q_names = [input() for _ in range(q)]

names.sort()
name_dict = {}

# Score using ascii code
for idx, name in enumerate(names):
    score = sum([ord(char) for char in name]) - len(name)*64
    name_dict[name] = (idx+1)* score


for name in q_names:
    print(name_dict[name])

n = int(input()) 
listic = 
negative = [x for x in listic if x < 0 ]
mini_abs = min(abs(negative))

positive = [x for x in listic if x >=0]
mini_pos = min(positive)

if mini_abs != None and mini_pos != None:
    res = mini_abs*mini_pos
    print(res)




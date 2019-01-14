num = input()

mul = 1
dec = 0
#print(type(num[::-1][0]))
for x in num[::-1]:
    dec += int(x) * mul
    mul = mul*2
    
print(dec)
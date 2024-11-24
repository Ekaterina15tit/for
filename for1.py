d = int (input('Кол-во чисел для ввода:'))
cnt = 0 

for i in range (d):
     e = int(input('Число для ввода:'))
     if (e == 0): 
         cnt+=1
     
print ('Кол-во чисел равных нулю:', cnt)     
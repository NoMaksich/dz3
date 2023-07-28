count=int(input("Введите количество кустов на грядке: "))
garden=[]
print("Введите количество ягод на каждом кусту")
for i in range(count):
    garden.append(int(input()))
max=garden[-1]+garden[0]+garden[1]
for i in range(count-1):
    if garden[i-1]+garden[i]+garden[i+1]>max:
        max=garden[i-1]+garden[i]+garden[i+1]
print(max)
num = int(input('Enter a number: '))

iteration = 0

for i in range(num, 0, -2):
    iteration+=1
    print(f'iteration #{iteration} | number = {i}')
num = int(input('Enter a number: '))

iteration = 0

for i in range(num, 0, -2):
    iteration+=1
    if 0 < num < 100:
        if 0 < iteration < 10:
            print(f'Iteration #0{iteration}: number = {i}')
        else:
            print(f'Iteration #{iteration}: number = {i}')
    elif 100 <= num <= 1000:
        if 0 < iteration < 10:
            print(f'Iteration #00{iteration}: number = {i}')
        elif 10 <= iteration < 100:
            print(f'Iteration #0{iteration}: number = {i}')
        else:
            print(f'Iteration #{iteration}: number = {i}')
    
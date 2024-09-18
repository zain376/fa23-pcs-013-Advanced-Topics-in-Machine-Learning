def compute(distance, time):
    if time == 0:
        print('Time error! It can not be zero')
    else:
        velocity = distance/time
        return velocity
distance = 120
time = 0
compute(distance,time)

even_num = []
for num in range(1, 13):
    if num % 2 == 0:
        even_num.append(num)

for num in even_num:
    print(num)


def mult(list_of_even_numbers):
    total_multiplication = 1
    for num in list_of_even_numbers:
        total_multiplication = total_multiplication * num
    print(total_multiplication)


mult(even_num)

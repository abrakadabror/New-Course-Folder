cars = ['ok', 'ok', 'faulty', 'ok', 'ok']

for status in cars:
    if status == 'faulty':
        print('Found faulty car, skipping')
        continue #break #stop the loop
    print(f'This car is {status}.')
    print('Shipping new car to customer')
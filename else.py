cars = ['ok','ok','ok','faulty','ok','ok']

for status in cars:
    if status == 'faulty':
        print('Stopping the producetion line')
        break
    print(f'This car is {status}.')
    print('Shipping new car to customer!')
else:
    print('All cars bulit successfully. No faulty cars!')
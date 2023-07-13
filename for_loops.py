# friends = ['Rolf', 'Jen', 'Anne']

# for friend in friends: #mowie pytonowi aby dal mi nowa zmienna nazwana friend dla kazdego frienda. Friend bedzie pierwszym elementem w liscie friends a pozniej drugim i trzecim
#     print(friend)

elements = [0,1,2,3,4,5,6,7,8,9]
for index in elements: #powtorzymy ta petle 10 razy gdyz jest 10 numerow w liscie
    print('Hello world') #w pryzpadku podania stringa zostanie on powtorzony 10 razy

for index in range(10):
    print('Kamil sie uczy...')

for index in range(5, 10): #odliczy od 5 do 9(bez 10)
    print(index)

for index in range(2, 20 ,3): #da nam numery od 2 do 20 ze skokiem co trzy numery
    print(index)
#### ponizej jest lista studentow z ich wynikami
students = [ 
    {'name': 'Rolf', 'grade': 98},
    {'name': 'Bob', 'grade': 78},
    {'name': 'Jen', 'grade': 100},

]

for student in students:
    name = student['name']
    grade = student['grade']

    print(f'{name} has a grade of {grade}.')

#for loop uzywamy gdy chemy powtorzyc cos okreslona ilosc razy
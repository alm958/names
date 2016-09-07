def pname(arr):
    for i in range(len(arr)):
        print arr[i]['first_name'] + ' ' + arr[i]['last_name']


students = [
            {'first_name': 'Michael', 'last_name' : 'Jordan'},
            {'first_name': 'John', 'last_name' : 'Rosales'},
            {'first_name': 'Mark', 'last_name' : 'Guillen'},
            {'first_name': 'KB', 'last_name' : 'Tonel'},
]

pname(students);

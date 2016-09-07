users = {
 'students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Trey', 'last_name' : 'Villafane'}
  ]
 }


for k, v in users.items():
    print k
    for i in range(len(v)):
        print str(i+1) +' - ' + v[i]['first_name'] + ' ' + v[i]['last_name'] +' - '+str(len(v[i]['first_name'])+len(v[i]['last_name']))

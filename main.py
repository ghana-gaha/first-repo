



users = [
    {'name': 'ram', 'gender': 'male', 'status': True},
    {'name': 'gita', 'gender': 'female', 'status': True},
    {'name': 'sita', 'gender': 'female', 'status': False},
    {'name': 'hari', 'gender': 'male', 'status': False},
    {'name': 'laxmi', 'gender': 'male', 'status': True},
]


total_users=len(users)
male =0
active_male =0
inactive_male=0
female =0
active_female =0
inactive_female =0

for i in range (len(users)):
    if (users[i]['name']):
        if (users[i]['gender'])== "male" :   
            male +=1
            if (users[i]['status'])== True:
                active_male +=1
            elif (users[i]['status'])== False:  
                inactive_male +=1   
        elif (users[i]['gender'])== "female":
            female +=1
            if (users[i]['status'])== True:
                active_female +=1
            elif (users[i]['status'])== False:
                inactive_female +=1 

print("Total users :", total_users)
print("Total male users:", male)
print("Total female users:", female)
print("Total active male users:", active_male)
print("Total inactive male users:", inactive_male)
print("Total active female users:", active_female)  
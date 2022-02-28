import collections
from typing import Counter

#the menue heading
print('''
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
''')

#menue list of content
menu ={
    "Appetizer": ["Wings","cookies","Spring Rolls"],
    "Entrees": ["Salmon","steak","Meat Tornado","A Literal Garden"],
    "Desserts":["Ice Cream","Cake","Pie"],
    "Drinks":["Coffee","Tea","Unicorn Tears"]
}

#print menue list 
for k in menu.keys():
    print(f'''{k}
----------
    '''.format())

    print("\n".join(menu[k]),"\n")


print("***********************************")

order=input("**What would you like to order?** ")

print("***********************************")


order_list=[]
#to save the order of the user 
counter={}
#dictionary used with collecation to count the element repetion and save it 

def order_list_fun():

    '''
    order_list_function

    it take the input (order) from the user 

    print each time the order name with its name and the number of repetetion for it 
    also make a dictionary for the user order named counter 

    '''

    not_in_the_menue =False
    for k in menu.keys():
        for i in menu[k]:
            if order==i:
                order_list.append(order)
                counter=collections.Counter(order_list)
                # Call collections.Counter() on a list to return the number of occurrences of each element as a Counter object
                # print(counter) give me a dictionary of the order and the number of repetition for each item 
                print(f"{counter[order]} order of {order} have been added to your meal")
                not_in_the_menue =False
                break
            elif order=="quit":
                break
        else:
            not_in_the_menue=True
            #continue in the inner loop if no break happen
            continue
        #leave the outer loop when the break happen in the inner loop
        break 

    if not_in_the_menue:
        print("sorry,it's not in the menue maybe we will add it in future try somthing else ^-^")

order_list_fun()        
#call function for the first time to run it then i used while to make the condition 

# using while ==> like do while in js
while order!="quit":
    order=input() 
    order_list_fun()   

 

counter=dict(collections.Counter(order_list)) 
# to make it as dictionary i use dict()

# to print all order for the user 
print("\norder list:")
print("\nyour order ==> no of item\n")
for l in counter.keys():
    print(f'{l} ==> {counter[l]} item \n')
print("snakes cafe")



        
        







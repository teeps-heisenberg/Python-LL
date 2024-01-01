from LinkedList import LinkedList

my_new_linked_list = LinkedList(11)
my_new_linked_list.append(24)
my_new_linked_list.append(3)
my_new_linked_list.append(14)
my_new_linked_list.print_list()

#Pop
print('Pop Operation Performed:')
my_new_linked_list.pop()
my_new_linked_list.print_list()

#Prepend
print('Prepend Operation:')
my_new_linked_list.prepend(5)
my_new_linked_list.print_list()

#Pop First
print('Pop First Operation:')
my_new_linked_list.pop_first()
my_new_linked_list.print_list()

#Get by Index
print('Get By Index Operation:')
print(my_new_linked_list.get(2).value)

#Set Value by Index
print('Set Value By Index Operation:')
my_new_linked_list.set_value(2,33)
my_new_linked_list.print_list()

#Insert Value by Index
print('Insert Value By Index Operation:')
my_new_linked_list.insert(index=1,value=78)
my_new_linked_list.print_list()

#Remove Value by Index
print('Remove Value By Index Operation:')
my_new_linked_list.remove(2)
my_new_linked_list.print_list()

#Reverse Linked List
print('Reverse Operation:')
my_new_linked_list.reverse()
my_new_linked_list.print_list()
name=["Anik","Arun","Devu","Radhika","Smita","Varun","Arun"]
numb=[1,2,22,5,8,0,12]
numb.reverse() # reverse elements in list
print(numb)
numb2=numb.copy() # to copy list
print(numb2)
name.sort() # to sort in ascending order
print(name)
name.extend(numb) # to append two list
print(name)
name.append("Vidusi") # to append element in the list 
print(name)
name.insert(0,"Aaradhya") # to insert element in the list at particular position
print(name)
name.remove("Vidusi")
print(name) # to remove 
print(name.count("Arun")) # to count elements
name.pop()
print(name) # remove last 
print(name.index("Devu")) # gives index of element
name.clear()
print(name) #to remove all elements
#Create a tuple with 20 numbers. Write a python program to print another tuple whose values are even numbers from the first tuple  
tup=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
etup=[]
for x in tup:
  if(x%2==0):
    etup.append(x)
print(tuple(etup))
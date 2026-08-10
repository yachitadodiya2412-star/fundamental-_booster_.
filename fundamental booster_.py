print("="*30)
print("Welcome To Interactive personal Data collector!")
print("="*30)

name=input("please enter your name :")
age=int(input("please enter your age :"))
height=float(input("please enter your heighi in meters :"))
number=int(input("please enter your favouite number :")) 

print("="*30)
print("thank you! here is the information we collected")
print("="*30)

print("name:",name)
print("type",type(name))
print("memory address:",id(name))
print("age:",age)
print("type",type(age))
print("memory address:",id(age))
print("height:",height)
print("type",type(height))
print("memory address:",id(height))
print("number:",number)
print("type",type(number))
print("memory address:",id(number))

birth_year=2026-age
print("your birth year is approximately:",birth_year)

print("="*30)
print("thank you for using the personal Data collector.")
print("good bye!")
print("="*30)

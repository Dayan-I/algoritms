from random import randint, uniform, choice
a = int(input('Enter low limit:'))
b = int(input('Enter upper limit:'))
c = float(input('Enter upper limit:'))
d = float(input('Enter upper limit:'))
e = input('Enter low limit letter:')
f = input('Enter upper limit letter:')
print(randint(a,b))
print(uniform(c, d))

print(choice([chr(i) for i in range(ord(e), ord(f))]))







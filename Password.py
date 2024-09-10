#password
import random
password = int(input("Enter the desired password length: "))
low = 'abcdefghijklmnopqrstuvwxyz'
cap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '1234567890'
op = '!@#$%^&*(){}||?/><.'
all = low + cap + num + op
pas= ''.join(random.choice(all) for i in range(password))
print("Generated Password:", pas)

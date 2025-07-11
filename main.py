import random 
import string

total = string.ascii_letters + string.digits 

length = int(input("Enter the length of the password: "))

password = ''.join(random.sample(total, length))
print("Generated password:", password)
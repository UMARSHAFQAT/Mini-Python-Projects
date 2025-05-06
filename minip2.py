import random
import string

characters= string.ascii_letters+ string.punctuation+string.digits

password=int(input("Enter the amount of digits you need your password to be:"))

generated_password="".join(random.choice(characters) for i in range (password))

print("Your generated password is:",generated_password)
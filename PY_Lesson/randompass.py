import numbers
import random

lower = 'qwertyuiopasdfghjklzxcvbnm'
upper = 'QWERTYUIOPASDFGHJKLZXCVBNM'
numbers = '1234567890'

all = lower + upper + numbers

lenght = 8
for x in range(10):
    password = "".join(random.sample(all, lenght))
    print(password)
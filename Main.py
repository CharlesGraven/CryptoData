import sys
import Filter
import random

#ord('a')>>97
#chr(97) >> a

password = raw_input("Give me your password:")
passwordlen = len(password)
newpassword = [passwordlen]

def generate_filter_block(count):
    filter_block = []
    for i in range(0,count):
        rand = random.randint(1,2)  #get a random weight 
       
        fil = Filter.Filter(rand) #uses a random weight

        filter_block.append(fil)   #add the filter to the list
    return filter_block


filter_block_1 = generate_filter_block(passwordlen)

for i in range (0,passwordlen):
    var = ord(password[i])
    crypto = filter_block_1[i].compute(var)
    print(chr(crypto))
    newpassword.insert(i,crypto)
#-------------------------------------------
for i in range (0,passwordlen):
    var = newpassword[i]
    crypto = filter_block_1[i].reverse_compute(var)
    print(chr(crypto))

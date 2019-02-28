import hashlib
some_string = "ecsc"

hash1 = "c89aa2ffb9edcc6604005196b5f0e0e4" ##The hash before this hash is the answer looked for, saved as hash1

for i in range(100000):##Attempt 100000 times
    some_string = hashlib.md5(some_string.encode("utf-8")).hexdigest() ##convert into a hash
    if some_string == hash1: #if the hash = the hash we're testing weve found it
        print("number found: " + str(i)) # print the number
        num = i #num = the given number
        print("hash matches: " + str(some_string))#print both hashes to ensure theyre the same
        print("hash matches: " + str(hash1))#print both hashes to ensure theyre the same

        break#end

new_string = "ecsc" #declare a new string of the same thing
for x in range(num):#attempt the amount of times (num{i})
    new_string = hashlib.md5(new_string.encode("utf-8")).hexdigest()#hash it
    if x == num - 1:#we're looking for the hash just before this, so we do hash - 1 to get the first previous hash
        print("Number found: " + str(x))#print the number and print the new hash
        print("Hash before the one given: " + str(new_string)) #print the hash.

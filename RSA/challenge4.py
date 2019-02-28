## Commands to generate keys with openssl from commandline.. not part of this pythonj code.
## openssl genrsa -out mykey.pem
## openssl rsa -in mykey.pem -pubout > mykey.pub
## -------------------------------------------------------------------------

import binascii
from Crypto.PublicKey import RSA
from base64 import b64decode

def string2int(my_str):
    return int(binascii.hexlify(my_str), 16)

def int2string(my_int):
    return binascii.unhexlify(format(my_int, "x").encode("utf-8")).decode("utf-8")

public_key_filename = 'mykey2'
rsa = M2Crypto.RSA.load_pub_key(pk)

pem_key = b'MIIEogIBAAKCAQEAlVmF7X4kiOIn5VKe/TYXBzvg6guyUFQjCr5rNTN+AonEgO1kAVU76EY+8KhnQU81mO87+x1bqBGRmvM88xspXqjcif5AO9YEu7j4ssHuFk8yIr/gcGKwnzNF78oPST9UYxZi61dpIKcbh7dJNXd4fLSIu5OGfOKw0SuJ4qTgvcz+MdBUkYtlQdp5hnSIqpBPCKfd8kRAU4e+gR8vm4mhY5b8EiEvOaoUJC5KF/ykyfeFz3l4vWZcZn1R+MGNJ7bjDhhq1Dwaxew1hEPJGTj3gLzsifk4RYi8znCHGoNR0aK56st/NtWUYSvdbN7lULH26SgozR4FpRGgj06lbAXocQIDAQABAoIBAGn0pFZ0WrkeMY25SwB7gmTob028VJo2xtGVfHu291wXn2iUgpGLhb/pLjgQUYj9CBpjB5vFHUSkijdy/7e9emEkzam8zpdk4+DGfvJbMW10bC5JEJLLAWFAwAo5wRSHMHhH5o/uaK/4vkhPmUmsY7edYTAqnow1S5pqGB3KOYONOQf4IhwgqgsO368kEU6uqVCIeroXEb4Cb8vtqj45+s9FaxdbW+15fzcRyJU6EKZiewcNk1j3qVwcLmPnb3nVXgiKyfg8kkRXxrLrrY0MizMvc3IUFvr/BkvZNYtN/aKGv7MNAfkEoUf35QPz2rArThABG3VwwGzKEUE1ICQ63A0CgYEAxYxEM7z2PEi+3lN2tjKggBWxlh/RoP+yuwf5xEdunoxoDpeDU8op8k5sm1DYQcilhOJKwlXbC/V4bpkFE706ea0MuYVMV1CvWw1R2MNiD08tS2ej5k9QWw7B9rJe3rfc6cQemf4Wf2OU3DMVmXdX7hKZhTTbYKUsXntPYA16gtMCgYEAwYped4EA2Ed1Ti5+lndBEi0GCu8V3T9FlYtoLDQFYMElrPYV4r4tsABg1xTfMDtt+ige288chXWvZ798aQXxPlbkxgsuwpED3GHjX3giuQq+8yMYfWoX47ZbhVp+4q6JTofaEPSXGJPCOKIUwe92tVU4ltcFjnop80lD6t8K9SsCgYBJGYVnS8YmOpj+dg4Yj5VasCxdq/qLQ/MkSGhBHFmvq68ZrzE2gTmSYzjHJFxRw2iUSpR1YwXCYBwneNIrIruPqNxrjgrYyI+K9tvRhUM0/Qx6uagpojHO8CAQJKL8cTb6/cqBG0fB7dx4uyKD/mh4PUO3yf5fvd80Oxb9KR+rZwKBgBkudrIXz9NUINgmRoQvSgEiaIndp7ucsuINPGWb8yMunkdN0XUqB2nB8tepOIze/qUwuSsiXHSk5kiaaoaDpmrVBXkbFV9tXNI8zkeqquHmmwephlMzDZ6sKGZGawH1cZoNJPtVx58EAp45wHenP4vCZdWCbo+mJ3UnEDYsBRH3AoGAYu83TpvPqLP3T2ukzRHo+wC+vFhuxEuT8bA0M/MOyxDxuLyW+PmNSpnNY0CWHR0JHxLWnfyQcXp/KBmJf3JoWbblblufQkX6av9W6FyekgBYyv+1vrWf8+7Bj9JevlTWCoaiKFVYOsPcvRrqoXKg9OiCvChU6oxE9uuuXLD18TE='
key = b64decode(pem_key)
keyPriv = RSA.importKey(key)

#print(keyPriv.keydata)
modulusN = keyPriv.n
pubExpE = keyPriv.e
priExpD = keyPriv.d
primeP = keyPriv.p
primeQ = keyPriv.q

ciphertext = 474862643754336865489984490773307542016161159436213530034995807183836312346778617047666360854948178434525541089212091928949344492697684657497682106740050084305554758259427768463395264318566101255923490595579348647860471822284428834756812967844672795316325109976652375135659724572710513755433401072885408968307124213606768098411795080747616961236626790699862671834311406129266854138764009952421206625693567227556664511584573464971029270576495696636132292906861410359486612705079004947333371264698887189359265840678094723729950785568382017843975809503403984016678927664449791524785943376314787680072596720311587221852

decrypted = pow(ciphertext, priExpD, modulusN)   ## decrypt
plaintext = int2string(decrypted)
print (plaintext)





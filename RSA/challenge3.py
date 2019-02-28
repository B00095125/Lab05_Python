## Commands to generate keys with openssl from commandline.. not part of this pythonj code.
## openssl genrsa -out mykey.pem
## openssl rsa -in mykey.pem -pubout > mykey.pub
## -------------------------------------------------------------------------

## To run type python rsa.py from the commandline (assuming you've pythonh installed
import binascii
from Crypto.PublicKey import RSA

from base64 import b64decode

def string2int(my_str):
    return int(binascii.hexlify(my_str), 16)

def int2string(my_int):
    return binascii.unhexlify(format(my_int, "x").encode("utf-8")).decode("utf-8")

pem_key = b'MIIEpQIBAAKCAQEAzGm6Ogrmlf4OSPDQ5nUIiDAJeR9wHdhce7m3NprE3QQqggdrK/itQlqfRxqTP8uFDzuvLCHkiBIkWXiB9uYx4nVP+y5Db0p8cA453Xc2wvpYO8m/6n3VFkAQyzIs7vSr77KqVyPvRzSn9OAjn9FEg1Z7TEmcbkfTo39S1urTBaTTvffwULIaEu/QWcVFnwjPAtVd0vwbgvTMIq09jiBQ+yi/AM8bqfPPG+2XVODk40f4ppX5IRngjjyR+2mXaK95hcv/EHNOSXkHGfvaJfLSbMtCKvVcPiajEZkQirq9PD/9VN8iAz30PoA5ok5NURhY8veU+rTFoZG3YHk7N6fhjwIDAQABAoIBAQDKgdvKcM4rvnssa9ao2TzQnrZj1m9eQeCtejk10XJCe0QZeXwFHeGXoOu2p29Ffjyd8MUD9bfPzhlQwgAPN9InxYytDRIliSdqY82Tx+zqkNUktiR5DJwz5Ng+VcEKIj7LwrbaiXEdm97gy8S/KbS0YNLZqvtcja/vg83vuMfCB9mz72vetpGhXQ9zRR4w89XjfEaIG280vPL3dmZ2I2YqlXpc6AggybdJpuJ/SNXhhKmRE28SrG8/yvy+NJeykgW5RXuDnBLJD5KlNANxl6ly1HKYTN6S7tP0BQDToqIapYjcKdxAsoOvUYd6hrdmqGgDbvI4XIZ4AMfQIjHr8s4RAoGBAOVAAW2pPC/45qNHYXHJ/vVHZD0UxE0tvsc2sHS5AT44Seb3hPwQQnSvE8y+tS2XioTDq1mYHE719V2KHJ5aciWkhuDeNn4FdSvMnz+0NawDwMSTDXyDvDlAA7PsA+8V65tDFDcABQPvKz5GK4bYbTIDFrgfgbibYtOrfnT3UcILAoGBAORDztBCPks5h4dVIkw52AYp/mNSex9sQsmkUqeFNMoz/sEgUJf7uRjNHP6R3iFB32WvVrj3e1ddTG5cHSc1DBQ8UuAxZzz14VFLvhYUvG+rHAXyDzqhNvZVjuBR5ErMD6bJ1r7HQ0ydceV15femeoBXEcnIcZ1FXjKeGDxltnUNAoGALNPCM75G7Z5/Auh/Tm/QMggeuq7n36uVRYEVKg3PB2qcUNSPpXZMeGKPvZaA+QRL6sAULnXG+02vB/ZsuC45adDtKuVoxGWuzry5WwyS/irRs96JYZKk6JDy6Gi7MDIaGwcX2dVgJa/LxeaUtk51s7TU6XYHuKBxx7AeDyMZUpcCgYEAvWF4o5ZiIn0vcVtzojRXgv2yPes/lVl3q932aV/95UjwMoDB/OZusiHyzU5uMb96Pd4UIE/LeDdC40jvMwky5VMLG1BBq/T/pDgoFB/OGwOms1QZyHXaqNNhP8ERm/Djh2hsD0o5DsaNqWeAjVAE0JfsfTIc+POFbI934hwtHb0CgYEAu0xdmmVf3uE0vrDoNA4cHSoPzupdFAXDv2G7NofJcOaNT9k6Zeut751jCN/bGlYmM3a0l/qBKmW/D/YP0NaLk3u1g5l8f3Rh+QwC3fCHcVAF/7ZFQJ5XhD90uXyXvv6qZFlD8Gq58vCmvg5HYyKnVIEhy25mDXrRyYVgnKEm9Ew='
key = b64decode(pem_key)
keyPriv = RSA.importKey(key)

#print(keyPriv.keydata)
modulusN = keyPriv.n
pubExpE = keyPriv.e
priExpD = keyPriv.d
primeP = keyPriv.p
primeQ = keyPriv.q
print(modulusN)
print(pubExpE)
print(priExpD)





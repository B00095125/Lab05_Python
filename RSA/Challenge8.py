#Challenge 8#
#This challenge is solveable if e is a very low number#
#No encryption occurs if M^e < n.#
#Therefore, the cube root of n = c

import decimal
import binascii

def int2string(my_int):
    return binascii.unhexlify(format(my_int, "x").encode("utf-8")).decode("utf-8")

n= 23516695565660963250242846975094031309572348962900032827958534374248114661507001374384417953124930587796472484525315334716723068326965228898857733318407681656604325744994115789416012096318656034667361976251100005599211469354510367804546831680730445574797161330145320706346512982316782618118878428893337849886890813813050423818145497040676697510093220374542784895778086554812954376689653727580227087363619223145837820593375994747273662064715654881379557354513619477314410917942381406981452545764657853425675230343749326640073923166795823683203941972393206970228647854927797483660176460658959810390117898333516129469397
e= 3
ciphertext = 145069245024457407970388457302568525045688441508350620445553303097210529802020156842534271527464635050860748816803790910853366771838992303776518246009397475087259557220229739272919078824096942593663260736405547321937692016524108920147672998393440513476061602816076372323775207700936797148289812069641665092971298180210327453380160362030493

#Find cubed root of large number in python#
#function sourced from: https://stackoverflow.com/questions/52313392/compute-cube-root-of-extremely-big-number-in-python3#
decimal.getcontext().prec = 2000
d = decimal.Decimal(ciphertext)
x = d ** (decimal.Decimal('1') / 3)

y = int(x + 1) #Add one because of rounding. If one is not added last letter of key is missing
plaintext = int2string(y)
print (plaintext)
print(y)




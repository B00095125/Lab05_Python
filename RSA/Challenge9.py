#Challenge 9#
#Same logic used to solve this as last program just with minor changes#
# Gauss's algorithm  used#

#logic for this solution sourced from: https://www.di-mgt.com.au/crt.html?fbclid=IwAR2fNqFHj06r7AoZOY2sxCF-t77VpcDxfknzDpsuo8egG-9PCLwoKhTUmm0
import decimal
from decimal import Decimal

import binascii

def int2string(my_int):
    return binascii.unhexlify(format(my_int, "x").encode("utf-8")).decode("utf-8")

e1 = 3
n1 = 1001191535967882284769094654562963158339094991366537360172618359025855097846977704928598237040115495676223744383629803332394884046043603063054821999994629411352862317941517957323746992871914047324555019615398720677218748535278252779545622933662625193622517947605928420931496443792865516592262228294965047903627
c1 = 613757444204638278262310351562876531607487738717774407185252131147104492450160428757483976067628603514761619532764928239807564974590961450735755461481051283186240767490110455431475543041011912015289781128865893349142785039408178696523937605624371679605130950843591197358935516266254687080122972023592091964871


e2 = 3
n2 = 405864605704280029572517043538873770190562953923346989456102827133294619540434679181357855400199671537151039095796094162418263148474324455458511633891792967156338297585653540910958574924436510557629146762715107527852413979916669819333765187674010542434580990241759130158992365304284892615408513239024879592309
c2 = 22657108022478695797486965023447848250682406595690518779077232421899889165762724488153241456845951937121308084431913683848889272505486222688188138471999687468256556616878979818168438370975399291696045396880071048188564812795530986969364538462949239012254381251606438993964309325106863727351705595563360310007


e3 = 3
n3 = 1204664380009414697639782865058772653140636684336678901863196025928054706723976869222235722439176825580211657044153004521482757717615318907205106770256270292154250168657084197056536811063984234635803887040926920542363612936352393496049379544437329226857538524494283148837536712608224655107228808472106636903723
c3 = 311096000497881387953904724284440481805457233048982756757007020410000443330941053703716829538086459727079448020579354693958905904778381820371160626001594619419169121166486655254993091181369105737797409452734836563374374511516011594235202125201067840325349354834604004321427713901643355933701994777952169157646

#Perform modInverse of 2 numbers
def modInverse(a, m) :
    m0 = m
    y = 0
    x = 1

    if (m == 1) :
        return 0

    while (a > 1) :

        # q is quotient
        q = a // m

        t = m

        # m is remainder now, process
        # same as Euclid's algo
        m = a % m
        a = t
        t = y

        # Update x and y
        y = x - q * y
        x = t

    # Make x positive
    if (x < 0) :
        x = x + m0

    return x


#mcubed by multiplying it by itself 3 times
mCubed = c1*c1*c1
#nmultiplied is the multiplication of 3 n values
nMultiplied = n1*n2*n3

#multiply n2 by n3
#mod inverse the number with n1
#gives us d1
test1 = n2*n3
d1 = modInverse(test1, n1)
print(d1)

#multiply n1 by n3
#mod inverse the number with n2
#gives us d2
test2 = n1*n3
d2 = modInverse(test2, n2)
print(d2)

#multiply n1 by n2
#mod inverse the number with n3
#gives us d3
test3 = n1*n2
d3 = modInverse(test3, n3)
print(d3)

#multiply each num with other nums
nu1 = n2*n3
nu2 = n1*n3
nu3 = n1*n2


x = c1*nu1*d1 + c2*nu2*d2 + c3*nu3*d3%nMultiplied
print("###")
print(x)

#tut is the x value mod the multiple of the three n values
tut = x%nMultiplied

#After this, the same logic as challenge 8 can be used in order to find the cipher

#Find cubed root of large number in python#
#function sourced from: https://stackoverflow.com/questions/52313392/compute-cube-root-of-extremely-big-number-in-python3#
decimal.getcontext().prec = 2000
d = decimal.Decimal(tut)
xyz = d ** (decimal.Decimal('1') / 3)
y = int(xyz + 1)#Add one because of rounding. If one is not added last letter of key is missing
print(y)

#convert to string
plaintext = int2string(y)
print (plaintext)


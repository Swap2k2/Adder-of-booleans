
entry_number= "2021tt11156"
last_two_digits=56
rem=(last_two_digits%4)
print("The remainder comes out to be ",rem)


##Q1)
#
def hadd(a, b):
    # defined half adder function
    #
    # Parameters:
    # a---> boolean , first input
    # b---> boolean , second input
    #
    # Returns: boolean (sum of a and b , carry of the sum)
    return ((a or b) and not (a and b), a and b)

def fadd(a, b, c):
    # defined full adder 
    # 
    # a---> boolean , first input
    # b---> boolean , second input
    # c---> boolean , third input
    #
    # Returns: Boolean sum of a,b,c as a tupple
    sum1, cout1 =  hadd(a, b)
    sum2, cout2 = hadd(c, sum1)
    cfinal  = cout1 or cout2
    return (sum2, cfinal)
# print(fadd(True,True,True))


##Q2)
#
def add4(a0, a1, a2, a3, b0, b1, b2, b3, c):
    # 𝑎3𝑎2𝑎1𝑎0 and 𝑏3𝑏2𝑏1𝑏0
    #  𝑎3𝑎2𝑎1𝑎0 + 𝑏3𝑏2𝑏1𝑏0 + 𝑐.
    #
    # defined function to implement 4 bit adders using the above defined full adder fuction fadd(a,b,c)
    #  
    # Parameters:
    # a0,a1,a2,a3,b0,b1,b2,b3,c ----> booleans, the inputs in boolean to find the adders 
    #
    # Returns: returns a tupple containing the sum of the booleans input in  boolean values 
    f0, c0 = fadd (a0, b0, c)
    f1, c1 = fadd (a1, b1, c0)
    f2, c2 = fadd (a2, b2, c1)
    f3, c3 = fadd (a3, b3, c2)
    return (f0, f1, f2, f3, c3)
# print(add4(True,True,False,False, False,False,False,False, True))


##Q3)
#
def cmp(a0, a1, a2, a3, b0, b1, b2, b3):
    #The last two digits of entry number 56 which leaves remainder 0 when divided by 4 
    # # case0---->  <
    # defined a function cmp to compare two 4 bit numerals
    #
    # a0,a1,a2,a3,b0,b1,b2,b3----> booleans
    #the numerals  will be written as a3a2a1a0 and b3b2b1b0
       
        # for last bit
    if (b3 == True and a3 == False):
        return True
    elif (b3 == False and a3 == True):
        return False

        # compare third bit
    if (b2 == True and a2 == False):
        return True
    elif (b2 == False and a2 == True):
        return False
        # compare second bit
    if (b1 == True and a1 == False):
        return True
    elif (b1 == False and a1 == True):
        return False
        # compare first bit

    if (b0 == True and a0 == False):
        return True
    elif (b0 == False and a0 == True):
        return False
    print("here")
# print(cmp(True,False,False,False,False,False,False,False))


##Q4)
#
def complement(b0, b1, b2, b3):
    # Defined complement to get the complement of the inputs  
    # 
    # Parameters: b0,b1,b2,b3----> boolean inputs
    
    b1 = not b1
    b0 = not b0
    b2 = not b2
    b3 = not b3
    return add4(b0, b1, b2, b3, True, False, False, False, False)

 
def sub4(a0, a1, a2, a3, b0, b1, b2, b3):
    # subtract two 4 bit numerals with inputs and returns in booleans 
    #
    # Parameters:
    # b0,b1,b2,b3,a0,a1,a2,a3 are booleans
    #
    # Returns (a3a2a1a0-b3b2b1b0)
    m0, m1, m2, m3, TwoComp = complement(b0, b1, b2, b3)
    
    r0, r1, r2, r3, cAdd = add4(m0, m1, m2, m3, a0, a1, a2, a3, False)
    # print((  r0,r1,r2,r3,cAdd))
    if(cAdd == True):
        return (r0, r1, r2, r3, False)
    else:
        z0, z1, z2, z3, cz = complement(r0, r1, r2, r3) 
        return (z0, z1, z2, z3, True)
# print( sub4(True,False,True,False, True,False,False,True))


### Part 2
#
#
def add8(a ,b ,c):
    # defined function add8 to implement 8bit adder
    #
    # Parameters:
    # a---> tupple of 8 inputs , inputs are boolean  
    # b---> tupple of 8 inputs , inputs are boolean 
    # c---> boolean input 
    #  
    # Returns the sum of booleans a,b,c
    #  
    (a0, a1, a2, a3, a4, a5, a6, a7) = a
    (b0, b1, b2, b3, b4, b5, b6, b7) = b
    x0, x1, x2, x3, carry1 = add4(a0, a1, a2, a3, b0, b1, b2, b3, c)
    # print((x0,x1,x2,x3,x1))

    x4, x5, x6, x7, cout = add4(a4, a5, a6, a7, b4, b5, b6, b7, carry1)
    # print((x4,x5,x6,x7))
    # print((x0,x1,x2,x3,x4,x5,x6,x7,carry2))
    x = (x0, x1, x2, x3, x4, x5, x6, x7) 
    return (x ,cout)
# print( add8((True,True,True,True,True,True,False,False),  (True,False,False,False,False,False,False,False), False))


##Q6)
# 
def mul4(a, b):
    # defined  mul4 function to multiply two binary numbers present in tupples a and b 
    #
    # Parameters: a and b are tupples and inputs of the tupple are booleans true and false 
    #
    #a1,a2,a3,a4,b1,b2,b3,b4 are inputs of a and b in boolean expression true and false
    #
    #a,b tupples contain four inputs 
    (a1, a2, a3, a4) = a
    (b1, b2, b3, b4) = b
    
    a_new = (a1, a2, a3, a4, False, False, False, False)
    res = (False, False, False, False, False, False, False, False)
    
    if(b1 == False and b2 == False and b3 == False and b4 == False):
        return res

    else:
        r, c1 = add8(a_new, res, False)
        q1, q2, q3, q4 ,_ = sub4(b1, b2, b3, b4, True, False, False, False)
        q = (q1, q2, q3, q4)
        s, z = add8(r, mul4(a,q), c1)
        return s
# print(mul4((True, False, False, False), (False, False, False, True)))
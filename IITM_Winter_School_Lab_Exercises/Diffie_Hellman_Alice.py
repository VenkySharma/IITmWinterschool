
from helper import *
import random

#-----------------------------------------------------------------------------
#--------------------------------Client Setup---------------------------------

def Alice(logging = False):
    c = socket_setup(client = True)
    #----------------------------------------------------------------
    #--------------------Client Server Interaction-------------------
    def interaction(logging = False): 
        group_sz = int(c.recv(1024).decode())
        if(logging):
            print("PUBLIC: Group Size Established to be ", group_sz)
            print("PUBLIC: Generator g = 2")
        #------------------------------
        # a is the private key of Alice
        a = random.SystemRandom().randint(1, group_sz - 1)
        
        # EXERCISE: Find g^a and uncomment the following lines
        g_a = pow(2, a, group_sz)
        if(logging):
            print("PUBLIC: Sending g^a = ", g_a)
        c.send(f"{g_a}".encode())
        #------------------------------
        g_b = int(c.recv(1024).decode())
        if(logging):
            print("PUBLIC: Received g^b = ", g_b)
        #------------------------------
        # EXERCISE: Find g^ab and uncomment the following lines
        g_ab = pow(g_b,a,group_sz)
        if(logging):
            print("PRIVATE: Constructed g^ab = ", g_ab)
            print("---Key Exchange Complete---")
        
        tuple_str = f"{a},{g_a},{g_ab}"
        c.send(tuple_str.encode())
        #------------------------------ 
        return a, g_a, g_ab
        
    return interaction(logging)

#----------------------------------------------------------------
Alice(logging = True)

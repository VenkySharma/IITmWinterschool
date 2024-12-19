from helper import *
import random


#----------------------------------------------------------------
#--------------------Server Setup--------------------------------
def Bob(logging = False):
    s = socket_setup()
    # EXERCISE: Find a large prime for the group size
    # group_sz = {insert_large_prime}
    #----------------------------------------------------------------
    #--------------------Client Server Interaction-------------------
    def interaction(logging = False):
        c, addr = s.accept()
        group_sz = gen_large_prime(128)
        if(logging):
            print("PUBLIC: Connection Established. Establishing Group Size.")
	# Uncomment after finding group_sz
        c.send(f"{group_sz}".encode())
        
        if(logging):
            print("PUBLIC: Group Size Established to be ", group_sz)
            print("PUBLIC: Generator g = 2")
        #------------------------------
        #EXERCISE: Write the missing code, import necessary functions from helper.py
        g_a = int(c.recv(1024).decode())
        b = random.SystemRandom().randint(1, group_sz - 1)
        g_b = pow(2,b,group_sz)
        c.send(f"{g_b}".encode())
        g_ab = pow(g_a,b, group_sz)
	#------------------------------
        if(logging):
            print("---Key Exchange Complete---")
        s.close()
        return b, g_b, g_ab
    return interaction(logging)
#----------------------------------------------------------------
Bob(logging = True)

# EXERCISE: Add an extra interaction to establish generator g instead of fixing it as 2

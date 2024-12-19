from helper import *
from hashlib import sha256

bit_length = 128
m = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Signed by Alice"

def Alice_Hash_Sign(m, logging = False):
    c = socket_setup(client = True)
    #-------------------------------
    # EXERCISE: Generate public private key pair of RSA. Copy answer from previous exercise.
    # p = 
    # q = 
    # n = 
    # e = 
    # d = 
    #-------------------------------
    # Split message into blocks of 16 characters
    # EXERCISE: Break message into blocks of 16 characters
    # blocks =   
    print("Message: ", m)
    #----------------------------------------------------------------
    #--------------------Client Server Interaction-------------------
    def interaction(logging = False): 
        bob_pub_key_str = c.recv(1024).decode()
        n_, e_ = map(int, bob_pub_key_str.split(","))
        if(logging):
            print("Bob's Public Key Received: ", bob_pub_key_str)
        #--------------------------------
        # Uncomment the below after getting private and public keys
        # c.send(f"{n}, {e}".encode())
        # if(logging):
        #     print("Alice's Public Key Sent: ", f"{n}, {e}")
        #--------------------------------
        # EXERCISE: Encrypt each block and send
        # for m_ in blocks:
        #        Do something
        #------------------------------
        
        # Send -1 to indicate end of blocks
        c.send(f"-1,".encode())
        #--------------------------------
        # Find hash value of full message
        # sign and send it
        sha256().update(str(m).encode())
        hash_m = int(sha256().hexdigest(), 16)
        #--------------------------------
        # EXERCISE: Compute signature and send it
        # signature = 
        # c.send(something)
        #--------------------------------
    interaction(logging)
    #----------------------------------------------------------------
Alice_Hash_Sign(m, logging = False)
from helper import *

bit_length = 128

def Bob(logging = False):
    s = socket_setup()
    #-------------------------------
    # EXERCISE: Generate public private key pair of RSA
    p = gen_large_prime(128)
    q = gen_large_prime(128)
    n = p*q
    e = random.SystemRandom().randint(1, n - 1)
    d = mod_inverse(e,(p-1)*(q-1))
    #-------------------------------
    # Uncomment when above code is complete
    def interaction(logging = False):
        c, addr = s.accept()
        pubkey_str = f"{n}, {e}"
        if(logging):
            print("Connection established. Sending public key: ", pubkey_str)
        c.send(pubkey_str.encode())
        cipher_text = int(c.recv(1024).decode())
        if(logging):
            print("Received cipher text: ", cipher_text)
        dec_m = mod_exp(cipher_text, d, n)
        return decode_message(dec_m)
    #-------------------------------    
    m = interaction(logging)
    print("Decrypted message: ", m)
#----------------------------------------------------------------
Bob(logging = True)

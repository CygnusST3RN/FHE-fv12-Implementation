from BFV_Scheme.bfv import Params,FV12,CipherText
import random
import time

params = Params(2**4, 2, 2**21, 2**63)
fv12 = FV12(params)
public_key, private_key = fv12.generate_keys()
x=random.randint(-1000,1000)

start = time.perf_counter()
y=public_key.encrypt(x)
z=private_key.decrypt(y)
end=time.perf_counter()

print("Plaintext: ",x)
print("Ciphertext: ",y)

if(x==z):
    print("Passed")
    print("Plaintext after decoding: ",z)
else:
    print("Failed")
    
ms = (end-start) * 10**6
print(f"Elapsed {ms:.03f} micro secs.")



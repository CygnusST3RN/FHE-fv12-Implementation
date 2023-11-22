from BFV_Scheme.bfv import Params,FV12,CipherText
import random
import time

params = Params(2**3, 2, 2**21, 2**63)
fv12 = FV12(params)
public_key, private_key = fv12.generate_keys()
x=random.randint(-1000,1000)

start = time.perf_counter()
y=public_key.encrypt(x)
end=time.perf_counter()
start1=time.perf_counter()
z=private_key.decrypt(y)
end1=time.perf_counter()

print("Plaintext: ",x)
print("Ciphertext: ",y)

if(x==z):
    print("Passed")
    print("Plaintext after decoding: ",z)
else:
    print("Failed")
    
ms = (end-start) * 10**6
print(f"Encryption time {ms:.03f} micro secs.")

ms1 = (end1-start1) * 10**6
print(f"Decryption time {ms1:.03f} micro secs.")



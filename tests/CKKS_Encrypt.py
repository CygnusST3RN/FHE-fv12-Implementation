from utils.plaintext import Plaintext
from utils.poly import Polynomial
from CKKS_Scheme.ckks_encoder import CKKSEncoder
import numpy as np
from CKKS_Scheme.ckks import Params,CKKS
import random
import time


def encode_value(a,scale):#takes a number and returns encoded plaintext
    encoder=CKKSEncoder(16,scale)
    a_encoded=encoder.encode(np.array([a]*4))
    a_encoded=Polynomial(a_encoded.coef)
    a_encoded.poly_floor()
    a_pt=Plaintext(a_encoded,scale)
    return a_pt


def decode_poly(a_pt):#takes an encoded plaintext and returns integer.
    pt=np.polynomial.Polynomial(a_pt.poly.convert_to_list())
    encoder=CKKSEncoder(16,a_pt.scale)
    pt=encoder.decode(pt)
    return pt[0].real


scale=1<<20
encoder=CKKSEncoder(16,scale)
params = Params(8,  1<<600,1<<1200)
ckks= CKKS(params)
public_key,private_key=ckks.generate_keys()

a=random.randint(-10,10)
start = time.perf_counter()
a_pt=encode_value(a,scale)
a_encrypted=public_key.encrypt(a_pt)
a_decrypted=private_key.decrypt(a_encrypted)
a_decoded=decode_poly(a_decrypted)
end=time.perf_counter()

print("Plaintext ",a)
print("Encrypted value ",a_encrypted)
print("Decoded value ", a_decoded)

if(a - 1 <= a_decoded <= a + 1):
    print("Passed")
else:
    print("Failed")

ms = (end-start) * 10**6
print(f"Elapsed {ms:.03f} micro secs.")
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
b=random.randint(-10,10)

a_pt=encode_value(a,scale)
a_encrypted=public_key.encrypt(a_pt)
b_pt=encode_value(b,scale)
b_encrypted=public_key.encrypt(b_pt)

start = time.perf_counter()
sum=a_encrypted+b_encrypted
sum_res=private_key.decrypt(sum)
sum_res_final=decode_poly(sum_res)
end=time.perf_counter()

start1=time.perf_counter()
sub=a_encrypted-b_encrypted
sub_res=private_key.decrypt(sub)
sub_res_final=decode_poly(sub_res)
end1=time.perf_counter()

start2=time.perf_counter()
mul=a_encrypted*b_encrypted
mul_res=private_key.decrypt(mul)
mul_res_final=decode_poly(mul_res)
end2=time.perf_counter()

print("The two numbers are: ",a,b)

if(a+b-1 <= sum_res_final <= a+b+1):
    print("Addition passed")
    print(sum_res_final)
else:
    print("Addition failed")
if(a-b-1 <= sub_res_final <= a-b+1):
    print("Subtraction passed")
    print(sub_res_final)
else:
    print("Subtraction failed")
if(a*b-1 <= mul_res_final <= a*b+1):
    print("Multiplication passed")
    print(mul_res_final)
else:
    print("Multiplication failed")
    
ms = (end-start) * 10**6
print(f"Time for addition {ms:.03f} micro secs.")

ms1 = (end1-start1) * 10**6
print(f"Time for subtraction {ms1:.03f} micro secs.")

ms2 = (end2-start2) * 10**6
print(f"Time for multiplication {ms2:.03f} micro secs.")

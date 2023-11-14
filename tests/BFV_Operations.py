from BFV_Scheme.bfv import Params,FV12,CipherText
import random
import time

params = Params(2**4, 2, 2**21, 2**63)
fv12 = FV12(params)
public_key, private_key = fv12.generate_keys()
a=random.randint(-10,10)
b=random.randint(-10,10)
start = time.perf_counter()
x=public_key.encrypt(a)
y=public_key.encrypt(b)
sum_ans=private_key.decrypt(x+y)
sub_ans=private_key.decrypt(x-y)
mul_ans=private_key.decrypt(x*y)
end=time.perf_counter()
print("The two numbers are: ",a,b)
if(sum_ans==a+b):
    print("Addition passed")
    print(sum_ans)
else:
    print("Addition failed")
if(sub_ans==a-b):
    print("Subtraction passed")
    print(sub_ans)
else:
    print("Subtraction failed")
if(mul_ans==a*b):
    print("Multiplication passed")
    print(mul_ans)
else:
    print("Multiplication failed")
    
end = time.perf_counter()
ms = (end-start) * 10**6
print(f"Elapsed {ms:.03f} micro secs.")



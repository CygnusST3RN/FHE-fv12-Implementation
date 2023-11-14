from BFV_Scheme.bfv import Params,FV12,CipherText
import random
import time

params = Params(2**4, 2, 2**21, 2**63)
fv12 = FV12(params)
public_key, private_key = fv12.generate_keys()
a=random.randint(-10,10)
b=random.randint(-10,10)
x=public_key.encrypt(a)
y=public_key.encrypt(b)
start = time.perf_counter()
sum_ans=private_key.decrypt(x+y)
end=time.perf_counter()
start1=time.perf_counter()
sub_ans=private_key.decrypt(x-y)
end1=time.perf_counter()
start2=time.perf_counter()
mul_ans=private_key.decrypt(x*y)
end2=time.perf_counter()
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
    
ms = (end-start) * 10**6
print(f"Time for addition {ms:.03f} micro secs.")

ms1 = (end1-start1) * 10**6
print(f"Time for subtraction {ms1:.03f} micro secs.")

ms2 = (end2-start2) * 10**6
print(f"Time for multiplication {ms2:.03f} micro secs.")




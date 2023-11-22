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

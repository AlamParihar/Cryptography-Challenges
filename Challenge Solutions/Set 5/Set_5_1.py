import os
import random

def DH_test():
    p=0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff
    g=2
    a=random.randint(0,p)
    b=random.randint(0,p)
    A=pow(g, a, p)
    B=pow(g, b, p)
    AA=pow(B, a, p)
    BB=pow(A, b, p)
    print(A)
    print(B)
    print(AA)
    print(BB)

def modexp(base, exp, mod):

    if(base==0):
        return 0
    if(exp==0):
        return 1

    if(exp%2==0):
        out=modexp(base, (exp/2), mod)

    else:
        out=base%mod
        out=(out*modexp(base, (exp-1), mod))%mod
    return (out+mod)%mod


DH_test()
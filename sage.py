print(factor(793479390729215512516507951283169066088130679960393952059283337873017453583023682367384822284289))

r = int("73eda753299d7d483339d80809a1d80553bda402fffe5bfeffffffff00000001", 16)
f = 3 * 11**2 * 10177**2 * 859267**2 * 52437899**2 * r + 1
q = int("1A0111EA397FE69A4B1BA7B6434BACD764774B84F38512BF6730D2A0F6B0F6241EABFFFEB153FFFFB9FEFFFFFFFFAAAB", 16)
F = GF(q)
#Fp2.<u> = F.extension(q^2 + 1)
K2.<x> = PolynomialRing(F)
F2.<u> = F.extension(x^2+1)
G2 = EllipticCurve(F2, [0, 4+u*4])
print(factor(f-1))
factor(G2.order() // r)
factors = [13, 13, 23, 23, 2713, 11953, 262069, r, 402096035359507321594726366720466575392706800671181159425656785868777272553337714697862511267018014931937703598282857976535744623203249]
print(factors)


from itertools import chain, combinations
from functools import reduce

def powerset(iterable):
    "list(powerset([1,2,3])) --> [(), (1,), (2,), (3,), (1,2), (1,3), (2,3), (1,2,3)]"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1))


divs = []
for p in powerset(factors):
    divs.append(reduce(lambda x,y : x*y, p))
print(list(map(str, sorted(set(divs)))))


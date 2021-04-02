# Probability

## Permutations (permutação)
Arranging all elements within then sample space
P(n) = n!

## Variation with repetitions
set = a, b, c, d, e, f
Can use 3 at same time

a, b, c
a, c, b
a, b, d
etc ...

n = 6
p = 3

V(n,p) = 6!/(6-3)!
       = 6!/3!
       = 6 * 5 * 4
       = 120

V(10,3) = 10!/(10-3)!
        = 10!/7!
        = 10 * 9 * 8 = 720

V(n,p) = n!/(n-p)!

### Example
You need take only 3 persons from a set of 5 competitors to make a podium (Primeiro, segundo e terceiro).
V(5,3) = 5!/(5-3)! = 5!/2! = 5 * 4 * 3 * 2 * 1 / 3 * 2 * 1 = 5 * 4 = 20 

## Combination
The order in which we pick them is not relevant

set = (a, b, c, d, e)
a, b, c
a, c, b
b, a, c
b, c, a
c, a, b
c, b, a
Any of the 6 permutations is a different variation, but NOT a different combination

C(n,p) = V(n,p)/P(p)
C(n,p) = n! / p! * (n-p)!
C(10,3) = 10! / 3! * (10-3)!
        = 10! / 3! * 7!
        = (10 * 9 * 8) / (3 * 2)
        = 10 * 3 * 4
        = 120

## Symmetry of combinations
C(n,p) = C(n,n-p)

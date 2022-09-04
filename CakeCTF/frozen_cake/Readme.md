
### I do not understand this solution

I struggled at this one for a basically a whole day.
I tried to understand the math behind this.
But the solution just kind of upsets me when I looked it up.

```
m = inverse(c * inverse(a*b, n) % n, n)
```

What is infuriating is that there is no reasoning for this.
I don't understand what cryptodomes inverse function really 
does even after reading and going through it.

```
def inverse(u, v):
    """The inverse of :data:`u` *mod* :data:`v`."""

    u3, v3 = u, v
    u1, v1 = 1, 0
    while v3 > 0:
        q = u3 // v3
        u1, v1 = v1, u1 - v1*q
        u3, v3 = v3, u3 - v3*q
    while u1<0:
        u1 = u1 + v
    return u1
```

And they don't have documentation to what an inverse mod is or what the purpose of this function is. 
It is essentially my euclidian function for a CS class in college.
Except it keeps track of how many divisions occur and does some funky math with that.


I don't get the what this inverse does and would love for
someone to explain it. Then, I could probably understand the solution. 

a = pow(m, p) % n
b = pow(m, q) % n
c = pow(m, n) % n





# Big Bang Challenge 

## What I Did 

I started by running the command given for the CTF:
```
nc rev.chal.csaw.io 5004
```

We get an out like this:
```
Welcome to the Big Bang challenge!
Enjoy this random bits : 0111000001101000110001111011111101100101101110010110101000001000010001110
```
I don't know what to enter but it gives you some joke from the Big Bang Theory. 
This is clearly a failed input.


So now I look into the code the CTF gives me that is running on the server.
I find a few interesting code snippets. 


### Keys and Magic Number 
```
MAGIC = ?
K1 = b'\xae@\xb9\x1e\xb5\x98\x97\x81!d\x90\xed\xa9\x0bm~G\x92{y\xcd\x89\x9e\xec2\xb8\x1d\x13OB\x84\xbf\xfaI\xe1o~\x8f\xe40g!%Ri\xda\xd14J\x8aV\xc2x\x1dg\x07K\x1d\xcf\x86{Q\xaa\x00qW\xbb\xe0\xd7\xd8\x9b\x05\x88'
K2 = b"Q\xbfF\xe1Jgh~\xde\x9bo\x12V\xf4\x92\x81\xb8m\x84\x862va\x13\xcdG\xe2\xec\xb0\xbd{@\x05\xb6\x1e\x90\x81p\x1b\xcf\x98\xde\xda\xad\x96%.\xcb\xb5u\xa9=\x87\xe2\x98\xf8\xb4\xe20y\x84\xaeU\xff\x8e\xa8D\x1f('d\xfaw"
K3 = b"\xc6j\x0b_\x8e\xa1\xee7\x9d8M\xf9\xa2=])WI]'x)w\xc1\xc4-\xab\x06\xff\xbd\x1fi\xdb t\xe1\x9d\x14\x15\x8f\xb3\x03l\xe8\ru\xebm!\xc9\xcbX\n\xf8\x98m\x00\x996\x17\x1a\x04j\xb1&~\xa1\x8d.\xaa\xc7\xa6\x82"
K4 = b'9\x95\xf4\xa0q^\x11\xc8b\xc7\xb2\x06]\xc2\xa2\xd6\xa8\xb6\xa2\xd8\x87\xd6\x88>;\xd2T\xf9\x00B\xe0\x96$\xdf\x8b\x1eb\xeb\xeapL\xfc\x93\x17\xf2\x8a\x14\x92\xde64\xa7\xf5\x07g\x92\xfff\xc9\xe8\xe5\xfb\x95N\xd9\x81^r\xd1U8Y}'
K5 = b"9\xf8\xd2\x1a\x8d\xa14\xb9X\xccC\xe8\xf5X\x05l:\x8a\xf7\x00\xc4\xeb\x8f.\xb6\xa2\xfb\x9a\xbc?\x8f\x06\xe1\xdbY\xc2\xb2\xc1\x91p%y\xb7\xae/\xcf\x1e\x99r\xcc&$\xf3\x84\x155\x1fu.\xb3\x89\xdc\xbb\xb8\x1f\xfbN'\xe3\x90P\xf1k"
K6 = b'\xc6\x07-\xe5r^\xcbF\xa73\xbc\x17\n\xa7\xfa\x93\xc5u\x08\xff;\x14p\xd1I]\x04eC\xc0p\xf9\x1e$\xa6=M>n\x8f\xda\x86HQ\xd00\xe1f\x8d3\xd9\xdb\x0c{\xea\xca\xe0\x8a\xd1Lv#DG\xe0\x04\xb1\xd8\x1co\xaf\x0e\x94'
```
First off, I am not given the value of the MAGIC number, but this lets me know that I need to figure this value out somehow.
The other keys that I am given are incomprehensible to just look at but have value later in the main function.


### Main Code
```
def main():

	print("Welcome to the Big Bang challenge!")

	iv_a, iv_b = gen_iv()
	keys = gen_keys()
	inp = my_input()
	
	output =  b"\x00"*MAGIC			
	for i in range(MAGIC):
		output = foo(output, foo(keys[i], foo(inp[i], iv_b[i], K5, K6), K3, K4), K1, K2)
		if not guardian(output, i, keys):
			print("Bazinga! You just fell to one of my classic pranks")
			exit(0)
	print(f"Congratulations, you are smarter than Sheldon!\nHere is your flag:\n{output}")
```
I like to follow the code in a linear fashion so I start looking that the main function.
I see some generation of IV (init vectors), keys, and input. Then, we get a MAGIC number length of zeroed bytes (as output).
Finally, looping MAGIC times we put our input, init vector b, and the keys through some foo().
I don't know what these are really doing, but I can look at the rest of the code to figure it out.


### Gen IV
```
def gen_iv():
	iv_a = "{0:b}".format(random.getrandbits(MAGIC)).zfill(MAGIC) 
	print(f"Enjoy this random bits : {iv_a}")
	return iv_a, [b"\xff" * MAGIC if iv_a[i]=='1' else b"\x00" * MAGIC for i in range(MAGIC)]
```
That init vector function generates to things a thing of MAGIC number bits randomly called iv_a.
Then, that iv_a gets printed out to us. We can learn the value of MAGIC by counting the bits. 
This comes out to be `73 bits`. Then, iv_b is created from iv_a.
Essentially, if a bit in iv_a is 1 then iv_b has 73 bytes of all 1s and the same for zeros both keeping the order from iv_a.
So we know exactly what iv_b is when we are given iv_a.


### Input 
```
def my_input():
	inp = input()
	inp = binascii.unhexlify(inp)
	
	if len(inp) != MAGIC**2:
		print(random.choice(jokes))
		exit(0)
	
	return [inp[MAGIC*i:MAGIC*(i+1)] for i in range(MAGIC)]
```
Next is the input. This is the function that keeps printing the awful jokes. Essentially, I learn 2 things.
Our input must a series of many 00 to ff to allow unhexify to convert our string input to an array of bytes. 
Then, since we know MAGIC == 73, we need 73 square or 5329 bytes which is actually 10658 characters. 
Then, it splits each 73 bytes into 73 arrays. 


At this point, I tried entering just all ones to see if I could get past the jokes. I actually found my 
terminal would truncate the input by running a modified challenge.py to be verbose. 
It would limit the input length to 4095 characters. Looking this up in stackoverflow, I find I needed to 
disable canonical mode. Run this `stty -icanon` to disable it and the terminal no longer limits your input. 


### Flag and Keys
```
with open("flag.txt",'r') as f:
	flag = f.read().encode()

def gen_keys():
	k = b"\x00"*MAGIC
	keys = []
	for i in range(MAGIC-1):
	    key = random.randbytes(MAGIC)
	    keys.append(key)
	    k = xor(k, xor(key,flag))
	keys.append(xor(k,flag))
	return keys
	
def guardian(out, i, keys, intersection=b"\x00"*MAGIC):
	for j in range(i+1):
		intersection = xor(intersection, keys[j])
	return intersection == out
```
Now the fun part with the keys and xor encryption. Essentially, the program just encrypts the flag 72 times using 
XOR with random bytes. The code only stores the keys, except the last key is k xor flag. 
This key is this sequence of xor of the keys and the flag 72 times. 
Just looking at this it seems complex.
But some fun properties with XOR make this simple. 
First, the order does not matter with XOR. A xor B xor C is the same regardless the order.
Second, zeroes mean nothing. 0 xor A is just A. 
Third, xoring the same value gives 0. A xor A will always be zero.


As k starts as zero, we can actually cancel out all but 1 flag and the k.
`Final key == key0 xor key1 ... xor key71 xor flag`

This means if we can xor all the keys with the final one we can get the flag back.
This is where I think the foo function comes into play and kinda what the guardian functions is checking for.

### Good ol' Foo
```
def foo(x, y, z, w):
	return bytes([(a&b&c&d | a&(b^255)&(c^255)&d | a&(b^255)&c&(d^255) | a&b&(c^255)&(d^255) | (a^255)&b&(c^255)&d | (a^255)&b&c&(d^255)) for a, b, c, d in zip(x, y, z, w)])
```
This function is oddly overwhelming. It looks to be a XNOR without the all zeroes case returning one. 
The code goes through this numerous times but we are trying to get that string to xor the keys together.
The only case we can change is the first one taking the input `foo(inp[i], iv_b[i], K5, K6)`. 
I actually know all of the inputs of this, but I think we base our input around what iv_b or b is doing. 
I can kind of treat this as binary as iv_b is all 1s or 0s and the ^255 (xor 255) as an inverse.  


I saw that when b is 0, only cases 2 and 3 matter. Senting our input a to 1 actually gives us an xor of c and d. 
This was interesting so went to see what the xors or the 3 K pairs are together. 
Interesting, K1 xor K2, K3 xor K4, and K5 xor K6, all return a stream of all high bits (a bunch of 0xff). 
However, if I can get the foo function to act as XOR always, then it ends up inverting 3 times.
So I think if the input can be used to zero out the first foo and then other 2 foos invert the keys twice.


Looking at foo, I can zero out the function when b is 0 by setting a to zero. I can when b = 1, but it's not obvious. 
What I can do is set a to 1 and get as what isn't forced zero `a&b&c&d | a&b&(c^255)&(d^255)`.
Drop a and b as both are 1 to get `c xnor d`, which means when c and d are the same it returns 1. 
However, c xor d is 1 so this always returns 0. 

Doing this turns the code into essentially being:
```
output = foo(output, foo(keys[i], 0, K3, K4), K1, K2)
```

The next foo becomes `a & (c xor d)` but K3 xor K4 == 1 so it just becomes a or keys[i].
The last foo is tricky. Though, I can remove any case where c and d need to be the same and simplify.

```
a&(b^255)&(c^255)&d | a&(b^255)&c&(d^255)| (a^255)&b&(c^255)&d | (a^255)&b&c&(d^255)
=>
(a&(b^255) & (c xor d) ) | ( (a^255)&b & (c xor d) )
```
Both xor operations can be removed as they are 1 and we get a final simplification of foo() as:
```
a xor b

OR

output xor keys[i]

```

Output is actually just the previous XORs of the keys that have been done.
This means going through the loop ends up undoing all encryption if our input matches iv_b.

I made a simple python script to get iv_b from iv_a. 
Just pipe the output to xclip and paste into the open netcat prompt.


```
Flag: flag{5h31d0n_54y5_7h47_7h3_b357_numb3r_1n_7h3_w0rld_15_73,_h3_15_r16h7!!}
```

Wow, this was a lot to write out my though process for something I thought was a lot quicker 
to and think through during the competition.



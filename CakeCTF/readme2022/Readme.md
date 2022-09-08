
# Readme-2022

Note: Other than the nimrev and frozen_cake events, this and the rest are post the CTF.
I am doing the rest that I can to learn more.

### What I did to solve this

I initially looked at the provided python and docker files.
Basically, from docker, the flag is loaded into /flag.txt and we 
can interface the server.py code through the netcat command given to us. 
From python, the program opens the flag to check its existence and 
lets us enter a pathname to read. This checks and prevents it from having a ".." 
to go up a directory or going to root by starting with '/'. 


What I noticed was the `filepath = os.path.expanduser(filepath)` code. 
I didn't know what this was so I checked geeksforgeeks and stackoverflow to learn
and wrote a quick program to test its functionality. It will convert '~' to the users home directory, 
but will also convert "~{username}" to that users home directory. This last bit seemed useful.
However, I don't know all the users or where they link to off the top of my head.


First, I checked my own device as it is Manjaro linux and may be similar to what is running.
I found that the user `nobody` is linked to root as its home and tried entering ~nobody/flag.txt. It failed.
So my set up isn't consistent with the debian docker, so I am not going trust anything else.


Next, I started up a docker container on my own device using what they provided. 
I ran bash using `docker container run -it {name_I_made} /bin/bash` and took a look at the /etc/passwd.
The first user that looked interest was `sys` as its home directory was /dev.
I don't remember everything /dev has but looking in there I found /dev/fd to really only be the one useful.
This links to all the file descriptors at /proc/self/fd. These "link" to the files the process has open.


Then, it hits me that the flag.txt actually never gets closed in the code after it is need/used.
So I go back to netcat and start trying ~sys/fd/#. 
I don't know how fds are given out whether random or incremented in someway per process. 
I know the first 0-2 are for in, out, and err. So 3 and 4 fail to open. 5 halts on me. 6 prints out the flag.
I was going to try the first 10 then write a shell script with netcat.


`CakeCTF{~USER_r3f3rs_2_h0m3_d1r3ct0ry_0f_USER}`


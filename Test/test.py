#!/usr/bin/python3
from ctypes import *
import platform, os, sys, random
from hexdump import hexDump

pl = platform.system()
if pl == 'Darwin':
  chacha = CDLL('../chacha20_poly1305.dylib')
elif pl == 'Linux':
  chacha = CDLL('../chacha20_poly1305.so')

RFC_8439_TAG_SIZE = 16
RFC_8439_NONCE_SIZE = 12
RFC_8439_KEY_SIZE = 32

plain = b"This is a test with a non-aligned length (this ain't AES bro!)"
TEXT_SIZE = len(plain)
plainB = cast(plain, POINTER(c_char))
buffer = bytes(TEXT_SIZE + RFC_8439_TAG_SIZE)
bufferB = cast(buffer, POINTER(c_char))
buffer2 = bytes(TEXT_SIZE)
buffer2B = cast(buffer2, POINTER(c_char))

ad = random.randbytes(TEXT_SIZE)
adB = cast(ad, POINTER(c_char))
key = random.randbytes(RFC_8439_KEY_SIZE)
keyB = cast(key, POINTER(c_char))
nonce = random.randbytes(RFC_8439_NONCE_SIZE)
nonceB = cast(nonce, POINTER(c_char))
print("PLAINTEXT")
hexDump(plain)
print("KEY")
hexDump(key)
print("NONCE")
hexDump(nonce)
print("AD")
hexDump(ad)

cipher_size = chacha.encrypt(plainB, TEXT_SIZE, adB, TEXT_SIZE, keyB, nonceB, bufferB)
print("CIPHER")
hexDump(buffer)

result = chacha.decrypt(buffer2B, key, nonce, ad, TEXT_SIZE, bufferB, cipher_size)
if result > -1:
  print("DECIPHERED")
  hexDump(buffer2)
else:
  print(f"Error: {result}")

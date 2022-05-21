# coding:utf-8
from pwn import *

context.arch = "aarch64"

context.os = "linux"

context.endian = "little"

context.word_size = 64


file = r"./dev.kc.macho.development"

kernel_base = 0x07004000

target = 0x0007C99748

offset = target - kernel_base

ass = asm("hvc #0x20")

# ass = asm("orr x2, x1, #0x2")

r = open(file, "rb")

r.seek(offset, 0)

former = r.read(4)

former_ins = disasm(former)

r.close()

print("[*] former instruction:", hex(offset), former_ins)

c = input("plz confirm (y): ")

print(c)

if c == "y\n":

    f = open(file, "r+b")

    f.seek(offset, 0)

    f.write(ass)

    f.close()

    print("[+] 写入成功")

    r = open(file, "rb")

    r.seek(offset, 0)

    former = r.read(4)

    former_ins = disasm(former)

    print("[*] latter instruction:", former_ins)

    r.close()

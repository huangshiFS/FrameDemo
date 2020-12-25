'''
编码转换
'''
from capstone import *

CODE = b"\x41\x4a"
md = Cs(CS_ARCH_X86,CS_MODE_32)
for i in md.disasm(CODE,0x1000000):
    print("%x:\t%s\t%s" %(i.address,i.mnemonic,i.op_str))

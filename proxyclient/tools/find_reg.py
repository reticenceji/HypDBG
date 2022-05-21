import sys, pathlib
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

from m1n1.setup import *
from m1n1.find_regs import *
from m1n1 import asm

p.iodev_set_usage(IODEV.FB,0)

if u.mrs(SPRR_CONFIG_EL1):
    u.msr(GXF_CONFIG_EL12, 0)
    u.msr(SPRR_CONFIG_EL12, 0)
    u.msr(GXF_CONFIG_EL1, 0)
    u.msr(SPRR_CONFIG_EL1, 0)

u.inst("nop",call="el1")

all_regs = set()
reg = APCTL_EL1
old_regs = set(find_regs(u,values=False))
#old_regs = set(find_regs(u,values=False))
#u.msr((3,4,15,0,4),0x1d)
new_regs = set(find_regs(u,values=False))
diff_regs = old_regs - new_regs

for r in sorted(old_regs):
    print(" %s : %lx" % (sysreg_name(r), u.mrs(r)))

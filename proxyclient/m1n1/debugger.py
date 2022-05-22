import functools, sys

from .proxy import M1N1Proxy
from .proxyutils import ProxyUtils

# def hard_break(p: M1N1Proxy, u: ProxyUtils):
#     pass
def __soft_break(p: M1N1Proxy, u: ProxyUtils):
    
    def soft_break(virtual_addr):
        physical_addr = p.hv_translate(virtual_addr)
        p.write32(virtual_addr)

def debugger(func):
    @functools.wraps(func)
    def wrapper(locals, msg, exitmsg = None):
        sys.ps1 = "(hdb) "
        sys.ps2 = ""
        # proxy = locals["p"]
        # utils = locals["u"]

        # locals["trans"] = locals["hv_translate"]
        # locals["dis"] = locals["disassemble_at"]
        return func(locals, msg, exitmsg)

    return wrapper

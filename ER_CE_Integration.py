from pymem import *
from pymem.process import *

mem = Pymem("eldenring.exe")
gameModule = module_from_name(mem.process_handle, "eldenring.exe").lpBaseOfDll

def GetPtrAddr(base, offsets):
    addr = mem.read_longlong(base)
    
    for i in offsets:
        if i != offsets[-1]:
            addr = mem.read_longlong(addr + i)
            
    return addr + offsets[-1]
    
def SetRunes(num_runes):
    if (not num_runes >= 0):
        return
        
    mem.write_int(GetPtrAddr(gameModule + 0x03CF1558, [0x20, 0x8, 0x30, 0x6C]), num_runes)

def SetHP(num_hp):
    if (not num_hp >= 0):
        return
       
    mem.write_int(GetPtrAddr(gameModule + 0x03CD8F60, [0x8, 0x0, 0x420, 0x10, 0x478]), num_hp)

def SetFP(num_fp):
    if (not num_fp >= 0):
        return
       
    mem.write_int(GetPtrAddr(gameModule + 0x03AD0898, [0x810, 0x190, 0x248, 0x8, 0x190, 0x0, 0x148]), num_fp)
    
#num = int(input("Write value: "))
#SetFP(num)
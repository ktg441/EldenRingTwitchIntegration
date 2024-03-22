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
        
    mem.write_int(GetPtrAddr(gameModule + 0x03CD4D88, [0x8, 0x6C]), num_runes)

def SetHP(num_hp):
    if (not num_hp >= 0):
        return
       
    mem.write_int(GetPtrAddr(gameModule + 0x03AA3DA0, [0x0, 0x190, 0x68, 0x20, 0x138]), num_hp)

def SetFP(num_fp):
    if (not num_fp >= 0):
        return
       
    mem.write_int(GetPtrAddr(gameModule + 0x03AA3DA0, [0x0, 0x190, 0x0, 0x148]), num_fp)
    
def SetStamina(num_stamina):
    if (not num_stamina >= 0):
        return
       
    mem.write_int(GetPtrAddr(gameModule + 0x03AA3DA0, [0x0, 0x190, 0x0, 0x110, 0x8C]), num_stamina)
    
def SetHeadSize(num_scale):
    if (not num_scale >= 0.0 or not num_scale <= 100.0):
        return
    
    mem.write_float(GetPtrAddr(gameModule + 0x044FF328, [0xB0, 0x0, 0x0, 0x80, 0x550]), num_scale)
    
def SetWeapon(weapon_id):
    if (not weapon_id >= 110000):
        return 
    
    mem.write_int(GetPtrAddr(gameModule + 0x03CDF238, [0x50, 0x30, 0x3A0]), weapon_id)
    
SetRunes(int(input("Runes: ")))
SetHP(int(input("HP: ")))
SetFP(int(input("FP: ")))
SetStamina(int(input("Stamina: ")))
SetHeadSize(float(input("Head Scale: ")))

# WorldChrMan -> 03AA3DA0
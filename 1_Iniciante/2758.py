import struct

def resolver_2758():

    linha1 = input().split()
    linha2 = input().split()
    
    A_original = float(linha1[0])
    B_original = float(linha1[1])
    C = float(linha2[0])
    D = float(linha2[1])
    
    A = struct.unpack('f', struct.pack('f', A_original))[0]
    B = struct.unpack('f', struct.pack('f', B_original))[0]
    
    print(f"A = {A:.6f}, B = {B:.6f}")
    print(f"C = {C:.6f}, D = {D:.6f}")
    
    print(f"A = {A:.1f}, B = {B:.1f}")
    print(f"C = {C:.1f}, D = {D:.1f}")
    
    print(f"A = {A:.2f}, B = {B:.2f}")
    print(f"C = {C:.2f}, D = {D:.2f}")
    
    print(f"A = {A:.3f}, B = {B:.3f}")
    print(f"C = {C:.3f}, D = {D:.3f}")
    
    print(f"A = {A:.3E}, B = {B:.3E}")
    print(f"C = {C:.3E}, D = {D:.3E}")
    
    print(f"A = {A:.0f}, B = {B:.0f}")
    print(f"C = {C:.0f}, D = {D:.0f}")

resolver_2758()
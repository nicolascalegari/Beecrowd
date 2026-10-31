import sys

def resolver():

    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
        
    t = int(input_data[0])
    
    for i in range(1, t + 1):
        pa, pb, g1, g2 = input_data[i].split()
        
        pa = int(pa)
        pb = int(pb)
        g1 = float(g1)
        g2 = float(g2)
        
        anos = 0
        
        while pa <= pb:

            pa += int(pa * (g1 / 100))
            pb += int(pb * (g2 / 100))
            anos += 1
            
            if anos > 100:
                break
                
        if anos > 100:
            print("Mais de 1 seculo.")
        else:
            print(f"{anos} anos.")

if __name__ == '__main__':
    resolver()

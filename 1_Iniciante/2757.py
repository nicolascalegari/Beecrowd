import sys

def main():
    A = int(sys.stdin.readline())
    B = int(sys.stdin.readline())
    C = int(sys.stdin.readline())

    print(f"A = {A}, B = {B}, C = {C}")
    print(f"A = {A:>10}, B = {B:>10}, C = {C:>10}")
    print(f"A = {A:0=10}, B = {B:0=10}, C = {C:0=10}")
    print(f"A = {A:<10}, B = {B:<10}, C = {C:<10}")

if __name__ == '__main__':
    main()
def resolver():

    T = int(input())
    
    for _ in range(T):

        bonus = int(input())
        
        ai_dabriel, di_dabriel, li_dabriel = map(int, input().split())
        
        ai_guarte, di_guarte, li_guarte = map(int, input().split())
        
        golpe_dabriel = (ai_dabriel + di_dabriel) / 2
        if li_dabriel % 2 == 0:
            golpe_dabriel += bonus
            
        golpe_guarte = (ai_guarte + di_guarte) / 2
        if li_guarte % 2 == 0:
            golpe_guarte += bonus
            
        if golpe_dabriel > golpe_guarte:
            print("Dabriel")
        elif golpe_guarte > golpe_dabriel:
            print("Guarte")
        else:
            print("Empate")

if __name__ == "__main__":
    resolver()
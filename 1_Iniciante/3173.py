from datetime import datetime, timedelta

def main():

    n = int(input())
    
    data_inicial = datetime(2020, 12, 21)
    
    # multiplicadas por 365.25 para incluir os anos bissextos automaticamente
    dias_jupiter = int(n * 11.9 * 365.25)
    dias_saturno = int(n * 29.6 * 365.25)
    
    data_jupiter = data_inicial + timedelta(days=dias_jupiter)
    data_saturno = data_inicial + timedelta(days=dias_saturno)
    
    print(f"Dias terrestres para Jupiter = {dias_jupiter}")
    print(f"Data terrestre para Jupiter: {data_jupiter.strftime('%Y-%m-%d')}")
    print(f"Dias terrestres para Saturno = {dias_saturno}")
    print(f"Data terrestre para Saturno: {data_saturno.strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    main()

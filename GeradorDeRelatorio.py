import csv

file = input("Qual o nome do arquivo?\n")
formatted_file = file + ".csv" 


with open(formatted_file, 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    counter = 0
    creatives_dict = {} 
    city = None   
    
    
    for row in reader:
        if city is None:
            city = row[3]
        
        creative = row[6]
        if row[6] != "Lead Manual" and "Orgânico" not in row[6]:
            counter += 1
            
        if "creative:" in creative:
            creative = creative.split("creative:")[1].split("/")[0].strip()
            if creative not in creatives_dict:
                creatives_dict[creative] = 0
            creatives_dict[creative] += 1
        

    
    print("=" * 50)
    print(f"Cidade: {city}")
    print(f"Total de Leads: {counter}")
    print("=" * 50)
    print(f"{'Creative':<30} | {'Quantidade':>10}")
    print("-" * 50)

    for creative, count in creatives_dict.items():
        print(f"{creative:<30} | {count:>10}")

    print("=" * 50)

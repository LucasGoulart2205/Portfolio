planetas = ["Mercuirio", 'Venus',"Terra", "Marte","Jupiter", "Saturno", "Urano", "Neturno"]

for i, planeta in enumerate(planetas):
    if planeta=="Andromedae b":
        print("Andromedae b encontrada")
        break
else:
    print('Planeta desconhecido')
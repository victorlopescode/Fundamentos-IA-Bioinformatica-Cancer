dna_normal = "GATCCAATG" 
dna_tumor = "GATGCAATG"

#Vamos comparar letra por letra

for posicao in range(len(dna_normal)):
    letra_normal = dna_normal[posicao]
    letra_tumor = dna_tumor[posicao]

    if letra_normal != letra_tumor:
        print(f'Alerta! Mutação encontrada na posição {posicao}:')
        print(f'Normal era: {letra_normal} -> no tumor virou: {letra_tumor}')
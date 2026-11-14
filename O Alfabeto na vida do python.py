
# Um pedaço de DNA qualquer
dna = "ATGCGATACTGA"
print(dna)
print("Tamanho do pedaço de DNA:", len(dna), "letras")

# A regra de conexão da vida

regras = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C'
}

fita_original = "ATGC"

# para cada letra achamos o  par dela:

fita_parceira = ""
for letra in fita_original:
    fita_parceira += regras[letra]

print("Fita Original: ", fita_original)
print("Fita Parceira: ", fita_parceira)
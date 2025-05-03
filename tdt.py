#Вариант 3 Лаба 2
def solve():
    protein_sequence = input("Введите последовательность аминокислот")
    codon_counts = {
        "F": 2, "L": 6, "I": 3, "M": 1, "V": 4,
        "S": 6, "P": 4, "T": 4, "A": 4,
        "Y": 2, "H": 2, "Q": 2, "N": 2, "K": 2, "D": 2, "E": 2,
        "C": 2, "W": 1, "R": 6, "G": 4,
        "*": 3
    } # Словарь,который хранит соответствия между аминокислотой и количеством кодирующих ее кодонов
    total_sequences = 1 # переменная хранящая общее количество возможных последовательностей РНК
    for amino_acid in protein_sequence:
        total_sequences = (total_sequences * codon_counts[amino_acid] ) %1000000
    total_sequences = (total_sequences * codon_counts["*"]) % 1000000
    print (total_sequences)
solve()




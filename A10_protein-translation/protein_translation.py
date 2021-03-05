protein_items = {"AUG": "Methionine",
                 "UUU": "Phenylalanine",
                 "UUC": "Phenylalanine",
                 "UUA": "Leucine",
                 "UUG": "Leucine",
                 "UCU": "Serine",
                 "UCC": "Serine",
                 "UCA": "Serine",
                 "UCG": "Serine",
                 "UAU": "Tyrosine",
                 "UAC": "Tyrosine",
                 "UGU": "Cysteine",
                 "UGC": "Cysteine",
                 "UGG": "Tryptophan",
                 "UAA": "STOP",
                 "UAG": "STOP",
                 "UGA": "STOP"
                 }


def proteins(strand):
    # break then into 3
    multiples_3 = 3
    initial_num = 0
    proteins = []
    target_proteins = []
    while multiples_3 <= len(strand):
        if strand[initial_num:multiples_3] not in proteins:
            proteins.append(strand[initial_num:multiples_3])
        initial_num = multiples_3
        multiples_3 += 3

    for i in proteins:
        if(protein_items[i] == "STOP"):
            break
        target_proteins.append(protein_items[i])

    return target_proteins


# proteins("UGGUGUUAUUAAUGGUUU")

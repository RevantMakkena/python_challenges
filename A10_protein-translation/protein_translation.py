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
    translations = ()
    while multiples_3 <= len(strand):
        translations = translations + \
            tuple(protein_items[strand[initial_num:multiples_3]])
        proteins.append(strand[initial_num:multiples_3])
        initial_num = multiples_3
        multiples_3 += 3
    print(proteins)
    print(translations)

    all_proteins = strand[0]


proteins("AUGUUUUGG")

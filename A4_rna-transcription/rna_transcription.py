def to_rna(dna_strand):
    translation = (("C", "G"), ("G", "C"), ("T", "A"), ("A", "U"))
    target = ""

    for char in dna_strand:
        target += ''.join([z for y, z in translation if y == char])

    return target


# print(to_rna(""))
# # UGCACCAGAAUU

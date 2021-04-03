def to_rna(dna_strand):
    rna = ""
    for i in dna_strand:
        if i == "G":    rna += "C"
        elif i == "C":  rna += "G"
        elif i == "T":  rna += "A"
        elif i == "A":  rna += "U"
    return rna

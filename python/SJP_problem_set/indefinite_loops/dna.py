ref = {
    "A": "T",
    "T": "A",
    "G": "C",
    "C": "G"
}

def check(string):
    search_strand = []
    [search_strand.insert(0, ref[char]) for char in string]
    search_strand = "".join(search_strand)
    success = False
    while not success and len(search_strand) >= 6:
        if search_strand in string[len(search_strand):]:
            success = True
        else:
            search_strand = search_strand[1:]
    if success:
        return True
    return False

def rna_transcription(dna_strand):
    promoter_index = dna_strand.index("TATAAT")
    trans_index = promoter_index + 10
    trans_unit = dna_strand[trans_index:]
    for i, letter in enumerate(trans_unit):
        if len(trans_unit[i:]) >= 12:
            success = check(trans_unit[i:])
        if success:
            break
    final = trans_unit[:i]
    rna = ""
    for nucleobase in final:
        if nucleobase == "A":
            rna += "U"
        else:
            rna += ref[nucleobase]
    return rna



print(rna_transcription("AGATTATATAATGATAGGATTTAGATTGACCCGTCATGCAAGTCCATGCATGACAGC"))

print(rna_transcription("AGTCTTCAAGGGGATTCCCAGGTATATAATGCAGATCGCGACGAAATATCGGGCGGGATCCATACCGACCCAGCCGCCCGA"))

print(rna_transcription("TATAATGGGGGAGAGACCGAGTGTTTAAGTCCCGAGGGATCGGGAGTGAGATTGAGGGAATTCCGGGAATCTCACT"))




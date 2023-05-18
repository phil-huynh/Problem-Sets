# **DNA transcription**

# DNA is made up of two twisted strands that encode genes using long combinations of four bases: Adenine, Cytosine, Guanine, and Thymine. The strands are complementary to one another, meaning that Adenine and Thymine are always opposite each other, and Cytosine and Guanine are always opposite each other, like this:

# ```
# A double strand of DNA:

# ATCAAGGCCTATTCCGGGAAAGG
# TAGTTCCGGATAAGGCCCTTTCC

# ```

# In order for the information in a gene to be used, it has to be transcribed into a strand of RNA. During this process, a portion of one strand of DNA is transcribed. This portion is known as the transcription unit. The start of the sequence to be transcribed is signaled by a sequence of bases known as a promoter, and the end is signaled by a sequence known as the terminator. For our purposes, the promoter is the sequence `TATAAT`, which begins 10 bases before the start of the transcription unit, and the terminator consists of two distinct, complementary, reversed sequences of at least length 6 that cause the RNA molecule to coil back on itself and pinch off the transcribed strand. If `TATAAT` appears twice on a strand, only the first occurrence counts as the promoter. An example is shown below.

# AGATTA**TATAAT**GATAGGATTTAGATTGACCC**GTCATGCAAGTCCATGCATGACAGC**

# **In this example, the promoter and terminator sequences are boldfaced, and the transcription unit is underlined.**

# **1. The first step is to find the *promoter*, specifically the sequence TATAAT.
# 2. Starting at the first T in the *promoter*, count forward 10 characters and that's where the *transcription unit* starts, in this case the first underlined G.
# 3. After the first letter of the *transcription unit*, search the remainder of the string for two sequences of letters at least six characters long that, when the first is matched up to the *reverse* of the second, it forms a valid double strand of DNA where A matches with T and G matches with C:

# `GTCATGCA
# CAGTACGT  (the reverse of the second sequence)`

# This is the *terminator*.
# 4. The *transcription unit* is the characters including the first letter of the *transcription unit* found in step 2 all the way up to, but not including, the first letter of the *terminator* found in step 3.
# The resulting RNA will be *complementary* to the transcription unit, except that in RNA Uracil takes the place of Thymine. Here's an example of how to turn the transcription unit into RNA:

# `Transcription unit: GGATTTAGATTGACCC
# Complement:         CCTAAATCTAACTGGG
# Replace T with U:   CCUAAAUCUAACUGGG`

# The final string is the RNA `CCUAAAUCUAACUGGG` for the gene.
# Your job is to write a function that performs this calculation.
# Here are some sample inputs and outputs for you to test your function as you write it. The *promoter*, *transcription unit*, and *terminator* are marked for each strand for you to better be able to see it.

# `Input:  AGATTATATAATGATAGGATTTAGATTGACCCGTCATGCAAGTCCATGCATGACAGC
#               |-P--|    |------TU------||--T---|      |--T---|
# Output: CCUAAAUCUAACUGGG

# Input:  AGTCTTCAAGGGGATTCCCAGGTATATAATGCAGATCGCGACGAAATATCGGGCGGGATCCATACCGACCCAGCCGCCCGA
#                                 |-P--|    |----TU------||--T---|                 |--T---|
# Output: UAGCGCUGCUUUAU

# Input:  TATAATGGGGGAGAGACCGAGTGTTTAAGTCCCGAGGGATCGGGAGTGAGATTGAGGGAATTCCGGGAATCTCACT
#         |-P--|    |------TU---------||-T--|    |-T--|
# Output: CUCUCUGGCUCACAAAUUC`
# 5DNA transcriptionSubmitted on 10/07/2022



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



# print(rna_transcription("AGATTATATAATGATAGGATTTAGATTGACCCGTCATGCAAGTCCATGCATGACAGC"))

# print(rna_transcription("AGTCTTCAAGGGGATTCCCAGGTATATAATGCAGATCGCGACGAAATATCGGGCGGGATCCATACCGACCCAGCCGCCCGA"))

# print(rna_transcription("TATAATGGGGGAGAGACCGAGTGTTTAAGTCCCGAGGGATCGGGAGTGAGATTGAGGGAATTCCGGGAATCTCACT"))




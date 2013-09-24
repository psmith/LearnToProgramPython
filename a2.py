def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) - len(dna2) > 0

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return nucleotide != '' and dna.count(nucleotide)

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1 and dna2 != ""

def is_valid_sequence(dna):
    """ (str) -> bool

    Return True if and only if DNA sequence is valid meaning only contains A, T, C, and/or G's

    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('ATCGGCR')
    False
    >>> is_valid_sequence('')
    False

    """
    for s in dna:
        if s != "A" and s != "T" and s != "C" and s != "G":
            return False
    return True

def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str

    Return a dna sequence where dna2 was inserted into dna1 at the given index

    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    >>> insert_sequence('CCGG', 'AT', 0)
    'ATCCGG'

    """
    return dna1 if (dna2 == None or dna2 == '') else dna1[:index] + dna2 + dna1[index:]
    
def get_complement(nucleotide):
    return get_complementary_sequence(nucleotide)

def get_complementary_sequence(dna_sequence):
    return None if dna_sequence == None else dna_sequence.translate(dna_sequence.maketrans("ACGT", "TGCA"))

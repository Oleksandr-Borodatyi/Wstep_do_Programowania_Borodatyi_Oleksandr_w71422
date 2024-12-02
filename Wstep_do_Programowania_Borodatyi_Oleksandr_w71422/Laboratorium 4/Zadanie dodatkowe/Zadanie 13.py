# Zadanie 13

def wspolne_wartosci(seq1, seq2):
    
    return list(set(seq1) & set(seq2))

seq1 = [1, 2, 3, 4, 5]
seq2 = [4, 5, 6, 7, 8]
print(wspolne_wartosci(seq1, seq2))  # [4, 5]

seq1 = ['a', 'b', 'c', 'd']
seq2 = ['c', 'd', 'e', 'f']
print(wspolne_wartosci(seq1, seq2))  # ['c', 'd']

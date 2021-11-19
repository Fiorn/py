#задание 1
print("Введите S1 и S2")
S1=input()
S2=input()
def comare(S1,S2):
    ngrams = [
        S1[i:i+3] for i in range(len(S1))
    ]
    count = 0
    for ngram in ngrams:
        count +=S2.count(ngram)
    return count/max(len(S1), len(S2))
print(comare(S1,S2))

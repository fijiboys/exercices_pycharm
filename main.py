###print.(len("jaime les phrase".split()))



phrase = "jaime les phrase"

def count_words(sentence):
    nombre = len(sentence.split())
    return nombre
print("-------------------------------------")
print("| phrase : ", phrase, "       |")
print("-------------------------------------")
print("| nombre de mot dans la phrase : ", count_words(phrase),"|")
print("-------------------------------------")
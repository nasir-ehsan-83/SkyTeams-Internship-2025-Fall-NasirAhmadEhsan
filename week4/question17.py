def abbreviate_sentence(sentence):
    words = sentence.split()
    return ' '.join(word[0] for word in words if word)

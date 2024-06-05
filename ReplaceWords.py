def replaceWords(dictionary, sentence: str) -> str:
    for word in dictionary:
        word_len = len(word)
        prev_index = 0
        while True:
            index = sentence.find(word, prev_index)
            if index == -1:
                break
            prev_index = index + word_len
            if sentence[index - 1] != ' ' and index != 0:
                continue
            next_space = sentence.find(' ', index)
            if next_space == -1:
                sentence = sentence[0:index + word_len]
                break
            sentence = sentence[0:index + word_len] + sentence[next_space:]
    return sentence

print(replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery"))
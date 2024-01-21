import string
import numpy
import numpy as np


def get_words(file1, file2):
    global first_text_words, second_text_words
    try:
        input1 = open(file1, 'r')
        first_text = input1.readlines()
        input1.close()
        first_text_words = {}
        for line in first_text:
            line.replace('\n', '')
            removed_punc_line = line.translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation)))
            lowercase_line = removed_punc_line.lower()
            line_words = lowercase_line.split()
            for word in line_words:
                first_text_words[word] = None
    except FileNotFoundError:
        print("File 1 was not found.")

    try:
        input2 = open(file2, 'r')
        second_text = input2.readlines()
        input2.close()
        second_text_words = {}
        for line in second_text:
            line.replace('\n', '')
            removed_punc_line = line.translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation)))
            lowercase_line = removed_punc_line.lower()
            line_words = lowercase_line.split()
            for word in line_words:
                second_text_words[word] = None
    except FileNotFoundError:
        print("File 2 was not found.")

    total_words = first_text_words | second_text_words
    total_list = list(total_words.keys())

    return [first_text_words, second_text_words, total_list]


def vectorize(first_words, second_words, total):
    file1_bools = [0] * len(total)
    file2_bools = [0] * len(total)

    for i in range(len(total)):
        if total[i] in first_words:
            file1_bools[i] = 1
        if total[i] in second_words:
            file2_bools[i] = 1

    file1_vector = np.array(file1_bools)
    file2_vector = np.array(file2_bools)

    return [file1_vector, file2_vector]


def cos_similarity(vector1, vector2):
    dot_prod = vector1.dot(vector2)
    norm1 = np.linalg.norm(vector1)
    norm2 = np.linalg.norm(vector2)
    similarity = (dot_prod) / (norm1 * norm2)
    return similarity

def display_results():
    first_file = input("Filename 1: ")
    second_file = input("Filename 2: ")
    dicts = get_words(first_file, second_file)
    vectors = vectorize(dicts[0], dicts[1], dicts[2])
    similarity = cos_similarity(vectors[0], vectors[1])
    percent_sim = "{:.2f}".format(similarity * 100)
    return f'Your text files are {percent_sim}% similar.'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(display_results())

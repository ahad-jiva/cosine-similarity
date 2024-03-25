import string
import numpy as np


def get_words(file1, file2):
    input1 = open(f'text files/{file1}', 'r')
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

    input2 = open(f'text files/{file2}', 'r')
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

    total_words = first_text_words | second_text_words
    total_list = list(total_words.keys())

    return [first_text_words, second_text_words, total_list]


def file_word_count(filename):
    text = open(f'text files/{filename}', 'r')
    words = 0
    for line in text:
        words += len(line.split())
    return words


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
    similarity = dot_prod / (norm1 * norm2)
    return similarity


def display_results():
    first_file = input("Filename 1: ")
    second_file = input("Filename 2: ")
    word_match_weight = float(input("Weight of text content similarity (enter a number between 0-100; 65 recommended): "))
    word_count_weight = float(input("Weight of text length similarity (enter a number between 0-100; 35 recommended): "))
    if word_match_weight + word_count_weight != 100:
        return "Invalid weight values (make sure weights sum to 100)"
    dicts = get_words(first_file, second_file)
    vectors = vectorize(dicts[0], dicts[1], dicts[2])
    similarity = cos_similarity(vectors[0], vectors[1])
    word_count1 = file_word_count(first_file)
    word_count2 = file_word_count(second_file)
    word_count_diff = 1 - abs((word_count1 - word_count2) / (word_count1 + word_count2))
    weighted_similarity = similarity * (int(word_match_weight) / 100)
    weighted_count = word_count_diff * (int(word_count_weight) / 100)
    weighted_percent_sim = "{:.3f}".format((weighted_similarity + weighted_count) * 100)
    no_length_percent_sim = "{:.3f}".format(similarity * 100)
    no_match_percent_sim = "{:.3f}".format(word_count_diff * 100)
    return f'Your text files are {weighted_percent_sim}% similar with a {word_match_weight}% weight on text content ' \
           f'similarity and a {word_count_weight}% weight on text length similarity.\nWithout accounting for text ' \
           f'length similarity, your text files are {no_length_percent_sim}% similar.\nWithout accounting for text ' \
           f'content similarity, your text files are {no_match_percent_sim}% similar.'

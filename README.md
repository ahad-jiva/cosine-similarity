# Text Similarity

This is a Python-based program that will determine how similar two text files are based on the words that they contain. The text files are vectorized, then the cosine similarity between the two is calculated.

## Getting Started

Place any two .txt files into the text files folder and run main.py


## Usage
Input the file names of the two text files you want to compare. You can also input weight values that affect whether file content or file length affects the similarity calculation more. The program will also calculate two additional similarity values, one where length isn't considered and one where content isn't considered.

## Picking weights
By default, weights of 65 and 35, respectively, give a good balance between comparing file content and file length. For text files with wildly different lengths, consider increasing the weight of text length similarity. For text files with similar lengths, consider increasing the weight of text content similarity.

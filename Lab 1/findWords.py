import sys


def get_file_content(file):
    with open(file, "r") as f:
        return f.read().split()


def count_words(content):
    dict = {}
    for word in content:
        if not dict.get(word, 0):
            dict[word] = 1
        else:
            dict[word] += 1
    return dict


if __name__ == '__main__':
    file = sys.argv[1]
    words = sys.argv[2:]
    content = get_file_content(file)

    dictionary = count_words(content)

    for key in words:
        print(key, dictionary.get(key, 0))

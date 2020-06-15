import reference

def find_longest_possible(bad_chars, words):
    current_longest_word = ''

    for word in words:
        if len(word) < len(current_longest_word):
            continue

        for char in bad_chars:
            if char in word:
                continue
        
        current_longest_word = word

    return current_longest_word


def main():
    words = reference.words.split('\n')
    bad_chars = ['g','k','m','q','v','w','x','z']
    print(find_longest_possible(bad_chars, words))


if __name__ == '__main__':
    main()
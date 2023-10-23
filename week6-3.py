from collections import Counter

def compare_word_frequencies(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        words1 = f1.read().lower().split()
        words2 = f2.read().lower().split()
        counter1 = Counter(words1)
        counter2 = Counter(words2)

        common_words = set(words1) & set(words2)

        print("공통된 단어와 각 파일에서의 빈도:")
        for word in common_words:
            print(f"'{word}': 파일1 - {counter1[word]}, 파일2 - {counter2[word]}")

if __name__ == "__main__":
    file1 = 'file1.txt'
    file2 = 'file2.txt'
    compare_word_frequencies(file1, file2)

from collections import defaultdict
import time
from pathlib import Path

basePath = 'D:\\Github Projects\\AnagramFinder\\Anagram\\'

def main():

    start_time = time.time()

    contents = Path(basePath + 'sample.txt').read_text()

    words = contents.split()

    anagram_groups = defaultdict(list)
    for word in words:
        sorted_letters = ''.join(sorted(word))
        key = sorted_letters
        anagram_groups[key].append(word)

    output_path = basePath + 'anagram_groups.txt'

    with open(output_path, 'w', encoding='utf-8') as f:
        for group in anagram_groups.values():
            f.write(' '.join(group) + '\n')

    end_time = time.time()
    execution_time = end_time - start_time

    print("The results have been successfully saved")

    print(f"The program ran in {execution_time:.6f} seconds")

if __name__ == "__main__":
    main()










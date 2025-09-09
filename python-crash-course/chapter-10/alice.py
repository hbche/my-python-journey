from pathlib import Path

path = Path('alice.txt')

try:
    contents = path.read_text(encoding='utf8')
except FileNotFoundError:
    print(f"Sorry, the file {path} dose not exist.")
else:
    # 统计文件中大致包含多少个单词
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")          # The file alice.txt has about 29564 words.
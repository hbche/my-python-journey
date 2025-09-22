from pathlib import Path

def count_words(file):
    """统计file对应的文件的字数"""
    
    path = Path(file)
    try:
        contents = path.read_text(encoding='utf8')
    except FileNotFoundError:
        # print(f"Sorry, the file {path} dosen't exist.")
        # 静默失败
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has {num_words} words.")
        
bookds = ['alice.txt', 'little_women.txt', 'moby _dick.txt', 'siddhartha.txt']
for book in bookds:
    count_words(book)
    
# The file alice.txt has 29564 words.
# The file little_women.txt has 24711 words.
# The file siddhartha.txt has 42186 words.
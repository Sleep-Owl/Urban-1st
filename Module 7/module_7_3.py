class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        result = {}
        for file in self.file_names:
            with open(file, 'r', encoding='utf-8') as f:
                text = f.read()
                text_lower = text.lower()
                words = text_lower.split()
                result[file] = words
        return result

    def find(self, word):
        word = word.lower()
        result = {}
        for filename, words in self.get_all_words().items():
            position = words.index(word)
            result[filename] = position + 1
        return result

    def count(self, word):
        word = word.lower()
        result = {}
        for filename, words in self.get_all_words().items():
            count = words.count(word)
            result[filename] = count
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

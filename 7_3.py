import string

class WordsFinder:
    def __init__(self,*file_names):
        self.file_names = list(file_names)

        
    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name,'r',encoding='utf-8') as file:
                text = file.read().lower()
                for char in string.punctuation:
                    if char != '-':
                        text = text.replace(char,'')
                text = text.replace(' - ','')
                words = text.split()
                all_words[file_name] = words
        return all_words
    

    def find(self,word):
        all_words = self.get_all_words
        word = word.lower()
        finddd = {}
        for file_name, words in all_words().items():
            if word in words:
                finddd[file_name] = words.index(word)
            else:
                finddd[file_name] = -1
        return finddd
    

    def count(self,word):
        word = word.lower
        word_count = {}
        all_words = self.get_all_words
        for file_name, words in all_words().items():
            word_count[file_name] = word.count(word)
        return word_count
    
finder2 = WordsFinder('test.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

import re
from task2.fileService import FileService

class TextAnalizer:

    def __init__(self):
        self.fs = FileService()
        self.text = self.fs.GetTextFromFile()
    
    def CountSentences(self):
        sentences = re.split(r"(?<=[.!?])\s+", self.text)
        sentences_count = len(sentences)
        self.fs.WriteInfoToResultFile("Number of sentences in text: " + str(sentences_count))

    def CountDifferentTypesOfSentences(self):
        narrative = re.split(r"(?<=[.])\s+", self.text)
        question = re.split(r"(?<=[?])\s+", self.text)
        exclamation = re.split(r"(?<=[!])\s+", self.text)
        narrative_count = len(narrative)
        question_count = len(question) - 1
        exclamation_count = len(exclamation) - 1
        self.fs.WriteInfoToResultFile("\nNumber of narrative sentences: " + str(narrative_count) +
                                      "\nNumber of question sentences: " + str(question_count) +
                                      "\nNumber of exclamation sentences: " + str(exclamation_count))

    def AverageSentenceLength(self):
        sentences = re.split(r"(?<=[.!?])\s+", self.text)
        total_sum = 0
        for sentence in sentences:
            words = sentence.split()
            for word in words:
                total_sum += len(word)
        total_sum = total_sum/len(sentences)
        self.fs.WriteInfoToResultFile("\nAverage sentence length: " + str(total_sum))

    def AverageWordLength(self):
        sentences = re.split(r"(?<=[.!?])\s+", self.text)
        total_sum = 0
        words_count = 0
        for sentence in sentences:
            words = sentence.split()
            words_count += len(words)
            for word in words:
                total_sum += len(word)
        total_sum = total_sum/words_count
        self.fs.WriteInfoToResultFile("\nAverage word length: " + str(total_sum))

    def EmojiCount(self):
        emojis = re.findall(r"(?<!\S)[:;]-*[\(\)\]\[]+\s+", self.text)
        for emoji in emojis:
            opening_round = emoji.count('(')
            closing_round = emoji.count(')')
            opening_sq = emoji.count('[')
            closing_sq = emoji.count(']')
            counts = [opening_round, closing_round, opening_sq, closing_sq]
            numb_counts = 0
            for count in counts:
                if count != 0:
                    numb_counts += 1
            if numb_counts > 1:
                emojis.remove(emoji)
        emojis_count = len(emojis)
        self.fs.WriteInfoToResultFile("\nNumber of emojis: " + str(emojis_count))

    def WordsWithSymbolsFromFtoY(self):
        words = re.findall(r'\b\w*[f-y]\w*\b', self.text)
        self.fs.WriteInfoToResultFile("\nWords with symbols from f to y: ")
        for word in words:
            self.fs.WriteInfoToResultFile(word + " ")

    def FindUSDorRURorEU(self):
        self.fs.WriteInfoToResultFile("\nPrices in USD, RUR, EU: ")
        valutes = re.findall(r'(\d+(?:\.\d+)?)\s+(USD|RUR|EU)\b', self.text)
        errors = []
        for val in valutes:
            if re.search(r'\.', val[0]):
                buff = val[0].split('.')
                if len(buff[1]) > 2 or len(buff[1]) == 0:
                    errors.append(val)
                    continue
        for err in errors:
            valutes.remove(err)
        for val in valutes:
            self.fs.WriteInfoToResultFile(val[0] + " " + val[1] + "  ")

    def WordsWithLenthLessThanSeven(self):
        self.fs.WriteInfoToResultFile("\nWords shoter than 7: ")
        sentences = re.split(r"(?<=[.!?])\s+", self.text)
        result_words = []
        for sentence in sentences:
            words = sentence.split()
            for word in words:
                if len(word) < 7:
                    result_words.append(word)
        for word in result_words:
            self.fs.WriteInfoToResultFile(word + " ")

    def ShortestWordWithABeginning(self):
        words_with_a = re.findall(r'\w+[a]\b', self.text)
        if len(words_with_a) > 0:
            shortest_word = min(words_with_a, key=len)
        else:
            shortest_word = None
        print(shortest_word)
        self.fs.WriteInfoToResultFile("\nThe shortest word ended with a: " + shortest_word)

    def SortedWords(self):
        self.fs.WriteInfoToResultFile("\nSorted words by length in reverse: ")
        words = re.findall(r'\b\w+\b', self.text) 
        sorted_words = sorted(words, key=len, reverse=True)
        for word in sorted_words:
            self.fs.WriteInfoToResultFile(word + " ")
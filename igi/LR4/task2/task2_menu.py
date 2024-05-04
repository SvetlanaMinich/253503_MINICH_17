from task2.textAnalizer import TextAnalizer

def Menu2():
    ta = TextAnalizer()
    ta.CountSentences()
    ta.CountDifferentTypesOfSentences()
    ta.AverageSentenceLength()
    ta.AverageWordLength()
    ta.EmojiCount()
    ta.WordsWithSymbolsFromFtoY()
    ta.FindUSDorRURorEU()
    ta.WordsWithLenthLessThanSeven()
    ta.ShortestWordWithABeginning()
    ta.SortedWords()
    ta.fs.CreateResultZipArchive()
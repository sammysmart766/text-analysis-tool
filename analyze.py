import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet, stopwords

from random_username.generate import generate_username
from nltk.tokenize import word_tokenize, sent_tokenize
import re


nltk.download("wordnet")
nltk.download("averaged_perceptron_tagger_eng")
nltk.download("stopwords")

wordLemmatizer = WordNetLemmatizer()

stopWords = set(stopwords.words("english"))


def welcomeUser():
    print(
        "\nWelcome to the text analysis tool. "
        "I will mine and analyze a body of text from the file you give me."
    )


def Getusername():
    maxAttempts = 3
    Attempts = 0

    while Attempts < maxAttempts:
        if Attempts == 0:
            inputPrompt = "\nTo begin, please enter your username: "
        else:
            inputPrompt = "\nPlease try again: "

        usernameFromInput = input(inputPrompt)

        if len(usernameFromInput) < 5 or not usernameFromInput.isidentifier():
            print(
                "\nYour username must be at least five characters long, "
                "use letters, numbers, or underscores, and have no spaces."
            )
            Attempts += 1
        else:
            return usernameFromInput

    print(
        "\nExhausted all "
        + str(maxAttempts)
        + " attempts. Assigning username instead."
    )
    return generate_username(1)[0]


def greetuser(name):
    print("Hello " + name)


def getArticleText():
    f = open("files/articles.txt", "r")
    rawText = f.read()
    f.close()
    return rawText.replace("\n", " ").replace("\r", "")


def tokenizeSentences(rawText):
    return sent_tokenize(rawText)


def tokenizeWords(sentences):
    words = []

    for sentence in sentences:
        words.extend(word_tokenize(sentence))

    return words


# Get key sentences based on search patterns

def extractKeySentences(sentences, searchPattern):
    matchedSentences = []

    for sentence in sentences:
        if re.search(searchPattern, sentence.lower()):
            matchedSentences.append(sentence)

    return matchedSentences


# Get the average words per sentence, excluding punctuation

def getWordsPerSentence(sentences):
    numSentences = len(sentences)

    if numSentences == 0:
        return 0

    totalWords = 0

    for sentence in sentences:
        totalWords += len(sentence.split(" "))

    return totalWords / numSentences


# Convert part of speech from pos_tag() function
# into wordnet compatible pos tag

posToWordnetTag = {
    "J": wordnet.ADJ,
    "V": wordnet.VERB,
    "N": wordnet.NOUN,
    "R": wordnet.ADV
}


def treebankPosToWordnetPos(partOfSpeech):
    posFirstChar = partOfSpeech[0]

    if posFirstChar in posToWordnetTag:
        return posToWordnetTag[posFirstChar]

    return wordnet.NOUN


# Filter raw tokenized words to only include valid English words

def cleanseWordList(posTaggedWordTuples):
    cleansedWords = []
    invalidWordPattern = "[^a-zA-Z-+]"

    for posTaggedWordTuple in posTaggedWordTuples:
        word = posTaggedWordTuple[0]
        pos = posTaggedWordTuple[1]

        cleansedWord = word.replace(".", "").lower()

        if (
            not re.search(invalidWordPattern, cleansedWord)
            and len(cleansedWord) > 1
            and cleansedWord not in stopWords
        ):
            cleansedWords.append(
                wordLemmatizer.lemmatize(
                    cleansedWord,
                    treebankPosToWordnetPos(pos)
                )
            )

    return cleansedWords


# Get user details

welcomeUser()
username = Getusername()
greetuser(username)


# Extract and tokenize text

articleTextRaw = getArticleText()
articleSentences = tokenizeSentences(articleTextRaw)
articleWords = tokenizeWords(articleSentences)


# Get analytics

stockSearchPattern = (
    "[0-9]|[%$€£]|thousand|million|billion|trillion|profit|loss"
)

keySentences = extractKeySentences(
    articleSentences,
    stockSearchPattern
)

wordsPerSentence = getWordsPerSentence(articleSentences)

wordsPosTagged = nltk.pos_tag(articleWords)

articleWordsCleansed = cleanseWordList(wordsPosTagged)


# Print for testing

print("GOT:")
print(articleTextRaw)
print(articleSentences)
print(articleWords)
print(wordsPosTagged)
print(keySentences)
print(wordsPerSentence)
print(articleWordsCleansed)
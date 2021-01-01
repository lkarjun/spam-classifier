import re
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords


def input_process(message: str) -> str:

    wordnet = WordNetLemmatizer()
    capturing_words = re.sub('[^a-zA-Z]', ' ', message)
    lowering_spliting = capturing_words.lower().split()
    rm_unwanted_words = [wordnet.lemmatize(word) for word in lowering_spliting
                            if not word in set(stopwords.words('english'))]
    finalized_word = ' '.join(rm_unwanted_words)

    return finalized_word

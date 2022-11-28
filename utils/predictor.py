import re
import pickle
import docx2txt
import nltk
nltk.download('omw-1.4')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer

wo = WordNetLemmatizer()
loaded_vectorizer = pickle.load(open('././models/vectorizer.pkl', "rb"))
loaded_model = pickle.load(open('././models/prediction.pkl', "rb"))


def preprocess(data):
    # preprocess
    a = re.sub('[^a-zA-Z]', ' ', data)
    a = a.lower()
    a = a.split()
    a = [wo.lemmatize(word) for word in a]
    a = ' '.join(a)
    return a


def read_docx():
    # read in word file
    result = docx2txt.process("././data/tips.docx")
    return result


def predict(text):
    a = preprocess(text)
    example_counts = loaded_vectorizer.transform([a])
    prediction = loaded_model.predict(example_counts)
    print(prediction)
    if prediction[0] == 0:
        output = 'Positive'
        tips = "Stay positive! Stay healthy!"
    elif prediction[0] == 1:
        output = 'Depressive'
        tips = read_docx()

    # print(prediction)
    return output, tips

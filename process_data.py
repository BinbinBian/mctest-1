import re
from object_model import *

# read raw data
def readRawData(path):

    # passages and correct answer file names
    passages_file = path + '.tsv'
    correct_answers_file = path + '.ans'

    # read passages
    f = open(passages_file)
    raw_passages = f.read()
    f.close()

    # read correct answers
    f = open(correct_answers_file)
    raw_correct_answers = f.read()
    f.close()

    return raw_passages, raw_correct_answers

# converts answers from characters to integers
# so they can be used as indices into the answer set
def letterToNum(answerIndex):
    conversion = {'A':0,'B':1,'C':2,'D':3}
    return conversion[answerIndex]

# parse correct answers

def processData(path):
    raw_passages, raw_correct_answers = readRawData(path)

    # correct answers
    correct_answers = [list(map(letterToNum,answer_set.split('\t'))) for answer_set in raw_correct_answers.split('\r\n') if len(answer_set) > 0]

    # parse passages
    data = []
    passages = raw_passages.split('\r\n')[:-1] # split passages
    for (i,passage) in enumerate(passages):
        elements = passage.split('\t') # split passage elements
        title = elements[0] # get title
        story = elements[2] # get story, replace escaped newlines and tabs
        story = re.sub(r'\\newline','\n',story)
        story = re.sub(r'\\tab','\t',story)
        questions = []
        for j in range(4):
            question_elements = elements[3+5*j:3+5*(j+1)] # get question elements
            qtype, qtext = question_elements[0].split(': ') # get question type and text
            answers = [Answer(text) for text in question_elements[1:5]] # get answers
            correct_answer = answers[correct_answers[i][j]] # get correct answer (from answer data)
            question = Question(qtext,qtype,answers,correct_answer) # define question
            questions[j:] = [question]
        p = Passage(title,story,questions) # define passage
        data[i:] = [p]

    return data


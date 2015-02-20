import nltk
import re
from object_model import *

# stories, questions, answers
f = open('data/mc160.dev.txt')
raw = f.read()
f.close()

# correct answers
f = open('data/mc160.dev.ans')
raw_ans = f.read()
f.close()

# converts answers from characters to integers
# so they can be used as indices into the answer set
def letterToNum(answerIndex):
    conversion = {'A':0,'B':1,'C':2,'D':3}
    return conversion[answerIndex]

# actual outputs
dev_answers = [list(map(letterToNum,answer_set.split('\t'))) for answer_set in raw_ans.split('\r\n') if len(answer_set) > 0]

dev_data = []
passages = raw.split('\r\n\r\n\r\n')[:-1]
for (i,passage) in enumerate(passages):
    passage = re.sub(r'\s+',' ',passage) # get rid of whitespace
    passage = re.sub(r'\*.*\(s\)\: \d+ ','',passage) # get rid of headers
    elements = re.split(r'\d:',passage) # split story and questions
    story,questions = elements[0].strip(),elements[1:] #split, remove whitespace
    qs = []
    for (j,question) in enumerate(questions):
        q_type, qa = question.split(': ') # split question type
        qa_split = re.split(r'..\) ',qa) # split question and each answer
        question, answers = qa_split[0], qa_split[1:]
        q_type = q_type.strip() # remove whitespace
        q_text = question.strip() # remove whitespace
        answers = [Answer(a.strip()) for a in answers] # remove whitespace
        q = Question(q_text,q_type,answers)
        qs[j:] = [q]
    p = Passage('mc160.dev.'+str(i),story,qs)
    dev_data[i:] = [p]



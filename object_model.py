import nltk

class Text(object):
    
    def __init__(self, text):
        self.text = text
        self.words = nltk.word_tokenize(text)
        self.sents = nltk.sent_tokenize(text)

class Passage(Text):

    def __init__(self, title, story, questions):
        Text.__init__(self,story)
        self.title = title
        self.questions = questions
    
    def display(self):
        print self.text
        for q in self.questions:
            print '\n' + q.text + ' (' + q.qtype + ')'
            for a in q.answers:
                print '\t' + a.text
            print '\n\tCorrect Answer: ' + q.correct_answer.text
        
class Question(Text):
    
    def __init__(self, qtext, qtype, answers, correct_answer):
        Text.__init__(self,qtext)
        self.qtype = qtype
        self.answers = answers
        self.correct_answer = correct_answer

class Answer(Text):
    
    def __init__(self, atext):
        Text.__init__(self,atext)
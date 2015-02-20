class Passage(object):

    def __init__(self, title, story, questions):
        self.title = title
        self.story = nltk.word_tokenize(story)
        self.questions = questions
    
    def display(self):
        print ' '.join(self.story)
        for q in self.questions:
            print '\n' + ' '.join(q.qtext) +' ('+q.qtype+')'
            for a in q.answers:
                print '\t' + ' '.join(a.atext)
        
class Question(object):
    
    def __init__(self, qtext, qtype, answers):
        self.qtext = nltk.word_tokenize(qtext)
        self.qtype = qtype
        self.answers = answers

class Answer(object):
    
    def __init__(self, atext):
        self.atext = nltk.word_tokenize(atext)
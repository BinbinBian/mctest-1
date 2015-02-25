import nltk

## different answer scorers

# selects answer that appears most in the story
# ignores words in answer that also appear in the question
def overlapScorer(passage,question,answer):
    return len([word for word in passage.words if word in set(answer.words).difference(question.words)])

# does not ignore words in answer that also appear in the question
def overlapScorer2(passage,question,answer):
    return len([word for word in passage.words if word in answer.words])

# like scorer1 but excludes stop words
def overlapScorer3(passage,question,answer):
    stopwords = nltk.corpus.stopwords.words(fileids=['english'])
    return len([word for word in passage.words if word in set(answer.words).difference(question.words+stopwords)])

def main():
    return overlapScorer2

if __name__ == '__main__':
    main()

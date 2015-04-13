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

# selects answer that appears most in the story
# ignores words in answer that also appear in the question
# if detects a negation, inverts answers
def overlapScorerNeg(passage,question,answer):
    score = len([word for word in passage.words if word in set(answer.words).difference(question.words)])
    if len(set(['not','n\'t']).difference(question.words)) < 2:
        return -1*score
    return score

def main():
    return overlapScorer2

if __name__ == '__main__':
    main()

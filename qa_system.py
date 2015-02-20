## different answer scorers

# scores highest the answer with words that appears most in the story
# ignores words in answer that also appear in the question
def overlapScorer(story,question,answer):
    return len([word for word in story if word in set(answer).difference(question)])

# does not ignore words in answer that also appear in the question
def overlapScorer2(story,question,answer):
    return len([word for word in story if word in answer])

# like scorer1 but excludes stop words
def overlapScorer3(story,question,answer):
    stopwords = nltk.corpus.stopwords.words(fileids=['english'])
    return len([word for word in story if word in set(answer).difference(question+stopwords)])


# answers a queston using an answer scorer
def answerQuestion(story,question,answers,scorer):
            
    best_score = 0
    best_answer = answers[0]
    for answer in answers:
        score = scorer(story,question,answer)
        if  score > best_score:
            best_answer = answer
            best_score = score
            
    return best_answer


# scores an answerer on passages
def evaluateOnPassages(scorer,passages,correct_answers,verbose = False):
    num_correct = 0
    num_total = sum([len(p.questions) for p in passages])
    for (i,passage) in enumerate(passages):
        if verbose: print ' '.join(passage.story) + '\n'
        for (j,question) in enumerate(passage.questions):
            answers = [a.atext for a in question.answers]
            best_answer = answerQuestion(passage.story,question.qtext,answers,scorer)
            best_index = [k for (k,a) in enumerate(question.answers) if a.atext == best_answer][0]
            correct_index = correct_answers[i][j]
            if best_index == correct_index: num_correct += 1
            if verbose:
                print ' '.join(question.qtext)
                for a in question.answers: print '\t' + ' '.join(a.atext)
                print '\n\tSelected answer: ' + ' '.join(best_answer)
                print '\tCorrect answer: ' + ' '.join(question.answers[correct_index].atext) + '\n'
    return num_correct / num_total


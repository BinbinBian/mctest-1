from __future__ import division
import sys
from process_data import *
from object_model import *
import answer_scorers


# answers a queston using an answer scorer
def answerQuestion(passage,question,answers,scorer):
            
    best_score = 0
    best_answer = answers[0]
    for answer in answers:
        score = scorer(passage,question,answer)
        if  score > best_score:
            best_answer = answer
            best_score = score
            
    return best_answer


# scores an answerer on passages
def evaluateOnPassages(scorer,passages,verbose = False):
    num_correct = 0
    num_total = sum([len(p.questions) for p in passages])
    for (i,passage) in enumerate(passages):
        if verbose: print passage.text + '\n\n***\n'
        for (j,question) in enumerate(passage.questions):
            best_answer = answerQuestion(passage,question,question.answers,scorer)
            if best_answer == question.correct_answer: num_correct += 1
            if verbose:
                print question.text
                for answer in question.answers: print '\t' + answer.text
                print '\n\tSelected answer: ' + best_answer.text
                print '\tCorrect answer: ' + question.correct_answer.text + '\n'
    return num_correct / num_total


# takes two arguments: path to data and name of answer scorer
def main():
    passages = processData(sys.argv[1])
    results = evaluateOnPassages(answer_scorers.main(),passages, verbose = False)
    print results


if __name__ == '__main__':
    main()

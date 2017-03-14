from enum import Enum
import random
class Arithematic(Enum):
    ADD = 1
    SUB = 2
    MUL = 3
class Question(object):
    def __init__(self, level):
        self.ans = 0
        self.guess = 0
        self.level = level
    def setAnswer(self,ans):
        self.ans = ans
    def setGuess(self,guess):
        self.guess = guess
    def getLevel(self):
        return self.level
    def checkAnswer(self):
        return self.ans == self.guess
class MathQuestion(Question):
    def __init__(self, operator, level):
        self.operand1 = 0
        self.operand2 = 0
        self.operator = Arithematic(operator)
        return super().__init__(level)
    def generateQuestion(self):
        start = 10**super().getLevel()
        stop = start*10 - 1
        self.operand1 = random.randint(start, stop)
        self.operand2 = random.randint(start, stop)
        if(self.operator == Arithematic.ADD):
            super().setAnswer(self.operand1+self.operand2)
        elif(self.operator == Arithematic.SUB):
            super().setAnswer(self.operand1-self.operand2)
        elif(self.operator == Arithematic.MUL):
            super().setAnswer(self.operand1*self.operand2)
    def printQuestion(self):
        if(self.operator == Arithematic.ADD):
            return int(input(str(self.operand1) + " + " + str(self.operand2) + " = "))
        elif(self.operator == Arithematic.SUB):
            return int(input(str(self.operand1) + " - " + str(self.operand2) + " = "))
        elif(self.operator == Arithematic.MUL):
            return int(input(str(self.operand1) + " * " + str(self.operand2) + " = "))
    def setGuess(self, guess):
        return super().setGuess(guess)
    def checkAnswer(self):
        return super().checkAnswer()
quiz = []
score = 0
def createQuiz(total, level):
    for i in range(total):
        question = MathQuestion(random.randint(1,3), level)
        question.generateQuestion()
        quiz.append(question)
def startQuiz():
    global score
    for question in quiz:
        question.setGuess(question.printQuestion())
        score+=question.checkAnswer()
def processLevel(level):
    if(level < 1):
        level = 1
    if(level > 3):
        level = 3
    return level-1
length = int(input("Enter Total Number of Questions in Quiz: "))
level = int(input("Enter Level(1,2,3) of Quiz: "))
createQuiz(length, processLevel(level))
startQuiz()
print("You got " + str(score) + " right!")

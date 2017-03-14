class Examination(object):
    def __init__(self, date, startTime, endTime, subject, location):
        self.date = date
        self.t0 = startTime
        self.t1 = endTime
        self.sub = subject
        self.loc = location
    def isSubject(self,sub):
        return self.sub.lower()==sub.lower()
    def display(self):
        print("********Exam********")
        print("Date\t\t: " + str(self.date))
        print("Start Time\t: " + str(self.t0))
        print("End Time\t: " + str(self.t1))
        print("Subject\t\t: " + str(self.sub))
        print("Location\t: " + str(self.loc))
        print(" ")

def searchBySubject(exams, subject):
    for exam in exams:
        if exam.isSubject(subject):
            exam.display()
            break
    else:
        print("no Exam of subject '%s' is scheduled" % subject)
    
exams = []
for i in range(5):
    exams.append(Examination(input("Enter Date: "),
                             input("Enter Start Time: "),
                             input("Enter End Time: "),
                             input("Enter Subject: "),
                             input("Enter Location: ")
                             )
                 )
while True:
    subject = input("Enter Subject to search or '-1' to quit: ")
    if subject == '-1':
        break
    else:
        searchBySubject(exams, subject)

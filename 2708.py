class Lesson:
    def __init__(self, lessonTitle : str, durationMinutes : int, requiresLab : bool) -> None:
        self.__lessonTitle = lessonTitle
        self.__durationMinutes = durationMinutes
        self.__requiresLab = requiresLab

    def outputLessonDetails(self):
        print(self.__lessonTitle)

class Assessment:
    def __init__(self,assessmentTitle : str,maxMarks : int) -> None:
        self.__assessmentTitle = assessmentTitle
        self.__maxMarks = maxMarks

    def OutputAssessmentDetails(self):
        print("Title : {0} , Maximum Marks : {1}".format(self.__assessmentTitle,self.__maxMarks))



class Course:
    def __init__(self,courseTitle : str, maxStudents : int) -> None:
        self.__courseTitle = courseTitle
        self.__maxStudents = maxStudents
        self.__numberOfLessons = 0
        self.__courseLesson = []
        self.__courseAssessment = Assessment
    

    def AddLesson(self,lesson : Lesson):
        if(self.__numberOfLessons <= 50):
            self.__numberOfLessons += 1
            self.__courseLesson.append(lesson)
        else:
            print("This course has too many lessons.")

    def AddAssessment(self,assessment : Assessment):
        self.__courseAssessment = assessment



maths = Course("math","20")
maths.AddAssessment(Assessment("Intro to CALC","10"))
for _ in range(60):
    maths.AddLesson(Lesson("Calc",60,False))


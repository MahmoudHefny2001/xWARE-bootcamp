import department
import course
import faculty
import professor
import students
import exams

#exit
while True:
    print("Enter 1 to read a department info")
    print("Enter 2 to update specific department ")
    print("Enter 3 to retrieve list ")
    print("Enter 4 to read a specific department ")
    print("Enter 5 to read Faculty info")
    print("Enter 6 to update a faculty info ")
    print("Enter 7 to link professors to Faculty ")
    print("Enter 8 to link departments to Faculty ")
    print("Enter 9 to retreive the content")
    print("Enter 10 to link professor to course")
    print("Enter 11 to lnk exams to course")
    print("Enter 12 to update specific course info")
    print("Enter 13 to retreive the content")
    print("Enter 14 to reading course info")
    print("Enter 15 to reading All exams info")
    print("Enter 16 to update Specific Exam info")
    print("Enter 17 to read Specific Exam info")
    print("Enter 18 to retrieve all exam info ")
    print("Enter 19 to reading all students info")
    print("Enter 20 to update specific students info")
    print("Enter 21 to read specific students info")
    print("Enter 22 to retrieve all students info ")
    print("Enter 23 to link course To Subject")
    print("Enter 24 to link professor To Subject")
    print("Enter 25 to reading all professors info")
    print("Enter 26 to update specific professor info")
    print("Enter 27 to read specific professor info")
    print("Enter 28 to retrieve all professor info ")
    print("Enter 29 to exit from program")
    print(" ")
    print("Your answer: ")
    x = int(input())
    if (x == 1):
        department.reading_department()
    elif (x==2):
        department.update_department()
    elif(x==3):
        print(department.retrieve_list())
    elif(x==4):
        print(department.read_specific_department_info())
    elif (x == 5):
        faculty.reading_faculty()
    elif (x==6):
        faculty.update_faculty()
    elif(x==7):
        faculty.link_professors_to_faculty()
    elif(x==8):
        faculty.link_departments_to_faculty()
    elif(x==9):
        faculty.retrieve_list()
    elif (x == 10):
        course.link_professors_to_course()
    elif (x==11):
        course.link_exams_to_course()
    elif(x==12):
        course.update_course()
    elif(x==13):
        print(course.retrieve_list())
    elif (x==14):
        course.reading_course()
    elif (x == 15):
        exams.reading_exams()
    elif (x==16):
        exams.update_specific_exams_info()
    elif(x==17):
       print(exams.read_specific_exams_info())
    elif(x==18):
       print(exams.retrieve_list())
    elif (x == 19):
        students.Reading_All_Subjects_info()
    elif (x==20):
        students.update_specific_studentss_info()
    elif(x==21):
       print(students.read_specific_studentss_info)
    elif(x==22):
       students.retrieve_list()
    elif (x == 23):
        students.Link_course_To_Subject()
    elif (x==24):
        students.Link_professor_To_Subject()
        
    elif (x == 25):
        professor.reading_professors()
    elif (x==26):
        professor.update_specific_professors_info()
    elif(x==27):
       print(professor.read_specific_professor_info())
    elif(x==28):
       print(professor.retrieve_list())
    elif(x==29):
        break
    else :
        print("you entered invalid number.")

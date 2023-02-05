class Grade:
    def __init__(self, stu_id, crc_code, score):
        self.student_id = stu_id
        self.course_code = crc_code
        self.score = score


class CourseUtil:
    data_address = 0
    def set_file(self, address):
        self.data_address = address
        with open(address , "r") as file : 
            self.data = str(file.read())
        
        self.data = self.data.split("\n")
        self.data_list = []
        for num in range(len(self.data)) : self.data_list.append(self.data[num].split(" "))

    def load(self, line_number):
        if 0 < line_number <= len(self.data_list) : 
            new_object = Grade(int(self.data_list[line_number -1][0]) , int(self.data_list[line_number -1][1]) , float(self.data_list[line_number -1][2]))
            return new_object
        return None

    def calc_student_average(self, student_id):
        try : 
            return sum([float(user[2]) for user in self.data_list if user[0] == str(student_id) ]) / len(list(filter(lambda x : x[0] == str(student_id) , self.data_list)))
        except :
            return 0.0
    def calc_course_average(self, course_code):
        try :
            return sum([float(user[2]) for user in self.data_list if user[1] == str(course_code) ]) / len(list(filter(lambda x : x[1] == str(course_code) , self.data_list)))
        except : 
            return 0.0

    def count(self) :
        return len(self.data_list)
    
    def save(self, grade):
        test = True
        for user in range(len(self.data_list)) :
            if self.data_list[user][0] == str(grade.student_id) and self.data_list[user][1] == str(grade.course_code) : 
                test = False
                break
        if test :
            with open(self.data_address , "a") as file :
                file.write(f"\n{grade.student_id} {grade.course_code} {grade.score}")
            self.data_list.append([f"{grade.student_id}" , f"{grade.course_code}" , f"{grade.score}"])

from console_color import *
from Student import Student

student_database = []


def welcome_screen():
    print(YELLOW, '****** Welcome To NIIT Student Management System ******')
    user_input = int(input('1. Add Student\n'
                           '2. View all Student details\n'
                           '3. Search for Student details\n'
                           '4. Delete Student Info\n'
                           '5. Update Student INfo\n'
                           '6. About System\n'
                           '7. Exit Application\n\n'
                           'Please Provide your request: '))
    user_option(user_input)


# user option
def user_option(user_input):
    if user_input == 1:
        responses = 'yes'
        while responses == 'yes':
            student_info = add_student()
            user_ans = input(BLUE + 'Do you want to save info?(y/n): ').lower()
            if user_ans == 'y':
                student_database.append(student_info)
                print(GREEN, f'{student_info.get_first_name()}'
                             f'{student_info.get_middle_name()}'
                             f'{student_info.get_last_name()} '
                             f'your details is save successful')
            elif user_ans == 'n':
                user_ans = input('Do you really want to cancel?(y/n): ').lower()
                if user_ans == 'y':
                    welcome_screen()
                else:
                    student_database.append(student_info)
            else:
                pass
            responses = input('Is there another Student?(y/n)').lower()

    if user_input == 2:
        pass
    if user_input == 3:
        pass
    if user_input == 4:
        pass
    if user_input == 5:
        pass
    if user_input == 6:
        about_us()
    if user_input == 7:
        close_program()
    else:
        invalid_request()


def invalid_request():
    print(RED, 'Request Invalid, Please Try Again.\n Thank You!!!')
    welcome_screen()


# about function
def about_us():
    print(BLUE, '****** This System keep track of Student Details. ******')
    welcome_screen()


# this is the close function
def close_program():
    print(BLUE, '**** Thank You for using our NIIT system, Hope to see you Again ****')
    exit(1)


def add_student():
    print(YELLOW, '**** Fill Detail below to Add Student ****', WHITE)
    sid = input('Provide Student ID: ')
    f_name = input('Provide First Name: ')
    m_name = input('Provide Middle Name: ')
    l_name = input('Provide Last Name: ')
    dob = input('Provide DOB e.g(dd-mm-yy): ')
    course = input('Provide Course: ')
    period = input('Provide Period: ')

    # creating student object
    student_ifo = Student(sid, f_name, m_name, l_name, dob, course, period)
    return student_ifo


welcome_screen()

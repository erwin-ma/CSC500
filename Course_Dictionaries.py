# creates a function to print the course details
def print_course_details(course_number):
    '''
    Print room number, instructor and meeting time.
    Input (string): course_number
    '''
    print(f"Room Number: {room_dict[course_number]}")
    print(f"Instructor: {instructor_dict[course_number]}")
    print(f"Meeting Time: {meeting_time_dict[course_number]}\n")
 
def get_course_number():
    '''
    Prompt the user for a course number until a valid one is entered
    '''
    while True:
        # first, print available course numbers
        print("Available Courses: CSC101, CSC102, CSC103, NET110, COM241")
        # get input
        course_number = input("Course number (or 'q' to quit): ")
        
        # check if user wants to quit.
        if course_number == 'q':
            return None
        
        # check if it's valid
        if course_number in room_dict:
            return course_number
        else:
            print("Bad course number!")
            print("Course prefixes are capitalized. Please try again.")
 
if __name__ == '__main__':
    
    # create dictionaries:
    # Dictionary for course_number, room_number pairs
    room_dict = {
        'CSC101': '3004',
        'CSC102': '4501',
        'CSC103': '6755',
        'NET110': '1244',
        'COM241': '1411'
    }
 
    # Dictionary for course_number, instructor pairs
    instructor_dict = {
        'CSC101': 'Haynes',
        'CSC102': 'Alvarado',
        'CSC103': 'Rich',
        'NET110': 'Burke',
        'COM241': 'Lee'
    }
 
    # Dictionary for course_number, meeting_time pairs
    meeting_time_dict = {
        'CSC101': '8:00 a.m.',
        'CSC102': '9:00 a.m.',
        'CSC103': '10:00 a.m.',
        'NET110': '11:00 a.m.',
        'COM241': '1:00 p.m.'
    }
 
    # while not specified in assignment, creating a loop 
    # so demonstration is easier.
    print("Welcome to CSU Global!")
    while True:
        # Ask user for a course number
        print("Please choose a course number to get your room, instructor, and meeting times.")
        
        # call input function above
        course_number = get_course_number()
    
        if course_number is None:
            print("Thank you for using the CSU Global Registrar. Bye!")
            break
 
        # call print function above
        print_course_details(course_number)

def letter_grade(grade):
    '''
    Args:
        score (float): the grade of a student in the range of 0-100
    Returns:
        The letter grade associated with the student's number grade
        90 -> A
        80 -> B
        and so on
    '''
    if (grade > 100) or (grade < 0):
        return "X"
    if (grade >= 90):
        return "A"
    if (grade >= 80):
        return "B"
    if (grade >= 70):
        return "C"
    if (grade >= 60):
        return "D"
    if (grade < 60) and (grade >= 0):
        return "E"
    
def pass_or_fail(letter_grade):
    '''
    The pass_or_fail function takes in one argument, letter_grade, and returns
    pass if the grade is either A, B, C, or D, and returns Fail otherwise. 

    Args:
        letter_grade (string): A single character representing a letter grade
    Returns:
        Pass if the arguement is either 'A', 'B', 'C', or 'D', Fail otherwise
    '''
    # Check if the length of letter_grade does not equal 1
    if (len(letter_grade) != 1):
        return "Error"
    if (letter_grade == "A" or letter_grade == "B" or letter_grade == "C"
        or letter_grade == "D"):
        return "Pass"
    
    return "Fail"

def point_grade(score, total_points):
    '''
    The point_grade function takes in two floats, score and total_points
    and returns score divided by total points to give the grade point as a 
    percentage
    
    Args:
        score, total_points (floats):
    Returns: 
        The percentage grade rounded to two decimal points
    '''
    percentage_grade = (score / total_points) * 100
    return round(percentage_grade, 2)

def get_grade_results(score, total_points):

    grade_score = point_grade(score, total_points)
    letter = letter_grade(grade_score)
    pass_fail = pass_or_fail(letter)

    return f"Your grade is {grade_score} ({letter} - {pass_fail})"
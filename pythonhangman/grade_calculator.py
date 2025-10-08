#student Grade Calculator

# "Grade"  >= 70 = 'A'
# "Grade"  >= 60 = 'B'
# "Grade"  >=  50 = 'C'
# "Grade"  >= 40 =  'D'
# "Grade"  <  40 =  'F'
#calculate total score
def calculate_grade(average):
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return"D"
    else:
        return"F"
    
    def calculate_score():
        student_name = "Mike"
        #calculate total, average and grade for a student
        subjects = ["English", "Maths", "Science", "History", "Civic"]
        scores = [85,78,65,55,90]
    
        total = sum(scores)
        average = total / len(scores)
        grade = calculate_grade(average)

        print("Result")
        print("Student Name:",student_name)
        print("Total score:",total)
        print("Average Score:",average)
        print(f"Grade:{grade}/n")
    
    #run the program
    calculate_score()



#calculate grade for multiple students using a loop
def calculate_scores():
    subjects = ["English", "Maths", "Science", "History", "Civic"]

    #Each student's scores dictionary
    students = {
                "Mike":[85,78,65,55,90],
                "Mary":[ 79, 84, 58,  98, 71],
                "Sam":[ 66, 81, 73, 62,  79],
                "James":[ 75, 88, 95, 62, 77],
               "Vincent":[70, 65, 55, 67, 81],
              "Kizito":[ 98, 85, 93, 94, 90]
                }

    #loop through each student
    for name, scores in students.items():
        total = sum(scores)
        average = total / len(scores)
        grade = calculate_grade(average)

        print("==================================")
        print(f"Student Name: {name}")
        print(f"Subjects: {subjects}")
        print(f"Total Score: {total}")
        print(f"Average Score: {average:.2f}")
        print(f"Grade:{grade}")
    print("==============================================") 

calculate_scores()   


#Save result to a text file named results.txt.
# Student Grade Calculator (User Input + Save to results.txt)

# Function to calculate grade from average
def calculate_grade(average):
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


# Main function
def calculate_scores():
    subjects = ["English", "Maths", "Science", "History", "Civic"]

    # Ask how many students to enter
    num_students = int(input("Enter number of students: "))

    students = {}

    # Collect input for each student
    for i in range(num_students):
        print("\n====================================")
        name = input(f"Enter name of student {i + 1}: ")

        scores = []
        for subject in subjects:
            score = float(input(f"Enter score for {subject}: "))
            scores.append(score)

        students[name] = scores

    # Prepare file to save results
    with open("student_results.txt", "w") as file:
        file.write("========= STUDENT RESULTS =========\n")

        # Process and display results
        for name, scores in students.items():
            total = sum(scores)
            average = total / len(scores)
            grade = calculate_grade(average)

            # Prepare result text
            result = (
                "====================================\n"
                f"Student Name: {name}\n"
                f"Subjects: {subjects}\n"
                f"Scores: {scores}\n"
                f"Total Score: {total}\n"
                f"Average Score: {average:.2f}\n"
                f"Grade: {grade}\n"
            )

            # Print to screen
            print(result)

            # Write to file
            file.write(result)

        file.write("====================================\n")

    print("\n✅ All results have been saved to 'student_results.txt'!")


# Run the program
calculate_scores()


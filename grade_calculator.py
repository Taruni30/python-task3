
#grade calculator

try:
    marks = float(input("Enter your marks (0–100): "))

    #handling invalid marks
    if marks < 0 or marks > 100:
        print("Invalid marks! Please enter marks between 0 and 100.")

    else:
        #Nested conditions with logical operators
        if marks >= 90:
            grade = "A+"
            message = "Excellent"
        elif marks >= 80 and marks < 90:
            grade = "A"
            message = "good"
        elif marks >= 70 and marks < 80:
            grade = "B"
            message = "Good"
        elif marks >= 60 and marks < 70:
            grade = "C"
            message = "Satisfactory"
        elif marks >= 50 and marks < 60:
            grade = "D"
            message = "can do better"
        else:
            grade = "F"
            message = "FAIL"

        print("Grade:", grade)
        print("Message:", message)

except ValueError:
    print("Invalid input")
    



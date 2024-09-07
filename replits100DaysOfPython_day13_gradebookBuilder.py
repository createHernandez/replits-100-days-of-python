print("Exam Grade Calculator")
print()

exam_name = input("Name of exam: ")
print()
max_score = int(input("Max. Possible Score: "))
print()
student_score = int(input("Your score: "))
print()

grade = round(student_score / max_score * 100)

if grade >= 90:
  print(f"You got a \033[32m{grade}%\033[0m which is an A")
elif grade >= 80 and grade < 90:
  print(f"You got a \033[33m{grade}%\033[0m which is an B")
elif grade >= 70 and grade < 80:
  print(f"You got a \033[33m{grade}%\033[0m which is an C")
elif grade >= 60 and grade < 70:
  print(f"You got a \033[31m{grade}%\033[0m which is an D")
elif grade < 60 and grade >= 0: 
  print(f"You got a \033[31m{grade}%\033[0m which is an F")
else: 
  print(f"Error! Unable to proccess grade. Please try again.")
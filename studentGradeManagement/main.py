import json

students = {
	"john": 85,
	"mary": 72,
	"peter": 40,

}

print(len(students))
try:

    with open("list.json", "r") as file:
        students = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    students = {}

def grade():
	print("\n ==== Student Grade Manager ==== \n")

	while True:	

		try:
			operation = int(input("1. Add student\n2. View all students\n3. Search student\n4. Update score\n5. Delete student\n6. Show passed students\n7. Show failed students\n8. Sort by score\n9. Sort by name\n10. Show class statistics\n11. Exit  "))

		except ValueError:
			print("\033[31m select from 1-11 to continue \033[0m")
			continue

			

		match operation:
			case 1:
				studentName = input("Enter name: ").strip().lower()

				if studentName in students:
					print("Student already exists.")
					continue
				else:

					try:
						studentScore = int(input("Enter score:  "))
						
					except ValueError:
						print("Score most be a number")
						continue

					students[studentName] = studentScore
			case 2:
				if len(students) > 0:
					print("student names and scores")
					for student,score in students.items():
						print(f"========{student}  :  {score}========")
				else:
					print("\n \033[31m ====Empty list enter 1 to add ==== \033[0m \n")
					continue

			case 3:
				studentName = input("Enter name: ").strip().lower()

				if studentName in students:
					print(f"\n {studentName} scored {students[studentName]} \n")
				else:
					print("\n \033[31m Student not found \033[0m \n")
					continue

			case 4:
				studentName = input("Enter student: ").strip().lower()

				if studentName  in students:

					try:
						newScore = int(input("Enter new score: "))

					except ValueError:
						print("Enter score to save")
						
					students[studentName] = newScore
					print(students)
				else:
					print("\n \033[31m Student not found \033[0m \n")

			case 5:
				studentName = input("Enter student:  ").strip().lower()

				if studentName in students:

					del(students[studentName])
				else:
					print("\n \033[31m student not found \033[0m")

			case 6:
				score = []
				for studentName in students:
					score.append(students[studentName])
						
					passScore = list(filter(lambda x:x >= 50, score))

				print(passScore)
			
			case 8:
				sortedScore = dict(sorted(students.items(), key=lambda student: student[0]))

				for studentName, score in students.items():
					print(f"\n {studentName} : {score} \n")

			case 9:
				sortedName = dict(sorted(students.items()))

				for studentName, score in students.items():
					print(f"\n {studentName} : {score} \n")


				print(sortedScore)
			case 11:
				break
	with open("list.json", "w") as data:
		json.dump(students,data,indent=3)


	
	
grade()
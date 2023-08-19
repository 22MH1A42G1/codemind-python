# Input marks for five subjects
english, maths, physics, chemistry, computer_science = map(int, input().split())

# Check if the student has more than 34 marks in EACH subject
if english > 34 and maths > 34 and physics > 34 and chemistry > 34 and computer_science > 34:
    print("PASSED")
else:
    print("FAILED")
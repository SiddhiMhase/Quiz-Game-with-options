print("Welcome to the quiz game")

# List of questions
questions = (
    "How many elements are in the periodic table?: ",
    "Which animal lays the largest eggs?: ",
    "What is the most abundant gas in the earth's atmosphere?: ",
    "How many bones are in the human body?: ",
    "Which planet in the solar system is the hottest?: "
)

# List of options for each question
options = (
    ("A.116", "B.117", "C.118", "D.119"),
    ("A.Whale", "B.Crocodile", "C.Elephant", "D.Ostrich"),
    ("A.Nitrogen", "B.Oxygen", "C.Carbon-Dioxide", "D.Hydrogen"),
    ("A.206", "B.207", "C.208", "D.209"),
    ("A.Mercury", "B.Venus", "C.Earth", "D.Mars")
)

# Correct answers
answers = ("C", "D", "A", "A", "B")

guesses = []  # Store user guesses
score = 0  # Initialize score
question_num = 0  # Initialize question number

# Start the quiz
for question in questions:
    print(".......................................................................")
    print(question)
    
    # Display options for the current question
    for option in options[question_num]:
        print(option)
    
    # Get the user's guess
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    
    # Check if the guess is correct
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    
    question_num += 1
    print(".......................................................................")

# After all questions have been asked, show the results
print(".......................RESULTS......................")
print(".......................................................................")
print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

# Calculate and display the score percentage
score_percentage = (score / len(questions)) * 100
print(f"Your score is: {score_percentage}%")

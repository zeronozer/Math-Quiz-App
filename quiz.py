import os
import csv
import time
import random
from datetime import datetime 

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12 
TOTAL_PROBLEMS = 10
MAX_SCORE = TOTAL_PROBLEMS * 10
WRONG_ANSWER_PENALTY = 10 
TIME_PENALTY_FACTOR = 0.5 

class Entry:
  def __init__(self, name, time, wrong_answers=0):
    self.name = name
    self.time = time
    self.date = datetime.now()
    self.wrong_answers = wrong_answers
    self.overall_score = 0

def generate_problem():
  left = random.randint(MIN_OPERAND, MAX_OPERAND)
  right = random.randint(MIN_OPERAND, MAX_OPERAND)
  operator = random.choice(OPERATORS)
  
  expr = str(left) + " " + operator + " " + str(right)
  answer = eval(expr)
  
  return expr, answer

def generate_problem():
  # Generate random problem
  left = random.randint(MIN_OPERAND, MAX_OPERAND)
  right = random.randint(MIN_OPERAND, MAX_OPERAND)
  operator = random.choice(OPERATORS)
  
  expr = str(left) + " " + operator + " " + str(right)
  answer = eval(expr)

  return expr, answer

def run_quiz():
  print("\n-----------------MATH QUIZ------------------")

  wrong_answers = 0

  input("\nPress enter to start!")
  print("----------------------")

  start_time = time.time()

  for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()

    while True:
      guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")  
      if guess == str(answer):
        break
      else:
        wrong_answers += 1
        
  end_time = time.time()
  total_time = round(end_time - start_time, 2)

  return wrong_answers, total_time

def calculate_score(wrong_answers, total_time):
  score = MAX_SCORE - (wrong_answers * WRONG_ANSWER_PENALTY)
  overall_score = score - (total_time * TIME_PENALTY_FACTOR)
  return overall_score  

def update_leaderboard(leaderboard, name, time, wrong_answers):
  overall_score = calculate_score(wrong_answers, time) 

  entry = Entry(name, time, wrong_answers)
  entry.overall_score = overall_score
  entry.date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

  leaderboard.append(entry)
  leaderboard.sort(key=lambda x: x.overall_score, reverse=True)

  with open('leaderboard.csv', 'a') as file:
    writer = csv.writer(file)
    writer.writerow([entry.name, entry.time, entry.wrong_answers, 
                     entry.overall_score, entry.date])

def initialize_leaderboard():
  leaderboard = []
  
  if not os.path.exists('leaderboard.csv'):
    with open('leaderboard.csv', 'w') as file:
      writer = csv.writer(file)
      writer.writerow(['Name', 'Time', 'Wrong_answers', 'Score', 'Date'])

  with open('leaderboard.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader) # skip header
    
    for row in reader:
      if len(row) >= 2:
        name = row[0]
        time = float(row[1])
        wrong_answers = int(row[2])

        entry = Entry(name, time, wrong_answers)

        score = calculate_score(wrong_answers, time)
        entry.overall_score = score

        entry.date = datetime.strptime(row[4], '%Y-%m-%d %H:%M:%S')
        leaderboard.append(entry)

  return leaderboard

def print_leaderboard(leaderboard):
  print("\n----------------LEADERBOARD----------------")
  for i, entry in enumerate(leaderboard[:10]):
    print(f"{i+1}. \t{entry.date}, {entry.name} - Score: {entry.overall_score:.2f}, - Time: {entry.time} secs")


def play_again():
  play_again = input("\nWould you like to play again? (y/n)").lower()
  if play_again == 'y':
    main()
  else:
    print("Thanks for playing!\n")
    exit()

def main():
  
    while True:
        wrong_answers, total_time = run_quiz()

        print("----------------------")
        print("Nice work! You finished in", total_time, "seconds!")

        overall_score = calculate_score(wrong_answers, total_time)
        print(f"You scored:, {overall_score:.2f}")

        name = input("\nEnter your name: ")
        leaderboard = initialize_leaderboard()

        update_leaderboard(leaderboard, name, total_time, wrong_answers)
        print_leaderboard(leaderboard)
        play_again()

if __name__ == "__main__":
  main()
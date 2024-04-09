import random
import matplotlib.pyplot as plt

print("\nDIAGNOSTIC TEST")
programming_questions = [
    "What does IP stand for?",
    "What does DNS stand for?",
    "Which programming language is commonly used for creating Android applications?",
    "What is the function of a router in a network?",
    "What is the purpose of an IDE?",
    "How to make an HTTP request using JavaScript?",
    "What is the binary equivalent of the decimal number 16?",
    "What is the output of the following code? print(bin(8))",
    "What is the role of an operating system in a computer?",
    "What is the command to list all files in the current directory? (Unix-based systems)"
]

correct_answers = [
    "Internet Protocol",
    "Domain Name System",
    "Java",
    "To connect different network segments and forward data packets",
    "To help programmers develop software code efficiently",
    "You can make an HTTP request using the fetch() function.",
    "10000",
    "0b1000",
    "To manage computer hardware and provide services to applications.",
    "ls"
]

def simulate_answers(correct_answer, error_probability):
    if random.random() < error_probability:
        return "Wrong answer"
    else:
        return correct_answer

num_runs = 10  # Change this value to set the number of runs (number of students)
threshold = 50.0

# Lists to store the results for each run
run_results = []



for run in range(num_runs):
    correct_counts = [0] * len(programming_questions)
    error_counts = [0] * len(programming_questions)

    for idx, question in enumerate(programming_questions):
        answer = simulate_answers(correct_answers[idx], .5)  # Assuming 50% error probability
        if answer != correct_answers[idx]:
            error_counts[idx] += 1
        else:
            correct_counts[idx] += 1

    # Calculate the accuracy rate for this run
    total_correct = sum(correct_counts)
    total_incorrect = sum(error_counts)
    accuracy_rate = (total_correct / (total_correct + total_incorrect)) * 100

    # Determine the module recommendation based on the accuracy rate
    if accuracy_rate >= threshold:
        module_recommendation = "Advanced Module"
    else:
        module_recommendation = "Beginner Module"

    # Append the results of this run to the run_results list
    run_results.append({
        "run": run + 1,
        "accuracy_rate": accuracy_rate,
        "module_recommendation": module_recommendation
    })

    # Show the results for each run in the console
    print(f"\nRun {run + 1} Results:")
    for idx, question in enumerate(programming_questions):
        print(f"Question {idx}: Correct: {correct_counts[idx]} | Incorrect: {error_counts[idx]}")

    print(f"Total Errors in Run {run + 1}: {sum(error_counts)} | Total Correct in Run {run + 1}: {sum(correct_counts)}")
    print(f"Accuracy Rate for Run {run + 1}: {accuracy_rate:.2f}%")
    print(f"Module Recommendation for Run {run + 1}: {module_recommendation}\n")

print("-" * 60)
print(f"PROGNOSTIC EXAM")

# Calculate the overall error rate and print it for each question
overall_error_rate = [(sum(run["accuracy_rate"] for run in run_results) / num_runs) for _ in range(len(programming_questions))]

# print("RESULT OF OVERALL RUN")
# for idx, question in enumerate(programming_questions):
#     print(f"Question {idx}: Overall Accuracy Rate: {overall_error_rate[idx]:.2f}%")

# Dictionary colors for the graph
colors = ['lightcoral', 'lightskyblue', 'lightgreen', 'lightyellow', 'lightpink', 
          'lightseagreen', 'lightblue', 'lightsalmon', 'lightgreen', 'lightcyan']

# Bar graph for questions and error frequencies
num_questions = list(range(1, len(programming_questions) + 1))  # Create a list with numbers from 1 to the total number of questions
plt.figure(figsize=(12, 6))
bars = plt.bar(num_questions, [run_result["accuracy_rate"] for run_result in run_results], color=colors)
plt.xticks(num_questions, rotation=90)
plt.xlabel('Number of Questions')
plt.ylabel('Accuracy Rate')
plt.title('Accuracy Rate for Each Question')
plt.tight_layout()

# plt.show()

"""

diagnostic exam - check
prognostic exam - adapt

"""
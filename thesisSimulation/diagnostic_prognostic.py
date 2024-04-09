import random
import matplotlib.pyplot as plt
from tqdm import tqdm

def module_recommendation(subject, difficulty_level):
    if difficulty_level == "Advanced":
        return f"Advanced {subject} Module"
    elif difficulty_level == "Beginner":
        return f"Beginner {subject} Module"

print("\nDIAGNOSTIC TEST")

programming_questions = [
    "What is the purpose of an IDE?",
    "How can you create an HTTP request using JavaScript?",
    "Provide the binary representation of the decimal number 16.",
    "When using the `print(bin(8))` code, what will be displayed as output?",
    "Expand the abbreviation 'IP'.",
    "Decode the acronym 'DNS'.",
    "Describe the function of a router within a network.",
    "Convert the decimal number 16 into its binary equivalent.",
    "Given the code `print(bin(8))`, what will be the resulting output?",
    "What is the command to list all files in the current directory? (Unix-based systems)"
]

correct_answers = [
    "To help programmers develop software code efficiently",
    "You can make an HTTP request using the fetch() function.",
    "10000",
    "0b1000",
    "Internet Protocol",
    "Domain Name System",
    "To connect different network segments and forward data packets",
    "Java",
    "0b1000",
    "ls"
]

subjects = {
    "Programming": ["programming", "language", "code", "IDE", "HTTP request"],
    "Networking": ["IP stand for", "DNS stand for", "router", "network"],
    "Data Structures and Algorithms": ["binary equivalent", "output of the following code"],
    "Hardware": ["role of an operating system"],
}

def simulate_answers(correct_answer, error_probability):
    if random.random() < error_probability:
        return "Wrong answer"
    else:
        return correct_answer

def detect_subject(question):
    for subject, keywords in subjects.items():
        if any(keyword.lower() in question.lower() for keyword in keywords):
            return subject
    return "Unknown"

num_runs = 10
threshold = 50.0
threshold_correct = 5

run_results = []

for run in tqdm(range(num_runs), desc="Diagnostic Exam Progress"):
    correct_counts = [0] * len(programming_questions)
    error_counts = [0] * len(programming_questions)
    random.shuffle(programming_questions)
    
    for idx, question in enumerate(programming_questions):
        answer = simulate_answers(correct_answers[idx], .5)
        if answer != correct_answers[idx]:
            error_counts[idx] += 1
        else:
            correct_counts[idx] += 1
    
    total_correct = sum(correct_counts)
    total_incorrect = sum(error_counts)
    accuracy_rate = (total_correct / (total_correct + total_incorrect)) * 100
    
    question_subjects = [detect_subject(question) for question in programming_questions]
    
    if accuracy_rate >= threshold:
        difficulty_level = "Advanced"
    else:
        difficulty_level = "Beginner"
    
    module_rec = module_recommendation("Programming", difficulty_level)
    
    run_results.append({
        "run": run + 1,
        "accuracy_rate": accuracy_rate,
        "module_recommendation": module_rec
    })
    
    print(f"\nRun {run + 1} Results:")
    for idx, question in enumerate(programming_questions):
        print(f"Question {idx + 1} (Subject: {question_subjects[idx]}): Correct: {correct_counts[idx]} | Incorrect: {error_counts[idx]}")
    
    print(f"Total Errors in Run {run + 1}: {sum(error_counts)} | Total Correct in Run {run + 1}: {sum(correct_counts)}")
    print(f"Accuracy Rate for Run {run + 1}: {accuracy_rate:.2f}%")
    print(f"Module Recommendation for Run {run + 1}: {module_rec}\n")

print("-" * 60)

overall_error_rate = [(sum(run["accuracy_rate"] for run in run_results) / num_runs) for _ in range(len(programming_questions))]

print("\nPROGNOSTIC EXAM")

adjusted_error_probabilities = [error_rate / 100 for error_rate in overall_error_rate]

prognostic_run_results = []

for run in tqdm(range(num_runs), desc="Prognostic Exam Progress"):
    incorrect_subjects = {}
    correct_answers_count = 0
    incorrect_answers_count = 0
    
    for idx, question in enumerate(programming_questions):
        answer = simulate_answers(correct_answers[idx], adjusted_error_probabilities[idx])
        if answer == correct_answers[idx]:
            correct_answers_count += 1
        else:
            subject = detect_subject(question)
            if subject in incorrect_subjects:
                incorrect_subjects[subject] += 1
            else:
                incorrect_subjects[subject] = 1
            incorrect_answers_count += 1
    
    total_score = correct_answers_count - incorrect_answers_count
    
    recommended_modules = []
    for subject, count in incorrect_subjects.items():
        difficulty_level = "Advanced" if count >= threshold_correct else "Beginner"
        module_rec = module_recommendation(subject, difficulty_level)
        recommended_modules.append(module_rec)
    
    prognostic_run_results.append({
        "run": run + 1,
        "correct_answers_count": correct_answers_count,
        "incorrect_subjects": incorrect_subjects,
        "recommended_modules": recommended_modules,
        "total_incorrect": incorrect_answers_count,
        "total_score": total_score
    })
    
    print(f"\nPrognostic Run {run + 1} Results:")
    print(f"Total Correct Answers in Prognostic Student {run + 1}: {correct_answers_count}")
    print(f"Total Incorrect Answers in Prognostic Student {run + 1}: {incorrect_answers_count}")
    print(f"Subjects with Incorrect Answers in Prognostic Student {run + 1}: {incorrect_subjects}")
    print(f"Recommended Modules for Prognostic Student {run + 1}: {recommended_modules}\n")

print("-" * 60)
print("PROGNOSTIC EXAM RESULTS")

colors = ['lightcoral', 'lightskyblue', 'lightgreen', 'lightyellow', 'lightpink', 
          'lightseagreen', 'lightblue', 'lightsalmon', 'lightgreen', 'lightcyan']

diagnostic_accuracy_rates = [run["accuracy_rate"] for run in run_results]

plt.figure(figsize=(10, 6))
diagnostic = plt.bar(range(1, num_runs + 1), diagnostic_accuracy_rates, color=colors)
plt.xlabel('Run')
plt.ylabel('Accuracy Rate (%)')
plt.title('Diagnostic Exam - Accuracy Rate for Each Student')
plt.xticks(range(1, num_runs + 1))
plt.ylim(0, 100)

for bar in diagnostic:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval, f'{round(yval, 2)}%', ha='center', va='bottom')

prognostic_incorrect_subjects = [run["incorrect_subjects"] for run in prognostic_run_results]

plt.figure(figsize=(10, 6))

for idx, subjects in enumerate(prognostic_incorrect_subjects):
    plt.bar(idx + 1, sum(subjects.values()), color=colors[idx], label=f"Run {idx+1}")

plt.xlabel('Run')
plt.ylabel('Number of Incorrect Answers')
plt.title('Prognostic Exam - Subjects with Incorrect Answers for Each Student')
plt.xticks(range(1, num_runs + 1))
plt.legend(loc="upper right")

diagnostic_accuracy_rates = [run["accuracy_rate"] for run in run_results]
prognostic_total_scores = [run["total_score"] for run in prognostic_run_results]

prognostic_accuracy_rates = [(run["correct_answers_count"] / len(programming_questions)) * 100 for run in prognostic_run_results]

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.bar(range(1, num_runs + 1), diagnostic_accuracy_rates, color='lightblue')
plt.xlabel('Run')
plt.ylabel('Accuracy Rate (%)')
plt.title('Diagnostic Exam - Accuracy Rate for Each Student')
plt.xticks(range(1, num_runs + 1))
plt.ylim(0, 100)

plt.subplot(1, 2, 2)
plt.bar(range(1, num_runs + 1), prognostic_total_scores, color='lightgreen')
plt.xlabel('Run')
plt.ylabel('Total Score')
plt.title('Prognostic Exam - Total Score for Each Student')
plt.xticks(range(1, num_runs + 1))

plt.figure(figsize=(10, 6))
prognostic_accuracy = plt.bar(range(1, num_runs + 1), prognostic_accuracy_rates, color=colors)
plt.xlabel('Run')
plt.ylabel('Accuracy Rate (%)')
plt.title('Prognostic Exam - Accuracy Rate for Each Student')
plt.xticks(range(1, num_runs + 1))
plt.ylim(0, 100)

for bar in prognostic_accuracy:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval, f'{round(yval, 2)}%', ha='center', va='bottom')

plt.show()

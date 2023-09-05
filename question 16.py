def calculate_average_score(scores_dict):
    if not scores_dict:
        return None  # Return None if the dictionary is empty

    total_score = sum(scores_dict.values())
    num_students = len(scores_dict)
    average_score = total_score / num_students
    return average_score

# Example usage:
student_scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 88,
    "Eve": 95
}

average = calculate_average_score(student_scores)
if average is not None:
    print("Average score:", average)
else:
    print("No scores available to calculate the average.")

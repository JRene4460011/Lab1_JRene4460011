import csv
import sys
import os
import time

def load_csv_data():
    """
    Prompts the user for a filename, checks if it exists, 
    and extracts all fields into a list of dictionaries.
    """
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")
    
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
        
    assignments = []
    
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert numeric fields to floats for calculations
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })
        return assignments
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

def evaluate_grades(data):
    """
    Implement your logic here.
    'data' is a list of dictionaries containing the assignment records.
    """
    print("\n--- Processing Grades ---")
    print("\n")
    
    # TODO: a) Check if all scores are percentage based (0-100)
    
    for item in data:
        if item['score'] < 0 or item['score'] > 100:
            print(f"Error: Score for '{item['assignment']}' is out of the given range (0-100).")
            sys.exit(1)
        else:
            print(f"Score for '{item['assignment']}' is valid: {item['score']}%")
    
    # TODO: b) Validate total weights (Total=100, Summative=40, Formative=60)
    
    print("\nValidating assignment weights......")
    time.sleep(1.5)

    print("\n")
    Total_weight = 0
    summative_weight = 0
    formative_weight = 0

    for item in data:
        Total_weight += item['weight']
        if item['group'].lower() == 'summative':
            summative_weight += item['weight']
        elif item['group'].lower() == 'formative':
            formative_weight += item['weight']

    if Total_weight != 100:
        print(f"The sum of all assignment weights should be 100%. The current total weight is: {Total_weight}%")
        sys.exit(1)
    else:
        print(f"Total assignments weight is valid: {Total_weight}%")   

    if summative_weight != 40:
        print(f"The total weight for summative assignments should be 40%. The current summative weight is: {summative_weight}%")
        sys.exit(1)
    else:
        print(f"Total Summative weights is valid: {summative_weight}%")

    if formative_weight != 60:
        print(f"The total weight for formative assignments should be 60%. The current formative weight is: {formative_weight}%")
        sys.exit(1)
    else:
        print(f"Total Formative weights is valid: {formative_weight}%")

    # TODO: c) Calculate the Final Grade and GPA

    Final_grade = 0
    Total_weight = 0
    Total_Scores = 0
    for item in data:
        # I think that even though weights are the same, I'd rather calculate the final grade by multiplying the score with the weight and dividing by total weight, so as to perfectly handle records with different weights.
        Total_weight += item['weight']
        Total_Scores += (item['score'] * item['weight'])
    
    Final_Grade = Total_Scores / Total_weight
    GPA = (Final_Grade / 100) * 5.0

    print(f"\nThe Final Grade is {Final_Grade:.2f}%")
    print(f"The GPA is {GPA:.2f}")

    # TODO: d) Determine Pass/Fail status (>= 50% in BOTH categories)

    formative_score = 0
    summative_score = 0
    for item in data:
        if item['group'].lower() == 'formative':
            formative_score += (item['score'] * item['weight'])
        elif item['group'].lower() == 'summative':
            summative_score += (item['score'] * item['weight'])
    
    formative_percentage = formative_score / formative_weight
    summative_percentage = summative_score / summative_weight

    if formative_percentage >= 50 and summative_percentage >= 50:
        print("\nStatus: PASSED")
    else:        
        print("\nStatus: FAILED")
    
    # TODO: e) Check for failed formative assignments (< 50%)
    #          and determine which one(s) have the highest weight for resubmission.
    
    failed_formative_assignments = []

    for item in data:
        if item['group'].lower() == 'formative' and item['score'] < 50:
            failed_formative_assignments.append(item)

    if failed_formative_assignments:
        # Figuring out the highest weight among all of the failed formative assignments
        max_weight = max(item['weight'] for item in failed_formative_assignments)
        
        # I'm keeping all assignments with that max_weight in the same list.
        eligible_for_resubmission = [item for item in failed_formative_assignments if item['weight'] == max_weight]
        
        # Print all eligible assignments
        for item in eligible_for_resubmission:
            print(f"\nThe assignment '{item['assignment']}' has the highest weight ({item['weight']}%) among the failed formative assignments and is eligible for resubmission.")
        
    # TODO: f) Print the final decision (PASSED / FAILED) and resubmission options
        
    print("\n--------- Final Decision ---------")
    print(f"Overall Status: {'PASSED' if formative_percentage >= 50 and summative_percentage >= 50 else 'FAILED'}")

    if eligible_for_resubmission:
        print("\nEligible assignment(s) for resubmission:")
        for item in eligible_for_resubmission:
            print(f"- {item['assignment']} (Score: {item['score']}%, Weight: {item['weight']}%)")
    else:
        print("No formative assignments need resubmission.")

if __name__ == "__main__":
    # 1. Load the data
    course_data = load_csv_data()
    
    # 2. Process the features
    evaluate_grades(course_data)
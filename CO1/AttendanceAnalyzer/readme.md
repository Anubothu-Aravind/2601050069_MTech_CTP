# Project: Student Attendance Analysis System

A procedural, function-based student attendance analysis system demonstrating data structures, input validation, and statistical analysis.

## 1. Problem Statement
An educational institution needs a Python-based program to analyze student attendance. The system should accept student name, stream/class, total classes conducted, and total classes attended. It needs to calculate individual attendance percentages, identify students with attendance below 75%, find the student(s) with the highest attendance, and calculate the overall class attendance metrics.

## 2. Divide into Parts/Modules
To keep the design clean and modular, the notebook is structured into these logical parts/modules:
* **Core Logic**: Clean, decoupled functions for attendance record insertion and calculations (`add_student`, `calculate_percentage`).
* **Computational Logic**: Functions for filtering and statistics (`get_low_attendance_students`, `get_highest_attendance_students`, `calculate_overall_attendance`) with support for optional stream-based filtering.
* **Data Store & Input Setup**: Defines the student registry data structure representing stream, conducted, and attended classes, and logic for importing records from a CSV file.
* **Driver Logic (Main)**: An interactive console menu loop that drives the operations and supports stream-based filtering.

## 3. Abstraction
Abstraction helps focus on essential parameters and hide unnecessary information.

### Needs (Essential Information)
- **Student Name**: String used as a unique identifier.
- **Stream**: String used to filter students by their department or class (e.g. CSE, ECE, AIML, DS).
- **Classes Conducted**: Integer representing the total lectures held for the student.
- **Classes Attended**: Integer representing the number of lectures attended.
- **Attendance Percentage Threshold**: Floating-point threshold (75.0%) for identifying low attendance.

### No Needs (Irrelevant Information)
- Student grades, phone numbers, email addresses, or physical addresses.
- Course codes, names of professors, schedules, or classroom locations.
- System logs, login passwords, or UI styling.

## 4. Algorithm
1. Initialize `student_db` by loading the default database of 40 students or importing from a CSV file.
2. Accept choice input from the user (1-7):
   - Note: At the start of every loop iteration, the system displays the available branches, student count per branch, and grand total of students.
   - **Option 1 (Add Student Record)**: Prompt for Name, Stream, Conducted classes, and Attended classes. Validate inputs (Name and Stream not empty, Conducted $> 0$, $0 \le \text{Attended} \le \text{Conducted}$). Store the record.
   - **Option 2 (View Attendance Report)**: Optionally filter by stream. Compute and print the attendance report of students in a formatted table displaying Name, Stream, Conducted, Attended, Percentage, and Status.
   - **Option 3 (Identify Low Attendance)**: Optionally filter by stream. Print students whose attendance percentage is $< 75.0\%$.
   - **Option 4 (Find Highest Attendance)**: Optionally filter by stream. Find the maximum attendance percentage and list all students matching that value (handling ties).
   - **Option 5 (Calculate Overall Metrics)**: Optionally filter by stream. If no filter is provided (user presses Enter), calculate and display the metrics stream-wise for every stream in the database (sorted by student count descending, then alphabetically), followed by the overall metrics for all streams combined. If a stream filter is provided, calculate and display metrics (Number of Students, Class Average Percentage, and Aggregate Attendance Rate) for only that specific stream.
   - **Option 6 (Load Student Records from CSV)**: Re-initialize `student_db` from a CSV path. Validate column headers (supporting `name`, `stream`, `conducted`, and `attended`) and individual row records.
   - **Option 7 (Exit)**: Terminate the program.

## 5. Core Logic
```python
def add_student(student_db, name, stream, conducted, attended):
    name = name.strip()
    stream = stream.strip()
    if not name:
        raise ValueError("Student name cannot be empty.")
    if not stream:
        raise ValueError("Stream cannot be empty.")
    if conducted <= 0:
        raise ValueError("Total conducted classes must be greater than zero.")
    if attended < 0:
        raise ValueError("Total attended classes cannot be negative.")
    if attended > conducted:
        raise ValueError("Attended classes cannot exceed conducted classes.")
    student_db[name] = {"stream": stream, "conducted": conducted, "attended": attended}

def calculate_percentage(conducted, attended):
    if conducted == 0:
        return 0.0
    return (attended / conducted) * 100.0

def get_low_attendance_students(student_db, threshold=75.0, stream=None):
    low_list = []
    for name, info in student_db.items():
        if stream and info.get("stream", "").strip().lower() != stream.strip().lower():
            continue
        pct = calculate_percentage(info["conducted"], info["attended"])
        if pct < threshold:
            low_list.append((name, info.get("stream", "N/A"), pct))
    return low_list

def get_highest_attendance_students(student_db, stream=None):
    if not student_db:
        return []
    
    filtered_db = {}
    for name, info in student_db.items():
        if stream and info.get("stream", "").strip().lower() != stream.strip().lower():
            continue
        filtered_db[name] = info
        
    if not filtered_db:
        return []
        
    max_pct = -1.0
    highest_list = []
    for name, info in filtered_db.items():
        pct = calculate_percentage(info["conducted"], info["attended"])
        if pct > max_pct:
            max_pct = pct
            highest_list = [(name, info.get("stream", "N/A"), pct)]
        elif pct == max_pct:
            highest_list.append((name, info.get("stream", "N/A"), pct))
    return highest_list

def calculate_overall_attendance(student_db, stream=None):
    filtered_db = {}
    for name, info in student_db.items():
        if stream and info.get("stream", "").strip().lower() != stream.strip().lower():
            continue
        filtered_db[name] = info
        
    if not filtered_db:
        return {"average_percentage": 0.0, "overall_rate": 0.0}
        
    total_pct_sum = 0.0
    total_conducted = 0
    total_attended = 0
    for name, info in filtered_db.items():
        pct = calculate_percentage(info["conducted"], info["attended"])
        total_pct_sum += pct
        total_conducted += info["conducted"]
        total_attended += info["attended"]
    return {
        "average_percentage": total_pct_sum / len(filtered_db),
        "overall_rate": (total_attended / total_conducted) * 100.0 if total_conducted > 0 else 0.0
    }
```

## 6. Data Store & Input Setup
The default database includes a preloaded set of 40 students divided equally across CSE, ECE, AIML, and DS streams.

```python
import csv
import os

DEFAULT_STUDENT_DB = {
    "Aarav": {"stream": "CSE", "conducted": 40, "attended": 35},
    "Ananya": {"stream": "CSE", "conducted": 40, "attended": 38},
    "Arjun": {"stream": "CSE", "conducted": 40, "attended": 29},
    # ... (other 37 records) ...
}

def load_student_db(csv_path=None):
    # Reads CSV, normalizes headers, validates contents, and handles errors
    # Falls back to DEFAULT_STUDENT_DB on error or if csv_path is None
```

CSV file structure (`students_sample.csv`):
```csv
name,stream,conducted,attended
Aarav,CSE,40,35
Ananya,CSE,40,38
Arjun,CSE,40,29
...
```

## 7. Sample Edge Cases (Test Cases)
Here are the test scenarios designed to verify system correctness:

### Test Case 1: Standard Verification
* **Input**: "Aarav" (CSE, 40 conducted, 35 attended = 87.5%), "Arjun" (CSE, 40 conducted, 29 attended = 72.5%).
* **Expected Output**: Aarav percentage = 87.5% (Good status), Arjun percentage = 72.5% (Low status, identified as below 75%).

### Test Case 2: Zero Attendance
* **Input**: "Charlie" (DS, 20 conducted, 0 attended).
* **Expected Output**: Percentage = 0.0%. Identified as below 75%.

### Test Case 3: Perfect Attendance
* **Input**: "Diana" (AIML, 30 conducted, 30 attended).
* **Expected Output**: Percentage = 100.0%.

### Test Case 4: Invalid Input Validations
* **Input**: "Eva" (CSE, conducted = -5, or attended = 15 when conducted = 10).
* **Expected Output**: System rejects input, raises `ValueError`, and prompts user to re-enter correctly.

### Test Case 5: Multiple Students Tie for Highest Attendance
* **Input**: "Diana" (AIML, 100%), "Kavya" (CSE, 50 conducted, 48 attended = 96%).
* **Expected Output**: Highest attendance report correctly identifies tie-breakers if any.

## 8. Driver Logic (Main)
To run the driver logic, open the [AttendanceAnalyzer.ipynb](AttendanceAnalyzer.ipynb) notebook and execute the cells.

## Sample Input and Output

### Interactive Dynamic Input Output (Sample Run)
```text
---------------------------------------------
AVAILABLE BRANCHES & STUDENT COUNTS
---------------------------------------------
AIML           : 10 student(s)
CSE            : 10 student(s)
DS             : 10 student(s)
ECE            : 10 student(s)
---------------------------------------------
Grand Total    : 40 student(s)
---------------------------------------------

--- STUDENT ATTENDANCE MENU ---
1. Add Student Record
2. View Attendance Report
3. Find Students Below 75% (Low Attendance)
4. Find Student(s) with Highest Attendance
5. Calculate Overall Class Attendance
6. Load Student Records from CSV
7. Exit
Enter choice (1-7): 5
Enter stream to filter by (or press Enter for all): 
---------------------------------------------
OVERALL CLASS ATTENDANCE METRICS
---------------------------------------------

AIML
---------------------------------------------
Number of Students:            10
Class Average Percentage:      80.48%
Aggregate Attendance Rate:     80.66%

CSE
---------------------------------------------
Number of Students:            10
Class Average Percentage:      83.16%
Aggregate Attendance Rate:     83.37%

DS
---------------------------------------------
Number of Students:            10
Class Average Percentage:      82.94%
Aggregate Attendance Rate:     82.70%

ECE
---------------------------------------------
Number of Students:            10
Class Average Percentage:      81.17%
Aggregate Attendance Rate:     80.67%

---------------------------------------------
ALL STREAMS
---------------------------------------------
Number of Students:            40
Class Average Percentage:      81.94%
Aggregate Attendance Rate:     81.84%
---------------------------------------------
---------------------------------------------
AVAILABLE BRANCHES & STUDENT COUNTS
---------------------------------------------
AIML           : 10 student(s)
CSE            : 10 student(s)
DS             : 10 student(s)
ECE            : 10 student(s)
---------------------------------------------
Grand Total    : 40 student(s)
---------------------------------------------

--- STUDENT ATTENDANCE MENU ---
1. Add Student Record
2. View Attendance Report
3. Find Students Below 75% (Low Attendance)
4. Find Student(s) with Highest Attendance
5. Calculate Overall Class Attendance
6. Load Student Records from CSV
7. Exit
Enter choice (1-7): 5
Enter stream to filter by (or press Enter for all): ds
---------------------------------------------
OVERALL CLASS ATTENDANCE METRICS
---------------------------------------------
Stream: DS
---------------------------------------------
Number of Students:            10
Class Average Percentage:      82.94%
Aggregate Attendance Rate:     82.70%
---------------------------------------------
```

# Project: Parking Lot Management System

An interactive Python program to manage a parking area with 100 slots, demonstrating allocation, release, occupancy checks, and fee calculation.

## 1. Problem Statement
A parking lot needs a system to manage 100 parking slots. The system should track slot availability, allocate a free slot to an incoming vehicle, release the slot when the vehicle departs, calculate parking charges based on the duration of stay, and check if the parking area is full.

## 2. Divide into Parts/Modules
To keep the design clean and modular, the notebook is structured into these logical parts/modules:
* **Core Logic**: Functions for slot allocation and release (`allocate_slot`, `release_slot`).
* **Computational Logic**: Functions for checking status and fees (`calculate_charges`, `get_occupancy_status`).
* **Data Store & Input Setup**: Defines the parking lot registry (a dictionary mapping slots 1 to 100).
* **Driver Logic (Main)**: An interactive console menu loop that drives the operations.

## 3. Abstraction
Abstraction helps focus on essential parameters and hide unnecessary information.

### Needs (Essential Information)
- **Slot Number**: Integer from 1 to 100 identifying the parking spaces.
- **Occupancy Map**: Dictionary mapping slot numbers to vehicle numbers (or `None` if vacant).
- **Vehicle License Plate**: String representing the vehicle identity.
- **Duration (Hours)**: Float representing duration to compute the parking charges.
- **Hourly Rate**: Numeric constant (e.g. $10 per hour) to compute fees.

### No Needs (Irrelevant Information)
- Vehicle make, model, color, or engine type.
- Parking lot lighting, camera setups, or structural drawings.
- Driver identity, name, gender, or payment card details.

## 4. Algorithm
1. Initialize a dictionary `parking_lot` representing 100 slots, all mapped to `None`.
2. Display a menu loop that automatically prints the parking lot status (either showing all slots are available, or listing unavailable/occupied slots if any exist) at the start of each iteration, followed by 5 options (Allocate Slot, Release Slot, View Availability, Show Status/Metrics, Exit).
3. On allocating a slot:
   - Prompt for the slot number (1-100) and the vehicle plate number.
   - Check if the slot number is valid and currently vacant.
   - If vacant, record the vehicle number and print the allocated slot. If invalid or occupied, print appropriate error.
4. On releasing a slot:
   - Prompt for slot number. Check if valid and currently occupied.
   - Prompt for hours parked, calculate charges (using hourly rate, rounding up to the nearest hour), clear the slot, and print invoice.
5. On viewing availability:
   - Print a formatted table showing available slot numbers.
6. On showing status/metrics:
   - Print total occupied slots, available slots, and state whether the parking area is full.

## 5. Core Logic
```python
def allocate_slot(parking_lot, slot_number, vehicle_number):
    if not (1 <= slot_number <= 100):
        raise ValueError("Invalid slot number. Must be between 1 and 100.")
    vehicle_number = vehicle_number.strip()
    if not vehicle_number:
        raise ValueError("Vehicle number cannot be empty.")
    if parking_lot[slot_number] is not None:
        raise ValueError(f"Slot {slot_number} is already occupied.")
    parking_lot[slot_number] = vehicle_number
    return slot_number

def release_slot(parking_lot, slot_number):
    if not (1 <= slot_number <= 100):
        raise ValueError("Invalid slot number. Must be between 1 and 100.")
    vehicle_number = parking_lot[slot_number]
    if vehicle_number is None:
        return None
    parking_lot[slot_number] = None
    return vehicle_number

def calculate_charges(hours, rate=10.0):
    if hours <= 0:
        raise ValueError("Duration must be greater than zero.")
    import math
    return math.ceil(hours) * rate

def get_occupancy_status(parking_lot):
    occupied = [slot for slot, val in parking_lot.items() if val is not None]
    total = len(parking_lot)
    occupied_count = len(occupied)
    available_count = total - occupied_count
    return {
        "occupied_count": occupied_count,
        "available_count": available_count,
        "is_full": occupied_count >= total
    }
```

## 6. Data Store & Input Setup
```python
parking_lot = {slot: None for slot in range(1, 101)}
```

## 7. Sample Edge Cases (Test Cases)
Here are the test scenarios designed to verify system correctness:

### Test Case 1: Standard Allocation and Release
* **Input**: Allocate "KA-01-1234". Re-check availability. Release slot with 2.5 hours stay.
* **Expected Output**: Allocated to Slot 1. Availability decreases. Charges calculated as $30.00 (3 hours * $10.00).

### Test Case 2: Parking Area Full
* **Input**: Fill all 100 slots and attempt to allocate another vehicle.
* **Expected Output**: System identifies lot is full, returns warning message, and refuses allocation.

### Test Case 3: Invalid Inputs
* **Input**: Release a vacant slot, enter negative hours, or input invalid slot numbers (e.g. 150).
* **Expected Output**: System detects invalid actions and displays appropriate errors.

### Test Case 4: Freeing up a Slot
* **Input**: Lot is full (100/100). Release Slot 5. Allocate new vehicle.
* **Expected Output**: Slot 5 is freed, and the next incoming vehicle is successfully directed to Slot 5.

## 8. Driver Logic (Main)
To run the driver logic, open the [ParkingSystem.ipynb](ParkingSystem.ipynb) notebook and execute the cells.

## Sample Input and Output

### Interactive Dynamic Input Output (Sample Run)
```text
---------------------------------------------
PARKING LOT STATUS
---------------------------------------------
All slots are available.
---------------------------------------------
--- PARKING LOT MENU ---
1. Allocate Parking Slot
2. Release Parking Slot
3. View Available Slots
4. Show Occupancy Status
5. Exit
Enter choice (1-5): 4
---------------------------------------------
PARKING LOT OCCUPANCY STATUS
---------------------------------------------
Total Slots:      100
Occupied Slots:   0
Available Slots:  100
Status:           Available (Not Full)
---------------------------------------------

---------------------------------------------
PARKING LOT STATUS
---------------------------------------------
All slots are available.
---------------------------------------------
--- PARKING LOT MENU ---
1. Allocate Parking Slot
2. Release Parking Slot
3. View Available Slots
4. Show Occupancy Status
5. Exit
Enter choice (1-5): 1
Enter Slot Number to allocate (1-100): 5
Enter Vehicle Plate Number: KA-01-AA-9999
Slot 5 has been successfully allocated to KA-01-AA-9999.

---------------------------------------------
PARKING LOT STATUS
---------------------------------------------
Unavailable (Occupied) Slots: 5
---------------------------------------------
--- PARKING LOT MENU ---
1. Allocate Parking Slot
2. Release Parking Slot
3. View Available Slots
4. Show Occupancy Status
5. Exit
Enter choice (1-5): 5
Exiting Parking Lot System. Goodbye!
```

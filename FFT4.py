import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Flow Flex - Menstrual Cycle Workout")

# buttons for each page, """ for multi lines, " for single lines
workouts = {
    "Menstrual Phase": {
        "Stretching": """1. Reclining or supine twist: Lie on your back with legs outstretched. Bend your right knee towards your chest, then lower it to the left side. Hold for 3 reps on each side.
2. Legs up the wall: Lie down with your legs vertical, resting against the wall. Hold for 2 minutes.
3. Knees to chest: Pull your knees towards your chest and rock gently. Hold or rock to release tension.""",
        
        "Yoga": """1. Fish Pose: Lie on your back, slide hands under buttocks, arch your back slightly. Hold for several breaths.
2. Cobra Pose: Lie face down, push your chest upwards, arching your back. Hold for a few breaths.
3. Forward Fold: Stand, hinge at hips, and fold forward. Hold for several breaths."""
    },
    "Follicular Phase": {
        "Pilates": """1. Glute Bridge: Lie on your back, knees bent, feet flat. Lift your hips. 5-8 reps.
2. Single Leg Circle: Lie on your back, extend one leg upwards. Make circles with your leg. 5-8 reps each direction per leg.
3. Swimming: Lie face down, alternate raising your opposite arm and leg in a swimming motion.""",
        
        "Yoga": """1. Mountain Pose: Stand tall, feet together, arms overhead, then bring hands to heart.
2. Upward Salute: Stand tall, arms up, stretching upwards, breathing deeply.
3. Forward Fold: Hinge at your hips and fold forward. Hold for a few breaths."""
    },
    "Ovulatory Phase": {
        "HIIT": """1. Jump Squats: Lower into a squat, then jump up, reaching arms overhead. 30 seconds on, 15 seconds rest, repeat 3 times.
2. Mountain Climbers: In a plank position, drive knees towards chest alternately. 30 seconds on, 15 seconds rest, repeat 3 times.
3. Burpees: Drop into a squat, jump feet back into plank, return, and explode up into a jump. 30 seconds on, 15 seconds rest, repeat 3 times.""",
        
        "Strength Training": """1. Deadlifts: Stand hip-width apart, hinge at hips, and grasp a barbell. Lift to standing. 4 sets of 8-10 reps.
2. Overhead Press: Hold a dumbbell at shoulder height, press overhead, and lower. 4 sets of 8-10 reps.
3. Lunges: Step forward, bending both knees, and return to standing. 3 sets of 10-12 reps per leg."""
    },
    "Luteal Phase": {
        "Resistance Band Exercises": """1. Banded Glute Bridges: Place a resistance band around your thighs, press through heels, lift hips. 3 sets of 12-15 reps.
2. Banded Lateral Walks: With a resistance band above your knees, step side to side. 3 sets of 10-12 steps per side.
3. Banded Seated Rows: Sit with a resistance band around your feet, pull towards your torso. 3 sets of 10-12 reps."""
    }
}

# buttons
def show_workout_options(phase):
    clear_buttons()
    for workout_name in workouts[phase]:
        button = tk.Button(root, text=workout_name, width=30, height=2, command=lambda w=workout_name: show_workout(w, phase))
        button.pack(pady=10)

    # BACK BUTTON!!!
    back_button = tk.Button(root, text="Back", width=30, height=2, command=create_home_page)
    back_button.pack(pady=10)

# buttons
def show_workout(workout_name, phase):
    workout_details = workouts[phase][workout_name]
    messagebox.showinfo(f"{workout_name} for {phase}", workout_details)

# buttons
def clear_buttons():
    for widget in root.winfo_children():
        widget.destroy()

# homepage
def create_home_page():
    clear_buttons()
    phases = ["Menstrual Phase", "Follicular Phase", "Ovulatory Phase", "Luteal Phase"]
    for phase in phases:
        button = tk.Button(root, text=phase, width=30, height=2, command=lambda p=phase: show_workout_options(p))
        button.pack(pady=10)

create_home_page()

# END W THIS OR IT WONT WORK
root.mainloop()

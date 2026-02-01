import tkinter as tk
from tkinter import messagebox

# ------------------ Functions ------------------

def add_course():
    cid = course_id_entry.get()
    name = course_name_entry.get()
    credit = course_credit_entry.get()

    if cid == "" or name == "" or credit == "":
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    with open("courses.txt", "a") as f:
        f.write(f"{cid},{name},{credit}\n")

    messagebox.showinfo("Success", "Course added successfully!")
    course_id_entry.delete(0, tk.END)
    course_name_entry.delete(0, tk.END)
    course_credit_entry.delete(0, tk.END)


def view_courses():
    output_text.delete("1.0", tk.END)
    try:
        with open("courses.txt", "r") as f:
            output_text.insert(tk.END, "---- Course List ----\n\n")
            for line in f:
                cid, name, credit = line.strip().split(",")
                output_text.insert(
                    tk.END, f"ID: {cid} | Name: {name} | Credits: {credit}\n"
                )
    except FileNotFoundError:
        output_text.insert(tk.END, "No course records found.")


def add_student():
    sid = student_id_entry.get()
    name = student_name_entry.get()

    if sid == "" or name == "":
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    with open("students.txt", "a") as f:
        f.write(f"{sid},{name}\n")

    messagebox.showinfo("Success", "Student added successfully!")
    student_id_entry.delete(0, tk.END)
    student_name_entry.delete(0, tk.END)


def register_course():
    sid = enroll_student_id_entry.get()
    cid = enroll_course_id_entry.get()

    if sid == "" or cid == "":
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    with open("enrollments.txt", "a") as f:
        f.write(f"{sid},{cid}\n")

    messagebox.showinfo("Success", "Student registered in course!")
    enroll_student_id_entry.delete(0, tk.END)
    enroll_course_id_entry.delete(0, tk.END)


def view_enrollments():
    output_text.delete("1.0", tk.END)
    try:
        with open("enrollments.txt", "r") as f:
            output_text.insert(tk.END, "---- Enrollments ----\n\n")
            for line in f:
                sid, cid = line.strip().split(",")
                output_text.insert(
                    tk.END, f"Student ID: {sid} ➝ Course ID: {cid}\n"
                )
    except FileNotFoundError:
        output_text.insert(tk.END, "No enrollment records found.")


def search_course():
    search_id = search_course_entry.get()
    found = False
    output_text.delete("1.0", tk.END)

    try:
        with open("courses.txt", "r") as f:
            for line in f:
                cid, name, credit = line.strip().split(",")
                if cid == search_id:
                    output_text.insert(
                        tk.END,
                        f"Course Found:\nID: {cid}\nName: {name}\nCredits: {credit}"
                    )
                    found = True
        if not found:
            output_text.insert(tk.END, "Course not found.")
    except FileNotFoundError:
        output_text.insert(tk.END, "Course file not found.")


# ------------------ UI Design ------------------

root = tk.Tk()
root.title("College Course Management System")
root.geometry("700x650")
root.configure(bg="#f0f4f7")

title = tk.Label(
    root,
    text="College Course Management System",
    font=("Arial", 20, "bold"),
    bg="#2c3e50",
    fg="white",
    pady=10
)
title.pack(fill=tk.X)

frame = tk.Frame(root, bg="#f0f4f7")
frame.pack(pady=10)

# ---- Course Section ----
tk.Label(frame, text="Add Course", font=("Arial", 14, "bold"), bg="#f0f4f7").grid(row=0, column=0, columnspan=2, pady=5)

tk.Label(frame, text="Course ID:", bg="#f0f4f7").grid(row=1, column=0, sticky="w")
course_id_entry = tk.Entry(frame)
course_id_entry.grid(row=1, column=1)

tk.Label(frame, text="Course Name:", bg="#f0f4f7").grid(row=2, column=0, sticky="w")
course_name_entry = tk.Entry(frame)
course_name_entry.grid(row=2, column=1)

tk.Label(frame, text="Credit Hours:", bg="#f0f4f7").grid(row=3, column=0, sticky="w")
course_credit_entry = tk.Entry(frame)
course_credit_entry.grid(row=3, column=1)

tk.Button(frame, text="Add Course", command=add_course, bg="#3498db", fg="white").grid(row=4, column=0, columnspan=2, pady=5)

# ---- Student Section ----
tk.Label(frame, text="Add Student", font=("Arial", 14, "bold"), bg="#f0f4f7").grid(row=5, column=0, columnspan=2, pady=10)

tk.Label(frame, text="Student ID:", bg="#f0f4f7").grid(row=6, column=0, sticky="w")
student_id_entry = tk.Entry(frame)
student_id_entry.grid(row=6, column=1)

tk.Label(frame, text="Student Name:", bg="#f0f4f7").grid(row=7, column=0, sticky="w")
student_name_entry = tk.Entry(frame)
student_name_entry.grid(row=7, column=1)

tk.Button(frame, text="Add Student", command=add_student, bg="#27ae60", fg="white").grid(row=8, column=0, columnspan=2, pady=5)

# ---- Enrollment Section ----
tk.Label(frame, text="Register Course", font=("Arial", 14, "bold"), bg="#f0f4f7").grid(row=9, column=0, columnspan=2, pady=10)

tk.Label(frame, text="Student ID:", bg="#f0f4f7").grid(row=10, column=0, sticky="w")
enroll_student_id_entry = tk.Entry(frame)
enroll_student_id_entry.grid(row=10, column=1)

tk.Label(frame, text="Course ID:", bg="#f0f4f7").grid(row=11, column=0, sticky="w")
enroll_course_id_entry = tk.Entry(frame)
enroll_course_id_entry.grid(row=11, column=1)

tk.Button(frame, text="Register", command=register_course, bg="#9b59b6", fg="white").grid(row=12, column=0, columnspan=2, pady=5)

# ---- Search ----
tk.Label(frame, text="Search Course", font=("Arial", 14, "bold"), bg="#f0f4f7").grid(row=13, column=0, columnspan=2, pady=10)

search_course_entry = tk.Entry(frame)
search_course_entry.grid(row=14, column=0, columnspan=2)

tk.Button(frame, text="Search", command=search_course, bg="#e67e22", fg="white").grid(row=15, column=0, columnspan=2, pady=5)

# ---- View Buttons ----
tk.Button(frame, text="View Courses", command=view_courses).grid(row=16, column=0, pady=5)
tk.Button(frame, text="View Enrollments", command=view_enrollments).grid(row=16, column=1, pady=5)

# ---- Output Area ----
output_text = tk.Text(root, height=10, width=80)
output_text.pack(pady=10)

root.mainloop()

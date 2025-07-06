# password_gui.py
import tkinter as tk
from tkinter import messagebox
from password_logic import check_password_strength, generate_password

def submit():
    pwd = password_entry.get()
    if not pwd:
        messagebox.showwarning("Input Error", "Please enter a password.")
        return

    result, remarks, tips = check_password_strength(pwd)
    result_label.config(text=result, fg="#4CAF50" if "Strong" in result else "#FF4C4C")

    feedback_text.config(state='normal')
    feedback_text.delete(1.0, tk.END)

    if remarks:
        feedback_text.insert(tk.END, "⚠️ Weaknesses:\n" + "\n".join(remarks) + "\n\n")
    if tips:
        feedback_text.insert(tk.END, "📘 Tips to Improve:\n" + "\n".join(tips))

    feedback_text.config(state='disabled')

def generate():
    pwd = generate_password()
    password_entry.delete(0, tk.END)
    password_entry.insert(0, pwd)
    submit()

def toggle_password():
    if password_entry.cget("show") == "":
        password_entry.config(show="*")
        toggle_btn.config(text="👁 Show")
    else:
        password_entry.config(show="")
        toggle_btn.config(text="🙈 Hide")

# -------------------------- GUI Layout -------------------------- #
root = tk.Tk()
root.title("🛡️ Smart Password Strength Checker")
root.geometry("600x500")
root.config(bg="#1e1e1e")

tk.Label(root, text="Smart Password Strength Checker", font=("Segoe UI", 18, "bold"), fg="#00ffc3", bg="#1e1e1e").pack(pady=15)

password_entry = tk.Entry(root, width=35, font=("Segoe UI", 12), show="*")
password_entry.pack(pady=10)

toggle_btn = tk.Button(root, text="👁 Show", command=toggle_password, bg="#444", fg="white", font=("Segoe UI", 9))
toggle_btn.pack(pady=2)

btn_frame = tk.Frame(root, bg="#1e1e1e")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Check Password", command=submit, bg="#4CAF50", fg="white", font=("Segoe UI", 11), width=20).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Generate Strong", command=generate, bg="#2196F3", fg="white", font=("Segoe UI", 11), width=20).grid(row=0, column=1, padx=10)

result_label = tk.Label(root, text="", font=("Segoe UI", 13, "bold"), bg="#1e1e1e", fg="white")
result_label.pack(pady=10)

tk.Label(root, text="🧠 Detailed Feedback", font=("Segoe UI", 12, "bold"), fg="#ffc107", bg="#1e1e1e").pack(anchor="w", padx=20)

feedback_text = tk.Text(root, height=10, width=70, wrap=tk.WORD, font=("Segoe UI", 10), bg="#292929", fg="white")
feedback_text.pack(padx=20, pady=10)
feedback_text.config(state='disabled')

root.mainloop()

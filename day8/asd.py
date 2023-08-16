import tkinter as tk
from tkinter import messagebox

def calculator():
    def perform_calculation():
        try:
            num1 = float(entry_num1.get())
            num2 = float(entry_num2.get())
            operator = operator_var.get()

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                result = num1 / num2
            elif operator == "//":
                result = num1 // num2
            elif operator == "%":
                result = num1 % num2
            elif operator == "**":
                result = num1 ** num2
            else:
                raise ValueError("Invalid operator selected.")

            label_result.config(text=f"Result: {result}")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero.")
    
    calculator_window = tk.Toplevel(root)
    calculator_window.title("Calculator")

    entry_num1 = tk.Entry(calculator_window)
    entry_num1.pack(pady=5)
    
    operator_var = tk.StringVar()
    operator_var.set("+")
    operator_menu = tk.OptionMenu(calculator_window, operator_var, "+", "-", "*", "/", "//", "%", "**")
    operator_menu.pack(pady=5)

    entry_num2 = tk.Entry(calculator_window)
    entry_num2.pack(pady=5)

    btn_calculate = tk.Button(calculator_window, text="Calculate", command=perform_calculation)
    btn_calculate.pack(pady=10)

    label_result = tk.Label(calculator_window, text="Result: ")
    label_result.pack(pady=5)

def check_voting_eligibility():
    def check_age():
        try:
            age = int(entry_age.get())
            if age >= 18:
                messagebox.showinfo("Eligibility", "You are eligible to vote.")
            else:
                messagebox.showinfo("Eligibility", "You are not eligible to vote.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid age.")

    voting_window = tk.Toplevel(root)
    voting_window.title("Check Voting Eligibility")

    label_age = tk.Label(voting_window, text="Enter your age:")
    label_age.pack(pady=5)

    entry_age = tk.Entry(voting_window)
    entry_age.pack(pady=5)

    btn_check_age = tk.Button(voting_window, text="Check Eligibility", command=check_age)
    btn_check_age.pack(pady=10)

def check_positive_negative_zero():
    def check_number():
        try:
            num = float(entry_number.get())
            if num > 0:
                messagebox.showinfo("Result", "The number is positive.")
            elif num < 0:
                messagebox.showinfo("Result", "The number is negative.")
            else:
                messagebox.showinfo("Result", "The number is zero.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    number_window = tk.Toplevel(root)
    number_window.title("Check Positive/Negative/Zero")

    label_number = tk.Label(number_window, text="Enter a number:")
    label_number.pack(pady=5)

    entry_number = tk.Entry(number_window)
    entry_number.pack(pady=5)

    btn_check_number = tk.Button(number_window, text="Check", command=check_number)
    btn_check_number.pack(pady=10)

def check_odd_even():
    def check_number():
        try:
            num = int(entry_number.get())
            if num % 2 == 0:
                messagebox.showinfo("Result", f"{num} is an even number.")
            else:
                messagebox.showinfo("Result", f"{num} is an odd number.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer.")

    odd_even_window = tk.Toplevel(root)
    odd_even_window.title("Check Odd/Even")

    label_number = tk.Label(odd_even_window, text="Enter a number:")
    label_number.pack(pady=5)

    entry_number = tk.Entry(odd_even_window)
    entry_number.pack(pady=5)

    btn_check_number = tk.Button(odd_even_window, text="Check", command=check_number)
    btn_check_number.pack(pady=10)

root = tk.Tk()
root.title("Python Utility Tool")

btn_calculator = tk.Button(root, text="Calculator", command=calculator)
btn_calculator.pack(pady=10)

btn_voting_eligibility = tk.Button(root, text="Check Voting Eligibility", command=check_voting_eligibility)
btn_voting_eligibility.pack(pady=10)

btn_positive_negative_zero = tk.Button(root, text="Check Positive/Negative/Zero", command=check_positive_negative_zero)
btn_positive_negative_zero.pack(pady=10)

btn_odd_even = tk.Button(root, text="Check Odd/Even", command=check_odd_even)
btn_odd_even.pack(pady=10)

root.mainloop()

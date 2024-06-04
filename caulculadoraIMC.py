import tkinter as tk
from tkinter import messagebox

class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de IMC")

        # Labels
        self.height_label = tk.Label(root, text="Altura (m):")
        self.height_label.grid(row=0, column=0)

        self.weight_label = tk.Label(root, text="Peso (kg):")
        self.weight_label.grid(row=1, column=0)

        # Entries
        self.height_entry = tk.Entry(root)
        self.height_entry.grid(row=0, column=1)

        self.weight_entry = tk.Entry(root)
        self.weight_entry.grid(row=1, column=1)

        # Calculate Button
        self.calculate_button = tk.Button(root, text="Calcular IMC", command=self.calculate_bmi)
        self.calculate_button.grid(row=2, columnspan=2)

        # Result Label
        self.result_label = tk.Label(root, text="IMC: ")
        self.result_label.grid(row=3, columnspan=2)

    def calculate_bmi(self):
        try:
            height = float(self.height_entry.get())
            weight = float(self.weight_entry.get())
            bmi = weight / (height ** 2)
            self.result_label.config(text=f"IMC: {bmi:.2f}")
            self.show_bmi_category(bmi)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos para altura e peso.")

    def show_bmi_category(self, bmi):
        if bmi < 18.5:
            category = "Abaixo do peso"
        elif 18.5 <= bmi < 24.9:
            category = "Peso normal"
        elif 25 <= bmi < 29.9:
            category = "Sobrepeso"
        else:
            category = "Obesidade"
        messagebox.showinfo("Categoria de IMC", f"Seu IMC é {bmi:.2f} e você está na categoria: {category}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop()

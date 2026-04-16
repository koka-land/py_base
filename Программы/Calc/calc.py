import tkinter as tk
import math


class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Научный калькулятор")

        self.entry = tk.Entry(root, width=30, font=('Arial', 16))
        self.entry.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('sin', 1, 0), ('cos', 1, 1), ('tan', 1, 2), ('√', 1, 3), ('^', 1, 4),
            ('π', 2, 0), ('e', 2, 1), ('(', 2, 2), (')', 2, 3), ('C', 2, 4),
            ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('/', 3, 3), ('⌫', 3, 4),
            ('4', 4, 0), ('5', 4, 1), ('6', 4, 2), ('*', 4, 3), ('ln', 4, 4),
            ('1', 5, 0), ('2', 5, 1), ('3', 5, 2), ('-', 5, 3), ('log', 5, 4),
            ('0', 6, 0), ('.', 6, 1), ('=', 6, 2), ('+', 6, 3), ('!', 6, 4)
        ]

        for (text, row, col) in buttons:
            btn = tk.Button(self.root, text=text, width=5, height=2,
                            command=lambda t=text: self.button_click(t))
            btn.grid(row=row, column=col, padx=2, pady=2)

    def button_click(self, text):
        current = self.entry.get()

        if text == 'C':
            self.entry.delete(0, tk.END)

        elif text == '⌫':
            self.entry.delete(len(current) - 1, tk.END)

        elif text == '=':
            try:
                expression = current
                # Замена специальных символов
                expression = expression.replace('π', str(math.pi))
                expression = expression.replace('e', str(math.e))
                expression = expression.replace('√', 'math.sqrt')
                expression = expression.replace('^', '**')
                expression = expression.replace('sin', 'math.sin')
                expression = expression.replace('cos', 'math.cos')
                expression = expression.replace('tan', 'math.tan')
                expression = expression.replace('ln', 'math.log')
                expression = expression.replace('log', 'math.log10')

                if '!' in expression:
                    num = int(expression.split('!')[0])
                    result = math.factorial(num)
                else:
                    result = eval(expression)

                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Ошибка")

        else:
            self.entry.insert(tk.END, text)


# Запуск калькулятора
if __name__ == "__main__":
    root = tk.Tk()
    calc = ScientificCalculator(root)
    root.mainloop()
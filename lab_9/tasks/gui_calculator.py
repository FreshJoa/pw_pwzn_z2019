import tkinter as tk
from functools import partial
from lab_9.tools.calculator import Calculator


class CalculatorGUI(tk.Frame):
    def __init__(self, master=None, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self.variables = {}
        self.state = tk.BooleanVar(value=True)
        self.init_variables()
        self.calculator = Calculator()

        self.screen = tk.Label(self, bg='white')
        self.screen.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.bottom_pad = self.init_bottom_pad()
        self.bottom_pad.pack(side=tk.BOTTOM)

        for number in range(1, 10):
            master.bind(number, partial(self.update_var, number))

        master.bind('<+>', partial(self.set_operator, '+'))
        master.bind('<->', partial(self.set_operator, '-'))
        master.bind('</>', partial(self.set_operator, '/'))
        master.bind('<*>', partial(self.set_operator, '*'))
        master.bind('<.>', partial(self.set_operator, '.'))
        master.bind('<Enter>', self.calculate_result)

    def init_variables(self):
        self.variables['var_1'] = ''
        self.variables['var_2'] = ''
        self.variables['operator'] = ''
        self.state.set(True)

    def init_bottom_pad(self):
        bottom_pad = tk.Frame(self)

        # klawiatura numeryczna
        num_pad = tk.Frame(bottom_pad)
        num_pad.pack(side=tk.LEFT)
        ii = 0
        for ii, num in enumerate(range(9, 0, -1)):
            tk.Button(
                num_pad, text=num, width=5,
                command=partial(self.update_var, num)
            ).grid(row=ii // 3, column=(2 - ii) % 3 + 1)

        tk.Button(
            num_pad, text='C', width=5,
            command=self.clear
        ).grid(row=3, column=0)

        tk.Button(
            num_pad, text='0', width=5,
            command=partial(self.update_var, '0')
        ).grid(row=3, column=1)

        tk.Button(
            num_pad, text='=', width=5,
            command=self.calculate_result
        ).grid(row=3, column=3)

        tk.Button(
            num_pad, text='.', width=5,
            command=partial(self.update_var, '.')
        ).grid(row=3, column=2)

        tk.Button(
            num_pad, text='MC', width=5,
            command=self.calculator.clean_memory
        ).grid(row=0, column=0)

        tk.Button(
            num_pad, text='MR', width=5,
            command=self.read_from_memory
        ).grid(row=1, column=0)

        tk.Button(
            num_pad, text='M+', width=5,
            command=self.save_to_memory
        ).grid(row=2, column=0)

        # klawiatura operacji
        operation_pad = tk.Frame(bottom_pad)
        operation_pad.pack(side=tk.RIGHT)
        for ii, operation in enumerate(self.calculator.operations.keys()):
            tk.Button(
                operation_pad, text=operation, width=5,
                command=partial(self.set_operator, operation),
            ).grid(row=ii, column=0)

        return bottom_pad

    def update_screen(self):
        text = f"{self.variables['var_1']}"
        if self.variables['operator']:
            text += f" {self.variables['operator']}"
        if self.variables['var_2']:
            text += f" {self.variables['var_2']}"
        self.screen['text'] = text

    def clear(self):
        state = self.state.get()
        if state:
            self.variables['var_1'] = ''
        else:
            self.variables['var_2'] = ''
        self.update_screen()

    def update_var(self, num, *args):
        state = self.state.get()
        if state:
            self.variables['var_1'] += str(num)
            self.variables['var_1'] = self.variables['var_1'].lstrip('0')
        else:
            self.variables['var_2'] += str(num)
            self.variables['var_2'] = self.variables['var_2'].lstrip('0')
        self.update_screen()

    def set_operator(self, operator):
        if self.variables['var_1']:
            self.variables['operator'] = operator
            self.state.set(not self.state.get())
            self.update_screen()

    def calculate_result(self, *args):
        if self.variables['var_1'] and self.variables['var_2']:
            var_1 = float(self.variables['var_1'])
            var_2 = float(self.variables['var_2'])
            self.screen['text'] = self.calculator.run(
                self.variables['operator'], var_1, var_2
            )
            self.init_variables()

    def read_from_memory(self):
        state = self.state.get()
        if state:
            self.variables['var_1'] = self.calculator.memory
        else:
            self.variables['var_2'] = self.calculator.memory

        self.update_screen()

    def save_to_memory(self):
        self.calculator._short_memory = self.variables['var_2'] or self.variables['var_1'] or \
                                        self.screen['text']
        self.calculator.memorize()


if __name__ == '__main__':
    root = tk.Tk()
    CalculatorGUI(root).pack()
    root.mainloop()

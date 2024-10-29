import tkinter as tk
from tkinter import messagebox

def turing_machine(input_string):
    tape = list(input_string) + ['B'] 
    state = 'q9'
    head = 0        
    while state != 'q0' and state != "qr":
        if state == 'q9':
            if tape[head] == '1':
                state = 'q10'
                head += 1
            else:
                state = 'qr'
        elif state == 'q10':
            if tape[head] == '0':
                state = 'q11'
                head += 1
            else:
                state = 'qr'
        elif state == 'q11':
            if tape[head] == '+':
                state = 'q0'
                head += 1
            else:
                state = 'qr'

    if head+1 >= len(tape):
        return state == 'qr'
    else:
        tape = tape[0:head] + ['0'] + tape[head+1:]
        if len(tape) > 2:
            tape[2] = '1'
        head = 0
    
    while state != 'q8' and state != 'qr':
        if state == 'q0':
            if tape[head] == '1' or tape[head] == '0':
                state = 'q1'
                head += 1
            elif tape[head] == 'B':
                state = 'qr'
            else:
                state = 'qr' 

        elif state == 'q1':
            if tape[head] == '0' or tape[head] == '1':
                state = 'q1'
                head += 1
            
            elif tape[head] == 'B':
                state = 'q2'
                head -= 1
            else:
                state = 'qr' 

        elif state == 'q2':
            if tape[head] == '1': 
                state = 'q2' 
                head -= 1

            elif tape[head] == '0':
                state = 'q3'
                tape[head] = '1'
                head += 1
            else:
                state = 'qr' 

        elif state == 'q3':
            if tape[head] == '1':
                state = 'q4'
                tape[head] = '0'
                head += 1
            else:
                state = 'qr'
        
        elif state == 'q4':
            if tape[head] == '0' or tape[head] == 'B':
                state = 'q4'
                head -= 1
            elif tape[head] == '1':
                state = 'q5'
                head -= 1
            else:
                state = 'qr'

        elif state == 'q5':
            if tape[head] == '1':
                state = 'q5'
                head -= 1
            elif tape[head] == '0':
                state = 'q3'
                tape[head] = '1'
                head += 1
            elif tape[head] == 'B':
                state = 'q6'
                head += 1
            else:
                state = 'qr'
        elif state == 'q6':
            if tape[head] == '1':
                state = 'q6'
                head += 1
            elif tape[head] == '0':
                state = 'q7'
                tape[head] = 'B'
                head += 1
            else:
                state = 'qr'
        elif state == 'q7':
            if tape[head] == '0':
                state = 'q7'
                tape[head] = 'B'
                head += 1
            elif tape[head] == 'B':
                state = 'q8'
                head -= 1
            else:
                state = 'qr'
                

    string_result = list(tape)
    for i in range(len(string_result)):
        if string_result[i] == 'B':
            string_result[i] = ''

    return state == 'q8', ''.join(string_result)

def validate_string():
    input_string = entry.get()
    resultado = turing_machine(input_string)

    if resultado[0]: 
        messagebox.showinfo("Resultado", "¡Cadena válida!")
        result_entry.config(state='normal')
        result_entry.delete(0, tk.END)
        result_entry.insert(0, resultado[1])
        result_entry.config(state='readonly')
    else:
        messagebox.showwarning("Resultado", "Cadena inválida.")
        result_entry.config(state='normal')
        result_entry.delete(0, tk.END)
        result_entry.config(state='readonly')

root = tk.Tk()
root.title("Máquina de Turing - Suma de decimal 10 con binarios")

root.geometry("600x200")

main_frame = tk.Frame(root)
main_frame.pack(padx=10, pady=10, expand=True)

left_frame = tk.Frame(main_frame)
left_frame.grid(row=0, column=0, padx=10, pady=10)

label = tk.Label(left_frame, text="Ingresa la cadena. Usa el formato '10+[Cadena Binaria]':")
label.pack(pady=5)

entry = tk.Entry(left_frame, width=30)
entry.pack(pady=5)

validate_button = tk.Button(left_frame, text="Validar", command=validate_string)
validate_button.pack(pady=5)

right_frame = tk.Frame(main_frame)
right_frame.grid(row=0, column=1, padx=10, pady=10)

result_label = tk.Label(right_frame, text="Cadena resultante:")
result_label.pack(pady=5)

result_entry = tk.Entry(right_frame, width=30, state='readonly')
result_entry.pack(pady=5)

root.mainloop()
import tkinter
import tkinter as tk


window = tk.Tk()
window.title("Decimal to Binary Converter")

def convert_to_binary():
    number = int(entry.get())
    binary = ''  

    
    while number > 0:
        remainder = number % 2
        binary = str(remainder) + binary
        number = number // 2

    
    result_label.config(text="Binary: " + binary)
    
entry = tk.Entry(window) 
entry.pack()

convert_button = tk.Button(window, text="Convert to Binary", command=convert_to_binary) 
convert_button.pack() 

result_label = tk.Label(window, text="Binary: ")
result_label.pack()
window.geometry("400x300")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_width = 400  
window_height = 300  

position_top = (screen_height // 2) - (window_height // 2)
position_left = (screen_width // 2) - (window_width // 2)

window.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")

window.mainloop()








""""
That is the old code maybe I should delet it or maybe not, who cares


number = 0
try: number = int(input("Enter the number you want to convert to Binary : "))

except:
    print("sorry that is not a valid number")
binary = ''
test = number
while number > 0:
    remainder = number % 2
    binary = str(remainder) + binary
    number = number // 2
    
print("The binary from " + str(test) + " " + "is:", binary)"""
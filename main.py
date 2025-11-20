import customtkinter 
import customtkinter as ctk 

def convert_temperature():
    choice = selected_value.get()
    if (choice == "C"):
        convert_to_celsius()
    else:
        convert_to_fahrenheit()


def convert_to_celsius():
    fahrenheit = float(temp_entry.get())
    celsius = (fahrenheit - 32) * 5 / 9
    celsius_text = f"{celsius: .2f} °C"
    celsius_text
    label_result.configure(text=celsius_text, text_color="green", font=ctk.CTkFont(size=20,weight="bold"))

def convert_to_fahrenheit():
    celsius = float(temp_entry.get())
    fahrenheit = (celsius * 9 / 5) + 32
    fahrenheit_text = f"{fahrenheit: .2f} °F"
    label_result.configure(text=fahrenheit_text, text_color="green", font=ctk.CTkFont(size=20,weight="bold"))

window = ctk.CTk()
customtkinter.set_appearance_mode("dark")
window.geometry("600x400")

window.title("Temperature Converter")

title_label = ctk.CTkLabel(window, text="Temperature Converter", font=ctk.CTkFont(size=30,weight="bold"))
title_label.pack(padx=20, pady=(30,10))

radio_frame = ctk.CTkFrame(window)
radio_frame.pack(fill="x", pady=20)

selected_value = ctk.StringVar(value="C")

radio_FtoC = ctk.CTkRadioButton(radio_frame, text="Fahrenheit To Celsius", variable=selected_value, value="C" )
radio_FtoC.pack(side="left", padx=(80,10),pady=10)

radio_CtoF = ctk.CTkRadioButton(radio_frame, text="Celsius To Fahrenheit", variable=selected_value, value="F" )
radio_CtoF.pack(side="left", padx=10,pady=10)

input_frame = ctk.CTkFrame(window)
input_frame.pack(fill="x", padx=50, pady=30)

temp_entry = ctk.CTkEntry(input_frame, placeholder_text="enter temperature.....")
temp_entry.pack(side="left", padx=(80,10), pady=20)

#convert button
convert_button = ctk.CTkButton(input_frame, text="convert", command=convert_temperature)
convert_button.pack(side="left", padx=10, pady=20)

result_frame = ctk.CTkFrame(window)
result_frame.pack(fill="x", padx=50)

label_result = ctk.CTkLabel(result_frame, text="")
label_result.pack()

window.mainloop()



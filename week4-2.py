import tkinter as tk

image_list = [ "jeju1.gif", "jeju2.gif", "jeju3.gif", "jeju4.gif", "jeju5.gif", "jeju6.gif", "jeju7.gif", "jeju8.gif", "jeju9.gif" ]

current_index = 0

def previous_image():
    global current_index
    current_index -= 1
    if current_index < 0:
        current_index = len(image_list) - 1
    update_image()

def next_image():
    global current_index
    current_index += 1
    if current_index >= len(image_list):
        current_index = 0
    update_image()

def update_image():
    image_label.config(text=image_list[current_index])

window = tk.Tk() 
window.title("이미지 뷰어")

image_label = tk.Label(window, text=image_list[current_index], font=("Helvetica", 12))
image_label.pack()

previous_button = tk.Button(window, text="<이전", command=previous_image)
previous_button.pack()

next_button = tk.Button(window, text="<다음", command=next_image)
next_button.pack()

window.mainloop()  

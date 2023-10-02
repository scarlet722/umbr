import tkinter as tk
from tkinter import messagebox

votes = {"강아지": 0, "고양이": 0, "토끼": 0}

def vote_animal():
    selected_animal = var.get()
    if selected_animal:
        votes[selected_animal] += 1
        update_result_label(selected_animal)
    else:
        messagebox.showinfo("경고", "동물을 선택하세요.")

def update_result_label(selected_animal):
    result_label.config(text=f"당신이 선택한 동물은 {selected_animal}입니다.")
    vote_label.config(text=f"투표 결과: {votes}")

window = tk.Tk() 
window.title("동물 투표 프로그램")

title_label = tk.Label(window, text="좋아하는 동물을 선택하세요:")
title_label.pack()

var = tk.StringVar()
var.set(None)  
radio_buttons = []
for animal in votes.keys():
    radio_button = tk.Radiobutton(window, text=animal, variable=var, value=animal)
    radio_buttons.append(radio_button)
    radio_button.pack()

image = tk.PhotoImage(file="animal.gif")
image_label = tk.Label(window, image=image)
image_label.pack()

result_label = tk.Label(window, text="", font=("Helvetica", 12))
result_label.pack()

vote_label = tk.Label(window, text="투표 결과: " + str(votes), font=("Helvetica", 12))
vote_label.pack()

vote_button = tk.Button(window, text="투표하기", command=vote_animal)
vote_button.pack()

window.mainloop()  

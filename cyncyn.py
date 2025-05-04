from customtkinter import *

window = CTk()


result = CTkEntry(window, height=40)
result.pack(fill="x")
frame = CTkFrame(window)
frame.pack()

button_1 = CTkButton(frame, text="1", width=80, height=80)
button_1.grid(row=0, column=0)

button_2 = CTkButton(frame, text="2", width=80, height=80)
button_2.grid(row=0, column=1)

button_3 = CTkButton(frame, text="3", width=80, height=80)
button_3.grid(row=0, column=2)

button_podilutu = CTkButton(frame, text="/", width=80, height=80)
button_podilutu.grid(row=0, column=3)

button_4 = CTkButton(frame, text="4", width=80, height=80)
button_4.grid(row=1, column=0)

button_5 = CTkButton(frame, text="5", width=80, height=80)
button_5.grid(row=1, column=1)

button_6 = CTkButton(frame, text="6", width=80, height=80)
button_6.grid(row=1, column=2)

button_pomnog = CTkButton(frame, text="*", width=80, height=80)
button_pomnog.grid(row=1, column=3)

button_7 = CTkButton(frame, text="7", width=80, height=80)
button_7.grid(row=2, column=0)

button_8 = CTkButton(frame, text="8", width=80, height=80)
button_8.grid(row=2, column=1)

button_9 = CTkButton(frame, text="9", width=80, height=80)
button_9.grid(row=2, column=2)

button_plus = CTkButton(frame, text="+", width=80, height=80)
button_plus.grid(row=2, column=3)

button_tochacka = CTkButton(frame, text=".", width=80, height=80)
button_tochacka.grid(row=3, column=0)

button_0 = CTkButton(frame, text="0", width=80, height=80)
button_0.grid(row=3, column=1)

button_coma = CTkButton(frame, text=",", width=80, height=80)
button_coma.grid(row=3, column=2)

button_minus = CTkButton(frame, text="-", width=80, height=80)
button_minus.grid(row=3, column=3)

window.mainloop()
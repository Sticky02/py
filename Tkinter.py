import tkinter as tk

root = tk.Tk(className="calculator")

lable = tk.Label(text="Calculator", padx=10, pady=10)
lable.pack()

root.geometry("500x500")

textarea = tk.Text(root,height=1, width=1)
textarea.pack(fill="both",padx=10)

frm = tk.Frame(root)
frm.columnconfigure(0,weight=1)
frm.columnconfigure(1,weight=1)
frm.columnconfigure(2,weight=1)

b1 = tk.Button(frm, text="")

Exit = tk.Button(root, text="Exit", command=root.quit)
Exit.place(x=0, y=250)

root.mainloop()
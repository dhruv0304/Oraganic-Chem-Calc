import tkinter as tk

root = tk.Tk()
root.title("Alkane Calculator")
root.geometry('900x600')
root.resizable(False, False)

substituents = [ 'methyl', 'ethyl', 'propyl', 'butyl', 'bromo' ]
chain = tk.StringVar()
cyclo = tk.IntVar()
number = { var: tk.StringVar() for var in substituents }
where = { var: tk.StringVar() for var in substituents }
answer_text = tk.StringVar()

class callback_holder:
    def __init__(self, **args):
        self.__dict__.update(args)
    def __call__(self, name='', index='', mode=''):
        if number[self.sub].get() != '' and int(number[self.sub].get()) != 0:
            self.entry.place(x=610, y=self.y)
        else:
            self.entry.place_forget()
            where[self.sub].set('')

background_photo = tk.PhotoImage(file="Alkane Calculator.png")
tk.Label(root, image=background_photo).place(x=-2, y=-2)
tk.Label(root, text="Please fill in the information below then click the calculate button to determine the name of your diagram.", font=('Roboto', 11), fg='white', bg='#40A4A6').pack(pady=250)

tk.Label(root, text="How many chains?", font=('Roboto', 9), fg='black', bg='#40A4A6').place(x=320, y=300)
tk.Label(root, text="Is there a cyclo chain?", font=('Roboto', 9), fg='black', bg='#40A4A6').place(x=320, y=320)
for idx, sub in enumerate(substituents):
    tk.Label(root, text="How many "+sub+" groups? Where?", font=('Roboto', 9), fg='black', bg='#40A4A6').place(x=320, y=340+(idx*20))
    tk.Entry(root, textvariable=number[sub], width=12).place(x=530, y=340+(idx*20))
    entry = tk.Entry(root, textvariable=where[sub], width=12)
    number[sub].trace_add('write', callback_holder(sub=sub, y=340+(idx*20), entry=entry))

tk.Entry(root, textvariable=chain, width=12).place(x=530, y=300)
pixel = tk.PhotoImage(width=1, height=1)
tk.Checkbutton(root, variable=cyclo, onvalue=1, offvalue=0, bg='#40A4A6', activebackground='#40A4A6', image=pixel).place(x=530, y=320)
tk.Label(root, textvariable=answer_text, font=('Roboto',9),fg='black',bg='#40A4A6').place(x=450, y=480, anchor='center')

def calculate():
    chain_map = { '0': '', '': '', '1': 'methane', '2': 'ethane', '3': 'propane', '4': 'butane', '5': 'pentane', '6': 'hexane', '7': 'heptane', '8': 'octane', '9': 'nonane', '10': 'decane' }
    methyl_map = { '0': '', '': '', '1': '-methyl-', '2': '-dimethyl-', '3': '-trimethyl-', '4': '-tetramethyl-' }
    ethyl_map = { '0': '', '': '', '1': '-ethyl-', '2': '-diethyl-', '3': '-triethyl-', '4': '-tetraethyl-' }
    propyl_map = { '0': '', '': '', '1': '-propyl-', '2': '-dipropyl-', '3': '-tripropyl-', '4': '-tetrapropyl-' }
    butyl_map = { '0': '', '': '', '1': '-butyl-', '2': '-dibutyl-', '3': '-tributyl-', '4': '-tetrabutyl-' }
    bromo_map = { '0': '', '': '', '1': '-bromo-', '2': '-dibromo-', '3': '-tribromo-', '4': '-tetrabromo-' }
    
    answer_text.set(
        where['bromo'].get() + bromo_map.get(number['bromo'].get(), 'invalid input') +
        where['butyl'].get() + butyl_map.get(number['butyl'].get(), 'invalid input') +
        where['ethyl'].get() + ethyl_map.get(number['ethyl'].get(), 'invalid input') +
        where['methyl'].get() + methyl_map.get(number['methyl'].get(), 'invalid input') +
        where['propyl'].get() + propyl_map.get(number['propyl'].get(), 'invalid input') +
        ('cyclo' if cyclo.get() else '') + chain_map.get(chain.get(), 'invalid input')
    )

tk.Button(text="Calculate", command=calculate).pack(pady=1)
root.mainloop()
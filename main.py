from tkinter import *
from tkinter import ttk
import random
root = Tk()
root.title("Sortowanie")
root.geometry("800x600")
lista=[]
for i in range(0,30):
    lista.append(random.randint(0,100))

listaString=""
for i in lista:
    listaString=listaString+str(i)+", "
numbersLabel=ttk.Label(root, text="Lista: "+listaString,font=('Arial',18))
numbersLabel.pack(padx=20,pady=20)
bubbleSortButton=ttk.Button(root, text="Bubble sort", command=root.destroy)
bubbleSortButton.pack()
quickSortButton=ttk.Button(root, text="Quick sort", command=root.destroy)
quickSortButton.pack()
mergeSortButton=ttk.Button(root, text="Merge sort", command=root.destroy)
mergeSortButton.pack()





exitButton=ttk.Button(root, text="Wyjdz", command=root.destroy)
exitButton.pack()
root.mainloop()

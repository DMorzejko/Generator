import tkinter as tk
from tkinter import messagebox
import dbConnection
import Generator
import InsertMaker


class Gui(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Generator Danych do bazy')
       # self.geometry('650x450')

        self.label1 = tk.Label(self, text='Do jakich tabel generujemy dane?', font=('Arial', 20, "bold"))
        self.label1.grid(row=0, column=0, columnspan=2, sticky='EW',pady=10)

        self.tabele = ['Klient', 'Obiekt + Przedmioty_przeglądu', 'Akumulator + Centrala + Typ + Brama']

        self.var = []
        self.chkb = []

        for i in range(len(self.tabele)):
            self.var.append(tk.IntVar())
            self.chkb.append(tk.Checkbutton(self, text=self.tabele[i], font=('Arial', 16), variable=self.var[i]))
            self.chkb[i].grid(row=(i + 1), column=0, sticky='WE')

        self.label1 = tk.Label(self, text='Liczba wpisów do wybranych tabel:', font=('Arial', 18, "bold"))
        self.label1.grid(row=6, column=0, columnspan=2,pady=15)
        self.ent = tk.Entry(self, font=('Arial', 18), justify='right')
        self.ent.grid(row=10, column=0, columnspan=2, sticky='WE')

        self.buta = tk.Button(self, text='Wypełnij bazę', font=('Arial', 18), bg='lightgray', command=self.buttonAdd)
        self.buta.grid(row=15, column=0, rowspan=2, columnspan= 2, sticky ='NEWS')

        self.butc = tk.Button(self, text='Koniec', font=('Arial', 18), bg='lightgray', command=self.quit)
        self.butc.grid(row=17, column=0, rowspan=2, columnspan= 2, sticky='NEWS')

    def buttonAdd(self):
        try:
            num = int(self.ent.get())
        except:
            messagebox.showerror('Błąd', 'Wartość ma być całkowitą liczbą.')
            print('Nie działa.')
            return

        conn = dbConnection.DbConnection()

        vartab = []
        for i in range(len(self.var)):
            vartab.append(self.var[i].get())
        gen = Generator.generator()
        noOfIns = vartab.copy()
        for i in range(len(self.var)):
            if vartab[i] == 0:
                continue
            noOfIns[i] -= 1
            dataSet = gen.get(i, num)
            if dataSet == 0:
                continue
            else:
                sqlSet = InsertMaker.genSQl(i, dataSet)
                for sql in sqlSet:
                    #print('sql:', sql)
                    conn.execute(sql)
                    noOfIns[i] += 1
        conn.commit()

        messagebox.showinfo('Działa', 'Operacja wykonana pomyślnie.')
        print('Działa.')
        del conn
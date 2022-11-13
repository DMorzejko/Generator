import tkinter as tk
from tkinter import messagebox
import dbConnection
import Generator
import InsertMaker


class Gui(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('DB fill')
        self.geometry('650x450')

        self.label1 = tk.Label(self, text='Wybierz tabele:', font=('Arial', 18))
        self.label1.grid(row=0, column=0)

        self.tabele = ['Klient', 'Obiekt', 'Brama']
        self.var = []
        self.chkb = []

        for i in range(len(self.tabele)):
            self.var.append(tk.IntVar())
            self.chkb.append(tk.Checkbutton(self, text=self.tabele[i], font=('Arial', 16), variable=self.var[i]))
            self.chkb[i].grid(row=(i + 1), column=0, sticky='W')

        self.label1 = tk.Label(self, text='Liczba wpisów do wybranych tabel:', font=('Arial', 18))
        self.label1.grid(row=0, column=2, columnspan=2)
        self.ent = tk.Entry(self, font=('Arial', 18), justify='right')
        self.ent.grid(row=1, column=2, columnspan=2, sticky='E')

        self.buta = tk.Button(self, text='Dodaj', font=('Arial', 18), bg='lightblue', command=self.buttonAdd)
        self.buta.grid(row=4, column=3, rowspan=4, sticky='NEWS')

        self.butc = tk.Button(self, text='Zamknij', font=('Arial', 18), bg='gray', command=self.quit)
        self.butc.grid(row=9, column=3, rowspan=4, sticky='NEWS')

    def buttonAdd(self):
        try:
            num = int(self.ent.get())
        except:
            messagebox.showerror('Błąd', 'Podano nieprawidłową wartość')
            return

        conn = dbConnection.DbConnection()

        vartab = []
        for i in range(len(self.var)):
            vartab.append(self.var[i].get())
        gen = Generator.generator()
        print('Liczba wierszy do dodania:', num)
        print('Do tabel:', vartab)
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
                    print('sql:', sql)
                    conn.execute(sql)
                    noOfIns[i] += 1

        conn.commit()


        info = 'Do tabel dodano: \n'
        for i in range(len(noOfIns)):
            if noOfIns[i] != 0:
                info += self.tabele[i] + ' - ' + str(int(noOfIns[i])) + ' wpisów\n'

        messagebox.showinfo('Podsumowanie', info)

        print('Dodano wierszy:', noOfIns)
        del conn
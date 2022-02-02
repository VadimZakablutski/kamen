from tkinter import*
root=Tk()
root.configure(bg="#c2abff")

Tunniplan={}
#with open("TextFile1.txt","r") as f:
#	for i in f: # создаем цикл по кол-ву строк
#		k,v=i.strip().split(" -") # отделяем слова на строчке в строчке по знаку " - "
#		Lessons[k.strip()]=v.strip() # добавляем в словарь

def newwind(a):
	a1=a.replace(" \n", "")
	#showinfo("tunni informatsioon",f"{a}")
	newwd=Toplevel() #tk()
	abc=Label(newwd,text=Lessons.get(a1),font="Calibri 23",fg="black",justify=CENTER)
	newwd.geometry("500x90")
	abc.pack()

def info(a):
    a_=a.replace(" \n","")
    infokno=Toplevel()
    okowko=Label(infokno,text=uroki.get(a_),font="Arial 26",fg="black",justify=CENTER)
    infokno.geometry("500x150")
    ak.pack()

def okno():
	showinfo(title="Oкно",message="Свободное время")
def estt():
	showinfo(title="Доп.Эстонский",message="Доп.урок\n Учитель - Olesja Ojamäe\n Кабинет - B 234")
def log():
	showinfo(title="Логистика",message="Основной урок\n Учитель - Inessa Klemanskaja\n Кабинет - B 002")
def mat():
	showinfo(title="Математика",message="Основной урок\n Учитель - Nadewda Voronova\n Кабинет - B 133")
def matt():
	showinfo(title="Доп.Математика",message="Доп.урок\n Учитель - Nadewda Voronova\n Кабинет - B 133")
def rus():
	showinfo(title="Русский",message="Основной урок\n Учитель - Ljudmila Mikhailova\n Кабинет - B 221")
def kemt():
	showinfo(title="Доп.Химия",message="Основной урок\n Учитель - Svetlana Pesestkaja\n Кабинет - B 144")
def progr():
	showinfo(title="Програмирование",message="Основной урок\n Учитель - Marina Oleinik\n Кабинет - E 07")
def füsik():
	showinfo(title="Физика",message="Основной урок\n Учитель - Nadewda Voronova\n Кабинет - B 133")
def kunst():
	showinfo(title="Исскуство",message="Основной урок\n Учитель - Aleksandrova\n Кабинет - B 232")
def fizra():
	showinfo(title="Физкультура",message="Основной урок\n Учитель - Maksim\n Кабинет - Zal A")
def rak():
	showinfo(title="Ракендусттарквара",message="Основной урок\n Учитель - Merkulova\n Кабинет - E 10")
def est():
	showinfo(title="Эстонский",message="Основной урок\n Учитель - Olesja Ojamäe\n Кабинет - B 234")
def anglt():
	showinfo(title="Доп.Английский",message="Доп.урок\n Учитель - Olga Borodina\n Кабинет - B 227")
def angl():
	showinfo(title="Английский",message="Основной урок\n Учитель - Olga Borodina\n Кабинет - B 227")

Label(text="0\n7.40-8.25", font=("Helvetica", 13,"bold"),fg="#ffb4e5",bg="#730086",borderwidth=1,relief="groove").grid(row=0,column=2,sticky=W+E+N+S)
Label(text="1\n8.30-9.15",font=("Helvetica", 13,"bold"),fg="#ffb4e5",bg="#730086",borderwidth=1,relief="groove").grid(row=0,column=3,sticky=W+E+N+S)
Label(text="2\n9.20-10.05",font=("Helvetica", 13,"bold"),fg="#ffb4e5",bg="#730086",borderwidth=1,relief="groove").grid(row=0,column=4,sticky=W+E+N+S)
Label(text="3\n10.10-10.55",font=("Helvetica", 13,"bold"),fg="#ffb4e5",bg="#730086",borderwidth=1,relief="groove").grid(row=0,column=5,sticky=W+E+N+S)
Label(text="4\n11.00-11.45",font=("Helvetica", 13,"bold"),fg="#ffb4e5",bg="#730086",borderwidth=1,relief="groove").grid(row=0,column=6,sticky=W+E+N+S)
Label(text="5\n11.50-12.35",font=("Helvetica", 13,"bold"),fg="#ffb4e5",bg="#730086",borderwidth=1,relief="groove").grid(row=0,column=7,sticky=W+E+N+S)
Label(text="6\n12.40-13.25",font=("Helvetica", 13,"bold"),fg="#ffb4e5",bg="#730086",borderwidth=1,relief="groove").grid(row=0,column=8,sticky=W+E+N+S)
Label(text="7\n13.30-14.15",font=("Helvetica", 13,"bold"),fg="#ffb4e5",bg="#730086",borderwidth=1,relief="groove").grid(row=0,column=9,sticky=W+E+N+S)
Label(text="8\n14.20-15.05",font=("Helvetica", 13,"bold"),fg="#ffb4e5",bg="#730086",borderwidth=1,relief="groove").grid(row=0,column=10,sticky=W+E+N+S)
Label(text="9\n15.10-15.55",font=("Helvetica", 13,"bold"),fg="#ffb4e5",bg="#730086",borderwidth=1,relief="groove").grid(row=0,column=11,sticky=W+E+N+S)
Label(text="10\n16.00-16.45",font=("Helvetica", 13,"bold"),fg="#ffb4e5",bg="#730086",borderwidth=1,relief="groove").grid(row=0,column=12,sticky=W+E+N+S)

Label(text="ПН",font=("Helvetica", 13,"bold"),fg="#ffb4e5",bg="#730086",borderwidth=1,relief="groove").grid(row=1,rowspan=2,column=0,columnspan=2,sticky=W+E+N+S)
Label(text="ВТ",font=("Helvetica", 13,"bold"),fg="#ffb4e5",bg="#730086",borderwidth=1,relief="groove").grid(row=3,rowspan=2,column=0,columnspan=2,sticky=W+E+N+S)
Label(text="СР",font=("Helvetica", 13,"bold"),fg="#ffb4e5",bg="#730086",borderwidth=1,relief="groove").grid(row=5,rowspan=2,column=0,columnspan=2,sticky=W+E+N+S)
Label(text="ЧТ",font=("Helvetica", 13,"bold"),fg="#ffb4e5",bg="#730086",borderwidth=1,relief="groove").grid(row=7,rowspan=2,column=0,columnspan=2,sticky=W+E+N+S)
Label(text="ПТ",font=("Helvetica", 13,"bold"),fg="#ffb4e5",bg="#730086",borderwidth=1,relief="groove").grid(row=9,rowspan=2,column=0,columnspan=2,sticky=W+E+N+S)
#1
Button(text=" ",height=2,bg="#c2abff",borderwidth=1,relief="groove").grid(row=1,column=3,sticky=W+E+N+S)
Button(text="доп.эстонский \n 2 группа",bg="#ff0086",borderwidth=1,relief="flat",command=estt).grid(row=2,column=3,sticky=W+E+N+S)
Button(text="логистика",bg="#ffb1da",borderwidth=1,relief="flat",command=log).grid(row=1,rowspan=2,column=4,columnspan=2,sticky=W+E+N+S)
Button(text="математика",bg="#fd41bd",borderwidth=1,relief="flat",command=mat).grid(row=1,rowspan=2,column=6,columnspan=2,sticky=W+E+N+S)
Button(text="окно",bg="#730086",borderwidth=1,relief="flat",command=okno).grid(row=1,rowspan=2,column=8,sticky=W+E+N+S)
Button(text="русский язык",bg="#FF35A0",borderwidth=1,relief="flat",command=rus).grid(row=1,rowspan=2,column=9,columnspan=2,sticky=W+E+N+S)
Button(text="доп.математика",bg="#fd41bd",borderwidth=1,relief="flat",command=matt).grid(row=1,rowspan=2,column=11,sticky=W+E+N+S)
#2
Button(text=" \n",bg="#c2abff",borderwidth=1,relief="groove").grid(row=6,column=3,sticky=W+E+N+S)
Button(text="доп.химия",borderwidth=1, height=4, relief="flat",bg="#C929CB",command=kemt).grid(row=3,rowspan=2,column=3,sticky=W+E+N+S)
Button(text="программирование",bg="#c57eff",borderwidth=1,relief="flat",command=progr).grid(row=3,rowspan=2,column=4,columnspan=3,sticky=W+E+N+S)
Button(text="окно",bg="#730086",borderwidth=1,relief="flat",command=okno).grid(row=3,rowspan=2,column=7,sticky=W+E+N+S)
Button(text="физика",bg="#9a76fa",borderwidth=1,relief="flat",command=füsik).grid(row=3,rowspan=2,column=8,columnspan=2,sticky=W+E+N+S)
#3
Button(text="доп.эстонский \n 1 группа",borderwidth=1,relief="flat",bg="#ff0086",command=estt).grid(row=5,column=3,sticky=W+E+N+S)
Button(text="искусство",borderwidth=1,relief="flat",bg="#C929CB",command=kunst).grid(row=5,rowspan=2,column=4,columnspan=2,sticky=W+E+N+S)
Label(text="окно",bg="#730086",borderwidth=1,relief="flat",command=okno).grid(row=5,rowspan=2,column=6,sticky=W+E+N+S)
Button(text="физкультура",borderwidth=1,relief="flat",bg="#C929CB",command=fizra).grid(row=5,rowspan=2,column=7,columnspan=2,sticky=W+E+N+S)
#4
Button(text="логистика",borderwidth=1,relief="flat",bg="#ffb1da",command=log).grid(row=7,rowspan=2,column=3,columnspan=2,sticky=W+E+N+S)
Button(text="окно",bg="#730086",borderwidth=1,relief="flat",command=okno).grid(row=7,rowspan=2,column=5,sticky=W+E+N+S)
Button(text="программирование",bg="#c57eff",borderwidth=1,relief="flat",command=progr).grid(row=7,rowspan=2,column=6,columnspan=2,sticky=W+E+N+S)
Button(text="английский \n 1 группа",bg="#c7b5f7",borderwidth=1,relief="flat",command=angl).grid(row=7,column=8,columnspan=2,sticky=W+E+N+S)
Button(text="офисные программы \n 2 группа",borderwidth=1,relief="flat",bg="#FF71BC",command=rak).grid(row=8,column=8,columnspan=2,sticky=W+E+N+S)
Button(text="офисные программы \n 1 группа",borderwidth=1,relief="flat",bg="#FF71BC",command=rak).grid(row=7,column=10,columnspan=2,sticky=W+E+N+S)
Button(text="эстонский \n 2 группа",bg="#ff0086",borderwidth=1,relief="flat",command=est).grid(row=8,column=10,columnspan=2,sticky=W+E+N+S)
#5
Button(text="эстонский \n 1 группа",bg="#ff0086",borderwidth=1,relief="flat",command=est).grid(row=9,column=3,columnspan=2,sticky=W+E+N+S)
Button(text="офисные программы \n 2 группа",borderwidth=1,bg="#FF71BC",relief="flat",command=rak).grid(row=10,column=3,columnspan=2,sticky=W+E+N+S)
Button(text="программирование",bg="#c57eff",borderwidth=1,relief="flat",command=progr).grid(row=9,rowspan=2,column=5,columnspan=5,sticky=W+E+N+S)
Button(text="офисные программы \n 1 группа",borderwidth=1,bg="#FF71BC",relief="flat",command=rak).grid(row=9,column=10,columnspan=2,sticky=W+E+N+S)
Button(text="английский \n 2 группа",borderwidth=1,bg="#c7b5f7",relief="flat",command=angl).grid(row=10,column=10,columnspan=2,sticky=W+E+N+S)


root.mainloop()

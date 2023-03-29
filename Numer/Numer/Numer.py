from tkinter import *
from tkinter.ttk import Combobox
def Loe_failist(fail:str)->list:
    f=open(fail,'r',encoding="utf-8")
    jarjend=[]
    for rida in f:
        jarjend.append(rida)
    f.close()
    return "".join(jarjend)
def Kirjuta_failisse(fail:str,jarjend:list):
     f=open(fail,'a',encoding="utf-8")
     for line in jarjend:
        f.write(line+"\n")
     f.close()
global valueT
n=0
def findArv(event):
    global n
    n+=1
    if n>0:
        global name
        name=ent.get()
        name=name.lower()
        intab = "аисъбйтывкуьглфэдмхюенцяёочжпшзрщ"
        intabList=list(intab)
        propet=Tk()
        propet.geometry("1920x1080")
        propet.title("Propeties")
        lblTest=Label(propet, text="",font="Arial 15")
        lblTest.pack()
        valueT= theme.get()
        if valueT=="Hele" or valueT=="Светлая":
            propet.configure(bg="White")
            lblTest.configure(fg="Black", bg="White")
        elif valueT=="Tume" or valueT=="Тёмная":
            propet.configure(bg="Black")
            lblTest.configure(fg="White",bg="Black")
        if all(char in intabList for char in name):
            intab = "аисъбйтывкуьглфэдмхюенцяёочжпшзрщ"
            out="111122223333444455556666777888999"
            trans=name.maketrans(intab,out)
            outi=name.translate(trans)
            outii=list(map(int,outi))
            outii=sum(outii)
            outii=str(outii)
            outii=list(outii)
            outii=list(map(int,outii))
            outii=sum(outii)
            outii=str(outii)
            outii=list(outii)
            outii=list(map(int,outii))
            outii=sum(outii)
            if outii==1:
                lblTest.configure(text=Loe_failist("ru1.txt"))
                Kirjuta_failisse("Nimi.txt",name)
            elif outii==2:
                lblTest.configure(text=Loe_failist("ru2.txt"))
                Kirjuta_failisse("Nimi.txt",name)
            elif outii==3:
                lblTest.configure(text=Loe_failist("ru3.txt"))
                Kirjuta_failisse("Nimi.txt",name)
            elif outii==4:
                lblTest.configure(text=Loe_failist("ru4.txt"))
                Kirjuta_failisse("Nimi.txt",name)
            elif outii==5:
                lblTest.configure(text=Loe_failist("ru5.txt"))
                Kirjuta_failisse("Nimi.txt",name)
            elif outii==6:
                lblTest.configure(text=Loe_failist("ru6.txt"))
                Kirjuta_failisse("Nimi.txt",name)
            elif outii==7:
                lblTest.configure(text=Loe_failist("ru7.txt"))
                Kirjuta_failisse("Nimi.txt",name)
            elif outii==8:
                lblTest.configure(text=Loe_failist("ru8.txt"))
                Kirjuta_failisse("Nimi.txt",name)
            elif outii==9:
                lblTest.configure(text=Loe_failist("ru9.txt"))
                Kirjuta_failisse("Nimi.txt",name)  
        else:
            intabEng ="ajsbktcludmvenwfoxgqzir"
            out="11112222333344445555666"
            trans=name.maketrans(intabEng,out)
            outi=name.translate(trans)
            print(name)
            outii=list(map(int,outi))
            outii=sum(outii)
            outii=str(outii)
            outii=list(outii)
            outii=list(map(int,outii))
            outii=sum(outii)
            outii=str(outii)
            outii=list(outii)
            outii=list(map(int,outii))
            outii=sum(outii)
            if outii==1:
                lblTest.configure(text=Loe_failist("et1.txt"))
                Kirjuta_failisse("Nimi.txt",name)
            elif outii==2:
                lblTest.configure(text=Loe_failist("et2.txt"))
                Kirjuta_failisse("Nimi.txt",name)
            elif outii==3:
                lblTest.configure(text=Loe_failist("et3.txt"))
                Kirjuta_failisse("Nimi.txt",name)
            elif outii==4:
                lblTest.configure(text=Loe_failist("et4.txt"))
                Kirjuta_failisse("Nimi.txt",name)
            elif outii==5:
                lblTest.configure(text=Loe_failist("et5.txt"))
                Kirjuta_failisse("Nimi.txt",name)
            elif outii==6:
                lblTest.configure(text=Loe_failist("et6.txt"))
                Kirjuta_failisse("Nimi.txt",name)
            elif outii==7:
                lblTest.configure(text=Loe_failist("et7.txt"))
                Kirjuta_failisse("Nimi.txt",name)
            elif outii==8:
                lblTest.configure(text=Loe_failist("et8.txt"))
                Kirjuta_failisse("Nimi.txt",name)
            elif outii==9:
                lblTest.configure(text=Loe_failist("et9.txt"))
                Kirjuta_failisse("Nimi.txt",name)
aken=Tk()
aken.iconbitmap("chair_lounge_icon_251515.ico")
vipad=Combobox(values=("EST","RUS"))
def get_vipad_value():
    value = vipad.get()
    if value=="EST":
        lbl.configure(text="Numerologia")
        lbl1.configure(text="Sisse nimi")
        btn.configure(text="Sisse")
        theme.configure(values=("Hele","Tume"))
        btnha.configure(text="Muuta teema")
        btnhak.configure(text="Tõlk")
    elif value=="RUS":
        lbl.configure(text="Нумерология")
        lbl1.configure(text="Введите имя")
        btn.configure(text="Ввод")
        theme.configure(values=("Светлая","Тёмная"))
        btnha.configure(text="Изменить тему")
        btnhak.configure(text="Перевод")
btnhak=Button(aken,text="Tõlk",font="Arial 10",width=5,bg="Green",fg="White", activeforeground="Green",command=get_vipad_value)
theme=Combobox(values=("Hele","Tume"))
def get_theme_value():
    valueT= theme.get()
    if valueT=="Hele" or valueT=="Светлая":
        aken.configure(bg="White")
        lbl.configure(bg="White", fg="Black")
        lbl1.configure(bg="White", fg="Black")
        ent.configure(bg="White", fg="Black")
        btn.configure(bg="White", fg="Black")
    elif valueT=="Tume" or valueT=="Тёмная":
        aken.configure(bg="Black")
        lbl.configure(bg="Black", fg="White")
        lbl1.configure(bg="Black", fg="White")
        ent.configure(bg="Black", fg="White")
        btn.configure(bg="Black", fg="White")
btnha=Button(aken,text="Muuta teema",font="Arial 10",width=14,bg="Green",fg="White", activeforeground="Green",command=get_theme_value)
aken.geometry("500x500")
aken.title("Numerologia")
lbl=Label(aken, text="Numerologia", font="Arial 50", width=30)
lbl1=Label(aken, text="Sisse nimi", font="Arial 24", width=10)
ent=Entry(aken, font="Arial 15", width=18)
btn=Button(aken, font="Arial 30", text="Sisse", bg="lightgrey")
btn.bind('<Button-1>',findArv)
obj=[vipad,btnhak,theme,btnha,lbl,lbl1, ent, btn]
for item in obj:
    item.pack(pady=5)
aken.mainloop()
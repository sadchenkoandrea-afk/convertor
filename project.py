from tkinter import *
Win_start=Tk()

Win_start.config(bg='grey')
Win_start.geometry("600x300+475+250")
Win_start.resizable(0,0)

def cal_dovzh():
    Win_start.destroy()

    def rozr_dovzh():
        vidp=dovzh.get()
        vidp1=dovzh1.get()
        znach=float(dovzh_pole.get())

        if vidp == 1 and vidp1 == 1:
            vidp_dovzh.config(text=znach)
        elif vidp == 1 and vidp1 == 2:
            vidp_dovzh.config(text=znach/10)
        elif vidp == 1 and vidp1 == 3:
            vidp_dovzh.config(text=znach/100)
        elif vidp == 1 and vidp1 == 4:
            vidp_dovzh.config(text=znach/1000)
        elif vidp == 1 and vidp1 == 5:
            vidp_dovzh.config(text=znach/1000000)
        elif vidp == 1 and vidp1 == 6:
            vidp_dovzh.config(text=znach/25.4)
        elif vidp == 1 and vidp1 == 7:
            vidp_dovzh.config(text=znach/304.8)

        elif vidp == 2 and vidp1 == 1:
            vidp_dovzh.config(text=znach*10)
        elif vidp == 2 and vidp1 == 2:
            vidp_dovzh.config(text=znach)
        elif vidp == 2 and vidp1 == 3:
            vidp_dovzh.config(text=znach/10)
        elif vidp == 2 and vidp1 == 4:
            vidp_dovzh.config(text=znach/100)
        elif vidp == 2 and vidp1 == 5:
            vidp_dovzh.config(text=znach/100000)
        elif vidp == 2 and vidp1 == 6:
            vidp_dovzh.config(text=znach/2.54)
        elif vidp == 2 and vidp1 == 7:
            vidp_dovzh.config(text=znach/30.48)

        elif vidp == 3 and vidp1 == 1:
            vidp_dovzh.config(text=znach*100)
        elif vidp == 3 and vidp1 == 2:
            vidp_dovzh.config(text=znach*10)
        elif vidp == 3 and vidp1 == 3:
            vidp_dovzh.config(text=znach)
        elif vidp == 3 and vidp1 == 4:
            vidp_dovzh.config(text=znach/10)
        elif vidp == 3 and vidp1 == 5:
            vidp_dovzh.config(text=znach/10000)
        elif vidp == 3 and vidp1 == 6:
            vidp_dovzh.config(text=znach/0.254)
        elif vidp == 3 and vidp1 == 7:
            vidp_dovzh.config(text=znach/304.8)

        elif vidp == 4 and vidp1 == 1:
            vidp_dovzh.config(text=znach*1000)
        elif vidp == 4 and vidp1 == 2:
            vidp_dovzh.config(text=znach*100)
        elif vidp == 4 and vidp1 == 3:
            vidp_dovzh.config(text=znach*10)
        elif vidp == 4 and vidp1 == 4:
            vidp_dovzh.config(text=znach)
        elif vidp == 4 and vidp1 == 5:
            vidp_dovzh.config(text=znach/1000)
        elif vidp == 4 and vidp1 == 6:
            vidp_dovzh.config(text=znach/0.0254)
        elif vidp == 4 and vidp1 == 7:
            vidp_dovzh.config(text=znach/0.3048)

        elif vidp == 5 and vidp1 == 1:
            vidp_dovzh.config(text=znach*1000000)
        elif vidp == 5 and vidp1 == 2:
            vidp_dovzh.config(text=znach*100000)
        elif vidp == 5 and vidp1 == 3:
            vidp_dovzh.config(text=znach*10000)
        elif vidp == 5 and vidp1 == 4:
            vidp_dovzh.config(text=znach*1000)
        elif vidp == 5 and vidp1 == 5:
            vidp_dovzh.config(text=znach)
        elif vidp == 5 and vidp1 == 6:
            vidp_dovzh.config(text=znach/0.0000254)
        elif vidp == 5 and vidp1 == 7:
            vidp_dovzh.config(text=znach/0.0003048)

        elif vidp == 6 and vidp1 == 1:
            vidp_dovzh.config(text=znach*25.4)
        elif vidp == 6 and vidp1 == 2:
            vidp_dovzh.config(text=znach*2.54)
        elif vidp == 6 and vidp1 == 3:
            vidp_dovzh.config(text=znach*0.254)
        elif vidp == 6 and vidp1 == 4:
            vidp_dovzh.config(text=znach*0.0254)
        elif vidp == 6 and vidp1 == 5:
            vidp_dovzh.config(text=znach*0.0000254)
        elif vidp == 6 and vidp1 == 6:
            vidp_dovzh.config(text=znach)
        elif vidp == 6 and vidp1 == 7:
            vidp_dovzh.config(text=znach/12)

        elif vidp == 7 and vidp1 == 1:
            vidp_dovzh.config(text=znach*304.8 )
        elif vidp == 7 and vidp1 == 2:
            vidp_dovzh.config(text=znach*30.48)
        elif vidp == 7 and vidp1 == 3:
            vidp_dovzh.config(text=znach*3.048)
        elif vidp == 7 and vidp1 == 4:
            vidp_dovzh.config(text=znach*0.3048)
        elif vidp == 7 and vidp1 == 5:
            vidp_dovzh.config(text=znach*0.0003048)
        elif vidp == 7 and vidp1 == 6:
            vidp_dovzh.config(text=znach*12)
        elif vidp == 7 and vidp1 == 7:
            vidp_dovzh.config(text=znach)

    def escape():
        Win_dovzh.destroy()

    Win_dovzh=Tk()
    Win_dovzh.config(bg='grey')
    Win_dovzh.geometry("900x450+316+166")
    Win_dovzh.resizable(0, 0)

    dovzh=IntVar()

    dovzh_txt=Label(text='Введіть довжину та одиницю міри', font='Arial 15', bg='grey')
    dovzh_txt.place(x=20, y=20)

    dovzh_pole=Entry(bg='grey')
    dovzh_pole.place(x=100, y=60)

    rad_mil=Radiobutton(text='Міліметр', bg='grey', font='Arial 13', value=1, variable=dovzh)
    rad_mil.place(x=20, y=100)

    rad_san = Radiobutton(text='Сантиметр', bg='grey', font='Arial 13', value=2, variable=dovzh)
    rad_san.place(x=20, y=135)

    rad_dm = Radiobutton(text='Дециметр', bg='grey', font='Arial 13', value=3, variable=dovzh)
    rad_dm.place(x=20, y=170)

    rad_m = Radiobutton(text='Mетр', bg='grey', font='Arial 13', value=4, variable=dovzh)
    rad_m.place(x=20, y=205)

    rad_km = Radiobutton(text='Кілометр', bg='grey', font='Arial 13', value=5, variable=dovzh)
    rad_km.place(x=20, y=240)

    rad_dum = Radiobutton(text='Дюйм', bg='grey', font='Arial 13', value=6, variable=dovzh)
    rad_dum.place(x=20, y=275)

    rad_fut = Radiobutton(text='Фут', bg='grey', font='Arial 13', value=7, variable=dovzh)
    rad_fut.place(x=20, y=310)

    dovzh1 = IntVar()

    dovzh_txt1 = Label(text='Введіть одиницю міри конвертації', font='Arial 15', bg='grey')
    dovzh_txt1.place(x=550, y=20)

    rad_mil1 = Radiobutton(text='Міліметр', bg='grey', font='Arial 13', value=1, variable=dovzh1)
    rad_mil1.place(x=760, y=100)

    rad_san1 = Radiobutton(text='Сантиметр', bg='grey', font='Arial 13', value=2, variable=dovzh1)
    rad_san1.place(x=760, y=135)

    rad_dm1 = Radiobutton(text='Дециметр', bg='grey', font='Arial 13', value=3, variable=dovzh1)
    rad_dm1.place(x=760, y=170)

    rad_m1 = Radiobutton(text='Mетр', bg='grey', font='Arial 13', value=4, variable=dovzh1)
    rad_m1.place(x=760, y=205)

    rad_km1 = Radiobutton(text='Кілометр', bg='grey', font='Arial 13', value=5, variable=dovzh1)
    rad_km1.place(x=760, y=240)

    rad_dum1 = Radiobutton(text='Дюйм', bg='grey', font='Arial 13', value=6, variable=dovzh1)
    rad_dum1.place(x=760, y=275)

    rad_fut1 = Radiobutton(text='Фут', bg='grey', font='Arial 13', value=7, variable=dovzh1)
    rad_fut1.place(x=760, y=310)

    Baton_dovzh_def=Button(text='Розрахунок', width=20, height=3, font='Arial 10', command=rozr_dovzh)
    Baton_dovzh_def.place(x=370, y=325)

    vidp_dovzh=Label(bg='grey')
    vidp_dovzh.place(x=370, y=390)

    Baton_escape_dovzh=Button(text="Escape", width=8, height=2, font='Arial 10', command=escape)
    Baton_escape_dovzh.place(x=810, y=390)

    Win_dovzh.mainloop()

def cal_masa():
    def escape():
        Win_masa.destroy()
    def rozr_masa():
        vidp = masa.get()
        vidp1 = masa1.get()
        znach = float(masa_pole.get())
        if vidp == 1 and vidp1 == 1:
            vidp_masa.config(text=znach)
        elif vidp == 1 and vidp1 == 2:
            vidp_masa.config(text=znach/1000)
        elif vidp == 1 and vidp1 == 3:
            vidp_masa.config(text=znach/1000000)
        elif vidp == 1 and vidp1 == 4:
            vidp_masa.config(text=znach/100000000)
        elif vidp == 1 and vidp1 == 5:
            vidp_masa.config(text=znach/1000000000)
        elif vidp == 1 and vidp1 == 6:
            vidp_masa.config(text=znach/28349.5)
        elif vidp == 1 and vidp1 == 7:
            vidp_masa.config(text=znach/453592.37)

        elif vidp == 2 and vidp1 == 1:
            vidp_masa.config(text=znach*1000)
        elif vidp == 2 and vidp1 == 2:
            vidp_masa.config(text=znach)
        elif vidp == 2 and vidp1 == 3:
            vidp_masa.config(text=znach/1000)
        elif vidp == 2 and vidp1 == 4:
            vidp_masa.config(text=znach/100000)
        elif vidp == 2 and vidp1 == 5:
            vidp_masa.config(text=znach/1000000)
        elif vidp == 2 and vidp1 == 6:
            vidp_masa.config(text=znach/28.3495)
        elif vidp == 2 and vidp1 == 7:
            vidp_masa.config(text=znach/453.59237)

        elif vidp == 3 and vidp1 == 1:
            vidp_masa.config(text=znach*1000000)
        elif vidp == 3 and vidp1 == 2:
            vidp_masa.config(text=znach*1000)
        elif vidp == 3 and vidp1 == 3:
            vidp_masa.config(text=znach)
        elif vidp == 3 and vidp1 == 4:
            vidp_masa.config(text=znach/100)
        elif vidp == 3 and vidp1 == 5:
            vidp_masa.config(text=znach/1000)
        elif vidp == 3 and vidp1 == 6:
            vidp_masa.config(text=znach/0.0283495)
        elif vidp == 3 and vidp1 == 7:
            vidp_masa.config(text=znach/0.45359237)

        elif vidp == 4 and vidp1 == 1:
            vidp_masa.config(text=znach*100000000)
        elif vidp == 4 and vidp1 == 2:
            vidp_masa.config(text=znach*100000)
        elif vidp == 4 and vidp1 == 3:
            vidp_masa.config(text=znach*100)
        elif vidp == 4 and vidp1 == 4:
            vidp_masa.config(text=znach)
        elif vidp == 4 and vidp1 == 5:
            vidp_masa.config(text=znach/10)
        elif vidp == 4 and vidp1 == 6:
            vidp_masa.config(text=znach/0.000283495)
        elif vidp == 4 and vidp1 == 7:
            vidp_masa.config(text=znach/0.0045359237)

        elif vidp == 5 and vidp1 == 1:
            vidp_masa.config(text=znach*1000000000)
        elif vidp == 5 and vidp1 == 2:
            vidp_masa.config(text=znach*1000000)
        elif vidp == 5 and vidp1 == 3:
            vidp_masa.config(text=znach*1000)
        elif vidp == 5 and vidp1 == 4:
            vidp_masa.config(text=znach*10)
        elif vidp == 5 and vidp1 == 5:
            vidp_masa.config(text=znach)
        elif vidp == 5 and vidp1 == 6:
            vidp_masa.config(text=znach/0.0000283495)
        elif vidp == 5 and vidp1 == 7:
            vidp_masa.config(text=znach/0.00045359237)

        elif vidp == 6 and vidp1 == 1:
            vidp_masa.config(text=znach*28349.5)
        elif vidp == 6 and vidp1 == 2:
            vidp_masa.config(text=znach*28.35)
        elif vidp == 6 and vidp1 == 3:
            vidp_masa.config(text=znach*0.02835)
        elif vidp == 6 and vidp1 == 4:
            vidp_masa.config(text=znach*0.0002835)
        elif vidp == 6 and vidp1 == 5:
            vidp_masa.config(text=znach*0.00002835)
        elif vidp == 6 and vidp1 == 6:
            vidp_masa.config(text=znach)
        elif vidp == 6 and vidp1 == 7:
            vidp_masa.config(text=znach/16)

        elif vidp == 7 and vidp1 == 1:
            vidp_masa.config(text=znach*453592.37)
        elif vidp == 7 and vidp1 == 2:
            vidp_masa.config(text=znach*453.59)
        elif vidp == 7 and vidp1 == 3:
            vidp_masa.config(text=znach*0.4536)
        elif vidp == 7 and vidp1 == 4:
            vidp_masa.config(text=znach*0.004536)
        elif vidp == 7 and vidp1 == 5:
            vidp_masa.config(text=znach*0.0004536)
        elif vidp == 7 and vidp1 == 6:
            vidp_masa.config(text=znach*16)
        elif vidp == 7 and vidp1 == 7:
            vidp_masa.config(text=znach)

    Win_start.destroy()
    Win_masa = Tk()
    Win_masa.config(bg='grey')
    Win_masa.geometry("900x450+316+166")
    Win_masa.resizable(0, 0)

    masa = IntVar()

    rad_mg = Radiobutton(text='Міліграм', bg='grey', font='Arial 13', value=1, variable=masa)
    rad_mg.place(x=20, y=100)

    rad_g = Radiobutton(text='Грам', bg='grey', font='Arial 13', value=2, variable=masa)
    rad_g.place(x=20, y=135)

    rad_cn = Radiobutton(text='Кілограм', bg='grey', font='Arial 13', value=3, variable=masa)
    rad_cn.place(x=20, y=170)

    rad_kg = Radiobutton(text='Центнер', bg='grey', font='Arial 13', value=4, variable=masa)
    rad_kg.place(x=20, y=205)

    rad_t = Radiobutton(text='Тонна', bg='grey', font='Arial 13', value=5, variable=masa)
    rad_t.place(x=20, y=240)

    rad_un = Radiobutton(text='Унція', bg='grey', font='Arial 13', value=6, variable=masa)
    rad_un.place(x=20, y=275)

    rad_funt = Radiobutton(text='Фунт', bg='grey', font='Arial 13', value=7, variable=masa)
    rad_funt.place(x=20, y=310)

    masa1 = IntVar()

    rad_mg1 = Radiobutton(text='Міліграм', bg='grey', font='Arial 13', value=1, variable=masa1)
    rad_mg1.place(x=760, y=100)

    rad_g1 = Radiobutton(text='Грам', bg='grey', font='Arial 13', value=2, variable=masa1)
    rad_g1.place(x=760, y=135)

    rad_kg1 = Radiobutton(text='Кілограм', bg='grey', font='Arial 13', value=3, variable=masa1)
    rad_kg1.place(x=760, y=170)

    rad_cn1 = Radiobutton(text='Центнер', bg='grey', font='Arial 13', value=4, variable=masa1)
    rad_cn1.place(x=760, y=205)

    rad_t1 = Radiobutton(text='Тонна', bg='grey', font='Arial 13', value=5, variable=masa1)
    rad_t1.place(x=760, y=240)

    rad_un1 = Radiobutton(text='Унція', bg='grey', font='Arial 13', value=6, variable=masa1)
    rad_un1.place(x=760, y=275)

    rad_funt1 = Radiobutton(text='Фунт', bg='grey', font='Arial 13', value=7, variable=masa1)
    rad_funt1.place(x=760, y=310)

    masa_txt = Label(text='Введіть довжину та одиницю міри', font='Arial 15', bg='grey')
    masa_txt.place(x=20, y=20)

    masa_pole = Entry(bg='grey')
    masa_pole.place(x=100, y=60)

    masa_txt1 = Label(text='Введіть одиницю міри конвертації', font='Arial 15', bg='grey')
    masa_txt1.place(x=550, y=20)

    Baton_masa_def = Button(text='Розрахунок', width=20, height=3, font='Arial 10', command=rozr_masa)
    Baton_masa_def.place(x=370, y=325)

    vidp_masa = Label(bg='grey')
    vidp_masa.place(x=370, y=390)

    Baton_escape_masa = Button(text="Escape", width=8, height=2, font='Arial 10', command=escape)
    Baton_escape_masa.place(x=810, y=390)

def cal_obiem():
    def escape():
        Win_obiem.destroy()

    def rozr_obiem():
        vidp = obiem.get()
        vidp1 = obiem1.get()
        znach = float(obiem_pole.get())
        if vidp == 1 and vidp1 == 1:
            vidp_obiem.config(text=znach)
        elif vidp == 1 and vidp1 == 2:
            vidp_obiem.config(text=znach/1000)
        elif vidp == 1 and vidp1 == 3:
            vidp_obiem.config(text=znach/1000000000)
        elif vidp == 1 and vidp1 == 4:
            vidp_obiem.config(text=znach/1000000000000000000)

        elif vidp == 2 and vidp1 == 1:
            vidp_obiem.config(text=znach*1000)
        elif vidp == 2 and vidp1 == 2:
            vidp_obiem.config(text=znach)
        elif vidp == 2 and vidp1 == 3:
            vidp_obiem.config(text=znach/1000000)
        elif vidp == 2 and vidp1 == 4:
            vidp_obiem.config(text=znach/1000000000000000)

        elif vidp == 3 and vidp1 == 1:
            vidp_obiem.config(text=znach*1000000000)
        elif vidp == 3 and vidp1 == 2:
            vidp_obiem.config(text=znach*1000000)
        elif vidp == 3 and vidp1 == 3:
            vidp_obiem.config(text=znach)
        elif vidp == 3 and vidp1 == 4:
            vidp_obiem.config(text=znach/1000000000)

        elif vidp == 4 and vidp1 == 1:
            vidp_obiem.config(text=znach * 1000000000000000000)
        elif vidp == 4 and vidp1 == 2:
            vidp_obiem.config(text=znach * 1000000000000000)
        elif vidp == 4 and vidp1 == 3:
            vidp_obiem.config(text=znach * 1000000000)
        elif vidp == 4 and vidp1 == 4:
            vidp_obiem.config(text=znach)

    Win_start.destroy()
    Win_obiem = Tk()
    Win_obiem.config(bg='grey')
    Win_obiem.geometry("900x450+316+166")
    Win_obiem.resizable(0, 0)

    obiem = IntVar()

    rad_mm3 = Radiobutton(text='Міліметр кубічний', bg='grey', font='Arial 13', value=1, variable=obiem)
    rad_mm3.place(x=20, y=100)

    rad_san3 = Radiobutton(text='Сантиметр кубічний', bg='grey', font='Arial 13', value=2, variable=obiem)
    rad_san3.place(x=20, y=135)

    rad_m3 = Radiobutton(text='Метр кубічний', bg='grey', font='Arial 13', value=3, variable=obiem)
    rad_m3.place(x=20, y=170)

    rad_km3 = Radiobutton(text='Кіломтер кубічний', bg='grey', font='Arial 13', value=4, variable=obiem)
    rad_km3.place(x=20, y=205)

    obiem1 = IntVar()

    rad_mm31 = Radiobutton(text='Міліметр кубічний', bg='grey', font='Arial 13', value=1, variable=obiem1)
    rad_mm31.place(x=710, y=100)

    rad_san31 = Radiobutton(text='Сантиметр кубічний', bg='grey', font='Arial 13', value=2, variable=obiem1)
    rad_san31.place(x=710, y=135)

    rad_m31 = Radiobutton(text='Метр кубічний', bg='grey', font='Arial 13', value=3, variable=obiem1)
    rad_m31.place(x=710, y=170)

    rad_km31 = Radiobutton(text='Кілометр кубічний', bg='grey', font='Arial 13', value=4, variable=obiem1)
    rad_km31.place(x=710, y=205)

    obiem_txt = Label(text='Введіть довжину та одиницю міри', font='Arial 15', bg='grey')
    obiem_txt.place(x=20, y=20)

    obiem_pole = Entry(bg='grey')
    obiem_pole.place(x=100, y=60)

    obiem_txt1 = Label(text='Введіть одиницю міри конвертації', font='Arial 15', bg='grey')
    obiem_txt1.place(x=550, y=20)

    Baton_obiem_def = Button(text='Розрахунок', width=20, height=3, font='Arial 10', command=rozr_obiem)
    Baton_obiem_def.place(x=370, y=325)

    vidp_obiem = Label(bg='grey')
    vidp_obiem.place(x=370, y=390)

    Baton_escape_obiem = Button(text="Escape", width=8, height=2, font='Arial 10', command=escape)
    Baton_escape_obiem.place(x=810, y=390)

def cal_temp():
    def escape():
        Win_temp.destroy()
    def rozr_temp():
        vidp = temp.get()
        vidp1 = temp1.get()
        znach = float(temp_pole.get())
        if vidp == 1 and vidp1 == 1:
            vidp_temp.config(text=znach)
        elif vidp == 1 and vidp1 == 2:
            vidp_temp.config(text=znach*1.8+32)
        elif vidp == 1 and vidp1 == 3:
            vidp_temp.config(text=znach+273.15)

        elif vidp == 2 and vidp1 == 1:
            vidp_temp.config(text=(znach-32)*(5/9))
        elif vidp == 2 and vidp1 == 2:
            vidp_temp.config(text=znach)
        elif vidp == 2 and vidp1 == 3:
            vidp_temp.config(text=(znach-32)*(5/9)+273.15)

        elif vidp == 3 and vidp1 == 1:
            vidp_temp.config(text=znach-273.15)
        elif vidp == 3 and vidp1 == 2:
            vidp_temp.config(text=(znach-273.15)*1.8+32)
        elif vidp == 3 and vidp1 == 3:
            vidp_temp.config(text=znach)

    Win_start.destroy()
    Win_temp = Tk()
    Win_temp.config(bg='grey')
    Win_temp.geometry("900x450+316+166")
    Win_temp.resizable(0, 0)

    temp = IntVar()

    rad_cel3 = Radiobutton(text='t за Цельсієм', bg='grey', font='Arial 13', value=1, variable=temp)
    rad_cel3.place(x=20, y=100)

    rad_far3 = Radiobutton(text='t за Фаренгейтом', bg='grey', font='Arial 13', value=2, variable=temp)
    rad_far3.place(x=20, y=135)

    rad_kcel3 = Radiobutton(text='t за Кельвіном', bg='grey', font='Arial 13', value=3, variable=temp)
    rad_kcel3.place(x=20, y=170)

    temp_txt = Label(text='Введіть довжину та одиницю міри', font='Arial 15', bg='grey')
    temp_txt.place(x=20, y=20)

    temp1 = IntVar()

    rad_cel31 = Radiobutton(text='t за Цельсієм', bg='grey', font='Arial 13', value=1, variable=temp1)
    rad_cel31.place(x=710, y=100)

    rad_far31 = Radiobutton(text='t за Фаренгейтом', bg='grey', font='Arial 13', value=2, variable=temp1)
    rad_far31.place(x=710, y=135)

    rad_kel31 = Radiobutton(text='t за Кельвіном', bg='grey', font='Arial 13', value=3, variable=temp1)
    rad_kel31.place(x=710, y=170)

    temp_pole = Entry(bg='grey')
    temp_pole.place(x=100, y=60)

    temp_txt1 = Label(text='Введіть одиницю міри конвертації', font='Arial 15', bg='grey')
    temp_txt1.place(x=550, y=20)

    Baton_temp_def = Button(text='Розрахунок', width=20, height=3, font='Arial 10', command=rozr_temp)
    Baton_temp_def.place(x=370, y=325)

    vidp_temp = Label(bg='grey')
    vidp_temp.place(x=370, y=390)

    Baton_escape_temp = Button(text="Escape", width=8, height=2, font='Arial 10', command=escape)
    Baton_escape_temp.place(x=810, y=390)

def cal_plosha():
    def escape():
        Win_plosha.destroy()

    def rozr_plosha():
        vidp = plosha.get()
        vidp1 = plosha1.get()
        znach = float(plosha_pole.get())
        if vidp == 1 and vidp1 == 1:
            vidp_plosha.config(text=znach)
        elif vidp == 1 and vidp1 == 2:
            vidp_plosha.config(text=znach*0.01)
        elif vidp == 1 and vidp1 == 3:
            vidp_plosha.config(text=znach/1000000)
        elif vidp == 1 and vidp1 == 4:
            vidp_plosha.config(text=znach/1000000000000)
        elif vidp == 1 and vidp1 == 5:
            vidp_plosha.config(text=znach/10000000000)

        elif vidp == 2 and vidp1 == 1:
            vidp_plosha.config(text=znach*100)
        elif vidp == 2 and vidp1 == 2:
            vidp_plosha.config(text=znach)
        elif vidp == 2 and vidp1 == 3:
            vidp_plosha.config(text=znach/10000)
        elif vidp == 2 and vidp1 == 4:
            vidp_plosha.config(text=znach/10000000000)
        elif vidp == 2 and vidp1 == 5:
            vidp_plosha.config(text=znach/100000000)

        elif vidp == 3 and vidp1 == 1:
            vidp_plosha.config(text=znach*1000000)
        elif vidp == 3 and vidp1 == 2:
            vidp_plosha.config(text=znach*10000)
        elif vidp == 3 and vidp1 == 3:
            vidp_plosha.config(text=znach)
        elif vidp == 3 and vidp1 == 4:
            vidp_plosha.config(text=znach/1000000)
        elif vidp == 3 and vidp1 == 5:
            vidp_plosha.config(text=znach/10000)

        elif vidp == 4 and vidp1 == 1:
            vidp_plosha.config(text=znach*1000000000000)
        elif vidp == 4 and vidp1 == 2:
            vidp_plosha.config(text=znach*10000000000)
        elif vidp == 4 and vidp1 == 3:
            vidp_plosha.config(text=znach*1000000)
        elif vidp == 4 and vidp1 == 4:
            vidp_plosha.config(text=znach)
        elif vidp == 4 and vidp1 == 5:
            vidp_plosha.config(text=znach*100)

        elif vidp == 5 and vidp1 == 1:
            vidp_plosha.config(text=znach*10000000000)
        elif vidp == 5 and vidp1 == 2:
            vidp_plosha.config(text=znach*100000000)
        elif vidp == 5 and vidp1 == 3:
            vidp_plosha.config(text=znach*10000)
        elif vidp == 5 and vidp1 == 4:
            vidp_plosha.config(text=znach*0.01)
        elif vidp == 5 and vidp1 == 5:
            vidp_plosha.config(text=znach)

    Win_start.destroy()
    Win_plosha = Tk()
    Win_plosha.config(bg='grey')
    Win_plosha.geometry("900x450+316+166")
    Win_plosha.resizable(0, 0)

    plosha = IntVar()

    rad_mm2 = Radiobutton(text='Міліметри квадратні', bg='grey', font='Arial 13', value=1, variable=plosha)
    rad_mm2.place(x=20, y=100)

    rad_san2 = Radiobutton(text='Сантиметри квадратні', bg='grey', font='Arial 13', value=2, variable=plosha)
    rad_san2.place(x=20, y=135)

    rad_m2 = Radiobutton(text='Метри квадратні', bg='grey', font='Arial 13', value=3, variable=plosha)
    rad_m2.place(x=20, y=170)

    rad_km2 = Radiobutton(text='Кілометри квадратні', bg='grey', font='Arial 13', value=4, variable=plosha)
    rad_km2.place(x=20, y=205)

    rad_ga = Radiobutton(text='Гектари', bg='grey', font='Arial 13', value=5, variable=plosha)
    rad_ga.place(x=20, y=240)

    plosha1 = IntVar()

    rad_mm21 = Radiobutton(text='Міліметри квадратні', bg='grey', font='Arial 13', value=1, variable=plosha1)
    rad_mm21.place(x=690, y=100)

    rad_san21 = Radiobutton(text='Сантиметри квадратні', bg='grey', font='Arial 13', value=2, variable=plosha1)
    rad_san21.place(x=690, y=135)

    rad_m21 = Radiobutton(text='Метри квадратні', bg='grey', font='Arial 13', value=3, variable=plosha1)
    rad_m21.place(x=690, y=170)

    rad_km21 = Radiobutton(text='Кілометри квадратні', bg='grey', font='Arial 13', value=4, variable=plosha1)
    rad_km21.place(x=690, y=205)

    rad_ga1 = Radiobutton(text='Гектари', bg='grey', font='Arial 13', value=5, variable=plosha1)
    rad_ga1.place(x=690, y=240)

    plosha_txt = Label(text='Введіть довжину та одиницю міри', font='Arial 15', bg='grey')
    plosha_txt.place(x=20, y=20)

    plosha_pole = Entry(bg='grey')
    plosha_pole.place(x=100, y=60)

    plosha_txt1 = Label(text='Введіть одиницю міри конвертації', font='Arial 15', bg='grey')
    plosha_txt1.place(x=550, y=20)

    Baton_plosha_def = Button(text='Розрахунок', width=20, height=3, font='Arial 10', command=rozr_plosha)
    Baton_plosha_def.place(x=370, y=325)

    vidp_plosha = Label(bg='grey')
    vidp_plosha.place(x=370, y=390)

    Baton_escape_plosha = Button(text="Escape", width=8, height=2, font='Arial 10', command=escape)
    Baton_escape_plosha.place(x=810, y=390)

def cal_makvin():
    def escape():
        Win_makvin.destroy()

    def rozr_makvin():
        vidp = makvin.get()
        vidp1 = makvin1.get()
        znach = float(makvin_pole.get())
        if vidp == 1 and vidp1 == 1:
            vidp_makvin.config(text=znach)
        elif vidp == 1 and vidp1 == 2:
            vidp_makvin.config(text=znach*3.6)
        elif vidp == 1 and vidp1 == 3:
            vidp_makvin.config(text=znach*2.23694)
        elif vidp == 1 and vidp1 == 4:
            vidp_makvin.config(text=znach*1.94384)

        elif vidp == 2 and vidp1 == 1:
            vidp_makvin.config(text=znach/3.6)
        elif vidp == 2 and vidp1 == 2:
            vidp_makvin.config(text=znach)
        elif vidp == 2 and vidp1 == 3:
            vidp_makvin.config(text=znach*0.621371)
        elif vidp == 2 and vidp1 == 4:
            vidp_makvin.config(text=znach*0.539957)

        elif vidp == 3 and vidp1 == 1:
            vidp_makvin.config(text=znach*0.44704)
        elif vidp == 3 and vidp1 == 2:
            vidp_makvin.config(text=znach*1.60934)
        elif vidp == 3 and vidp1 == 3:
            vidp_makvin.config(text=znach)
        elif vidp == 3 and vidp1 == 4:
            vidp_makvin.config(text=znach*0.868976)

        elif vidp == 4 and vidp1 == 1:
            vidp_makvin.config(text=znach*0.514444)
        elif vidp == 4 and vidp1 == 2:
            vidp_makvin.config(text=znach*1.852)
        elif vidp == 4 and vidp1 == 3:
            vidp_makvin.config(text=znach*1.15078)
        elif vidp == 4 and vidp1 == 4:
            vidp_makvin.config(text=znach)

    Win_start.destroy()
    Win_makvin = Tk()
    Win_makvin.config(bg='grey')
    Win_makvin.geometry("900x450+316+166")
    Win_makvin.resizable(0, 0)

    makvin = IntVar()

    rad_m_s = Radiobutton(text='Метри на секунду', bg='grey', font='Arial 13', value=1, variable=makvin)
    rad_m_s.place(x=20, y=100)

    rad_km_h = Radiobutton(text='Кілометри на годину', bg='grey', font='Arial 13', value=2, variable=makvin)
    rad_km_h.place(x=20, y=135)

    rad_m_h = Radiobutton(text='Милі на годину', bg='grey', font='Arial 13', value=3, variable=makvin)
    rad_m_h.place(x=20, y=170)

    rad_v = Radiobutton(text='Вузли', bg='grey', font='Arial 13', value=4, variable=makvin)
    rad_v.place(x=20, y=205)

    makvin1 = IntVar()

    rad_m_s1 = Radiobutton(text='Метри на секунду', bg='grey', font='Arial 13', value=1, variable=makvin1)
    rad_m_s1.place(x=690, y=100)

    rad_km_h1 = Radiobutton(text='Кілометри на годину', bg='grey', font='Arial 13', value=2, variable=makvin1)
    rad_km_h1.place(x=690, y=135)

    rad_m_h1 = Radiobutton(text='Милі на годину', bg='grey', font='Arial 13', value=3, variable=makvin1)
    rad_m_h1.place(x=690, y=170)

    rad_v1 = Radiobutton(text='Вузли', bg='grey', font='Arial 13', value=4, variable=makvin1)
    rad_v1.place(x=690, y=205)

    makvin_txt = Label(text='Введіть довжину та одиницю міри', font='Arial 15', bg='grey')
    makvin_txt.place(x=20, y=20)

    makvin_pole = Entry(bg='grey')
    makvin_pole.place(x=100, y=60)

    makvin_txt1 = Label(text='Введіть одиницю міри конвертації', font='Arial 15', bg='grey')
    makvin_txt1.place(x=550, y=20)

    Baton_makvin_def = Button(text='Розрахунок', width=20, height=3, font='Arial 10', command=rozr_makvin)
    Baton_makvin_def.place(x=370, y=325)

    vidp_makvin = Label(bg='grey')
    vidp_makvin.place(x=370, y=390)

    Baton_escape_makvin = Button(text="Escape", width=8, height=2, font='Arial 10', command=escape)
    Baton_escape_makvin.place(x=810, y=390)

Baton_dovzh=Button(text='Довжина l', width=20, height=5, command=cal_dovzh)
Baton_dovzh.place(x=35,y=30)

Baton_masa=Button(text='Вага m', width=20, height=5, command=cal_masa)
Baton_masa.place(x=225,y=30)

Baton_obiem=Button(text="Об'єм V", width=20, height=5, command=cal_obiem)
Baton_obiem.place(x=415,y=30)

Baton_temp=Button(text='Температура t', width=20, height=5, command=cal_temp)
Baton_temp.place(x=35,y=180)

Baton_plosha=Button(text='Площа S', width=20, height=5, command=cal_plosha)
Baton_plosha.place(x=225,y=180)

Baton_makvin=Button(text='Швидкість V', width=20, height=5, command=cal_makvin)
Baton_makvin.place(x=415,y=180)

Win_start.mainloop()
from tkinter import *
import random
LEBAR = 600
TINGGI = 600
KECEPATAN = 200
BADAN = 3
TEMPAT = 50
WARNAULAR = "#11f705"
WARNAMAKANAN = "#ff6200"
LATARBELAKANG = "black"
class Ular:
    def __init__(self):
        self.ukuran = BADAN
        self.koordinat = []
        self.kotak = []
        for i in range(0, BADAN):
            self.koordinat.append([0, 0])
        for x, y in self.koordinat:
            segiempat = kanvas.create_rectangle(x, y, x+TEMPAT, y+TEMPAT, fill = WARNAULAR, tag = "ular")
            self.kotak.append(segiempat)

class Makanan:
    def __init__(self):
        x = random.randint(0, (LEBAR/TEMPAT)-1)*TEMPAT
        y = random.randint(0, (TINGGI/TEMPAT)-1)*TEMPAT
        self.koordinat = [x, y]
        kanvas.create_oval(x, y, x+TEMPAT, y+TEMPAT, fill=WARNAMAKANAN, tag = "makanan")
def berikut(ular, makanan):
    x, y = ular.koordinat[0]
    if arah =="atas":
        y-=TEMPAT
    elif arah == "kiri":
        x-=TEMPAT
    elif arah =="bawah":
        y+=TEMPAT
    elif arah =="kanan":
        x+=TEMPAT
    ular.koordinat.insert(0, (x, y))
    segiempat = kanvas.create_rectangle(x, y, x+TEMPAT, y+TEMPAT, fill=WARNAULAR)
    ular.kotak.insert(0, segiempat)
    if x == makanan.koordinat[0] and y == makanan.koordinat[1]:
        global skor
        skor +=1
        label.config(text = "skor: {}".format(skor))
        kanvas.delete("makanan")
        makanan = Makanan()
    else:
        del ular.koordinat[-1]
        kanvas.delete(ular.kotak[-1])
        del ular.kotak[-1]
    if tabrak(ular):
        kalah()
    else:
        window.after(KECEPATAN, berikut, ular, makanan)
def ubah_arah(arahbaru):
    global arah
    if arahbaru =="atas":
        if arah != "bawah":
            arah = arahbaru
    elif arahbaru == "bawah":
        if arah != "atas":
            arah = arahbaru
    elif arahbaru == "kanan":
        if arah != "kiri":
            arah = arahbaru
    elif arahbaru == "kiri":
        if arah != "kanan":
            arah = arahbaru
def tabrak(ular):
    x, y = ular.koordinat[0]
    if x < 0 or x >= LEBAR:
        return True
    elif y < 0 or y >= TINGGI:
        return True
    for bagian in ular.koordinat[1:]:
        if x == bagian[0] and y == bagian[1]:
            return True
    return False
def kalah():
    kanvas.delete(ALL)
    kanvas.create_text(kanvas.winfo_width()/2, kanvas.winfo_height()/2, font = ("consolas", 70), text = "PERMAINAN \nBERAKHIR", fill = "#ff6200", tag = "gameover" )
window = Tk()
window.title("Ular")
window.resizable(False, False)
skor = 0
arah = "bawah"
label = Label(window, text = "skor: {}".format(skor), font = ('consolas', 40))
label.pack()
kanvas = Canvas(window, bg = LATARBELAKANG, height = TINGGI, width = LEBAR)
kanvas.pack()
window.update()
lebarwindow = window.winfo_width()
tinggiwindow = window.winfo_height()
lebarlayar = window.winfo_screenwidth()
tinggilayar = window.winfo_screenheight()
x = int((lebarlayar/2)-(lebarwindow/2))
y = int((tinggilayar/2)-(tinggiwindow/2))

window.geometry(f"{lebarwindow}x{tinggiwindow}+{x}+{y}")
window.bind('<Left>', lambda event: ubah_arah("kiri"))
window.bind('<Right>', lambda event: ubah_arah("kanan"))
window.bind('<Up>', lambda event: ubah_arah("atas"))
window.bind('<Down>', lambda event: ubah_arah("bawah"))

ular = Ular()
makanan = Makanan()
berikut(ular, makanan)
window.mainloop()
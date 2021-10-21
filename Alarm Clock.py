from tkinter import *
from tkinter.messagebox import *
from datetime import datetime
from time import sleep
from winsound import MessageBeep


window = Tk()
window.title('Alarm Clock')
time_str = ''


def update_cur_time():
    frame.configure(text=f'Current Time {str(datetime.now().time())[:8]}')
    window.after(ms=100, func=update_cur_time)


frame = LabelFrame(window, padx=64, pady=64)
update_cur_time()
frame.pack(expand=True, pady=16)


Label(frame, text='Set an Alarm: ').pack(side=TOP)

h = IntVar()
h.set(' H')
om1 = OptionMenu(frame, h, *range(24))
om1.pack(side=LEFT)
om1.configure()

m = IntVar()
m.set(' M')
om2 = OptionMenu(frame, m, *range(60))
om2.pack(side=LEFT)
om2.configure()

s = IntVar()
s.set(' S')
om3 = OptionMenu(frame, s, *range(60))
om3.pack(side=LEFT)
om3.configure()


def get_input():
    global time_str
    try:
        h1 = str(h.get())
    except TclError:
        h1 = '0'
    try:
        m1 = str(m.get())
    except TclError:
        m1 = '0'
    try:
        s1 = str(s.get())
    except TclError:
        s1 = '0'
    time_str = f'{h1 if len(h1)!=1 else f"0{h1}"}:{m1 if len(m1)!=1 else f"0{m1}"}:{s1 if len(s1)!=1 else f"0{s1}"}'
    globals()['l'] = Label(frame, text=f'Alarm Set for {time_str}')
    globals()['l'].place(x=30, y=90)
    check_alarm()


def check_alarm():
    stop = False

    def ring():
        if not stop:
            MessageBeep()
            sleep(1)
            window.after(ms=100, func=ring)

    if time_str == str(datetime.now().time())[:8]:
        ring()
        globals()['l'].destroy()
        showinfo('Knock-Knock', 'Stop Alarm?')
        stop = True
    else:
        window.after(ms=100, func=check_alarm)


set_butt = Button(frame, text='Set', command=get_input)
set_butt.place(x=70, y=60)

window.mainloop()

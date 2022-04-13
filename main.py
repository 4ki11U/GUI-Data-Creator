# -*- coding: utf8 -*-
import random
from tkinter import messagebox, filedialog, Label, StringVar, Entry, Tk, BooleanVar, Checkbutton, Button, END

### Создаём наше окно программы ###
window = Tk()
window.title("Генератор данных")
### Высчитаем размеры окна и ставим приложение в центре экрана
w = window.winfo_screenwidth()
h = window.winfo_screenheight()
w = w // 2  # середина экрана
h = h // 2
w = w - 200  # смещение от середины
h = h - 200
window.geometry('274x345+{}+{}'.format(w, h))
window.configure(background='#B5F2EA')
window.resizable(width=False, height=False)
### Обработка горячих клавиш для вставки в поля ###

def _onKeyRelease(event):
    ctrl = (event.state & 0x4) != 0
    if event.keycode == 88 and ctrl and event.keysym.lower() != "x":
        event.widget.event_generate("<<Cut>>")
    if event.keycode == 86 and ctrl and event.keysym.lower() != "v":
        event.widget.event_generate("<<Paste>>")
    if event.keycode == 67 and ctrl and event.keysym.lower() != "c":
        event.widget.event_generate("<<Copy>>")
    if event.keycode == 65 and ctrl and event.keysym.lower() != "a":
        event.widget.event_generate("<<SelectAll>>")


window.bind_all("<Key>", _onKeyRelease, "+")


### Обработка красивого полу-прозрачного шрифта ###

def focus_out_entry_box(widget, widget_text):
    if widget['fg'] == 'Black' and len(widget.get()) == 0:
        widget.delete(0, END)
        widget['fg'] = 'Grey'
        widget.insert(0, widget_text)


def focus_in_entry_box(widget):
    if widget['fg'] == 'Grey':
        widget['fg'] = 'Black'
        widget.delete(0, END)


### Поле для ввода номера задачи ###
ticket_number_label = Label(text="Введите номер задачи :", background='#B5F2EA').grid(row=0, column=0, sticky='w')
ticket_number = StringVar()
enter_ticket_number_by_user = Entry(window, textvariable=ticket_number, fg='Grey')
enter_ticket_number_by_user.insert(0, 'Обязательный ввод')
enter_ticket_number_by_user.bind("<FocusIn>", lambda args: focus_in_entry_box(enter_ticket_number_by_user))
enter_ticket_number_by_user.bind("<FocusOut>",
                                 lambda args: focus_out_entry_box(enter_ticket_number_by_user, 'Обязательный ввод'))
enter_ticket_number_by_user.grid(row=0, column=1, sticky='nwse', padx=5, pady=5)
label0 = Label(text="", background='#B5F2EA').grid(row=1, column=0, sticky='w')

### Обработка имени ###
name_label = Label(text="Введите имя :", background='#B5F2EA').grid(row=2, column=0, sticky='w')
enter_name_by_user = StringVar()
name_entry_by_user = Entry(textvariable=enter_name_by_user, fg='Grey')
name_entry_by_user.insert(0, 'Обязательно, буквы')
name_entry_by_user.bind("<FocusIn>", lambda args: focus_in_entry_box(name_entry_by_user))
name_entry_by_user.bind("<FocusOut>", lambda args: focus_out_entry_box(name_entry_by_user, 'Обязательно, буквы'))
name_entry_by_user.grid(row=2, column=1, sticky='nwse', padx=5, pady=5)

### Обработка фамилии ###
surname_label = Label(text="Введите фамилию:", background='#B5F2EA').grid(row=3, column=0, sticky='w')
enter_surname_by_user = StringVar()
surname_entry = Entry(textvariable=enter_surname_by_user, fg='Grey')
surname_entry.insert(0, 'Обязательно, буквы')
surname_entry.bind("<FocusIn>", lambda args: focus_in_entry_box(surname_entry))
surname_entry.bind("<FocusOut>", lambda args: focus_out_entry_box(surname_entry, 'Обязательно, буквы'))
surname_entry.grid(row=3, column=1, sticky='nwse', padx=5, pady=5)

label1 = Label(text="", background='#B5F2EA').grid(row=4, column=0, sticky='w')

### Обработка логина CallWay ###
login_callway_label = Label(text="Введите логин CallWay : ", background='#B5F2EA').grid(row=5, column=0, sticky='w')
login_callway_by_user = StringVar()
login_callway_entry = Entry(textvariable=login_callway_by_user, fg='Grey')
login_callway_entry.insert(0, 'Только цифры')
login_callway_entry.bind("<FocusIn>", lambda args: focus_in_entry_box(login_callway_entry))
login_callway_entry.bind("<FocusOut>", lambda args: focus_out_entry_box(login_callway_entry, 'Только цифры'))
login_callway_entry.grid(row=5, column=1, sticky='nwse', padx=5, pady=5)

label2 = Label(text="", background='#B5F2EA').grid(row=6, column=0, sticky='w')

dop_label = Label(text="Где еще нужно создавать ?", background='#B5F2EA').grid(row=7,
                                                                               column=0,
                                                                               columnspan=3,
                                                                               sticky='nwse')

### обрабатываем Логин CallWay отдельной функцией, для его дальнейшего удобства использования ###
pass_callway = random.choice(range(1000, 9999))


def data_callway():
    login_callway = None
    pass_callway = None
    if not login_callway_entry.index("end") == 0:
        login_callway = login_callway_entry.get()
        pass_callway = random.choice(range(1000, 9999))
    return login_callway, pass_callway


### Обработка DeskControl-checkbox ###
def checkbox_deskcontrol():
    deskcontrol_login = None
    if deskcontrol.get() == True:
        deskcontrol_login = data_callway()[0]
    return deskcontrol_login


deskcontrol = BooleanVar()
deskcontrol_checkbutton = Checkbutton(text="DeskControl",
                                      background='#B5F2EA',
                                      activebackground="white",
                                      variable=deskcontrol,
                                      onvalue=1,
                                      offvalue=0,
                                      command=checkbox_deskcontrol).grid(row=8,
                                                                         column=0,
                                                                         sticky='w')


### Обработка ГородОК-checkbox ###
def checkbox_gorodok():
    gorodok_login = None
    gorodok_pass = None
    if gorodok.get() == True:
        gorodok_login = str(data_callway()[0]) + '@ukrods.com.ua'
        gorodok_pass = str(random.choice(range(1000, 9999))) + str(random.choice(range(1000, 9999)))
    return gorodok_login, gorodok_pass


gorodok = BooleanVar()
gorodok_checkbutton = Checkbutton(text="ГородОК",
                                  background='#B5F2EA',
                                  activebackground="white",
                                  variable=gorodok,
                                  onvalue=1,
                                  offvalue=0,
                                  command=checkbox_gorodok).grid(row=9,
                                                                 column=0,
                                                                 sticky='w')


### Обработка Email-checkbox ###
def checkbox_email():
    email_login = None
    email_pass = None
    if email.get() == True:
        email_login = get_username() + '@ukrods.com.ua'
        email_pass = generator(12)
    return email_login, email_pass


email = BooleanVar()
email_checkbutton = Checkbutton(text="Почта", background='#B5F2EA',
                                activebackground="white",
                                variable=email,
                                onvalue=1,
                                offvalue=0,
                                command=checkbox_email).grid(row=10,
                                                             column=0,
                                                             sticky='w')


### Обработка SmartBox-checkbox ###
def checkbox_smartbox():
    smartbox_login = None
    smartbox_pass = None
    if smartbox.get() == True:
        smartbox_login = data_callway()[0]
        smartbox_pass = str(random.choice(range(100000, 999999)))
    return smartbox_login, smartbox_pass


smartbox = BooleanVar()
smartbox_checkbutton = Checkbutton(text="SmartBox",
                                   background='#B5F2EA',
                                   activebackground="white",
                                   variable=smartbox,
                                   onvalue=1,
                                   offvalue=0,
                                   command=checkbox_smartbox).grid(row=8,
                                                                   column=1,
                                                                   sticky='w')


### Обработка VPN-checkbox ###
def checkbox_vpn():
    vpn_login = None
    vpn_pass = None
    if vpn.get() == True:
        vpn_login = get_username()
        vpn_pass = generator(16)
    return vpn_login, vpn_pass


vpn = BooleanVar()
vpn_checkbutton = Checkbutton(text="VPN",
                              background='#B5F2EA',
                              activebackground="white",
                              variable=vpn,
                              onvalue=1,
                              offvalue=0,
                              command=checkbox_vpn).grid(row=9,
                                                         column=1,
                                                         sticky='w')


def get_username():
    return transliterate(str(enter_name_by_user.get().lower()))[0] + '.' + transliterate(
        str(enter_surname_by_user.get().lower()))


def transliterate(name):
    '''Функция, делающая транслит.
    По логике разработчика - укр букву должно преобразовать как укр, русс как русс.'''
    alphabet_ru = {
        'г': 'g',
        'и': 'i',
        'ъ': '',
        'ы': 'y',
        'э': 'e',
        'ё': 'e',
        'й': 'y',
        'Г': 'G',
        'И': 'i',
        'Ъ': '',
        'Ы': 'Y',
        'Э': 'E',
        'Ё': 'E',
        'Й': 'Y'
    }
    alphabet_ua = {
        'г': 'h',
        'ґ': 'g',
        'є': 'ie',
        'и': 'y',
        'і': 'i',
        'ї': 'i',
        'й': 'i',
        'Ґ': 'G',
        'Є': 'Ye',
        'И': 'Y',
        'І': 'i',
        'Ї': 'Yi',
        'Й': 'Y'
    }
    alphabet = {
        'а': 'a',
        'б': 'b',
        'в': 'v',
        'д': 'd',
        'е': 'e',
        'ж': 'zh',
        'з': 'z',
        'к': 'k',
        'л': 'l',
        'м': 'm',
        'н': 'n',
        'о': 'o',
        'п': 'p',
        'р': 'r',
        'с': 's',
        'т': 't',
        'у': 'u',
        'ф': 'f',
        'х': 'kh',
        'ц': 'ts',
        'ч': 'ch',
        'ш': 'sh',
        'щ': 'shch',
        'ю': 'іu',
        'я': 'ia',
        'ь': '',
        'А': 'A',
        'Б': 'B',
        'В': 'V',
        'Д': 'D',
        'Е': 'E',
        'Ж': 'Zh',
        'З': 'Z',
        'К': 'K',
        'Л': 'L',
        'М': 'M',
        'Н': 'N',
        'О': 'O',
        'П': 'P',
        'Р': 'R',
        'С': 'S',
        'Т': 'T',
        'У': 'U',
        'Ф': 'F',
        'Х': 'Kh',
        'Ц': 'Ts',
        'Ч': 'Ch',
        'Ш': 'Sh',
        'Щ': 'Shch',
        'Ю': 'Yu',
        'Я': 'Ya',
        'Ь': '',
    }
    if 'ы' or 'э' in name:
        full_alphabet = alphabet | alphabet_ru
    else:
        full_alphabet = alphabet | alphabet_ua
    try:
        for key in full_alphabet:
            name = name.replace(key, full_alphabet[key])
        return name
    except TypeError as tye:
        print(tye)


def generator(length):
    all_chars = '1234567890abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    try:
        password = ''
        for i in range(length):
            password += random.choice(all_chars)
        return password
    except TypeError as tye:
        print(tye)


def user_creator():
    try:
        user_name = str(enter_name_by_user.get())
        user_surname = str(enter_surname_by_user.get())
        user_login_callway = str(login_callway_by_user.get())

        pystaya_str_dlya_zapisi = ''

        pystoy_parol = str(random.choice(range(1000, 9999)))

        if not user_surname.isalpha():
            messagebox.showerror("Некорректные Имя и\или Фамилия пользователя",
                                 "Имя и Фамилия пользователя должны состоять только из букв."
                                 "\n\nЦифры, спец. символы или пробел не допускаются"
                                 "\n\nПожалуйста, проверьте на правильность")
        else:
            name_for_file = user_name[0] + '.' + user_surname + f' [{ticket_number.get()}]'
            file_path = filedialog.askdirectory()
            file_name = "/" + name_for_file + '.txt'
            filename_and_path = file_path + file_name

            pystaya_str_dlya_zapisi += f'Данные доступа для Оператора : {user_surname} {user_name}\n'

            if user_login_callway.isdigit():
                pystaya_str_dlya_zapisi += f'\nЛогин в CallWay : {data_callway()[0]}\nПароль для CallWay : {str(pystoy_parol)}'

            if not checkbox_deskcontrol() is None and not checkbox_deskcontrol() is None:
                pystaya_str_dlya_zapisi += f'\n\nЛогин в DeskControl : {data_callway()[0]}\nПароль для DeskControl : {str(pystoy_parol)}'

            if not checkbox_gorodok()[0] is None and not checkbox_gorodok()[1] is None:
                pystaya_str_dlya_zapisi += f'\n\nЛогин для Учетной Системы ГородОК : {checkbox_gorodok()[0]}\nПароль для Учетной Системы ГородОК : {checkbox_gorodok()[1]}'

            if not checkbox_email()[0] is None and not checkbox_email()[1] is None:
                pystaya_str_dlya_zapisi += f'\n\nЛогин для Почты : {checkbox_email()[0]}\nПароль для Почты : {checkbox_email()[1]}'

            if not checkbox_smartbox()[0] is None and not checkbox_smartbox()[1] is None:
                pystaya_str_dlya_zapisi += f'\n\nЛогин в SmartBox : {checkbox_smartbox()[0]}\nПароль для SmartBox : {checkbox_smartbox()[1]}'

            if not checkbox_vpn()[0] is None and not checkbox_vpn()[1] is None:
                pystaya_str_dlya_zapisi += f'\n\nVPN-логин : {checkbox_vpn()[0]}\nVPN-пароль : {checkbox_vpn()[1]}'

            with open(f'{filename_and_path}', 'w') as file:
                print(pystaya_str_dlya_zapisi)
                print(type(pystaya_str_dlya_zapisi))

                file.write(pystaya_str_dlya_zapisi)

            quetion = messagebox.askyesno('Вопрос', "Нужно ли создавать еще одного пользователя ?")
            if not quetion:
                window.destroy()

            else:
                name_entry_by_user.delete(0, END)
                surname_entry.delete(0, END)
                login_callway_entry.delete(0, END)
                messagebox.showinfo("Информация", "Поля очищены - можно вводить данные для нового пользователя")
    except IndexError:
        messagebox.showwarning('Внимание', f'Упс, шота пошло не так, а именно {IndexError}')
    except FileNotFoundError:
        messagebox.showwarning('Внимание', 'Такой путь не найден!')
    except TypeError:
        messagebox.showinfo('Внимание', f'{TypeError}')


label5 = Label(text="", background='#B5F2EA').grid(row=13, column=0, sticky='w')

message_button = Button(text="Сгенерировать данные !", command=user_creator, width=30, height=2, background='white',
                        activebackground="white", font=('Arial', '10', 'bold')).grid(row=14, column=0, columnspan=3)

window.mainloop()

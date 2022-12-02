import tkinter
from Cryptography import caesar_crypt
from Cryptography import caesar_decrypt
from Cryptography import frequency_analisys
from Cryptography import vigener_crypt
from Cryptography import vigener_decrypt
from Cryptography import vernam_crypt
from Cryptography import vernam_decrypt
from tkinter.ttk import Combobox


def interface_tkinter():
    """создание нового окна для ввода имени файла, выбора шифра и ввода шага/ключа шифрования"""
    def clicked():
        """обработка ввода пользователя"""
        file_name = str(txt.get())
        key = txt2.get()
        type_of_crypt = combo.get()
        if type_of_crypt == "шифр Цезаря":
            caesar_crypt(file_name, key)
        if type_of_crypt == "шифр Виженера":
            vigener_crypt(file_name, key)
        if type_of_crypt == "шифр Вернама":
            vernam_crypt(file_name)
        if type_of_crypt == "дешифр Цезаря":
            caesar_decrypt(file_name, key)
        if type_of_crypt == "дешифр Виженера":
            vigener_decrypt(file_name, key)
        if type_of_crypt == "дешифр Вернама":
            vernam_decrypt(file_name, key)
        if type_of_crypt == "взлом шифра Цезаря":
            frequency_analisys(file_name)
    window = tkinter.Tk()
    window.title("Добро пожаловать в приложение PythonRu")
    window.geometry('1000x100')
    lbl = tkinter.Label(window, text="Введите путь к файлу")
    lbl.grid(column=0, row=0)
    txt = tkinter.Entry(window, width=20)
    txt.grid(column=1, row=0)
    combo = Combobox(window)
    combo['values'] = (
        "шифр Цезаря", "шифр Виженера", "шифр Вернама", "дешифр Цезаря", "дешифр Виженера", "дешифр Вернама",
        "взлом шифра Цезаря")
    combo.current(0)
    combo.grid(column=3, row=0)
    lbl1 = tkinter.Label(window, text="Введите шаг/ключ шифрования (кроме шифра Вернама и взлома шифра Цезаря)")
    lbl1.grid(column=0, row=1)
    txt2 = tkinter.Entry(window, width=20)
    txt2.grid(column=1, row=1)
    btn = tkinter.Button(window, text="Клик!", command=clicked)
    btn.grid(column=2, row=0)
    window.mainloop()


def start():
    """запуск работы программы"""
    interface_tkinter()



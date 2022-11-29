# Project_Cryptography

def start() - запуск работы программы

def interface_tkinter() - создание нового окна для ввода имени файла, выбора шифра и ввода шага/ключа шифрования

def clicked() - обработка ввода пользователя

class Const - хранение констант

def get_message(way_in) - чтение и обработка теста файла

def caesar_crypt(way_in, key) - реализация шифра Цезаря

def caesar_decrypt(way_in, key) - реализация дешифра Цезаря

def generate_key(message, key) - увеличение длины ключа до длины текста

def vigener_crypt(way_in, key) - реализация шифра Виженера

def vigener_decrypt(way_in, key) - реализация дешифра Виженера

def vernam_crypt(way_in) - реализация шифра Вернама

def decryption(message, keys_lower, keys_upper) - дешифровка Вернама

def vernam_decrypt(way_in, key) - работа с текстовым файлом для дешифровки Вернама

def my_frequency_fill(message, min_difference) - поиск частоты появления букв в данном тексте и определения шага шифрования

def decrypt_frequency_analysis(message, original, shift) - создание дешифрованного текста

def frequency_analisys(file_in) - реализация взлома шифра Цезаря методами частотного анализа

import random
import sys
import tkinter as tk


# Генерация пароля
def create_password():

    # База для генерации пароля
    _alph = "abcdefghijklmnopqrstuvwxyz"
    _num = "0123456789"
    _symb = "!@#$%^&*()-_=+~`:;,.?/{}[]"

    # Считать данные с полей
    try:
        length = int(text_length.get())
        difficulty = int(text_diff.get())

        # Если сложность не соответствует диапазону, вызвать ошибку.
        if not 1 <= difficulty <= 4:
            raise Exception()

    # Если случилась ошибка, сообщает о неправильном вводе.
    # Например, неправильно указана сложность или поля не содержат ТОЛЬКО цифры.
    except BaseException:
        text_result.set("Неправильно указаны данные")
        return

    # Подготовка к генерации пароля
    password = ""
    var = [i for i in range(difficulty)]

    # Генерация пароля до тех пор, пока длина пароля не соответствует данным.
    while len(password) != length:

        # Подбирает случайное число сложности, каждое соответствующее для
        # следующего случайного выбора символа из базы.
        match(random.choice(var)):

            # Случайный выбор буквы нижнего регистра
            case 0:
                char = random.choice(_alph)
            # Случайный выбор цифры
            case 1: 
                char = random.choice(_num)
            # Случайный выбор буквы высшего регистра
            case 2:
                char = random.choice(_alph.upper())
            # Случайный выбор специального символа
            case 3:
                char = random.choice(_symb)

        password += char

        # Если пароль соответствует длине, проверяет его на сложность.
        if len(password) == length:

            # Если пароль не имеет букв нижнего регистра, обнуляет его.
            if difficulty >= 1 and len(set(password) & set(_alph)) == 0:
                password = ""
            # Если пароль не имеет цифр, обнуляет его.
            if difficulty >= 2 and len(set(password) & set(_num)) == 0:
                password = ""
            # Если пароль не имеет букв высшего регистра, обнуляет его.
            if difficulty >= 3 and len(set(password) & set(_alph.upper())) == 0:
                password = ""
            # Если пароль не имеет специальных символов, обнуляет его.
            if difficulty >= 4 and len(set(password) & set(_symb)) == 0:
                password = ""

    # Вывод случайного пароля (консоль + интерфейс)
    print("Случайный пароль: " + password)
    text_result.set(password)

# Создание окна и настройка
root = tk.Tk()
root.geometry('600x400')
root.title('Password Generator')

# Создание строковых переменных для Entry
text_result = tk.StringVar()
text_length = tk.StringVar()
text_diff = tk.StringVar()


# Поле результата
result_field = tk.Entry(root, width=80, font=('Times', 14), textvariable=text_result)
result_field.grid(column=0, row=0, columnspan=8)
result_field.config(state='disabled')

# Поле длины пароля
length_field = tk.Entry(root, width=80, font=('Times', 14), textvariable=text_length)
length_field.grid(column=0, row=1, columnspan=8)
# Поле сложности пароля
diff_field = tk.Entry(root, width=80, font=('Times', 14), textvariable=text_diff)
diff_field.grid(column=0, row=2, columnspan=8)
# Информация о работе с приложением
lbl = tk.Label(root, text="В первое поле нужно указать длину пароля.\nВо втором - сложность пароля от 1 до 4 \n(чем выше, тем сложнее)", font=('Agency FB', 14))
lbl.grid(column=3, row=5)
# Кнопка для генерации пароля
btn = tk.Button(root, text='Generate a password', font=('Times', 14), bg='white', fg='black',
                            command=create_password, width=25)
btn.grid(column=3, row=4)
# Запустить основной цикл
root.mainloop()

                

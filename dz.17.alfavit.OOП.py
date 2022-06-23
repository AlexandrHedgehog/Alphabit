# Класс Alphabet
# 1. Создайте класс Alphabet
# 2. Создайте метод __init__(), внутри которого будут определены два динамических свойства:
# 1) lang - язык и 2) letters - список букв. Начальные значения свойств берутся из входных параметров метода.
# 3. Создайте метод print(), который выведет в консоль буквы алфавита
# 4. Создайте метод letters_num(), который вернет количество букв в алфавите
import string
class Alphabet:
    def __init__(self, languag, list_lett):
        self.lang = languag
        self.letterts = list_lett

        #pechataem bukvi alfavita
    def print(self):
        print(self.letterts)

        #vozvrasch bukvi alffavita
    def letters_num(self):
        len(self.letterts)

# Класс EngAlphabet
# 1. Создайте класс EngAlphabet путем наследования от класса Alphabet
# 2. Создайте метод __init__(), внутри которого будет вызываться родительский метод __init__().
# В качестве параметров ему будут передаваться обозначение языка(например, 'En') и строка, состоящая из
# всех букв алфавита(можно воспользоваться свойством ascii_uppercase из модуля string).
# 3. Добавьте приватное статическое свойство __letters_num, которое будет хранить количество букв в алфавите.
# 4. Создайте метод is_en_letter(), который будет принимать букву в качестве параметра и определять, относится ли
# эта буква к английскому алфавиту.
# 5. Переопределите метод letters_num() - пусть в текущем классе классе он будет возвращать значение свойства __letters_num.
# 6. Создайте статический метод example(), который будет возвращать пример текста на английском языке.

class EngAlphabet(Alphabet):
    __letters_num = 26


    def __init__(self):
        super().__init__('En', string.ascii_uppercase)

        #proverjaem otnositsja li eta bukva k angl alfavit
    def is_en_letter(self, letter):
        if letter.upper() in self.letterts:
            return True
        return False

        # vozvraschaem angl alfavit
    def letters_num(self):
        return EngAlphabet.__letters_num

        #tekst na angl

    @staticmethod
    def example():
        print("English tekst:\nSomeday i well become a cool programmer:).")

# Тесты:
# 1. Создайте объект класса EngAlphabet
# 2. Напечатайте буквы алфавита для этого объекта
# 3. Выведите количество букв в алфавите
# 4. Проверьте, относится ли буква F к английскому алфавиту
# 5. Проверьте, относится ли буква Щ к английскому алфавиту
# 6. Выведите пример текста на английском языке



eng_alphabet = EngAlphabet()
eng_alphabet.print()
print(eng_alphabet.letters_num())
print(eng_alphabet.is_en_letter('F'))
print(eng_alphabet.is_en_letter('Щ'))
EngAlphabet.example()
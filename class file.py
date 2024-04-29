import os


class FileManipulator:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return file.read()
        else:
            return "Файл не существует."

    def write(self, data):
        with open(self.filename, 'a') as file:
            file.write(data + ' ')

    def append(self, data):
        with open(self.filename, 'a') as file:
            file.write(data + ' ')

    def count_words(self):
        text = self.read()
        return len(text.split())

    def count_characters(self):
        text = self.read()
        return len(text)

    def count_lines(self):
        text = self.read()
        return text.count('\n') + 1

    def count_occurrences(self, target):
        text = self.read()
        return text.count(target)

    def add_line_at_position(self, line, position):
        lines = self.read().split('\n')
        lines.insert(position - 1, line)
        self.write('\n'.join(lines))

    def remove_line(self, line_number):
        lines = self.read().split('\n')
        del lines[line_number - 1]
        self.write('\n'.join(lines))

    def add_sentence(self, sentence):
        self.append('\n' + sentence)

    def remove_sentence(self, sentence):
        text = self.read()
        updated_text = text.replace(sentence, '')
        self.write(updated_text)

    def main():
        filename = input("Введите путь к файлу: ")
        file_manipulator = FileManipulator(filename)

        while True:
            print("\n1. Прочитать файл.")
            print("2. Записать в файл.")
            print("3. Добавить текст в конец файла.")
            print("4. Посчитать количество слов в файле.")
            print("5. Посчитать количество символов в файле.")
            print("6. Посчитать количество строк в файле.")
            print("7. Посчитать количество вхождений набора символов в файле.")
            print("8. Добавить строку в файл на определенную позицию.")
            print("9. Удалить строку из файла.")
            print("10. Добавить предложение в конец файла.")
            print("11. Удалить предложение из файла.")
            print("12. Выйти.")

            choice = input("\nВыберите действие: ")

            if choice == '1':
                print(file_manipulator.read())
            elif choice == '2':
                data = input("Введите данные для записи в файл: ")
                file_manipulator.write(data)
            elif choice == '3':
                data = input("Введите данные для добавления в конец файла: ")
                file_manipulator.append(data)
            elif choice == '4':
                print("Количество слов в файле:", file_manipulator.count_words())
            elif choice == '5':
                print("Количество символов в файле:", file_manipulator.count_characters())
            elif choice == '6':
                print("Количество строк в файле:", file_manipulator.count_lines())
            elif choice == '7':
                target = input("Введите набор символов для подсчета вхождений: ")
                print(f"Количество вхождений '{target}' в файле:", file_manipulator.count_occurrences(target))
            elif choice == '8':
                line = input("Введите строку для добавления: ")
                position = int(input("Введите позицию, на которую вы хотите добавить строку: "))
                file_manipulator.add_line_at_position(line, position)
            elif choice == '9':
                line_number = int(input("Введите номер строки, которую вы хотите удалить: "))
                file_manipulator.remove_line(line_number)
            elif choice == '10':
                sentence = input("Введите предложение для добавления в конец файла: ")
                file_manipulator.add_sentence(sentence)
            elif choice == '11':
                sentence_to_remove = input("Введите предложение, которое вы хотите удалить из файла: ")
                file_manipulator.remove_sentence(sentence_to_remove)
            elif choice == '12':
                print("Программа завершена.")
                break
            else:
                print("Ошибка: Неверный ввод. Попробуйте еще раз.")

a = FileManipulator
a.main()

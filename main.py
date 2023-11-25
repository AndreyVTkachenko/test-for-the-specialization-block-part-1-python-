import datetime
import json


# Функция для загрузки заметок из файла
def load_notes():
    try:
        with open('notes.json', 'r') as file:
            my_notes = json.load(file)
    except FileNotFoundError:
        my_notes = []
    return my_notes


# Функция для сохранения заметок в файл
def save_notes(my_notes):
    with open('notes.json', 'w') as file:
        json.dump(my_notes, file, indent=4)

# Загрузка заметок при запуске приложения
notes = load_notes()

# Основной цикл программы
while True:
    print("\nМеню:")
    print("1. Добавить заметку")
    print("2. Показать все заметки")
    print("3. Редактировать заметку")
    print("4. Удалить заметку")
    print("5. Выйти")

    choice = input("Введите команду (1-5): ")

    if choice == "1":
        add_note()
    elif choice == "2":
        display_notes()
    elif choice == "3":
        edit_note()
    elif choice == "4":
        delete_note()
    elif choice == "5":
        print("До новых встреч!")
        break
    else:
        print("Неверная команда. Попробуйте еще раз.")

# Функция для добавления новой заметки
def add_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите тело заметки: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        'id': len(notes) + 1,
        'title': title,
        'body': body,
        'timestamp': timestamp
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно сохранена.")

# Функция для удаления заметки
def delete_note():
    note_id = int(input("Введите ID заметки для удаления: "))
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена.")
            return
    print("Заметка с указанным ID не найдена.")
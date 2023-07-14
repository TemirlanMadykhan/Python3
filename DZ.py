import pickle

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class NoteManager:
    def __init__(self):
        self.notes = []

    def create_note(self, title, content):
        note = Note(title, content)
        self.notes.append(note)
        print("Заметка создана.")

    def save_notes(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.notes, file)
        print("Заметки сохранены.")

    def load_notes(self, filename):
        with open(filename, 'rb') as file:
            self.notes = pickle.load(file)
        print("Заметки загружены.")

    def list_notes(self):
        if not self.notes:
            print("Заметок пока нет.")
        else:
            for i, note in enumerate(self.notes):
                print(f"Заметка {i+1}:")
                print(f"Заголовок: {note.title}")
                print(f"Содержимое: {note.content}")
                print()

    def view_note(self, note_index):
        if note_index >= 0 and note_index < len(self.notes):
            note = self.notes[note_index]
            print(f"Заметка {note_index+1}:")
            print(f"Заголовок: {note.title}")
            print(f"Содержимое: {note.content}")
        else:
            print("Неверный индекс заметки.")

    def edit_note(self, note_index, new_title, new_content):
        if note_index >= 0 and note_index < len(self.notes):
            note = self.notes[note_index]
            note.title = new_title
            note.content = new_content
            print("Заметка отредактирована.")
        else:
            print("Неверный индекс заметки.")

    def delete_note(self, note_index):
        if note_index >= 0 and note_index < len(self.notes):
            del self.notes[note_index]
            print("Заметка удалена.")
        else:
            print("Неверный индекс заметки.")

    def search_notes(self, keyword):
        matching_notes = []
        for note in self.notes:
            if keyword.lower() in note.title.lower() or keyword.lower() in note.content.lower():
                matching_notes.append(note)
        
        if not matching_notes:
            print("Заметок с указанным ключевым словом не найдено.")
        else:
            print(f"Найдено {len(matching_notes)} заметок с ключевым словом '{keyword}':")
            for note in matching_notes:
                print(f"Заголовок: {note.title}")
                print(f"Содержимое: {note.content}")
                print()

def print_menu():
    print("Выберите опцию:")
    print("1. Создать заметку")
    print("2. Сохранить заметки в файл")
    print("3. Загрузить заметки из файла")
    print("4. Показать список заметок")
    print("5. Просмотреть заметку по индексу")
    print("6. Редактировать заметку")
    print("7. Удалить заметку")
    print("8. Поиск заметок по ключевому слову")
    print("0. Выход")

note_manager = NoteManager()

while True:
    print_menu()
    choice = input("Введите номер опции: ")

    if choice == "1":
        title = input("Введите заголовок заметки: ")
        content = input("Введите содержимое заметки: ")
        note_manager.create_note(title, content)
    elif choice == "2":
        filename = input("Введите имя файла для сохранения: ")
        note_manager.save_notes(filename)
    elif choice == "3":
        filename = input("Введите имя файла для загрузки: ")
        note_manager.load_notes(filename)
    elif choice == "4":
        note_manager.list_notes()
    elif choice == "5":
        index = int(input("Введите индекс заметки: ")) - 1
        note_manager.view_note(index)
    elif choice == "6":
        index = int(input("Введите индекс заметки для редактирования: ")) - 1
        title = input("Введите новый заголовок: ")
        content = input("Введите новое содержимое: ")
        note_manager.edit_note(index, title, content)
    elif choice == "7":
        index = int(input("Введите индекс заметки для удаления: ")) - 1
        note_manager.delete_note(index)
    elif choice == "8":
        keyword = input("Введите ключевое слово для поиска: ")
        note_manager.search_notes(keyword)
    elif choice == "0":
        break
    else:
        print("Некорректный ввод. Попробуйте снова.")
    print()

print("Программа завершена.")

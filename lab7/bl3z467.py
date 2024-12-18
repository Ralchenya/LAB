import os
import shutil
def list_directory(path):
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                print(entry.name)
    except FileNotFoundError:
        print(f"Директория не найдена: {path}")
def delete_file_or_folder(path):
    try:
        if os.path.isfile(path):
            os.remove(path)
            print(f"Файл удален: {path}")
        elif os.path.isdir(path):
            shutil.rmtree(path)
            print(f"Папка удалена: {path}")
        else:
            print(f"Объект не найден: {path}")
    except Exception as e:
        print(f"Ошибка при удалении: {e}")
def rename_file_or_folder(current_path, new_name):
    try:
        base_path = os.path.dirname(current_path)
        new_path = os.path.join(base_path, new_name)
        os.rename(current_path, new_path)
        print(f"Переименование прошло успешно: {current_path} -> {new_path}")
    except FileNotFoundError:
        print(f"Файл или папка не найдены: {current_path}")
    except Exception as e:
        print(f"Ошибка при переименовании: {e}")
def main():
    while True:
        print("\nФайловый менеджер")
        print("1. Раскрыть директорию")
        print("2. Удалить файл/папку")
        print("3. Переименовать файл/папку")
        print("4. Выйти")

        choice = input("Выберите действие (1-4): ")

        if choice == '1':
            path = input("Введите путь к директории: ")
            list_directory(path)
        elif choice == '2':
            path = input("Введите путь к файлу или папке: ")
            delete_file_or_folder(path)
        elif choice == '3':
            current_path = input("Введите текущий путь к файлу или папке: ")
            new_name = input("Введите новое имя: ")
            rename_file_or_folder(current_path, new_name)
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите действие от 1 до 4.")
if __name__ == "__main__":
    main()

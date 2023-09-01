# Задача 1.


def split_file_path(data: str):
    dir_name, file_name = data.rsplit("\\", 1)
    name, extension = file_name.split(".")
    return dir_name, name, extension


input_str = r"C:\Путь\к\файлу\Файл.py"
print(split_file_path(input_str))

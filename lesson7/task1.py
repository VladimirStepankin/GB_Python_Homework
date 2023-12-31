import os


def rename_files(desired_name, num_digits, source_extension, target_extension, name_range):
    file_count = 1
    source_files = [f for f in os.listdir() if f.endswith(source_extension)]

    for filename in source_files:
        original_name = filename[:name_range[1] + 1]  # Выбираем диапазон символов из исходного имени

        if desired_name:
            new_name = original_name + desired_name + str(file_count).zfill(num_digits) + target_extension
        else:
            new_name = original_name + str(file_count).zfill(num_digits) + target_extension

        os.rename(filename, new_name)
        file_count += 1


rename_files("new_name", 2, ".txt", ".md", [3, 6])

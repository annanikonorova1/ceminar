import os
def renames(new_name: str, start_count_number: int = '', select_expansion: str = '',
            end_expansion: str = '', range_char_old_name: list = []):
# создаём спиок файлов в текущей дериктории
    all_files_directory = os.listdir()
# Проходимся по каждому файлу в текущей директории
    for file in all_files_directory:
        if file == "main.py":
            continue
# Создаём две переменные (количество символов старого имени, расширение старого имени)
        count_char_old_name, expansion_old_file = '', file.split('.')[1]
# Если при указании аргументов задали выбранное расширени и такого нет в списке файлов, то пропускаем итерацию
        if select_expansion != '' and expansion_old_file != select_expansion:
            continue
# Если не указывали аргумент изменения расширения, то оставвляем прежнее расширение
        if end_expansion == '':
            end_expansion = expansion_old_file
# Если в аргументах указали с какого по каой символ нужно сохранить от старого имени, то формируем срез
        if len(range_char_old_name) == 2:
            count_char_old_name = file[range_char_old_name[0] - 1:range_char_old_name[1]:]
# Вызываем метод переименования файла для склейки получившегося имени
        os.rename(file, f'{count_char_old_name}{new_name}{str(start_count_number)}.{end_expansion}')
# если указано в аргументах число, с которого нужно начать номераци, то запускается счётчик
        if start_count_number != '':
            start_count_number += 1


renames('new_name', 10, 'md', 'csv', [1, 4])
print(os.listdir())
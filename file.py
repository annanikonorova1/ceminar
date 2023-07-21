import os
def renames(new_name: str, start_count_number: int = '', select_expansion: str = '',
            end_expansion: str = '', range_char_old_name: list = []):
    all_files_directory = os.listdir()

    for file in all_files_directory:
        if file == "main.py":
            continue
        count_char_old_name, expansion_old_file = '', file.split('.')[1]

        if select_expansion != '' and expansion_old_file != select_expansion:
            continue
        if end_expansion == '':
            end_expansion = expansion_old_file

        if len(range_char_old_name) == 2:
            count_char_old_name = file[range_char_old_name[0] - 1:range_char_old_name[1]:]

        os.rename(file, f'{count_char_old_name}{new_name}{str(start_count_number)}.{end_expansion}')
        if start_count_number != '':
            start_count_number += 1


renames('new_name', 10, 'md', 'csv', [1, 4])
print(os.listdir())
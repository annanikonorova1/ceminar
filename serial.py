from hw_pack import dir_info as di

JSON_FILENAME = "info.json"
CSV_FILENAME = "info.csv"
PICK_FILENAME = "info.pcl"

if __name__ == '__main__':
    print("Информация о каталоге: ")
    dir_info = di.dir_info()  
    print(dir_info)
  
    print("Сохранение информации в файлы")
    di.save_to_json(dir_info, JSON_FILENAME)
    di.save_to_picle(dir_info, PICK_FILENAME)
    di.save_to_csv(dir_info, CSV_FILENAME)

    print(f"Информация в файлах: {JSON_FILENAME}, {CSV_FILENAME}, {PICK_FILENAME}")
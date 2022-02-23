import os #Модель позволяет работать с операционной системой(причем с любой)

#current_dir = os.path.abspath(os.path.dirname(__file__)) #Получает путь к директории тукущего исполняемого файла
#file_path = os.path.join(current_dir, 'file.txt') # добавляем к этому пути имя файла

# element.send_keys(file_path) с помощью этой команды может передавать нашим элементам файлы

print(os.path.abspath(os.path.dirname(__file__)))





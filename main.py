import argparse
from Reading_File import ReadingFile
from Writing import write, read
from mysort_selection import selection_sort

#from Writing import write_file_after_deserialization, write_file_pickle, write, read
import timeit

"""
with open("Нашjson.json") as myfile:
    print(myfile.read())
"""
myfile = ReadingFile("Valid_data.txt")
norm_text = myfile.get_data_without_json()

print("Выберите по какому полю отсортировать записи")
menu = {
    1: 'weight',
    2: 'work_experience',
}
check = True
while check:
    for key in menu.keys():
        print(key, ':', menu[key])
    name_field = ''
    try:
        option = int(input('Enter your choice: '))
    except BaseException:
        print('Надо число')
    if option == 1:
        name_field = "weight"
        check = False
    elif option == 2:
        name_field = 'work_experience'
        check = False
    else:
        print("Что то пошло не по плану")

start_time = timeit.default_timer()
selection_sort(norm_text, name_field)
t = timeit.default_timer() - start_time
print("Вы потратили " + str(t) + " секунд жизни впустую")

write(norm_text, "Нашpicle")
myfile = ReadingFile(r"C:\Users\1162\PycharmProjects\Lr_3-master\Нашpicle.pickle")
norm_text = myfile.get_data_json()
read(norm_text, "deserialized_file")
if __name__=="__main__":
    print("Hello")
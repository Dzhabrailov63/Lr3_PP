import pickle


#def write_file_pickle(lst: list, filename) -> None:
   # """Сериализация списка и запись его в словарь"""
   # with open(filename + ".pickle", "rb") as write_file:
       # pickle.dump(lst, write_file)


#def write_file_after_deserialization(lst: list, filename: str):
   # """Запись списка в текстовый файл"""
  #  with open(filename + '.txt', 'wb') as txt_file:
   #     for item in lst:
    #        txt_file.write("%s\n" % item)


def write(lst: list, filename):
    with open(filename, 'wb') as write_file:
        pickle.dump(lst, write_file)

def read(filename):
    with open(filename, 'rb') as read_file:
        pickle.load(read_file)

"""valid_data = ValidPeople(pathlib.Path("correct_data.txt"))
sort_data = selection_sort(valid_data.data, "height")
print(sort_data)
json.dump(
    sort_data,
    open(
        "result_sort.txt", "w"),indent=4)"""
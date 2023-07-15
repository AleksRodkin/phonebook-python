book_dict = {}
path = 'phonebook/phonebook.txt'

def open_file():
	with open(path, 'r', encoding='UTF-8') as file: 
		data = file.readlines()
	for contact in data:
		uid, name, phone, comment = contact.strip().split(';') 
		book_dict[int(uid)] = [name, phone, comment]
                
def save_file():
	with open(path, 'w', encoding='UTF-8') as file:
		all_contacts = []
		for uid, contact in book_dict.items():
			all_contacts.append(';'.join([str(uid), contact[0], contact[1], contact[2]]))
		all_contacts = '\n'.join(all_contacts)
		file.write(all_contacts)

def show_contact(book: dict[int, list[str]]):
  print('\n' + '=' * 67)
  if book:
    for uid, contact in book.items():
      print(f'{uid: >3}. {contact[0]: <20} {contact[1]: <20} {contact[2]: <20}') 
  else:
    print('ERROR ERROR ЯОЯЯƎ ЯОЯЯƎ')
  print('=' * 67 + '\n')

def input_new_contact(input_list: list[str]):
	new_contact = []
	for item in input_list:
		new_contact.append(input(item))
	return new_contact

fields_new_contact = ['Введите имя контакта: ', 'Введите телефон: ', 'Введите комментарий: ']

def add_contact(new: list[str]):
  uid = max(book_dict) + 1
  book_dict[uid] = new
  return f'\nКонтакт успешно добавлен'

def detele_contact(uid: int) -> str:
	return book_dict.pop(uid)[0]

def search(word):
  result = {}
  for uid, contact in book_dict.items():
    for field in contact:
      if word.lower() in field.lower():
        result[uid] = contact
        break
  return result

def change_contact(uid: int, rename: list[str]):
	contact = book_dict.get(uid)
	for i in range(3):
		if rename[i]:
			contact[i] = rename[i]
	book_dict[uid] = contact
	return contact[0]

def input_new_contact(input_list: list[str]):
	new_contact = []
	for item in input_list:
		new_contact.append(input(item))
	return new_contact

fields_rename_contact = [
					'Введите новое имя контакта (или Enter - без изменений): ', 
					'Введите новый телефон (или Enter - без изменений): ', 
					'Введите новый комментарий (или Enter - без изменений): '
					]



open_file()
flag=True
while flag:
  print('''
  1 - Добавить контакт
  2 - Найти контакт
  3 - Удалить контакт
  4 - Показать контакты
  5 - Изменить контакт
  6 - Выйти''')
  answer = input("\nВведите 1, 2, 3, 4, 5 для выбора варианта или 6 если хотите выйти: " )
  if answer == '1':
    contact = input_new_contact(fields_new_contact)
    print(add_contact(contact))
    save_file()
  if answer =='2':
      insert_name = input("Введите имя или номер контакта: ")
      result = search(word=insert_name)
      show_contact(result)
  if answer == '3':
      insert_name = input("Введите имя или номер контакта: ")
      result = search(word=insert_name)
      show_contact(result)
      uid = int(input("Введите ID контакта, которого хотите удалить: "))
      name = detele_contact(uid)
      save_file()
      print("Контакт успешно удалён!")
  if answer == '4':
      print(show_contact(book_dict))
  if answer == '5':
      insert_name = input("Введите имя или номер контакта: ")
      result = search(word=insert_name)
      show_contact(result)
      uid = int(input("Введите ID контакта, которого хотите изменить: "))
      rename = input_new_contact(fields_rename_contact)
      change_contact(uid, rename)
      print('\nКонтакт успешно изменён')
      save_file()
  if answer == '6':
      flag=False
print('Goodbye'.upper())
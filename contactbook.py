while True:
  q = input('Add (a) \nSearch (s) \nQuit (q): ')

  if q == 'a':
    with open('PhoneBook-GUI/contact.txt', 'a') as f:
      name = input('Name: ')
      phone = input('Phone: ')
      f.writelines((name, ' : ', phone, '\n'))
  
  elif q == 's':
    with open('PhoneBook-GUI/contact.txt', 'r') as f:
      search = input('Search: ')
      for i in f:
        if search in i:
          print(i)
  else:
    break
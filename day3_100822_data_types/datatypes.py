item_list = []
ask_user = input('Please enter something: ')

while True:
    if str(ask_user) == 'exit':
        print('you have completed the list...')
        print('The list is:\n', item_list)
        SystemExit(0)
    else:
        item_list.append(ask_user)
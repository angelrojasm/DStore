import xmlrpc.client

client = xmlrpc.client.ServerProxy('http://localhost:8000')
ans = 0

while(ans != 6):
    print("Welcome to DStore!")
    print('----------------------------')
    print('| 1. Add Item              |')
    print('| 2. Get Item              |')
    print('| 3. Increment Item Count  |')
    print('| 4. Delete Item           |')
    print('| 5. Set Item Expiration   |')
    print('| 6. Quit                  |')
    print('----------------------------')

    ans = input('Choose Your Option: ')
    if(ans.isnumeric()):
        ans = int(ans)

    def one():
        name = input('what is the name of the item? ')
        val = input('what is the value of the item? ')
        if(val.isnumeric()):
            val = int(val)
        return client.Set(name, val)

    def two():
        name = input('what is the name of the item? ')
        return client.Get(name)

    def three():
        name = input('what is the name of the item? ')
        return client.Inc(name)

    def four():
        name = input('what is the name of the item? ')
        return client.Delete(name)

    def five():
        name = input('what is the name of the item? ')
        val = input(
            'How long do you want to wait before the item expires? (in Seconds): ')
        return client.Expire(name, float(val))

    def six():
        return 'Thank you for visiting the store!'

    switcher = {
        1: one,
        2: two,
        3: three,
        4: four,
        5: five,
        6: six,
    }
    # Get the function from switcher dictionary
    func = switcher.get(ans, lambda: "Invalid Option")
    # Execute the function
    print(func())

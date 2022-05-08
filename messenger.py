class Messenger:

    '''Surprise! it's a messenger'''

    def __init__(self, name, users = {}, chats = {}):
        self.__name = name
        self._users = users
        self._chats = chats


    @property
    def name(self):
        return self.__name


    @property
    def users(self):
        return self._users


    @property
    def chats(self):
        return self._chats


    def add_user(self, new_user):
        if not isinstance(new_user, user):
            print("This is not a valid user")
            return
        if new_user.login in self.users:
            print("Error! The user with this login is already registered")
            return
        else:
            self._users[new_user.login] = user


    def add_chat(self, new_chat):
        if not isinstance(new_chat, chat):
            print("This is not a chat")
            return
        if new_chat.name in self.chats:
            print("Error! The chat with this name already exists")
            return
        else:
            self._chats[new_chat.name] = new_chat

    # def create_chat(self, new_chat)

    # add method for printing

class user:
    '''messenger's user'''
    def __init__(self, login, name, age = None, city = None, country=None ):
        self.__login = login
        self._personal = {}
        self._chats = set()
        self._personal["name"] = name
        self._personal["age"] = age
        self._personal["city"] = city
        self._personal["country"] = country
        # self._status = "offline"


    @property
    def login(self):
        return self.__login


    @property
    def name(self):
        return self._personal["name"]


    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise AssertionError('name should be a string')
        else:
            self._personal["name"] = name


    @property
    def age(self):
        return self._personal["age"]


    @age.setter
    def age(self, age):
        try:
            if age == None or 18 <= age < 100:
                self._personal["age"] = age
            elif age < 18:
                raise ValueError('You should be older then 18')
            elif age > 100:
                raise ValueError('Please enter real age or None')
        except(TypeError):
            raise AssertionError('Age should be an integer')


    @property
    def city(self):
        return self._personal["city"]


    @city.setter
    def city(self, city):
        if not isinstance(city, str):
            raise AssertionError('City should be a string')
        else:
            self._personal["city"] = city


    @property
    def country(self):
        return self._personal["country"]


    @country.setter
    def country(self, country):
        if not isinstance(country, str):
            raise AssertionError('country should be a string')
        else:
            self._personal["country"] = country

    def get_chats_list(self):
        return self._chats


    def add_to_chat(self, old_messenger, new_chat):
        if not isinstance(old_messenger, Messenger):
            raise AssertionError('This is not a messenger')
        elif new_chat.name in old_messenger.chats:
            self._chats.add(new_chat)
            print("success")
        else:
            print(f"the chat {new_chat.name} does not exist in {old_messenger.name}")

    def send_message(self, my_chat, text):
        '''Adds message to the chat's attribute "messages", assigns ID to it.
        Returns(prints) user : message'''
        if my_chat in self._chats:
            new_msg = message(my_chat, self, text)
            my_chat.add_message(new_msg)
            print(my_chat.name, ":", sep = "")
            print(self.login, ":", text)
        else:
            print(f"You have no permission to send messages to this chat. Please, join the chat {my_chat.name} first.")


    def edit_message(self, ed_chat, ed_ID, new_text):
        '''Allows to change message text, if ID exists in this chat and user is the same as message.user'''

        if not isinstance(new_text, str):
            print(f"Error! Message should be a string")  # Empty strings are allowed
        if not isinstance(ed_chat, chat):
            print(f"The chat {ed_chat} does not exist")  # Don't want to raise error
        for m_id, msg in ed_chat._messages.items():
            if m_id == ed_ID:
                if self == msg.user:
                    msg.text = new_text
                else:
                    print("Only {msg.user.name} can edit this message")
                return
        print("message not found")


    # def delete_message




    # def check_status(user)
    # def set_status


class chat:


    '''messenger chat
       Stores messages in "messages" attribute, assigns a unique id to each new
       last_id just stores the last id namber to autoincrement it
    '''


    def __init__(self, name):
        self.name = name #check for string
        self._messages = {}
        self.__last_id = 0

    def add_message(self, new_message):
        new_id = self.__last_id + 1
        self.__last_id = new_id
        self._messages[new_id] = new_message

    def search_message(self, pattern):
        """Prints message ID and text, if patteern is in the message"""
        for m_id, msg in self._messages.items():
            if m_id != 'last_id' and msg.text.find(pattern) >= 0:
                print(f'message ID {m_id}: "{msg.text}"')


    def get_message(self, m_id):
        return self._messages[m_id]

    def edit_message(self, m_id, new_text):
        self._messages[m_id].text = new_text
        return self._messages[m_id]


class message:
    '''message'''
    def __init__(self, msg_chat, msg_user, msg_text):
        #check they exist
        self.chat=msg_chat
        self.user=msg_user
        self.text=msg_text


if __name__ == '__main__':
    my_messenger = Messenger('my_messenger')
    print(my_messenger.users)
    Olkins = user('Olkins', 'Olkins', 20)
    print(Olkins.age)
    Olkins.age = 30
    print(Olkins.age)
    print(Olkins.name)
    my_messenger.add_user(Olkins)
    print(my_messenger.users)
    Vovan = user('Vovan', 'Vovan', 30, 'Mordor')
    my_messenger.add_user(Vovan)
    print(my_messenger.users)
    print(Vovan._personal)
    main_chat = chat('main_chat')
    my_messenger.add_chat(main_chat)
    print(my_messenger.chats)
    Olkins.send_message(main_chat, "Hello!")
    Vovan.send_message(main_chat, "Hi!")
    my_messenger.add_chat(main_chat)
    Olkins.add_to_chat(my_messenger, main_chat)
    Vovan.add_to_chat(my_messenger, main_chat)
    Olkins.send_message(main_chat, "Hello!")
    Vovan.send_message(main_chat, "Hi!")
    print(main_chat.get_message(1).text)
    main_chat.search_message("H")
    Vovan.edit_message(main_chat, 1, "Hi")
    print(main_chat.get_message(1).text)
    Olkins.edit_message(main_chat, 1, "Hello there")
    print(main_chat.get_message(1).text)

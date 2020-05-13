

users = {
    'user1': ('fakefakerton123', 'fakepassword123'),
    'user2': ('email', 'password')
}


def get_user(user: str):
    return users.get(user)

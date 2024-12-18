import pickle
import random
import string
def generate_new_password(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
users = {
    "Ivanov": {
        "Google": "password1",
        "Facebook": "Password2",
        "Twitter": "password3",
        "Instagram": "password4",
        "LinkedIn": "password5",
        "GitHub": "password6"
    },
    "Petrov": {
        "Google": "p@ssword",
        "Facebook": "Passw0rd",
        "Twitter": "myPass123",
        "Instagram": "InstaPassword",
        "LinkedIn": "p@ssLinked",
        "GitHub": "securePass"
    },
    "Sidorov": {
        "Google": "S1dorov",
        "Facebook": "FbS1dorov",
        "Twitter": "Tw1tter",
        "Instagram": "In5tagram",
        "LinkedIn": "LinkedInS1d",
        "GitHub": "GitHubPass"
    },
    "Smirnov": {
        "Google": "GPass",
        "Facebook": "FPass",
        "Twitter": "TPass",
        "Instagram": "IPass",
        "LinkedIn": "LPass",
        "GitHub": "GHPass"
    },
    "Kuznetsov": {
        "Google": "KuzNet",
        "Facebook": "FbKuz",
        "Twitter": "TwKuz",
        "Instagram": "InstaKuz",
        "LinkedIn": "LinkKuz",
        "GitHub": "GitKuz"
    },
    "Popov": {
        "Google": "PopPass",
        "Facebook": "FbPop",
        "Twitter": "TwPop",
        "Instagram": "InstaPop",
        "LinkedIn": "LinkPop",
        "GitHub": "GitPop"
    },
    "Sokolov": {
        "Google": "SokolPass",
        "Facebook": "fbSokol",
        "Twitter": "TwSokol",
        "Instagram": "InstaSokol",
        "LinkedIn": "LinkSokol",
        "GitHub": "GitSokol"
    }
}
for user, passwords in users.items():
    avg_length = sum(len(password) for password in passwords.values()) / len(passwords)
    print(f"Пользователь: {user}, Средняя длина паролей: {avg_length:.2f}")
for user, passwords in users.items():
    min_site = min(passwords, key=lambda k: len(passwords[k]))
    print(f"Пользователь: {user}, Сайт с минимальным паролем: {min_site}")
for user, passwords in users.items():
    seen_passwords = {}
    for site, password in passwords.items():
        if password in seen_passwords:
            new_password = generate_new_password()
            while new_password in passwords.values():
                new_password = generate_new_password()
            passwords[site] = new_password
        seen_passwords[password] = site
for user, passwords in users.items():
    if passwords["Facebook"][0].isupper():
        print(f"Пользователь с заглавной буквой в пароле Facebook: {user}")
with open("data.pickle", "wb") as f:
    pickle.dump(users, f)
with open("data.pickle", "rb") as f:
    loaded_users = pickle.load(f)
print("Загруженные данные из файла:")
print(loaded_users)

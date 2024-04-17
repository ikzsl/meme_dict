import random
meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное",
            "ЛОХ": "Оскорбление",
            "ВАЙБ": 'Настроение',
            "ИЗИ": 'Легко'
            }
while True:
    command = input('Какую комманду вы выберете?')
    if command == 'Словарь':
        word = input("Введите непонятное слово (большими буквами!): ")
        if word in meme_dict.keys():
            # Что делать, если слово нашлось?
            print(meme_dict[word])
        else:
            # Что делать, если слово не нашлось?
            print('Такого слова нет')
    elif command == 'Угадай слово':
        slovo = random.choice(meme_dict.keys())
        print(meme_dict[slovo])
        m = input('Какое это слово?(капсом)')
        if m == (slovo):
            print('Верно!')
        else:
            print('Не верно')

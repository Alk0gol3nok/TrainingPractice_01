print('Здравствуй, далее пойдёт цикл, в котором тебе нужно будет ввести: "exit", чтобы его завершить')
while True:
    print('Введите слово "exit", чтобы завершить бесконечный цикл')
    word = input('Жду ваше слово:')
    if word != 'exit':
        continue
    break
print('Программа завершилась, вы ввели:', word)
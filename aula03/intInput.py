def intInput(input_text):
    while not (value := input(input_text)).isdigit():
        print(f'O valor \"{value}\" não é um número. Por favor insira um número.')
    return int(value)

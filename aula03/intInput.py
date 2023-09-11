def intInput(input_text, condition=lambda value: True):
    while not (value := input(input_text)).isdigit() and condition(value):
        print(f'O valor \"{value}\" não é um número. Por favor insira um número.')
    return int(value)

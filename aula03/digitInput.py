def digitInput(input_text, condition=lambda value: True):
    while (value := input(input_text)) and not value.replace('.','',1).isdigit() and condition(value):
        print(f'O valor \"{value}\" não é um número. Por favor insira um número.')
    return value

def intInput(input_text, condition=lambda value: True):
    return int(floatInput(input_text, condition))


def floatInput(input_text, condition=lambda value: True):
    return float(digitInput(input_text, condition))

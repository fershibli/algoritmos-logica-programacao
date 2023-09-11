def digitInput(input_text, condition=lambda value: True, parse_float=False):
    while not (value := input(input_text)).isdigit() and condition(value):
        print(f'O valor \"{value}\" não é um número. Por favor insira um número.')
    if parse_float:
        return float(value)
    else:
        return int(value)

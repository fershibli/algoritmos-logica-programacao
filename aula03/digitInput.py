DEFAULT_ERROR_MESSAGE ='O valor \"{value}\" não é um número. Por favor insira um número.'
def digitInput(
        input_text,
        condition=lambda value: True,
        error_message=DEFAULT_ERROR_MESSAGE):
    while (value := input(input_text)) and \
            not value.replace('.', '', 1).isdigit() or \
            not condition(float(value)):
        print(error_message.format(**locals()))
    return value


def intInput(input_text, condition=lambda value: True, error_message=DEFAULT_ERROR_MESSAGE):
    return int(floatInput(input_text, condition, error_message))


def floatInput(input_text, condition=lambda value: True, error_message=DEFAULT_ERROR_MESSAGE):
    return float(digitInput(input_text, condition, error_message))

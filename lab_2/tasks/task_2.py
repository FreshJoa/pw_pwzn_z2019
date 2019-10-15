def stack_operation(stack_commands):
    """
    Funkcja przyjmuję listę jedno i dwu elementowych krotek - operacji na stosie.
    Pierwszy element krotki to operacja, drugi wartość (opcjonalnie). Operacje:
    push - dodaj element do stosu
    pop - usuń element ze stosu
    show_max - wypisz maksymalny element w stosie
    Uzupełnij funkcje tak, by dla podanej zwróciła ciąg maksymalnych elementów (zgodny z liczbą operacj 3).

    :param stack_commands: List of tuples of stack commands.
    :type stack_commands: list
    :return: List of outputs from commands.
    :rtype: list
    """
    stack = []
    response_list = []
    for command in stack_commands:
        if command[0] is 'push':
            stack.append(command[1])
        elif command[0] is 'pop':
            stack.pop()
        elif command[0] is 'show_max':
            response_list.append(max(stack))

    return response_list


if __name__ == "__main__":
    commands = [
        ('push', 97),
        ('pop',),
        ('push', 20), 
        ('pop',), 
        ('push', 26), 
        ('push', 20), 
        ('pop',), 
        ('show_max',), 
        ('push', 91), 
        ('show_max',)
    ]
    assert stack_operation(commands) == [26, 91]

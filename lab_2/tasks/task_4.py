def count_letters(msg):
    """
    Zwraca pare (znak, liczba zliczeń) dla najczęściej występującego znaku w wiadomości.
    W przypadku równości zliczeń wartości sortowane są alfabetycznie.

    :param msg: Message to count chars in.
    :type msg: str
    :return: Most frequent pair char - count in message.
    :rtype: list
    """
    response_dict = {}
    for letter in msg:
        if response_dict.get(letter):
            response_dict[letter] = response_dict[letter] + 1
        else:
            response_dict[letter] = 1
    max_count = max(response_dict.values())
    list_frequent_chars = [key for key in response_dict.keys() if response_dict[key] == max_count]

    frequent_char = min(list_frequent_chars)
    return [frequent_char, response_dict[frequent_char]]


if __name__ == '__main__':

    msg = 'Abrakadabra'
    assert count_letters(msg) == ['a', 4]
    assert count_letters('za') == ['a', 1]

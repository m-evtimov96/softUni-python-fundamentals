def int_to_char(word):
    word_list = list(word)
    num_str = ''

    while True:
        if not word_list[0].isdigit():
            break

        num_str += word_list[0]
        word_list.pop(0)

    num_int = int(num_str)
    word_list.insert(0, chr(num_int))
    return ''.join(word_list)


def switch_letters(word):
    word_list = list(word)
    word_list[1], word_list[-1] = word_list[-1], word_list[1]
    return ''.join(word_list)


def decrypt_word(word):
    word = int_to_char(word)
    word = switch_letters(word)
    return word


message = input().split(' ')
decrypted_message = [decrypt_word(word) for word in message]
print(' '.join(decrypted_message))

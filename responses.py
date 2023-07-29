import random

keywords = ['hello', 'roll', 'add', 'div']

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == keywords[0]:
        return 'hey there'

    if p_message == keywords[1]:
        return str(random.randint(1,6))

    if p_message.startswith(keywords[2]):
        current_number = ''
        result = 0
        is_in_number = False

        for character in p_message[len(keywords[2]):]:
            if character.isdigit():
                current_number += character
                is_in_number = True

            elif is_in_number:
                result += int(current_number)
                current_number = ''
                is_in_number = False

        if is_in_number:
            result += int(current_number)

        #numbers = [int(i) for i in p_message.split() if i.isdigit()]
        #result = sum(numbers)
        return result

    if p_message.startswith(keywords[3]):
        current_number = ''
        result = None
        is_in_number = False

        for character in p_message[len(keywords[3]):]:
            if character.isdigit():
                current_number += character
                is_in_number = True

            elif is_in_number:
                if result is None:
                    result = int(current_number)
                else:
                    result /= int(current_number)
                current_number = ''
                is_in_number = False

        if is_in_number:
            if result is None:
                result = int(current_number)
            else:
                result /= int(current_number)

        return result

    if p_message == 'help':
        keywords1 = ','.join(keywords)
        return f'The keywords are "{keywords1}"' \
               f'\nUsing the "?" modifier will send private message instead' \
               f'\n{keywords[0]}: Is a friendly greeting' \
               f'\n{keywords[1]}: Is a Dice roll from 1 to 6' \
               f'\n{keywords[2]}: Will add any numbers included in the message' \
               f'\n{keywords[3]}: Will Divide any numbers included in the message'
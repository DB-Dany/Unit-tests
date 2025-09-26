def check_reverse(string: str) -> str:
    # Напишите ваш код здесь
    result = string[::-1].lower()
    return result


if __name__ == '__main__':
    assert reverse('!dlroW olleH') == 'hello world!'
    assert reverse('AvadaKedavraaaaA!') == '!aaaaarvadekadava'
    assert reverse('хаЗерс хишав ХИТЭ в ясларбозар от-ценокан Я') == 'я наконец-то разобрался в этих ваших срезах'
    print("\nОтличная работа, отправляйте на проверку!")
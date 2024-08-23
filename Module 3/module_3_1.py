calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(str):
    str = len(str), str.upper(), str.lower()
    count_calls()
    return str


def is_contains(str, list):
    list = [x.lower() for x in list]
    count_calls()
    if str.lower() in list:
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)

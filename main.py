import time


array = {
    '1': [[0,1,0], [0,1,0], [0,1,0], [0,1,0], [0,1,0]],
    '2': [[0,1,1,1,0], [0,0,0,1,0], [0,1,1,1,0], [0,1,0,0,0], [0,1,1,1,0]],
    '3': [[0,1,1,1,0], [0,0,0,1,0], [0,1,1,1,0], [0,0,0,1,0], [0,1,1,1,0]],
    '4': [[0,1,0,1,0], [0,1,0,1,0], [0,1,1,1,0], [0,0,0,1,0], [0,0,0,1,0]],
    '5': [[0,1,1,1,0], [0,1,0,0,0], [0,1,1,1,0], [0,0,0,1,0], [0,1,1,1,0]],
    '6': [[0,1,1,1,0], [0,1,0,0,0], [0,1,1,1,0], [0,1,0,1,0], [0,1,1,1,0]],
    '7': [[0,1,1,1,0], [0,0,0,1,0], [0,0,0,1,0], [0,0,0,1,0], [0,0,0,1,0]],
    '8': [[0,1,1,1,0], [0,1,0,1,0], [0,1,1,1,0], [0,1,0,1,0], [0,1,1,1,0]],
    '9': [[0,1,1,1,0], [0,1,0,1,0], [0,1,1,1,0], [0,0,0,1,0], [0,0,0,1,0]],
    '0': [[0,1,1,1,0], [0,1,0,1,0], [0,1,0,1,0], [0,1,0,1,0], [0,1,1,1,0]],
    'spacing': [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]],
    'colon': [[0,0,0], [0,1,0], [0,0,0], [0,1,0], [0,0,0]],
}


def main():
    while True:
        hours = time.strftime('%H')
        minutes = time.strftime('%M')
        seconds = time.strftime('%S')

        display = zip(array[hours[0]], array[hours[1]], array['colon'],
                    array[minutes[0]], array[minutes[1]], array['colon'],
                    array[seconds[0]], array[seconds[1]], array['spacing'])

        for row in display:
            for number in row:
                [print('\033[47m \033[0m' if character == 1 else ' ', end='') for character in number]
            print()
        time.sleep(1)
        print('\033[6A')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
# -*- coding: utf-8 -*-
while True:
    try:
        number = raw_input()
        number = int(number)

        if number < 0: break
        if number:
            hexa = hex(int(number))
            print '0x' + str(hexa[2:]).upper()

    except:
        print int(float.fromhex(number))

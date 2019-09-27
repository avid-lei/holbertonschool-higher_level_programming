#!/usr/bin/python3
def list_division(a, b, list_length):
    new_list = []
    num = 0
    for x in range(list_length):
        try:
            num = a[x] / b[x]
        except (TypeError, ValueError):
            print("wrong type")
            num = 0
        except ZeroDivisionError:
            print("division by 0")
            num = 0
        except IndexError:
            print("out of range")
            num = 0
        finally:
            new_list.append(num)

    return new_list

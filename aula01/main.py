# This is a sample Python script.
import time, math
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(text):
    # Use a breakpoint in the code line below to debug your script.
    for i, n in enumerate(text):
        print(n, end='')  # Press Ctrl+F8 to toggle the breakpoint.
        # time.sleep(abs(math.sin(i/10)/10))
        if i!=0 and i%80==0:
            print('\n', end='')
        elif i!=0 and i%10==0:
            print(' '*10, end='')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('HelloWorld'*10000)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

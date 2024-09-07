import win32con, win32api
from keyCodes import VK_CODE
from time import sleep
import search_terms

def click(x: int, y: int) -> None:
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x,y,0,0)

def type_letters(letters: str) -> None: # I dont want to do **args because that would be less practical to do letters individually
                                      # I can, instead, iterate all letters into a list
    args = [char for char in letters.lower()]
    for arg in args:
        if arg == ' ':
            arg = 'spacebar'
        win32api.keybd_event(VK_CODE[arg], 0,0,0)
        win32api.keybd_event(VK_CODE[arg], 0,win32con.KEYEVENTF_KEYUP,0)
        sleep(0.03)
    win32api.keybd_event(VK_CODE['enter'],0,0,0)
    win32api.keybd_event(VK_CODE['enter'],0,win32con.KEYEVENTF_KEYUP,0)

search_terms_lst: list = search_terms.search_terms
def main() -> None:
    print("AUTO LOOKUP")
    print("Hover your mouse over the search bar, then press enter\nwatch as you earn points quickly")
    print(f"How many searches? 1-{len(search_terms_lst)}")
    try:
        searches = int(input())
    except ValueError:
        print("Do an actual number")
    except Exception as e:
        print(e)
    print("Press enter when your mouse is on the search bar")
    input()
    x,y = win32api.GetCursorPos()
    for i in range(0,searches-1):
        click(x,y)
        type_letters(search_terms_lst[i])

if __name__ == '__main__':
    main()
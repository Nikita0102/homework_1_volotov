
from pyfiglet import figlet_format
from termcolor import colored

ascii_art = figlet_format('Nick')
print(ascii_art)

print("\n *    *  *     *****   *  *  ");
print("\n **   *       *        * *  ");
print("\n * *  *  *   *         **  ");
print("\n *   **  *    *        *  *  ");
print("\n *   **  *     *****   *   *  ");

print("Escape sequences \n\\a \tBell (alert) \n\\b \tBackspace \n\\n \tNew line \n\\t \tHorizontal tab "
      "\n\\\ \tBackslash \n\\\" \tDouble quotation mark “ \n\\\' \tSingle quotation mark ‘ """)




x = int(input("ïnsert num x:"))
y = int(input("ïnsert num y:"))
print(  x + y , x * y , x // y , x ** y , x - y )


x = int(input("ïnsert num x:"))
y = int(input("ïnsert num y:"))
print("sum" ,x + y , x * y , x // y , x ** y , x - y )
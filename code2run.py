import time
from colorama import Fore, Back, Style

print('<div class="ui segment green inverted">Starting</div>')
for x in range(10):
            time.sleep(0.1)
            print('code2run - this is '+str(x))
            if x%2==0:
                print('this is an even number')
            else:
                print('this is an Odd number')
print('<div class="ui segment green inverted">Finished</div>')


def code3run():
    print('<div class="ui segment green inverted">Starting</div>')
    for x in range(10):
                time.sleep(0.1)
                print('<span style="color:red;">Code3run - this is '+str(x)+'</span>')
                if x%2==0:
                    print('<span style="color:blue;">this is an even number</span>')
                else:
                    print('<span style="color:teal;">this is an Odd number</span>')
    print('<div class="ui segment green inverted">Finished</div>')

code3run()    
         
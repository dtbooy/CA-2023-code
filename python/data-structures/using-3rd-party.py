from colort import colorize, ForegroundColor as fc, Style, BackgroundColor as bc
#code for this package at https://github.com/thep0y/colort/blob/main/colort/colort.py

colored_text = colorize("Hello World!!", bc.BLACK, fc.GREEN, Style.BOLD)
print("colored text: ", colored_text)


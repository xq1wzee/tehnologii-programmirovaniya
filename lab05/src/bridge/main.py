from bridge import Monitor, Printer, TextOutput, ImageOutput

def main():
    monitor = Monitor()
    printer = Printer()
    text_on_monitor = TextOutput(monitor)
    text_on_printer = TextOutput(printer)
    text_on_monitor.render("Hello, world!")
    text_on_printer.render("Hello, world!")
    image_on_monitor = ImageOutput(monitor)
    image_on_monitor.render("101010101")

if __name__ == "__main__":
    main()
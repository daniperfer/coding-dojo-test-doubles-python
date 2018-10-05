from utils import DateCollaborator, PrintCollaborator


class PrintDate:
    def __init__(self, printer=PrintCollaborator(), dater=DateCollaborator()):
        self.printer = printer
        self.dater = dater

    def print_current_date(self):
        self.printer.print_param(self.dater.get_current_date())


if __name__ == '__main__':
    # Do NOT touch this function or you will be fired!
    # This function must still work once you finish!
    PrintDate().print_current_date()

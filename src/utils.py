from datetime import datetime


class PrintCollaborator:
    def __init__(self):
        pass

    def print_param(self, param):
        print(param)


class DateCollaborator:
    def __init__(self):
        pass

    def get_current_date(self):
        return datetime.now()

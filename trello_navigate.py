from Trello.trello import TrelloCommand

from operations import BoardOperation

class TrelloNavigateCommand(TrelloCommand):
    def work(self, edit):
        BoardOperation(self.conn.me).execute(self)

    def display(self, names, callback = None):
        self.show_quick_panel(names, callback)

    def output(self, text):
        self.show_output_panel(text)

    def input(self, label, callback = None):
        self.show_input_panel(label, "", callback)
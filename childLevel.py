class ChildDialog(tk.Toplevel):
    def __init__(self, parent, app, ...)
        self.app = app
        ...
        self.ok_button = tk.Button(parent, ..., command=self.on_ok)
        ...
    def on_ok(self):
        # send the data to the parent
        self.app.new_data(... data from this dialog ...)

class MainApplication(tk.Tk):
    ...

    def on_show_dialog(self):
        dialog = ChildDialog(self)
        dialog.show()

    def new_data(self, data):
        ... process data that was passed in from a dialog ...
from PyQt5 import QtWidgets
import requests

from login_ui import Ui_login_dialog
from signup_ui import Ui_signup_dialog
from msg_dialog_ui import Ui_msg_dialog
from admin_ui import Ui_admin_dialog


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.base_url = 'http://127.0.0.1:8000'

        self.current_window = None
        self.to_login()

    def change_window(self, new_window):
        if self.current_window is not None:
            self.current_window.hide()

        new_window.show()
        self.current_window = new_window

    def show_msg_dialog(self, msg):
        self.msg_dialog = QtWidgets.QDialog()
        self.msg_dialog_ui = Ui_msg_dialog()
        self.msg_dialog_ui.setupUi(self.msg_dialog)

        self.msg_dialog_ui.msg_label.setText(msg)

        self.msg_dialog.show()

    def to_login(self):
        self.login_window = QtWidgets.QMainWindow()
        self.login_ui = Ui_login_dialog()
        self.login_ui.setupUi(self.login_window)

        self.login_ui.passwd_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)

        self.login_ui.login_button.clicked.connect(self.login_logic)
        self.login_ui.sign_up_button.clicked.connect(self.to_signup)

        self.change_window(self.login_window)

    def login_logic(self):
        username = self.login_ui.username_lineEdit.text()
        passwd = self.login_ui.passwd_lineEdit.text()

        login_resp = requests.post(f'{self.base_url}/users/{username}/login', json={'password': passwd})
        if login_resp.status_code == 200:
            if username == 'admin':
                self.to_admin()
            else:
                self.username_logged_in = username
                self.to_users()
        else:  # user not exists, password incorrect, or need to confirm via email
            get_resp = requests.get(f'{self.base_url}/users/{username}')
            user_exists = get_resp.status_code == 200
            if user_exists and not (is_active := get_resp.json()['is_active']):
                self.show_msg_dialog('Please confirm signup via email')
            else:
                self.show_msg_dialog('Incorrect username or password')

    def to_signup(self):
        signup_window = QtWidgets.QMainWindow()
        self.signup_ui = Ui_signup_dialog()
        self.signup_ui.setupUi(signup_window)

        self.signup_ui.passwd_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signup_ui.signup_button.clicked.connect(self.signup_logic)

        self.change_window(signup_window)

    def signup_logic(self):
        username = self.signup_ui.username_lineEdit.text()
        passwd = self.signup_ui.passwd_lineEdit.text()
        email = self.signup_ui.email_lineEdit.text()
        card = self.signup_ui.card_lineEdit.text()
        phone = self.signup_ui.phone_lineEdit.text()
        body = {'nickname': username, 'email': email, 'pay_method': card,
                'phone_number': phone, 'password': passwd}

        post_resp = requests.post(f'{self.base_url}/users', json=body)
        if post_resp.status_code == 201:
            self.change_window(self.login_window)
            self.show_msg_dialog('Please confirm signup via email')
        else:
            self.show_msg_dialog('Username already exists')

    def to_admin(self):
        admin_window = QtWidgets.QMainWindow()
        self.admin_ui = Ui_admin_dialog()
        self.admin_ui.setupUi(admin_window)

        self.admin_logic()

        self.change_window(admin_window)

    def admin_logic(self):
        self.update_taxies_list()

        self.admin_ui.taxi_listWidget.setAlternatingRowColors(True)
        self.admin_ui.taxi_listWidget.itemClicked.connect(self.show_taxi_info)

    def update_taxies_list(self):
        self.admin_ui.taxi_listWidget.clear()
        get_resp = requests.get(f'{self.base_url}/taxies/')
        self.taxies = get_resp.json()

        for taxi in self.taxies:
            taxi_item = QtWidgets.QListWidgetItem(taxi['name'], self.admin_ui.taxi_listWidget)
            taxi_state = 'Libre' if taxi['is_free'] is True else 'Ocupado'
            taxi_item.setToolTip(taxi_state)

    def show_taxi_info(self):
        taxi_name = self.admin_ui.taxi_listWidget.currentItem().text()
        for taxi in self.taxies:
            if taxi['name'] == taxi_name:
                taxi_state = 'Libre' if taxi['is_free'] is True else 'Ocupado'
                self.admin_ui.label_status_response.setText(taxi_state)
                self.admin_ui.label_location_response.setText(taxi['actual'])
                self.admin_ui.label_destination_response.setText(taxi['destination'])
                break

    def to_users(self):
        ...


def main():
    app = QtWidgets.QApplication([])
    window = MainWindow()
    # window.show()
    # window.showMaximized()
    app.exec_()


if __name__ == "__main__":
    main()

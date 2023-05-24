import json
import platform
from pathlib import Path
from typing import Generator

from PySide6 import QtGui
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMessageBox, QPushButton, QWidget

from application.dependencies.schemas import STest
from display.test_window import Ui_Form
from application.dependencies.depends import Files


class Test(QWidget, Ui_Form, Files):
    def __init__(self, path_to_test: str):
        super().__init__()
        self.setupUi(self)
        self.path_to_test = path_to_test
        self.current_test = self.load_current_test(path=path_to_test)

        self.text_answers_from_user = list()
        self.equal_answers_from_user = list()
        self.student: dict = dict()
        self.result: dict = dict()
        self.auth_data: dict = dict()

        self.time2test: int = self.current_test.get('time2test')
        self.questions: list = self.current_test.get('questions')

        self.buttons: list[QPushButton] = [self.btnAnswer_1, self.btnAnswer_2, self.btnAnswer_3, self.btnAnswer_4]
        self.gen: Generator = self.get_gen_test_text(label=self.tbrQuestion, buttons=self.buttons, data=self.questions)
        self.progressBar.setRange(0, len(self.questions) - 1)
        self.progress_bar_counter: int = -1

        self.setup_interactive_elements()
        self.setup_non_interactive_elements()
        self.setup_placeholders()

        self.setWindowTitle('Тестирование')
        self.setWindowIcon(QtGui.QIcon(f'{self.path_to_icon()}'))

    def setup_interactive_elements(self):
        self.btnAnswer_1.clicked.connect(lambda: self.__next_question(self.gen, buttons=self.buttons))
        self.btnAnswer_2.clicked.connect(lambda: self.__next_question(self.gen, buttons=self.buttons))
        self.btnAnswer_3.clicked.connect(lambda: self.__next_question(self.gen, buttons=self.buttons))
        self.btnAnswer_4.clicked.connect(lambda: self.__next_question(self.gen, buttons=self.buttons))
        self.btnLogin.clicked.connect(lambda: self.__parse_auth_data())
        self.btnFinish.clicked.connect(lambda: self.finish_program())

    def setup_non_interactive_elements(self):
        timer_dt: list = self.__init_time_for_test()
        if len(timer_dt) > 1:
            h, m = self.__init_time_for_test()
            self.lblTimer.setText(f"{f'0{h}' if h < 9 else h}:{m}:00")
        else:
            self.lblTimer.setText(f"00:10:00" if timer_dt[0] == 0 else f"00:{timer_dt[0]}:00")
        self.timer: QTimer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(lambda: self.__minus_sec())

    def setup_placeholders(self):
        self.ledtReceiverEMail.setPlaceholderText("Введите адрес почты преподавателя")
        self.ledtSecondName.setPlaceholderText("Введите свою фамилию")
        self.ledtGroupName.setPlaceholderText("Введите номер группы. (Например 403 ИСП)")

    def finish_program(self):
        self.timer.stop()
        self.__calculate_score(self.text_answers_from_user[1:], self.current_test)
        self.__message_about_sending_results(self.equal_answers_from_user)
        self.close()

    def __calculate_score(self, answers: list[str], origin_data: dict):
        dt: STest = STest(**origin_data)
        for ans, dtt in zip(answers, dt.questions):
            for a in dtt.answers:
                print(ans, a)
                if ans[0] == a.text_answer:
                    self.equal_answers_from_user.append(a.is_true)

    def __add_percent_in_progress_bar(self):
        self.progress_bar_counter += 1
        self.progressBar.setValue(self.progress_bar_counter)

    def __init_time_for_test(self):
        minutes: int = self.time2test
        if minutes > 59:
            hours: int = minutes // 60
            minutes = minutes - hours * 60
            return [hours, minutes]
        else:
            return [minutes]

    def __next_question(self, gen: Generator, buttons: list[QPushButton]):
        if not self.timer.isActive():
            self.timer.start()
        text_answer = [btn.text() for btn in buttons if btn.isChecked()]
        dt = next(gen, False)
        if dt is False:
            self.finish_program()
        else:
            self.text_answers_from_user.append(text_answer)
        self.__add_percent_in_progress_bar()
        [btn.setCheckable(False) for btn in buttons if btn.isChecked()]
        [btn.setCheckable(True) for btn in buttons if not btn.isChecked()]

    def __parse_auth_data(self):
        default_data: str = str(Path(Path.cwd(), 'static', 'files', '.load_data.json'))
        with open(default_data, 'r') as file:
            dt = json.loads(file.read())
        lg, ps = self.decode_dt(dt=dt)
        self.auth_data["sender_email"] = lg
        self.auth_data["password"] = ps
        self.student["name"] = self.ledtSecondName.text()
        self.student["group"] = self.ledtGroupName.text()

        self.stackedWidget.setCurrentWidget(self.pgTest)

    def __minus_sec(self):
        hours, minutes, seconds = list(map(int, self.lblTimer.text().split(":")))
        if hours == 0 and minutes == 0 and seconds == 0:
            self.finish_program()
        if 0 < seconds < 60:
            seconds -= 1
        else:
            seconds = 59
            if 0 < minutes < 60:
                minutes -= 1
            else:
                if 0 < hours < 24:
                    minutes = 59
                    hours -= 1
                else:
                    QMessageBox.critical(self, "КРИТИЧЕСКАЯ ОШИБКА", "НЕЛЬЗЯ ДАВАТЬ ТАКИЕ ТЕСТЫ")
        self.lblTimer.setText(f'{hours if hours > 9 else f"0{hours}"}:'
                              f'{minutes if minutes > 9 else f"0{minutes}"}:'
                              f'{seconds if seconds > 9 else f"0{seconds}"}')

    def __message_about_sending_results(self, answers: list[bool]):
        sp: str = '/' if platform.system() == "Linux" else "\\"
        self.result["test_number"] = self.path_to_test.split(sp)[-1].split(".")[0]
        self.result["result"] = answers

        msg = QMessageBox(self)
        msg.setWindowTitle("Поздравляю!")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText(f"{self.student['name']} {self.student['group']},\n"
                    f"количество баллов равно: {sum(answers)}\n"
                    f"Результат будет выслан на почту {self.ledtReceiverEMail.text()}")
        btn_continue = msg.addButton("Отправить результат", QMessageBox.ButtonRole.NoRole)
        msg.setDefaultButton(btn_continue)
        btn_continue.clicked.connect(lambda: self.__send_email_to_teacher())
        msg.exec()

    def __send_email_to_teacher(self):
        with self.get_smtp_server() as server:
            message = self.get_message(send_from=self.auth_data['sender_email'], send_to=self.ledtReceiverEMail.text(),
                                       send_subject=self.student['group'], student=self.student, result=self.result)
            self.send_message(server=server, login_data=self.auth_data, receiver_email=self.ledtReceiverEMail.text(),
                              message=message)

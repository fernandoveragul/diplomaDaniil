import hashlib
import json
import os
import shutil
from functools import partial
from pathlib import Path

from PySide6 import QtGui
from PySide6.QtCore import QUrl
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QMainWindow, QLayout, QPushButton, QMessageBox, QFileDialog

from display.main_window import Ui_MainWindow
from .dependencies import design_style
from .dependencies.depends import Files
from .dependencies.schemas import STest, SQuestion, SAnswer
from .test_win import Test


class Application(QMainWindow, Ui_MainWindow, Files):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.path_to_test = None
        self.test_schema = dict()
        self.__enable_all_buttons([self.layTutorial, self.layExample, self.layMethodist],
                                  ['tutorials', 'examples', 'methodist'])
        self.__enable_pdf_view([self.pdfTutorial, self.pdfExample, self.pdfMethodist])
        self.__enable_runtime_rbuttons()
        self.__enable_funcs_in_buttons()

        self.setWindowTitle('Учебное пособие "Поддержка и тестирование программных модулей"')
        self.setWindowIcon(QtGui.QIcon(f'{self.path_to_icon()}'))
        self.setStyleSheet(design_style.DESIGN_STYLE)

    def __create_buttons(self, layout: QLayout, folder: str):
        def add_func(ind: int):
            paths: list = self.paths2files(folder)
            match folder:
                case 'tutorials':
                    self.pdfTutorial.setUrl(QUrl.fromLocalFile(paths[ind]))
                case 'examples':
                    self.pdfExample.setUrl(QUrl.fromLocalFile(paths[ind]))
                    self.path_to_test = self.paths2files('tests')[ind]
                case 'methodist':
                    self.pdfMethodist.setUrl(QUrl.fromLocalFile(paths[ind]))

        files: list[str] = self.files_without_extension(folder)
        btn_text = ''
        for i, file in enumerate(files):
            ch_, cu = file.split('_')
            btn = QPushButton()
            btn.setObjectName(f'btn{folder.capitalize()}{ch_}{cu}')
            match folder:
                case 'tutorials':
                    btn_text = f'ГЛАВА {cu}'
                case 'examples':
                    btn_text = f'ЗАДАНИЕ К ГЛАВЕ {cu}'
                case 'tests':
                    btn_text = f'ТЕСТ К ГЛАВЕ {cu}'
            btn.setText(btn_text)
            index = i
            btn.clicked.connect(partial(add_func, index))
            layout.addWidget(btn)

    def __enable_runtime_rbuttons(self):
        self.ledtAnswerFirst.textChanged.connect(lambda: self.rbtnAnswerFirst.setText(self.ledtAnswerFirst.text()))
        self.ledtAnswerSecond.textChanged.connect(lambda: self.rbtnAnswerSecond.setText(self.ledtAnswerSecond.text()))
        self.ledtAnswerThird.textChanged.connect(lambda: self.rbtnAnswerThird.setText(self.ledtAnswerThird.text()))
        self.ledtAnswerFour.textChanged.connect(lambda: self.rbtnAnswerFour.setText(self.ledtAnswerFour.text()))

    def __enable_all_buttons(self, layouts: list[QLayout], folders: list[str]):
        for lay, fl in zip(layouts, folders):
            self.__create_buttons(lay, fl)

    def __open_window_with_current_test(self):
        path_to_test = self.path_to_test.replace(".pdf", ".json")
        exist_tests: list[str] = self.paths2files(folder="tests")
        if path_to_test in exist_tests:
            self.__window_with_test = Test(path_to_test=path_to_test)
            self.__window_with_test.show()
        else:
            QMessageBox.warning(self, "Ошибка", "Такого теста пока не существует")

    def __enable_funcs_in_buttons(self):
        self.btnTest.clicked.connect(self.__open_window_with_current_test)
        self.btnStartApp.clicked.connect(lambda: self.stackApp.setCurrentWidget(self.pgApp))
        self.btnLogin.clicked.connect(lambda: self.__login_admin())

        self.btnShowExample.clicked.connect(lambda: self.stckStudent.setCurrentWidget(self.pgExample))
        self.btnShowTutorial.clicked.connect(lambda: self.stckStudent.setCurrentWidget(self.pgTutorial))
        self.btnShowMethodist.clicked.connect(lambda: self.stckStudent.setCurrentWidget(self.pgMethodist))
        self.btnGoToStartState.clicked.connect(lambda: self.stckStudent.setCurrentWidget(self.pgTutorial))

        self.btnAddQuestion.clicked.connect(lambda: self.clear_text_editors(is_end=False))
        self.btnEndCreateTest.clicked.connect(lambda: self.clear_text_editors(is_end=True))

        self.btnAddMethodist.clicked.connect(lambda: self.__add_file_to_files(folder_name="methodist"))
        self.btnDelMethodist.clicked.connect(lambda: self.__delete_file_from_files(folder_name="tutorials"))

        self.btnAddTutorial.clicked.connect(lambda: self.__add_file_to_files(folder_name="tutorials"))
        self.btnDelTutorial.clicked.connect(lambda: self.__delete_file_from_files(folder_name="tutorials"))

        self.btnAddExample.clicked.connect(lambda: self.__add_file_to_files(folder_name="examples"))
        self.btnDelExample.clicked.connect(lambda: self.__delete_file_from_files(folder_name="examples"))

        self.btnDelTest.clicked.connect(lambda: self.__delete_file_from_files(folder_name="tests"))

    @staticmethod
    def __enable_pdf_view(pdf_widgets: list[QWebEngineView]):
        for wid in pdf_widgets:
            wid.settings().setAttribute(wid.settings().WebAttribute.PluginsEnabled, True)
            wid.settings().setAttribute(wid.settings().WebAttribute.PdfViewerEnabled, True)

    ############################
    # FIRST ADMIN PAGE ESSENCE #
    ############################
    def __login_admin(self):
        path_to_login_data: str = str(Path(Path.cwd(), 'static', 'files', '.load_data.json'))
        login: str = hashlib.sha256(self.ledtLogin.text().encode()).hexdigest()
        password: str = hashlib.sha256(self.ledtPassword.text().encode()).hexdigest()

        with open(path_to_login_data, 'r') as login_data:
            dt: dict = json.loads(login_data.read())

        if login == dt['login'] and password == dt['password']:
            self.stackProfessor.setCurrentWidget(self.pgCreate)
        else:
            QMessageBox.information(self, "НЕУДАЧА", 'Неверный логин или пароль')

        self.stackProfessor.setCurrentWidget(self.pgCreate)

    def clear_text_editors(self, is_end: bool = False):
        meta_data: list = self.ledtTimeToDo.text().split()
        self.__add_question()
        if not is_end:
            self.__clear_editors()
        else:
            self.__final_adding_question(meta_data=meta_data)

    def __clear_editors(self):
        self.ledtAnswerFirst.setText("")
        self.ledtAnswerSecond.setText("")
        self.ledtAnswerThird.setText("")
        self.ledtAnswerFour.setText("")
        self.ptedQuestion.setPlainText("")

    def __add_file_to_files(self, folder_name: str):
        def_folder: str = str(Path(Path.home()))
        try:
            cp_from: str = QFileDialog.getOpenFileName(self, "PDF файл",
                                                       dir=def_folder,
                                                       filter="All Files (*);;EXAMPLES Files (*.pdf)")[0]
            shutil.copy2(cp_from, f'{Path(Path.cwd(), "static", folder_name)}')
        except FileNotFoundError:
            QMessageBox.critical(self, "ОШИБКА", "ОКНО ЗАКРЫТО БЕЗ ВЫБОРА ФАЙЛА\nЛИБО НЕ СУЩЕСТВУЕТ ТАКОГО ФАЙЛА")

    def __delete_file_from_files(self, folder_name: str):
        def_folder: str = str(Path(Path.cwd(), "static", folder_name))
        try:
            deleting_file: str = QFileDialog.getOpenFileName(self, "Open File",
                                                             dir=def_folder,
                                                             filter="All Files (*);;Tutorial or Example Files (*.pdf);;"
                                                                    "Tests Files (*.json)")[0]
            os.remove(deleting_file)
        except FileNotFoundError:
            QMessageBox.critical(self, "ОШИБКА", "ОКНО ЗАКРЫТО БЕЗ ВЫБОРА ФАЙЛА\nЛИБО НЕ СУЩЕСТВУЕТ ТАКОГО ФАЙЛА")

    def __add_question(self):
        for_adding_dictionary = SQuestion(text_question=self.ptedQuestion.toPlainText(),
                                          answers=[
                                              SAnswer(text_answer=self.ledtAnswerFirst.text(),
                                                      is_true=self.rbtnAnswerFirst.isChecked()).dict(),
                                              SAnswer(text_answer=self.ledtAnswerSecond.text(),
                                                      is_true=self.rbtnAnswerSecond.isChecked()).dict(),
                                              SAnswer(text_answer=self.ledtAnswerThird.text(),
                                                      is_true=self.rbtnAnswerThird.isChecked()).dict(),
                                              SAnswer(text_answer=self.ledtAnswerFour.text(),
                                                      is_true=self.rbtnAnswerFour.isChecked()).dict()
                                          ]).dict()

        self.test_schema['questions'].append(for_adding_dictionary)
        QMessageBox.information(self, "УСПЕХ", f"Вопрос был добавлен к текущему тесту")

    def __final_adding_question(self, meta_data: list[str]):
        if len(meta_data) == 0:
            QMessageBox.critical(self, "КРИТИЧЕСКАЯ ОШИБКА", "НЕЛЬЗЯ СОЗДАТЬ ТЕСТ БЕЗ ЕГО НОМЕРА")
        else:
            self.test_schema['time2test'] = meta_data[-1]
            self.test_schema['questions'].append(SQuestion(text_question='Спасибо что прошли тест',
                                                           answers=[
                                                               SAnswer(text_answer='Нажмите, чтобы продолжить',
                                                                       is_true=False).dict(),
                                                               SAnswer(text_answer='Нажмите, чтобы продолжить',
                                                                       is_true=False).dict(),
                                                               SAnswer(text_answer='Нажмите, чтобы продолжить',
                                                                       is_true=False).dict(),
                                                               SAnswer(text_answer='Нажмите, чтобы продолжить',
                                                                       is_true=False).dict()
                                                           ]).dict())
        self.save_current_test(name=f'1_{meta_data[0]}.json',
                               test=STest(**self.test_schema))
        self.__clear_editors()
        QMessageBox.information(self, "УСПЕХ", "Тест был создан, перезапустите приложение, "
                                               "чтобы он инициализировался")
        self.ledtTimeToDo.setText('')
        self.__counter_questions = 0
        self.test_schema = self.load_default_test()

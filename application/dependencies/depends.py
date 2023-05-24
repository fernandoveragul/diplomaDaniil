import json
import os
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

from PySide6.QtWidgets import QTextBrowser, QPushButton

from application.dependencies.schemas import STest


class Files:
    @staticmethod
    def paths2files(folder: str) -> list[str]:
        path: str = f'{Path(Path.cwd(), "static", folder)}'
        return [f'{Path(path, i)}' for i in os.listdir(path)]

    @staticmethod
    def files_without_extension(folder: str) -> list[str]:
        path: str = f'{Path(Path.cwd(), "static", folder)}'
        return list(map(lambda file_name: file_name.split('.')[0], sorted(os.listdir(path))))

    @staticmethod
    def save_current_test(name: str, test: STest) -> None:
        path: str = f'{Path(Path.cwd(), "static", "tests", name)}'
        with open(path, 'w') as file_test:
            file_test.write(json.dumps(test.dict(), indent=4))

    @staticmethod
    def load_current_test(name: str = None, path: str = None) -> dict:
        path_: str = f'{Path(Path.cwd(), "static", "tests", name)}' if not path else path
        with open(path_, 'r') as test:
            current_test: dict = json.loads(test.read())
        return current_test

    @staticmethod
    def load_default_test() -> dict:
        path: str = f'{Path(Path.cwd(), "static", "tests", "schema.json")}'
        with open(path, 'r') as test:
            current_test: dict = json.loads(test.read())
        return current_test

    @staticmethod
    def get_smtp_server() -> smtplib.SMTP_SSL:
        contex = ssl.create_default_context()
        return smtplib.SMTP_SSL("smtp.gmail.com", 465, context=contex)

    @staticmethod
    def get_message(*, send_from: str, send_to: str, send_subject: str, student: dict, result: dict) -> MIMEMultipart:
        msg = MIMEMultipart()
        msg["From"] = send_from
        msg["To"] = send_to
        msg["Subject"] = send_subject
        message_text = f"""\

        <html>
            <body>
                <div>
                    <h1>{student.get("name")} {student.get("group")}</h1>
                </div>
                <div>
                    <h3>Тест по практической работе номер {result.get("test_number")}</h3>
                </div>
                <div>
                    <h3>Количество баллов {sum(result.get("result"))}</h3>
                </div>
            </body>
        </html>
        """
        message = MIMEText(message_text, "html")
        msg.attach(message)
        return msg

    @staticmethod
    def send_message(*, server, login_data: dict, receiver_email: str, message):
        sender_email, password = login_data.get("sender_email"), login_data.get("password")
        server.login(sender_email, password=password)
        server.send_message(message, sender_email, receiver_email)

    @staticmethod
    def decode_dt(*, dt: dict):
        import base64
        lg, ps = dt['email'].split("\\")
        lg = base64.a85decode(base64.b85decode(lg.encode())).decode()
        ps = base64.a85decode(base64.b85decode(ps.encode())).decode()
        return lg, ps

    @staticmethod
    def get_gen_test_text(*, label: QTextBrowser, buttons: list[QPushButton], data: list[dict]):
        for ind_dt, dt in enumerate(data):
            label.setText(dt.get("text_question"))
            for ind, btn in enumerate(buttons):
                btn.setText(dt.get("answers")[ind].get("text_answer"))
            yield dt

    @staticmethod
    def get_gen_questions_slide(*, questions: list[dict]):
        for q in questions:
            yield q

    @staticmethod
    def path_to_icon() -> str:
        path: Path = Path(Path.cwd(), 'static', 'files', 'icon.png')
        return str(path)

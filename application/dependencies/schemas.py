import json
from pathlib import Path

from pydantic import BaseModel


class SAnswer(BaseModel):
    text_answer: str
    is_true: bool = False


class SQuestion(BaseModel):
    text_question: str
    answers: list[SAnswer]


class STest(BaseModel):
    time2test: int
    questions: list[SQuestion]


# def some():
#     with open(f'{Path(Path.cwd(), "static", "tests", "1_1.json")}', 'w') as f:
#         obj = Test(time2test='00:30:00',
#                    questions=[
#                        Question(text_question='text',
#                                 answers=[
#                                     Answer(text_answer='text', is_true=False),
#                                     Answer(text_answer='text', is_true=True),
#                                     Answer(text_answer='text', is_true=False),
#                                     Answer(text_answer='text', is_true=False)
#                                 ])])
#         json.dump(obj=obj.dict(), fp=f, indent=4)


class SLoadData(BaseModel):
    login: str
    password: str
    email: str

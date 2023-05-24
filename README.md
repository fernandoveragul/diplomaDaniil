# Учебное пособие "Поддержка и тестирование программных модулей"
## Чтобы собрать приложение необходимо выполнить несколько этапов
***
### Клонировать репозиторий
```bash
git clone https://github.com/fernandoveragul/diplomaDaniil
```
***
### Перейдя в папку с приложеним с помощью команды ```cd``` создать виртуальное окружение
```bash
python -m venv env
```
***
### Активировать виртуальное окружение

##### MS Windows
```bash
env\Scripts\activate
```
##### Unix
```bash
source env\bin\activate
```
***
### Установить зависимости проекта
```bash
pip install --no-cache-dir -r requirements.txt
```
***
### Выполнить сборку
```bash
pyinstaller main.spec
```
***
### Приложение будет находиться в дирректории с проектом по пути 
##### MS Windows ```diplomaDaniil/dist/main.exe``` 
##### Unix ```diplomaDaniil/dist/main``` 
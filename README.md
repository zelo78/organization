# Структура организации

## Тестовое задание

Создайте веб страницу, которая будет выводить древовидную структуру отделов со списком сотрудников
 
Информация о каждом сотруднике должна храниться в базе данных и содержать следующие данные:

- ФИО;
- Должность;
- Дата приема на работу;
- Размер заработной платы;
- Подразделение - подразделения имеют структуру до 5 уровней;
 
Дерево должно отображаться в свернутом виде. 
 
База данных должна содержать не менее 50 000 сотрудников и 25 подразделений в 5 уровнях иерархий
 
Управление записями CRUD через административную часть Django
 
Django 3+, Python 3.5+, база на свое усмотрение

Используйте Twitter Bootstrap для создания базовых стилей Вашей страницы.
 
Если используете дополнительные библиотеки, то необходимо оформить все в requirements.txt
 
Готовое задание, необходимо разместить Github/Bitbucket

## Выполненное задание

### Развёртывание выполненного задания

```shell
pip install -Ur src/requirements.txt
python src/manage.py migrate
```

### Запуск локального сервера

```shell
python src/manage.py migrate --noinput
python src/manage.py collectstatic --noinput
python src/manage.py runserver
```

### Наполнение базы данных случайными Подразделениями и Сотрудниками

(указана команда для 25 подразделений и 50.000 сотрудников)

```shell
python src/manage.py populate -d 25 -e 50000 
```

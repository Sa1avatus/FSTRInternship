# Проект виртуальной стажировки ФСТР 
 
## Установка


1. Если не установлен Python, [установите отсюда](https://www.python.org/downloads/)

2. Клонируйте репозиторий

3. Зайдите  в директорию проекта

   ```bash
   $ cd FSTR
   ```

4. Создайте виртуальное окружение

   ```bash
   $ python -m venv venv
   $ . venv/bin/activate
   ```

5. Установите зависимости

   ```bash
   $ pip install -r requirements.txt
   ```

6. Создайте копию файла окружения .env

   ```bash
   $ cp .env.example .env
   ```

7. Заполните необходимые данные в созданном файле `.env`

8. Запустите приложение

   ```bash
   $ python manage.py runserver 
   ```

Доступ к порталу будет по ссылке [http://localhost:8000](http://localhost:8000)

Опубликованный на хостинге данный проект: http://8.211.14.75:8000/submitData

Документация по работе с API: http://8.211.14.75:8000/swagger/

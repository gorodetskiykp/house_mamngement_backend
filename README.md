# house_management_backend
Система управления многоквартирным домом
## установка приложения
1. Установить виртуальное окружение: python -m venv venv
2. Активировать виртуальное окружение: venv\Scripts\activate
3. Нужно выполнить команду pip install -r requirements.txt
4. Создаем администартора python manage.py migrate
5. Создаем логим и пароль администаротора: python manage.py createsuperuser
6. Запустить сервер: python manage.py runserver
7. Зайти по адресу приложения и залогинится под админом: http://127.0.0.1:8000/admin
8. Убедится, что открывается админка
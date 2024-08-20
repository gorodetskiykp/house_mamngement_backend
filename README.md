# house_management_backend
Система управления многоквартирным домом

## Установка приложения
1. Устанавливаем виртуальное окружение: `python -m venv venv`
1. Активируем виртуальное окружение:
      + `venv\Scripts\activate` - Windows
      + `source venv/bin/activate` - MacOS / Linux
1. Устанавливаем зависимости: `pip install -r requirements.txt`
1. Готовим миграции: `python manage.py makemigrations`
1. Выполняем миграции: `python manage.py migrate`
1. Создаем администартора: `python manage.py createsuperuser`
1. Запускаем локальный сервер: `python manage.py runserver`
1. Заходим по адресу приложения и логинимся под админом: http://127.0.0.1:8000/admin
1. Проверяем, что админка открывается

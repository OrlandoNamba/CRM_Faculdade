import os
import webbrowser
import threading
from django.core.management import execute_from_command_line
from database.criar_banco import criar_tabelas


def abrir_navegador():
    webbrowser.open('http://127.0.0.1:8000/')


if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crm_django.settings')

    criar_tabelas()

    threading.Timer(1.5, abrir_navegador).start()

    execute_from_command_line(['manage.py', 'runserver'])
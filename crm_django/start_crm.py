import os
import threading
import webbrowser
from django.core.management import execute_from_command_line
from database.criar_banco import criar_tabelas


def abrir_navegador():
    webbrowser.open('http://127.0.0.1:8000/')


if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crm_django.settings')

    # cria banco e tabelas
    criar_tabelas()

    # abre navegador depois de 1.5s
    threading.Timer(1.5, abrir_navegador).start()

    # roda servidor (SEM autoreload - obrigatório no exe)
    execute_from_command_line(['manage.py', 'runserver', '--noreload'])
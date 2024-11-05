import argparse
import os
import sys
from report_accounts import report_accounts
from loading_screen import show_loading_screen
from banner import show_banner
import logging

# Configure o logger
logging.basicConfig(filename='app.log', level=logging.DEBUG)

def log_message(self, message):
    logging.info(message)
    self.log_text.insert("end", f"{message}\n")
    self.log_text.see("end")


def resource_path(relative_path):
    """Retorna o caminho absoluto do recurso, considerando se está em um executável"""
    if hasattr(sys, '_MEIPASS'):
        # Caminho temporário do PyInstaller para arquivos empacotados
        return os.path.join(sys._MEIPASS, relative_path)
    # Caminho para desenvolvimento
    return os.path.join(os.path.abspath("."), relative_path)


def get_options():
    parser = argparse.ArgumentParser(description="Este bot ajuda os usuários a reportar contas em massa com material inadequado.")
    parser.add_argument("-u", "--username", type=str, default="", help="Nome de usuário para reportar.")
    parser.add_argument("-f", "--file", type=str, default=resource_path("acc.txt"),
                        help="Lista de contas (padrão: acc.txt no diretório do programa).")
    return parser.parse_args()


def main():
    args = get_options()
    username = args.username
    accounts_file = args.file
    show_banner()
    show_loading_screen(3)
    
    if username == "":
        username = input("User: ")

    show_loading_screen(3)
    report_accounts(username, accounts_file)


if __name__ == "__main__":
    main()

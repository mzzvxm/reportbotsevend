import customtkinter as ctk
from tkinter import filedialog, messagebox, scrolledtext
from report_accounts import report_accounts
import threading
import sys
import os
import logging

# Configure o logger
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Instagram Report by @sevend7")
        self.geometry("400x300")
        self.resizable(False, False)

        # Estilo
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Containers principais
        self.main_frame = ctk.CTkFrame(self, width=600, height=500, fg_color="#2C2F33")
        self.log_frame = ctk.CTkFrame(self, width=600, height=500, fg_color="#2C2F33")

        # Inicialmente, exibir a main_frame
        self.main_frame.pack(fill="both", expand=True)

        # Botões para alternar entre abas
        self.toggle_frame = ctk.CTkFrame(self, width=600, height=30, fg_color="#23272A")
        self.toggle_frame.pack(fill="x")

        self.main_button = ctk.CTkButton(self.toggle_frame, text="Principal", command=self.show_main_frame)
        self.main_button.grid(row=0, column=0, padx=10, pady=5)

        self.log_button = ctk.CTkButton(self.toggle_frame, text="Logs", command=self.show_log_frame)
        self.log_button.grid(row=0, column=1, padx=10, pady=5)

        # Componentes na página principal
        self.title_label = ctk.CTkLabel(self.main_frame, text="Instagram Report by @sevend7", font=("Helvetica", 20, "bold"))
        self.title_label.pack(pady=10)

        self.username_label = ctk.CTkLabel(self.main_frame, text="Nome de Usuário:")
        self.username_label.pack(pady=(10, 0))
        self.username_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Digite o nome de usuário")
        self.username_entry.pack(pady=(0, 10))

        self.filepath = ""
        self.file_button = ctk.CTkButton(self.main_frame, text="Selecionar Arquivo de Contas", command=self.select_file)
        self.file_button.pack(pady=10)

        self.start_button = ctk.CTkButton(self.main_frame, text="Iniciar Relatório", command=self.start_report)
        self.start_button.pack(pady=10)

        self.progress = ctk.CTkProgressBar(self.main_frame)
        self.progress.pack(pady=20, fill="x")

        # Componentes na aba de logs
        self.log_label = ctk.CTkLabel(self.log_frame, text="Logs:")
        self.log_label.pack(pady=(10, 0))
        self.log_text = scrolledtext.ScrolledText(self.log_frame, wrap="word", height=10, bg="#2C2F33", fg="white", font=("Helvetica", 12))
        self.log_text.pack(padx=10, pady=10, fill="both", expand=True)

    def show_main_frame(self):
        self.log_frame.pack_forget()
        self.main_frame.pack(fill="both", expand=True)

    def show_log_frame(self):
        self.main_frame.pack_forget()
        self.log_frame.pack(fill="both", expand=True)

    def log_message(self, message):
        """ Adiciona uma mensagem ao log e exibe no widget de log. """
        logging.info(message)
        self.log_text.insert("end", f"{message}\n")
        self.log_text.see("end")

    def select_file(self):
        self.filepath = filedialog.askopenfilename(title="Selecionar Arquivo", filetypes=[("Text Files", "*.txt")])
        if self.filepath:
            self.log_message("Arquivo carregado com sucesso.")
        else:
            self.log_message("Nenhum arquivo selecionado.")

    def start_report(self):
        username = self.username_entry.get().strip()
        if not username:
            messagebox.showwarning("Aviso", "Por favor, insira o nome de usuário.")
            return
        if not self.filepath:
            messagebox.showwarning("Aviso", "Por favor, selecione um arquivo.")
            return

        self.log_message("Processando...")
        self.progress.start()
        thread = threading.Thread(target=self.process_report, args=(username,))
        thread.start()

    def process_report(self, username):
        try:
            report_accounts(username, self.filepath)
            self.log_message("Relatório concluído com sucesso!")
        except Exception as e:
            self.log_message(f"Erro: {e}")
        finally:
            self.progress.stop()

if __name__ == "__main__":
    app = App()
    app.mainloop()

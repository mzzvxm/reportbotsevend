# coding: utf-8
from cx_Freeze import setup, Executable

# Informações do seu projeto
build_exe_options = {
    "packages": [],  # Liste pacotes adicionais se necessário
    "include_files": ["acc.txt"],  # Inclua arquivos adicionais se necessário
}

# Configuração do executável
setup(
    name="Instagram Report @sevend7",
    version="0.1",
    description="Report Bot do Instagram feito pela @sevend7",
    options={"build_exe": build_exe_options},
    executables=[Executable("gui.pyw", base="Win32GUI")],  # base="Win32GUI" para aplicativos sem console
)

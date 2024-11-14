@echo off
setlocal

:: Define os caminhos para os arquivos
set "REQUIREMENTS_PATH=requirements.txt"
set "PYTHON_SCRIPT=Home.py"

:: Instala as bibliotecas listadas no requirements.txt
if exist "%REQUIREMENTS_PATH%" (
    echo Instalando Bibliotecas Listadas em %REQUIREMENTS_PATH%
    pip install -r "%REQUIREMENTS_PATH%"
) else (
    echo Arquivo não Encontrado em %REQUIREMENTS_PATH%
    pause
    exit /b 1
)

:: Verificação se o arquivo Python existe
if exist "%PYTHON_SCRIPT%" (
    echo Executando script em Python: %PYTHON_SCRIPT%
    python -m streamlit run "%PYTHON_SCRIPT%"
) else (
    echo Arquivo %PYTHON_SCRIPT% não Encontrado
    pause
    exit /b 1
)

pause

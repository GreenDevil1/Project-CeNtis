@echo off
setlocal enabledelayedexpansion

REM Überprüfen, ob Python installiert ist
where python >nul 2>&1
if %errorlevel% neq 0 (
    REM Python herunterladen und installieren
    echo Python wird heruntergeladen und installiert...
    powershell -Command "Invoke-WebRequest https://www.python.org/ftp/python/3.9.6/python-3.9.6-amd64.exe -OutFile %TEMP%\python-installer.exe"
    %TEMP%\python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
    echo Python wurde installiert.
) else (
    echo Python ist bereits installiert.
)

REM Installieren der erforderlichen Pakete
echo Installieren der erforderlichen Pakete...
pip install colorama cryptography pytube moviepy phonenumbers folium

REM Überprüfen, ob Git installiert ist
where git >nul 2>&1
if %errorlevel% neq 0 (
    REM Git herunterladen und installieren
    echo Git wird heruntergeladen und installiert...
    winget install --id Git.Git -e --source winget
    echo Git wurde installiert.
) else (
    echo Git ist bereits installiert.
)

REM Klonen des Repositorys
echo Klonen des Repositorys...
git clone https://github.com/GreenDevil1/Project-CeNtis.git

REM Erstellen einer Verknüpfung im Autostart-Ordner
echo Erstellen einer Verknüpfung im Autostart-Ordner...
set script_path=C:\Users\%USERNAME%\Project-CeNtist\Project CeNtist\firewall.py
set startup_folder=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup
set link_path=%startup_folder%\firewall.lnk

powershell -Command "$ws = New-Object -ComObject WScript.Shell; $s = $ws.CreateShortcut('!link_path!'); $s.TargetPath = '!script_path!'; $s.Save()"

echo Die Verknüpfung wurde erstellt.

pause

REM Starten des Skripts
echo Starten des Skripts...
python "C:\Users\%USERNAME%\Project-CeNtis\Project CeNtis\CeNtis.py"

pause

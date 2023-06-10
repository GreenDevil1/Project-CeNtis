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

REM Entpacken des Archivs
echo Entpacken des Archivs...
powershell -Command "Expand-Archive -Path C:\Users\%USERNAME%\Project-CeNtis\Project-CeNtis\Project CeNtis.zip -DestinationPath C:\Users\%USERNAME%\Project-CeNtis\Project-CeNtis"

REM Starten des Skripts
echo Starten des Skripts...
python "C:\Users\%USERNAME%\Project-CeNtis\Project CeNtis\CeNtis.py"

REM Fragen, ob der Benutzer eine Aufgabe in der Aufgabenplanung erstellen möchte
set /p create_task="Möchtest du eine Aufgabe in der Aufgabenplanung erstellen (j/n)? "
if /i "!create_task!"=="j" (
    REM Erstellen einer Aufgabe in der Aufgabenplanung
    echo Erstellen einer Aufgabe in der Aufgabenplanung...
    schtasks /create /tn "Firewall_blocks_IPs" /tr "\"C:\Users\%USERNAME%\Project-CeNtist\Project CeNtist\firewall.py\"" /sc onlogon /ru %USERNAME% /rl highest /f
    echo Die Aufgabe wurde erstellt.
)

pause

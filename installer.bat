# Check for internet connection
if (!(Test-NetConnection -ComputerName www.google.com -InformationLevel Quiet)) {
    Write-Host "No internet connection detected. Exiting."
    exit
}

# Check if Python is installed
if (!(Get-Command python -ErrorAction SilentlyContinue)) {
    # Download and install Python
    $url = "https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe"
    $destination = "$env:USERPROFILE\Downloads\python-3.11.4-amd64.exe"

    (New-Object Net.WebClient).DownloadFile($url, $destination)
    Start-Process -FilePath $destination -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1" -Wait

    # Install the required modules using pip
    pip install colorama cryptography pytube moviepy phonenumbers folium

    # Open a GUI window to display a message
    Add-Type -AssemblyName System.Windows.Forms
    $form = New-Object System.Windows.Forms.Form
    $form.Text = "Installation Complete"
    $label = New-Object System.Windows.Forms.Label
    $label.Text = "Python and the required modules have been installed."
    $label.ForeColor = "Red"
    $label.AutoSize = $true
    $form.Controls.Add($label)
    $form.ShowDialog()
}

# Check if Git is installed
if (!(Get-Command git -ErrorAction SilentlyContinue)) {
    # Download and install Git
    $url = "https://github.com/git-for-windows/git/releases/download/v2.35.1.windows.2/Git-2.35.1.2-64-bit.exe"
    $destination = "$env:USERPROFILE\Downloads\Git-2.35.1.2-64-bit.exe"

    (New-Object Net.WebClient).DownloadFile($url, $destination)
    Start-Process -FilePath $destination -ArgumentList "/VERYSILENT /NORESTART /NOCANCEL /SP-" -Wait
}

# Download the Git repository
$url = "https://github.com/GreenDevil1/Project-CeNtis.git"
$destination = "$env:USERPROFILE\Downloads\Project-CeNtis"

git clone $url $destination

# Unzip the file in the repository
$zipPath = "$destination\Project-CeNtis\Project-CeNtis.zip"
Expand-Archive -Path $zipPath -DestinationPath "$env:USERPROFILE\Downloads"

# Run the Python script
$scriptPath = "$env:USERPROFILE\Project-CeNtis\Project CeNtis\Project CeNtis - Kopie\CeNtis.py"
Start-Process python -ArgumentList "`"$scriptPath`""

Write-Host "Done."

echo
start "" "C:\Program Files (x86)\Steam\steam.exe"
timeout /T 5 /nobreak >nul
start D:\"SteamLibrary\steamapps\common\rocketleague\Binaries\Win64\RocketLeague.exe"
start "" "C:\Program Files\BakkesMod\BakkesMod.exe"
timeout /T 10 /nobreak >nul
taskkill /IM BakkesMod.exe /F
echo
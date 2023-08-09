#Requires AutoHotkey v2.0

if WinExist( "ahk_exe telegram.exe")
	WinActivate
else
	Run "C:\Users\Asus\AppData\Roaming\Telegram Desktop\Telegram.exe"


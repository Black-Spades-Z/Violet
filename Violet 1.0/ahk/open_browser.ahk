#Requires AutoHotkey v2.0

If WinExist("ahk_exe browser.exe")
	WinActivate
else
	Run "C:\Users\Asus\AppData\Local\Yandex\YandexBrowser\Application\browser.exe"
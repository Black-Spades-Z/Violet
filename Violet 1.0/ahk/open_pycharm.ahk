#Requires AutoHotkey v2.0

if WinExist( "ahk_exe pycharm64.exe")
	WinActivate
else
	Run "D:\apps\coding IDE\PyCharm 2022.1.1\bin\pycharm64.exe"

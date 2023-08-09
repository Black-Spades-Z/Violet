#Requires AutoHotkey v2.0

if WinExist( "ahk_exe VALORANT-Win64-Shipping.exe")
	WinActivate
else
	Run "D:\apps\games\Riot Games\Riot Client\RiotClientServices.exe"

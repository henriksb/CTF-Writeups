PS C:\Users\h-byg\Desktop\EvtxeCmd> curl.exe "challenge.ctf.games:30131/admin"
<?xml version="1.0" encoding="UTF-8"?>
<Error><Code>AccessDenied</Code><Message>Access Denied.</Message><BucketName>admin</BucketName><Resource>/admin</Resource><RequestId>17FB56DE130658BD</RequestId><HostId>dd9025bab4ad464b049177c95eb6ebf374d3b3fd1af9251148b658df7ac2e3e8</HostId></Error>

(obvious hint, "bucket" which you bring to a beach, and is amazon s3 bucket)

PS C:\Users\h-byg\Desktop> curl.exe "challenge.ctf.games:30131/bucket" -o output.txt

(found key and used it in request)

PS C:\Users\h-byg\Desktop> curl.exe "challenge.ctf.games:30131/bucket/0wLiQJMy/NuT6wXCU/xzbDiWPZ/cB2H4cbAMlqN3leJ" -o flag.txt
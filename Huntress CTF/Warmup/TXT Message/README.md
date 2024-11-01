root@henrik:~# dig ctf.games TXT

; <<>> DiG 9.18.18-0ubuntu0.22.04.1-Ubuntu <<>> ctf.games TXT
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 40603
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4000
;; QUESTION SECTION:
;ctf.games.                     IN      TXT

;; ANSWER SECTION:
ctf.games.              14357   IN      TXT     "146 154 141 147 173 061 064 145 060 067 062 146 067 060 065 144 064 065 070 070 062 064 060 061 144 061 064 061 143 065 066 062 146 144 143 060 142 175"

;; Query time: 9 msec
;; SERVER: 10.255.255.254#53(10.255.255.254) (UDP)
;; WHEN: Sun Oct 06 21:05:02 CEST 2024
;; MSG SIZE  rcvd: 202

ASCII to text
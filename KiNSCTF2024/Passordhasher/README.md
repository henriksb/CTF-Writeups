# Passordhasher

## NTLM1 og NTLM2
Knakk automatisk med nettsite: https://ntlm.pw/


## NTLM3
Dictionary attack med hashcat. Brukte følgende kommando for å knekke hashen: `hashcat -m 1000 -a 0 A452E53125F77778AD5FE10236BB7463 rockyou.txt -r d3ad0ne.rule`

Hashcat knakk hashen på et par sekunder, men svaret var feil. Det jeg ikke innså var at det er et mellomrom på slutten av svaret.
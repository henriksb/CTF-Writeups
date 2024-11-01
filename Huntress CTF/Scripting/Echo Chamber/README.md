Even though this was a "Scripting" task. I solved it manually using Wireshark. By using the hint "Echo chamber" i filtered by `icmp.type == 8`, which is echo. By quickly scrolling through the ascii, I saw a closing parenthesis, and thereby the flag.

This task can also be automated using tshark:
```sh
tshark -r echo_chamber.pcap -Y "icmp.type == 8" -T fields -e data | awk '{print substr($0, length($0)-1, 2)}' | xxd -r -p
```
..or a more cleaned output:
```sh
tshark -r echo_chamber.pcap -Y "icmp.type == 8" -T fields -e data | awk '{print substr($0, length($0)-1, 2)}' | xxd -r -p | tr -cd '\11\12\15\40-\176' | grep -o 'flag{[^}]*}'
```
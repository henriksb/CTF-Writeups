# Kari og Olas hastigheter
kari_hastighet = 50  # km/t
ola_hastighet = 30  # km/t

# Avstanden Kari kjører i løpet av Olas forsinkelse (1 time)
avstand_kari_forsprang = kari_hastighet * 1  # km

# Gjenværende avstand når Ola starter
gjenværende_avstand = 150 - avstand_kari_forsprang  # km

# Kombinert hastighet
kombinert_hastighet = kari_hastighet + ola_hastighet  # km/t

# Tiden det tar før de møtes etter Ola starter
tid_til_møte = gjenværende_avstand / kombinert_hastighet  # timer

# Total tid Kari kjører
total_tid_kari = 1 + tid_til_møte  # timer

# Avstand Kari kjører
avstand_kari = total_tid_kari * kari_hastighet  # km

# Konvertere tid til klokkeslett
start_tid = 12  # 1200 timer
møte_tid = start_tid + total_tid_kari  # klokkeslett

# Konvertere avstand til meter
avstand_kari_meter = avstand_kari * 1000  # meter

møte_tid, avstand_kari_meter

#helsectf{1415_112500}

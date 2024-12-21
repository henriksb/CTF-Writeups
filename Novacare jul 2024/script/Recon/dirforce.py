import requests
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm  # Progress bar

base_url = 'https://www.kodekalender.no/'

# SecLists ordliste
ordliste = "subdomains-top1million-110000.txt"
max_tråder = 30  # Antall tråder

# Funksjon for å sjekke en directory om gangen
def sjekk_directory(directory):
    url = f"{base_url}/{directory}"
    try:
        # Bruke session cookies for å sjekke directory
        response = requests.get(url)
        # Hvis statuskode 200, directoryen eksisterer
        if response.status_code == 200:
            tqdm.write(f"[+] Fant: {url}")
    except requests.RequestException as e:
        tqdm.write(f"Feil ved tilgang til {url}: {e}")

# Bruke tråder og tqdm for å scanne directories med progress bar
def scan_directories():
    with open(ordliste, 'r') as fil:
        directories = fil.read().splitlines()

    # Progress bar med antall directories
    with ThreadPoolExecutor(max_workers=max_tråder) as executor:
        list(tqdm(executor.map(sjekk_directory, directories), total=len(directories), desc="Scanner directories"))

if __name__ == "__main__":
    print("Starter...")
    scan_directories()
 
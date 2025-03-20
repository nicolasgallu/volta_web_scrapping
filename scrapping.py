import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import re
import math

BASE_URL = "https://volta.net.ar/registro"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

def get_locations():
    """Extract available locations from the dropdown menu."""
    response = requests.get(BASE_URL, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    options = soup.find_all("option")  # Find all dropdown options
    locations = [opt.text.strip() for opt in options if opt.text.strip() and "Seleccione" not in opt.text]
    
    print(f"Found {len(locations)} locations.")
    return locations

def get_total_pages(soup):
    """Extract total number of pages by computing total registers / 50."""
    text = soup.get_text()
    match = re.search(r"(\d+)\s+registros", text)
    if match:
        total_registers = int(match.group(1))
        pages = math.ceil(total_registers / 50)
        print(f"Total registers: {total_registers}, computed pages: {pages}")
        return pages
    return 1  # Default to 1 if not found

def scrape_location(location):
    """Scrape data for a given location, handling pagination."""
    data = []
    page = 1
    total_pages = None  # We'll get this dynamically

    while True:
        params = {
            "gd": "", "categoria": "", "nombre": "", "cuil": "", "registro": "",
            "localidad": location.replace(" ", "+"), "page": page
        }
        response = requests.get(BASE_URL, params=params, headers=HEADERS)
        soup = BeautifulSoup(response.text, "html.parser")

        # Get total number of pages on the first request
        if total_pages is None:
            total_pages = get_total_pages(soup)
            print(f"{location}: Found {total_pages} pages.")

        # Find all table rows containing data
        rows = soup.find_all("tr")[1:]  # Skip header row

        for row in rows:
            columns = row.find_all("td")
            if len(columns) < 7:
                continue  # Skip if it doesn't match expected column count

            # Extract "Contacto" and split into multiple fields
            raw_contacto_text = columns[7].text.strip()
            contacto_values = [c.strip() for c in raw_contacto_text.split("\n") if c.strip()]
            contacto_dict = {f"contacto_{i+1}": contacto_values[i] for i in range(len(contacto_values))}

            # Fix column shifting issue by ignoring the first column (#)
            entry = {
                "CUIL": columns[1].text.strip(),
                "Nombre": columns[2].text.strip(),
                "Categoría": columns[3].text.strip(),
                "Registro": columns[4].text.strip(),
                "Localidad": columns[5].text.strip(),
                "Barrio": columns[6].text.strip(),
                **contacto_dict  # Add contact fields dynamically
            }
            data.append(entry)

        print(f"Scraped {len(rows)} entries from {location} - Page {page}/{total_pages}")

        # Stop if we've reached the last page
        if page >= total_pages:
            break

        page += 1
        time.sleep(1)  # Avoid overloading the server

    return data

# Start scraping
locations = get_locations()
all_data = []

for loc in locations:  # Limit to 5 locations for testing if needed
    all_data.extend(scrape_location(loc))

# Export to Excel
df = pd.DataFrame(all_data)
df.to_excel("scraped_data.xlsx", index=False)
print(f"Exported {len(all_data)} records to 'scraped_data.xlsx'")

# Scraping and Cleaning Project

This repository contains two Python scripts—**`scrapping.py`** and **`clean_scrapping.py`**—designed to:

1. **Scrape data** from a public registry at [volta.net.ar/registro](https://volta.net.ar/registro).
2. **Clean and structure** the scraped data to extract useful contact information (emails and phone numbers).

Below is a detailed overview of each script, their functionalities, and how to use them effectively.

---

## Table of Contents

1. [Project Description](#project-description)  
2. [Features](#features)  
3. [Prerequisites](#prerequisites)  
4. [Usage](#usage)  
   - [Scraping Phase](#scraping-phase)  
   - [Cleaning Phase](#cleaning-phase)  
5. [Output](#output)  
6. [Customization](#customization)  
7. [Limitations & Notes](#limitations--notes)  
8. [License](#license)

---

## Project Description

The **Scraping and Cleaning Project** automates data extraction from a target website that lists entities (such as professionals or businesses) along with their CUIL (tax ID), names, categories, registration details, and contact information.

The workflow is split into two main steps:

1. **Scraping the Website:**  
   - Collects a list of locations from a dropdown menu.
   - Iterates through each location and retrieves multiple pages of results.
   - Extracts key fields like `CUIL`, `Nombre`, `Categoría`, `Registro`, `Localidad`, `Barrio`, and multiple `contacto_#` fields.

2. **Cleaning the Data:**  
   - Reads the initial spreadsheet from the scraping phase.
   - Extracts and normalizes emails and phone numbers into separate columns.
   - Saves the cleaned output into a new Excel file.

This structure allows for a modular approach, enabling easier maintenance, data correction, and potential expansion for new extraction or cleaning rules.

---

## Features

- **Dynamic Location Discovery**  
  Automatically detects all available locations from a dropdown menu on the target page.

- **Pagination Handling**  
  Detects how many pages of data exist for each location and iterates through them gracefully.

- **Data Extraction & Structuring**  
  Collects row data (CUIL, Name, etc.) and neatly organizes contact information in separate columns.

- **Contact Normalization**  
  Uses regular expressions to extract valid phone numbers and identifies emails in the second phase.

- **Excel Exports**  
  Both scripts output Excel files (`scraped_data.xlsx` and `scraped_clean.xlsx`) containing structured and cleaned data.

---

## Prerequisites

- **Python 3.6+** (Recommended Python 3.8+)
- Required Python packages (install via `pip install <package>` if needed):
  - `requests`
  - `beautifulsoup4`
  - `pandas`
  - `openpyxl`
  - `re` and `math` (both included in the Python standard library)

---

## Usage

1. **Clone this repository** or download the two scripts into a local directory.
2. **Install the required libraries** (see [Prerequisites](#prerequisites)).

### Scraping Phase

1. Open your terminal or command prompt.
2. Navigate to the directory containing `scrapping.py`.
3. Run:
   ```bash
   python scrapping.py
The script will:

Fetch all available locations.
Iterate over each location, scraping relevant data across all pages.
Save the extracted records to scraped_data.xlsx.
Display progress in your terminal (e.g., number of locations, pages, and entries processed).
Note: If you want to limit the number of locations (for testing), you can modify the loop:

python
Copiar
Editar
for loc in locations[:5]:  # Example: scrape only the first 5 locations
    ...
Cleaning Phase
Once scraping finishes, run:

bash
Copiar
Editar
python clean_scrapping.py
This script will:

Read scraped_data.xlsx.
Identify and normalize email addresses (lowercase, remove extra quotes).
Identify and normalize phone numbers (strip non-digit characters, up to 12 digits).
Save the final data (original columns + new email and phone columns) to scraped_clean.xlsx.
Output
The scripts produce two Excel files in the same directory:

scraped_data.xlsx

Raw, scraped data containing columns like:
CUIL
Nombre
Categoría
Registro
Localidad
Barrio
Multiple contacto_# columns
scraped_clean.xlsx

Cleaned version of the data with two additional fields:
email
phone
Customization
Location Filtering
You can modify the location list or the loop within scrapping.py to scrape only specific locations.

Wait Time Between Requests
time.sleep(1) in scrapping.py controls how long the script waits after each page request. Adjust it to reduce server load or speed up scraping.

Phone/Email Extraction Logic
In clean_scrapping.py, you can adjust the regex or logic used to detect phone and email formats, if your data has unique formatting needs.

Output Format
If you prefer CSV, replace the to_excel calls with to_csv in both scripts:

python
Copiar
Editar
df.to_csv("scraped_data.csv", index=False)
Limitations & Notes
Website Policies
Ensure compliance with the target site's terms of service. Scraping may be disallowed or subject to specific rules.

Data Freshness
The target website might change its layout or data. If that happens, the extraction logic may need to be updated.

Performance
This is a straightforward, non-parallel approach. For very large datasets, consider optimizing the script (e.g., running in parallel or caching data).

Error Handling
The current scripts handle some potential issues (like missing columns). You can extend them with more robust logging or exception handling as needed.

License
This project is open-source and available under an MIT License (or any license you choose to include). Feel free to modify and distribute it responsibly.

Happy Scraping!
If you have any questions or run into issues, please open an issue or pull request. Contributions are always welcome.

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

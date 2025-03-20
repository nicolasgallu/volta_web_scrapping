import pandas as pd
import re

# Read the entire Excel file
df = pd.read_excel('scraped_data.xlsx')

# Function to extract email from a list of contact fields
def extract_email(row):
    for contact in row:
        if isinstance(contact, str) and '@' in contact:
            # Normalize email (lowercase and remove quotes)
            return contact.lower().replace('"', '').replace("'", '')
    return None

# Function to extract phone number (first numeric value with the longest length, but <= 12 digits)
def extract_phone(row):
    phone_candidates = []
    for contact in row:
        if isinstance(contact, str) and not '@' in contact:
            # Remove non-numeric characters (spaces, hyphens, etc.)
            cleaned_contact = re.sub(r'\D', '', contact)
            if cleaned_contact and len(cleaned_contact) <= 12:  # Only consider non-empty and <= 12 digit numbers
                phone_candidates.append(cleaned_contact)
    
    # If we have phone candidates, return the longest one, but only up to 12 digits
    if phone_candidates:
        return max(phone_candidates, key=len)
    return None

# Select only the contact columns for email and phone extraction
contact_columns = ['contacto_1', 'contacto_2', 'contacto_3', 'contacto_4']

# Apply the extraction functions to each row of the selected columns
df['email'] = df[contact_columns].apply(lambda row: extract_email(row), axis=1)
df['phone'] = df[contact_columns].apply(lambda row: extract_phone(row), axis=1)

# Save the cleaned data to a new Excel file, including all original columns and the new 'email' and 'phone' columns
df.to_excel('scraped_clean.xlsx', index=False)

print("File cleaned and saved as 'scraped_clean.xlsx'")

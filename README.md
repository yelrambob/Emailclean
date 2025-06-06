# Emailclean

# Gmail Filter Email Blocker

This script helps you generate Gmail filter rules from a list of email addresses.

## Features
- Removes duplicate email addresses
- Groups addresses by domain (e.g., `@example.com`)
- Outputs chunks of addresses separated by a visual marker to avoid Gmail filter character limits

## Instructions

1. Save your email addresses in a CSV file named `senders.csv`
    - Ensure the CSV has a column titled `Email`
2. Run the script:
```bash
python gmail_filter_email_blocker.py
# alu_regex-data-extraction-MizeroEloi

# Text Data Extractor

A lightweight Python utility for identifying and extracting structured data patterns from text documents. This tool scans through any text input to locate emails, web addresses, phone numbers, payment card details, and timestamp information while providing validation feedback.

## Features Overview

**Email Detection**: Locates email addresses throughout text and validates their format structure
**Web Address Parsing**: Extracts URLs with various prefixes including `http://`, `https://`, and `www` patterns  
**Phone Number Recognition**: Identifies phone numbers across multiple formatting styles like `(123) 456-7890`
**Payment Card Discovery**: Detects credit card numbers formatted with spaces or hyphen separators
**Time Pattern Matching**: Recognizes both 24-hour format (`14:30`) and standard 12-hour notation (`2:30 PM`)

## Getting Started

To see the extractor in action, execute the included demonstration script:

```bash
python3 test_extractors.py
```

This will process sample text and display categorized results showing both successfully matched and problematic entries.

## Project Structure

**`extractor.py`** - Core functionality implementing regex-based pattern matching and validation logic
**`test_extractors.py`** - Demonstration script showcasing extraction capabilities with sample data

## Available Methods

**`extract_emails(text)`** - Returns valid email addresses and flags formatting issues
**`extract_urls(text)`** - Identifies web links and validates URL structure  
**`extract_phone_numbers(text)`** - Captures phone numbers in standard formats
**`extract_credit_cards(text)`** - Locates payment card numbers with common separators
**`extract_times(text)`** - Finds time expressions and validates format correctness

## Sample Results

Running the demo produces output similar to this:

```
=== Email Detection Results ===
Found valid: ['user@example.com', 'firstname.lastname@company.co.uk']
Format issues: ['Malformed email: wrong@.com', 'Incomplete email: user@site']

=== URL Detection Results ===
Found valid: ['https://www.example.com', 'http://testsite.org', 'www.example.com/page']
Format issues: ['Malformed URL: invalid_link']

=== Phone Number Results ===
Found valid: ['(123) 456-7890', '123-456-7890', '123.456.7890', '1234567890']
Format issues: ['Incomplete number: (1234567890']

=== Credit Card Results ===
Found valid: ['1234 5678 9012 3456', '1234-5678-9012-3456']
Format issues: ['Invalid card format: 1234567890123456']

=== Time Detection Results ===
Found valid: ['14:30', '2:30 PM', '02:30 pm', '7:00AM', '7:00']
Format issues: ['Invalid time: 25:00']
```

## Requirements

Python 3.x (uses standard library `re` module - no additional dependencies needed)

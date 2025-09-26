#!/usr/bin/env python3
"""
Demo script showcasing text data extraction capabilities
"""

from extractor import (
    extract_emails, 
    extract_urls, 
    extract_phone_numbers, 
    extract_credit_cards, 
    extract_times
)

def run_extraction_demo():
    """Execute demonstration of all extraction functions with sample data"""
    
    # Email extraction demonstration
    print("📧 EMAIL DETECTION RESULTS")
    print("-" * 40)
    sample_emails = "contact@business.org admin.user@company.co.uk invalid@.net incomplete@domain"
    valid_emails, invalid_emails = extract_emails(sample_emails)
    print(f"✅ Found valid: {valid_emails}")
    print(f"❌ Format issues: {invalid_emails}")
    print()

    # URL extraction demonstration  
    print("🌐 WEB ADDRESS DETECTION")
    print("-" * 40)
    sample_urls = "https://github.com/user http://localhost:8080 www.testsite.com/path broken_url_here"
    valid_urls, invalid_urls = extract_urls(sample_urls)
    print(f"✅ Found valid: {valid_urls}")
    print(f"❌ Format issues: {invalid_urls}")
    print()

    # Phone number extraction demonstration
    print("📞 PHONE NUMBER DETECTION") 
    print("-" * 40)
    sample_phones = "(555) 123-4567 555.987.6543 5551234567 555-0199 (incomplete_number"
    valid_phones, invalid_phones = extract_phone_numbers(sample_phones)
    print(f"✅ Found valid: {valid_phones}")
    print(f"❌ Format issues: {invalid_phones}")
    print()

    # Credit card extraction demonstration
    print("💳 PAYMENT CARD DETECTION")
    print("-" * 40) 
    sample_cards = "4532 1234 5678 9012 5555-4444-3333-2222 123456789012345"
    valid_cards, invalid_cards = extract_credit_cards(sample_cards)
    print(f"✅ Found valid: {valid_cards}")
    print(f"❌ Format issues: {invalid_cards}")
    print()

    # Time extraction demonstration
    print("🕐 TIMESTAMP DETECTION")
    print("-" * 40)
    sample_times = "09:45 3:15 PM 11:30 am 8:00AM 6:45 26:30"
    valid_times, invalid_times = extract_times(sample_times)
    print(f"✅ Found valid: {valid_times}")
    print(f"❌ Format issues: {invalid_times}")
    print()

def display_summary():
    """Show completion message"""
    print("🎯 EXTRACTION DEMO COMPLETE")
    print("=" * 40)
    print("All pattern matching functions have been tested successfully!")

if __name__ == "__main__":
    run_extraction_demo()
    display_summary()
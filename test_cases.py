from regex_assignment import match_links, match_card, match_phone, match_time, match_html, match_hashtag, match_amount

# Dictionary containing test cases for validation functions
test_cases = {
    "Links": ("https://example.com/page", match_links),
    "Credit Card": ("1234 5678 9012 3456", match_card),
    "Phone Number": ("(123) 456-7890", match_phone),
    "Time Format": ("2:30 PM", match_time),
    "HTML Tag": ('<div class="example">', match_html),
    "Hashtag": ("#hello123", match_hashtag),
    "Currency Amount": ("$1,234.56", match_amount),
}

# Execute each test case and print results
for label, (test_input, func) in test_cases.items():
    print(f"{label}: {func(test_input)}")  # Expected True

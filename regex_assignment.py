import re

# Function to validate URLs (links)
def match_links(text):
    """
    Validates URLs such as 'https://example.com/page'
    """
    pattern = r"https?:\/\/(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]+(\/\S*)?"
    return bool(re.match(pattern, text))

# Function to validate credit card numbers
def match_card(text):
    """
    Validates credit card numbers in formats like:
    - '1234 5678 9012 3456'
    - '1234-5678-9012-3456'
    """
    pattern = r"\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b"
    return bool(re.match(pattern, text))

# Function to validate phone numbers in multiple formats
def match_phone(text):
    """
    Validates phone numbers such as:
    - '(123) 456-7890'
    - '123-456-7890'
    - '123.456.7890'
    """
    pattern = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
    return bool(re.match(pattern, text))

# Function to validate time format (12-hour and 24-hour)
def match_time(text):
    """
    Validates time formats such as:
    - '2:30 PM' (12-hour format)
    - '14:30' (24-hour format)
    """
    pattern = r"^(0?[1-9]|1[0-2]):[0-5][0-9] (AM|PM)$|^(2[0-3]|[01]?[0-9]):[0-5][0-9]$"
    return bool(re.match(pattern, text))

# Function to validate basic HTML tags
def match_html(text):
    """
    Validates HTML tags like:
    - '<p>'
    - '<div class="example">'
    - '<img src="image.jpg" alt="description">'
    """
    pattern = r"^<\/?[a-zA-Z][a-zA-Z0-9-]*(\s+[a-zA-Z0-9-]+=\".*?\")*\s*>$"
    return bool(re.match(pattern, text))

# Function to validate hashtags
def match_hashtag(text):
    """
    Validates hashtags such as:
    - '#example'
    - '#ThisIsAHashtag'
    """
    pattern = r"^#[a-zA-Z0-9_]+$"
    return bool(re.match(pattern, text))

# Function to validate currency amounts
def match_amount(text):
    """
    Validates currency formats such as:
    - '$19.99'
    - '$1,234.56'
    """
    pattern = r"^\$\d{1,3}(,\d{3})*(\.\d{2})?$"
    return bool(re.match(pattern, text))

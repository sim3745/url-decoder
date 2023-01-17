import pyperclip
import urllib.parse

while True:
    # Prompt the user for the URL
    current_url = input("Enter the URL to decode: ")

    print("This is the URL that will be decoded: " + current_url)

    # Decode the URL
    decoded_url = urllib.parse.unquote(current_url)

    # Copy the decoded URL to the clipboard
    pyperclip.copy(decoded_url)
    print("This is the decoded URL: " + decoded_url + ". The URL had been pasted to clipboard")

# credentials.py

# Ask user for name
name = input("Enter your GitHub username: ")

# Ask user for token (input is hidden for security)
import getpass
token = getpass.getpass("Enter your GitHub token: ")

print("\n--- Your GitHub Credentials ---")
print(f"Username: {name}")
print(f"Token: {token}")  # Be careful printing tokens in real use!

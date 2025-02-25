# Open necessary files
with open("passwordDump.txt", "r", encoding="latin-1") as hash_file, open("rockyou.txt", "r", encoding="latin-1") as wordlist_file:
    hashes = [line.strip().split(":", 1) for line in hash_file]  # Extract username and hash
    words = [word.strip() for word in wordlist_file]  # Load wordlist

# Create a new salted wordlist
with open("salted_rockyou.txt", "w", encoding="latin-1") as outfile:
    for username, hash_val in hashes:
        for word in words:
            outfile.write(f"{username}{word}\n")  # Prepend username
            outfile.write(f"{word}{username}\n")  # Append username

print("✅ Salted wordlist saved to salted_rockyou.txt")

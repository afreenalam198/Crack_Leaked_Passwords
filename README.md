# Goldman Sachs Software Engineering Virtual Internship (Forage) - Crack Leaked Passwords Using Hashcat

## Project Deliverables

In this job simulation as a Goldman Sachs governance ananlyst responsible for assessing IT security and suggesting improvements, I was tasked with the following -
1. Reviewing this Ars Technica article on the [Anatomy of a hack: How crackers ransack passwords like “qeadzcwrsfxv1331”](https://arstechnica.com/information-technology/2013/05/how-crackers-make-minced-meat-out-of-your-passwords/)
2. Cracking as many passwords as possible provided in the 'password dump' file.
3. Determining the type of hashing algorithm used to protect the passwords.
5. Writing a memo for my supervisor summarizing a range of proposed uplifts to increase the company’s level of password protection.

## Password Cracking Techniques: Insights from Ars Technica

This section summarizes key password cracking methods discussed in the Ars Technica article:

* **Efficient Guessing:** Prioritizing dictionary attacks, pattern recognition, and variations of common words to maximize success before resorting to brute-force.
* **Brute-Force Attacks:** Systematically testing all possible password combinations against hashed values, particularly effective for cracking short (1-6 character) passwords.
* **Hybrid Strategies:** Merging dictionary and brute-force attacks to broaden the search while maintaining efficiency.
* **Intelligent Brute-Force:** Employing analysis of cracked passwords to statistically generate brute-force attacks based on Markov chains to predict likely password patterns, enabling targeted brute-force attacks (e.g., using tools like Hashcat).
  
## Password Cracking Methodology

Here's a breakdown of the steps I took to crack the passwords in `passwordDump.txt`:

1.  **Data Preparation:**
    * Downloaded `passwordDump.txt` containing password hashes.
    * Cleaned the file to isolate the hashes.

2.  **Tool Setup:**
    * Installed Hashcat using Homebrew: `brew install hashcat`.

3.  **Hash Algorithm Identification:**
    * Utilized an online hash identifier (e.g., [hashes.com](https://hashes.com/en/tools/hash_identifier)) to determine the hash type: MD5.
    * Set the Hashcat mode to MD5 (`-m 0`).

4.  **Dictionary Attack (Method 1):**
    * Downloaded the `rockyou.txt` wordlist.
    * Executed the following command:
        ```bash
        hashcat -m 0 passwordDump.txt rockyou.txt --username
        ```
    * Result: 13 passwords cracked.
    * Downloaded additional wordlists from SecLists.
    * Attempted to crack additional passwords, but no new passwords were cracked.

5.  **Rule-Based Attack (Method 2):**
    * Applied Hashcat's `best64` rule to the `rockyou.txt` wordlist.
    * Executed the following command:
        ```bash
        hashcat -m 0 passwordDump.txt rockyou.txt -r /opt/homebrew/Cellar/hashcat/6.2.6_1/share/doc/hashcat/rules/best64.rule --username
        ```
    * Result: 1 additional password cracked.

6.  **Salting Attack (Method 3):**
    * Developed a Python script to generate a salted version of `rockyou.txt` using usernames from `passwordDump.txt`.
    * Implemented both username prepending and appending to the wordlist.
    * Executed the following command:
        ```bash
        hashcat -m 0 passwordDump.txt salted_rockyou.txt -r /opt/homebrew/Cellar/hashcat/6.2.6_1/share/doc/hashcat/rules/best64.rule --username
        ```
    * Result: 3 additional passwords cracked.

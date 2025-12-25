# ==============================
# JIGU'S DOT-NUMBER CIPHER v1.0
# Fully ready-to-use
# ==============================

# --- SET YOUR KEY HERE ---
KEY = 1  # change this to any number you like for encode/decode

# --- Special mapping for non-letter characters ---
special_chars = {
    ' ': '0',       # space (optional)
    '.': '27',
    ',': '28',
    '!': '29',
    '?': '30',
    '…': '31',
    '’': '32',
    '"': '33',
    '“': '34',
    '”': '35',
    '\n': '36',
    '🎵': '37',
    '—': '38',
    '–': '39',
}

reverse_special = {v: k for k, v in special_chars.items()}

# --- ENCODE FUNCTION ---
def encode_text(text):
    text = text.lower()
    words = text.split()
    encoded_words = []

    for word in words:
        encoded_letters = []
        for char in word:
            if char.isalpha():
                number = ord(char) - ord('a') + 1
                encoded_letters.append(str(number + KEY))
            elif char in special_chars:
                encoded_letters.append(special_chars[char])
        encoded_words.append('.'.join(encoded_letters))

    return ' '.join(encoded_words)

# --- DECODE FUNCTION ---
def decode_text(code):
    words = code.split()
    decoded_words = []

    for word in words:
        letters = word.split('.')
        decoded_letters = []
        for num in letters:
            if num.isdigit():
                if num in reverse_special:
                    decoded_letters.append(reverse_special[num])
                elif 1 <= int(num) - KEY <= 26:
                    decoded_letters.append(chr(int(num) - KEY + ord('a') - 1))
                else:
                    decoded_letters.append('?')  # unknown code
        decoded_words.append(''.join(decoded_letters))

    return ' '.join(decoded_words)

# ==============================
# --- PASTE YOUR TEXT HERE ---
# ==============================
text = """the sun rises in east"""
# ==============================
# --- RUN ENCODE + DECODE ---
# ==============================
encoded = encode_text(text)
decoded = decode_text(encoded)

print("Original:\n", text, "\n")
print("Encoded:\n", encoded, "\n")
print("Decoded:\n", decoded)

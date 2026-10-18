def _shift_text(text, key, alphabet, direction):
    key = key.lower().replace('ё', 'е')
    if not key or any(ch not in alphabet for ch in key):
        raise ValueError("Key must be non-empty and contain only alphabet letters")

    n, result, key_pos = len(alphabet), '', 0

    for char in text:
        lower = char.lower()
        if lower not in alphabet:
            result += char
            continue

        char_id = alphabet.index(lower)
        key_id = alphabet.index(key[key_pos % len(key)])
        key_pos += 1

        new_char = alphabet[(char_id + direction * key_id) % n]
        result += new_char.upper() if char.isupper() else new_char

    return result


def encrypt(plaintext, key, alphabet):
    plaintext = plaintext.replace('ё', 'е').replace('Ё', 'Е')
    return _shift_text(plaintext, key, alphabet, 1)


def decrypt(ciphertext, key, alphabet):
    return _shift_text(ciphertext, key, alphabet, -1)
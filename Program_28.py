'''  
@author: 22000409 Kaushal Ramoliya  
@description: 28. -  Write a Python script for language transliteration between Gujarati and English Script. 
Input : આપણે બધા કત્રિમ બદ્ધિ ત્રિષય શીખી રહ્યા છે. 
output : Aapde badha krutrim buddhi vishay sikhi rahya chee.
'''  
# Simple transliteration maps
gujarati_to_english_map = {
    'અ': 'a', 'આ': 'aa', 'ઇ': 'i', 'ઈ': 'ee', 'ઉ': 'u', 'ઊ': 'oo',
    'ઋ': 'ru', 'એ': 'e', 'ઐ': 'ai', 'ઓ': 'o', 'ઔ': 'au',
    'ક': 'k', 'ખ': 'kh', 'ગ': 'g', 'ઘ': 'gh', 'ઙ': 'ng',
    'ચ': 'ch', 'છ': 'chh', 'જ': 'j', 'ઝ': 'jh', 'ઞ': 'ny',
    'ટ': 't', 'ઠ': 'th', 'ડ': 'd', 'ઢ': 'dh', 'ણ': 'n',
    'ત': 't', 'થ': 'th', 'દ': 'd', 'ધ': 'dh', 'ન': 'n',
    'પ': 'p', 'ફ': 'ph', 'બ': 'b', 'ભ': 'bh', 'મ': 'm',
    'ય': 'y', 'ર': 'r', 'લ': 'l', 'વ': 'v',
    'શ': 'sh', 'ષ': 'sh', 'સ': 's', 'હ': 'h',
    'ળ': 'l', 'ક્ષ': 'ksh', 'જ્ઞ': 'gy',
    'ા': 'aa', 'િ': 'i', 'ી': 'ee', 'ુ': 'u', 'ૂ': 'oo',
    'ે': 'e', 'ૈ': 'ai', 'ો': 'o', 'ૌ': 'au',
    'ૃ': 'ru',
    '્': '',    # halant
    'ં': 'n', 'ઃ': 'h', 'ઁ': 'n'
}

# Reverse mapping for English to Gujarati
english_to_gujarati_map = {v: k for k, v in gujarati_to_english_map.items()}

# Special cases where mapping conflicts (like 'sh' for both શ and ષ)
# So you can manually fix if needed.

# Matras list
matras = ['ા', 'િ', 'ી', 'ુ', 'ૂ', 'ે', 'ૈ', 'ો', 'ૌ', 'ૃ']

def transliterate_gujarati_to_english(text):
    result = ''
    skip_next = False
    for idx, char in enumerate(text):
        if skip_next:
            skip_next = False
            continue

        if char == '્' and idx > 0:
            continue

        if idx + 1 < len(text) and text[idx + 1] in matras:
            base = gujarati_to_english_map.get(char, char)
            matra = gujarati_to_english_map.get(text[idx + 1], '')
            result += base + matra
            skip_next = True
        else:
            result += gujarati_to_english_map.get(char, char)

    return result

def transliterate_english_to_gujarati(text):
    result = ''
    idx = 0
    while idx < len(text):
        match = ''
        match_char = ''

        # Try to match the longest possible sequence (3-letter, 2-letter, 1-letter)
        for l in [3, 2, 1]:
            if idx + l <= len(text):
                part = text[idx:idx+l]
                if part in english_to_gujarati_map:
                    match = part
                    match_char = english_to_gujarati_map[part]
                    break

        if match:
            result += match_char
            idx += len(match)
        else:
            result += text[idx]
            idx += 1

    return result

if __name__ == "__main__":
    print("Select option:")
    print("1. Gujarati to English")
    print("2. English to Gujarati")
    choice = input("Enter 1 or 2: ")

    with open('Program_28_input.txt', 'r', encoding='utf-8') as f:
        input_text = f.read()

    if choice == '1':
        output_text = transliterate_gujarati_to_english(input_text)
    elif choice == '2':
        output_text = transliterate_english_to_gujarati(input_text)
    else:
        print("Invalid choice.")
        exit()

    with open('Program_28_output.txt', 'w', encoding='utf-8') as f:
        f.write(output_text)

    print("Transliteration complete. Output saved to output.txt.")

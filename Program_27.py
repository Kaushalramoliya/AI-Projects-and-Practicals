'''  
@author: 22000409 Kaushal Ramoliya  
@description: 27. - Write a python script to transliterate between hindi and Gujarati and vice-versa. 
Please find unicode chart 
'''  
def transliterate(content, mode="gujarati_to_hindi"):
    result = ""

    for ch in content:
        code_point = ord(ch)
        if mode == "gujarati_to_hindi":
            # Gujarati Unicode Range
            if 2688 <= code_point <= 2815:
                result += chr(code_point - 384)
            else:
                result += ch
        elif mode == "hindi_to_gujarati":
            # Hindi Unicode Range
            if 2304 <= code_point <= 2431:
                result += chr(code_point + 384)
            else:
                result += ch
    return result

# Main Program
if __name__ == "__main__":
    print("Choose Transliteration Mode:")
    print("1. Gujarati to Hindi")
    print("2. Hindi to Gujarati")
    
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        input_filename = "Program_27_gujarati_input.txt"
        output_filename = "Program_27_hindi_output.txt"
        mode = "gujarati_to_hindi"
    elif choice == "2":
        input_filename = "Program_27_hindi_input.txt"
        output_filename = "Program_27_gujarati_output.txt"
        mode = "hindi_to_gujarati"
    else:
        print("Invalid choice. Please select 1 or 2.")
        exit()

    try:
        with open(input_filename, "r", encoding="utf-8") as fp:
            content = fp.read()

        transliterated_content = transliterate(content, mode)

        with open(output_filename, "w", encoding="utf-8") as fw:
            fw.write(transliterated_content)

        print(f"Transliteration completed successfully!")
        print(f"Input File: {input_filename}")
        print(f"Output File: {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file {input_filename} was not found.")

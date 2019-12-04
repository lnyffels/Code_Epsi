# Correction
def capitalize(s):
    result = replace_i(s)
    result = replace_first_letter(result)
    result = capitalize_first_letter_after_accentuation_character(result)
    return result


def replace_i(s: str)->str:
    result = s.replace(" i ", " I ")
    return result

def replace_first_letter(s):
    if len(s) > 0:
        s = s[0].upper() + s[1: len(s)]
    return s

def capitalize_first_letter_after_accentuation_character(s):
    pos = 0
    while pos < len(s):
        if s[pos] == "." or s[pos] == "?" or s[pos] == "!":
            pos += 1
            # passer les espaces
            while pos < len(s) and s[pos] == " ":
                pos += 1
            if pos < len(s):
                s = s[0:pos] + s[pos].upper() + s[pos+1:len(s)]
        pos+=1

    return s

# def main():
#     s = input("Entrer le texte :")
#     s_capitalized = capitalize(s)
#     print ("la chaine formatéé : ", s_capitalized)
#
#
# main()
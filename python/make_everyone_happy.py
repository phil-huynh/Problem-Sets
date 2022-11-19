def smile(text):
    text = [x for x in text]
    eyes = [":", ";", "="]
    noses = ["-", "~"]
    smiles = { "[": "]", "(": ")"}
    result = ""
    for i in range(len(text)):
        if text[i] in eyes:
            try:
                if text[i + 1] in smiles:
                    text[i + 1] = smiles[text[i + 1]]
                if text[i + 1] in noses and text[i + 2] in smiles:
                    text[i + 2] = smiles[text[i + 2]]
                result += text[i]
            except IndexError:
                result += text[i]
        else:
            result += text[i]
    return result
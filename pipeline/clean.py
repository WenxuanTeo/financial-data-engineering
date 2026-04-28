def clean_text(text):
    if not text:
        return ""
    text = text.replace("\n", " ")
    text = text.replace("  ", " ")
    return text.strip()

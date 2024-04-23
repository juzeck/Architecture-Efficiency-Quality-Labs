def clean_string(text):
    cleaned = text.strip().lower()
    if cleaned and cleaned[-1].isalpha():
        return cleaned + '.'
    else:
        return ''.join(c for c in cleaned if c.isalpha()) + '.'


def process_data(data):
    return [clean_string(item) for item in data]

def process_data(data):
    result = []
    for item in data:
        processed = item.strip().lower()
        if len(processed) > 0:
            if processed[-1].isalpha():
                processed += '.'
            else:
                chars = list(processed)
                for i in range(len(chars) - 1, -1, -1):
                    if not chars[i].isalpha():
                        chars[i] = ''
                    else:
                        break
                processed = ''.join(chars) + '.'
            result.append(processed)
    return result

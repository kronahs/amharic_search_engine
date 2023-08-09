prefixes_set = ['እንደ', 'እስኪ', 'በየ', 'ከነ', 'ያለ', 'እነ', 'ስለ', 'ለ', 'ከ', 'የ', 'በ']

def prefix(input):
    if not isinstance(input, str):
        return ''
    input = input.strip()
    if not input:
        return ''
    for prefix in prefixes_set:
        if input.startswith(prefix) and len(input)>3:
            input = input.removeprefix(prefix)
            return input
    return input

print(prefix('ስለሆነም'))
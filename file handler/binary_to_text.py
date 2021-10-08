with open('binary_to_text.py', 'wb') as f:
    ga = b'\xea\xB0\x80'
    f.write(ga)

with open('binary_to_text.bin', 'r', encoding='utf-8') as f:
    data = f.read()

print(data)
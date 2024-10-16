def generate_playfair_matrix(key):
    # Menghilangkan huruf duplikat dari kunci dan menggabungkan J dengan I
    key = ''.join(dict.fromkeys(key.replace('J', 'I')))
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = []
    used_chars = set(key)
    
    # Menyusun matriks berdasarkan kunci
    for char in key:
        matrix.append(char)
    
    # Melengkapi matriks dengan huruf-huruf alfabet yang belum digunakan
    for char in alphabet:
        if char not in used_chars:
            matrix.append(char)
    
    # Mengubah list menjadi format matriks 5x5
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def prepare_text(plaintext):
    # Mengubah menjadi huruf kapital, menggabungkan J dengan I, dan menghapus spasi
    plaintext = plaintext.upper().replace('J', 'I').replace(" ", "")
    
    # Memisahkan ke dalam bigram dan menambahkan 'X' jika diperlukan
    bigrams = []
    i = 0
    while i < len(plaintext):
        a = plaintext[i]
        b = plaintext[i + 1] if i + 1 < len(plaintext) else 'X'
        if a == b:
            bigrams.append(a + 'X')
            i += 1
        else:
            bigrams.append(a + b)
            i += 2
    
    # Jika ganjil, tambahkan X di akhir
    if len(plaintext) % 2 != 0:
        bigrams.append(plaintext[-1] + 'X')
    
    return bigrams

def find_position(matrix, letter):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col
    return None

def encrypt_bigram(bigram, matrix):
    row1, col1 = find_position(matrix, bigram[0])
    row2, col2 = find_position(matrix, bigram[1])
    
    # Jika keduanya berada di baris yang sama
    if row1 == row2:
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    
    # Jika keduanya berada di kolom yang sama
    elif col1 == col2:
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    
    # Jika mereka berada di baris dan kolom yang berbeda
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def playfair_encrypt(plaintext, key):
    matrix = generate_playfair_matrix(key)
    bigrams = prepare_text(plaintext)
    encrypted_text = ''
    
    for bigram in bigrams:
        encrypted_text += encrypt_bigram(bigram, matrix)
    
    return encrypted_text

# Enkripsi dengan kunci "TEKNIK INFORMATIKA"
plaintexts = [
    "GOOD BROOM SWEEP CLEAN",
    "REDWOOD NATIONAL STATE PARK",
    "JUNK FOOD AND HEALTH PROBLEMS"
]

key = "TEKNIK INFORMATIKA"
for plaintext in plaintexts:
    encrypted = playfair_encrypt(plaintext, key)
    print(f"Plaintext: {plaintext}\nEncrypted: {encrypted}\n")

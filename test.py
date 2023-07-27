def sha256_hash(text):
    # Khởi tạo các hằng số
    h0 = 0x6a09e667
    h1 = 0xbb67ae85
    h2 = 0x3c6ef372
    h3 = 0xa54ff53a
    h4 = 0x510e527f
    h5 = 0x9b05688c
    h6 = 0x1f83d9ab
    h7 = 0x5be0cd19

    # Khởi tạo danh sách các hằng số
    k = [
        0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
        0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
        0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
        0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
        0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
        0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
        0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
    ]

    # Chuyển đổi chuỗi thành dạng byte
    byte_string = bytearray(text.encode('utf-8'))

    # Thêm byte padding
    byte_string.append(0x80)

    while len(byte_string) % 64 != 56:
        byte_string.append(0x00)

    # Gắn vào 64 bit cuối của độ dài chuỗi
    length = len(text) * 8
    byte_string += length.to_bytes(8, 'big')

    # Tạo các block 512-bit từ chuỗi byte
    blocks = [byte_string[i:i + 64] for i in range(0, len(byte_string), 64)]

    for block in blocks:
        # Tạo danh sách từng từ 32-bit từ block
        words = [int.from_bytes(block[i:i + 4], 'big') for i in range(0, 64, 4)]

        # Mở rộng từ 16-word đến 64-word
        for i in range(16, 64):
            s0 = right_rotate(words[i - 15], 7) ^ right_rotate(words[i - 15], 18) ^ (words[i - 15] >> 3)
            s1 = right_rotate(words[i - 2], 17) ^ right_rotate(words[i - 2], 19) ^ (words[i - 2] >> 10)
            words.append((words[i - 16] + s0 + words[i - 7] + s1) & 0xffffffff)

        # Khởi tạo các biến băm
        a = h0
        b = h1
        c = h2
        d = h3
        e = h4
        f = h5
        g = h6
        h = h7

        # Thực hiện vòng lặp chính
        for i in range(64):
            S1 = right_rotate(e, 6) ^ right_rotate(e, 11) ^ right_rotate(e, 25)
            ch = (e & f) ^ ((~e) & g)
            temp1 = (h + S1 + ch + k[i] + words[i]) & 0xffffffff
            S0 = right_rotate(a, 2) ^ right_rotate(a, 13) ^ right_rotate(a, 22)
            maj = (a & b) ^ (a & c) ^ (b & c)
            temp2 = (S0 + maj) & 0xffffffff

            h = g
            g = f
            f = e
            e = (d + temp1) & 0xffffffff
            d = c
            c = b
            b = a
            a = (temp1 + temp2) & 0xffffffff

        # Cộng thêm các giá trị ban đầu
        h0 = (h0 + a) & 0xffffffff
        h1 = (h1 + b) & 0xffffffff
        h2 = (h2 + c) & 0xffffffff
        h3 = (h3 + d) & 0xffffffff
        h4 = (h4 + e) & 0xffffffff
        h5 = (h5 + f) & 0xffffffff
        h6 = (h6 + g) & 0xffffffff
        h7 = (h7 + h) & 0xffffffff

    # Kết hợp các giá trị băm thành chuỗi kết quả
    hashed_text = '{:08x}{:08x}{:08x}{:08x}{:08x}{:08x}{:08x}{:08x}'.format(h0, h1, h2, h3, h4, h5, h6, h7)

    return hashed_text

def right_rotate(value, count):
    return ((value >> count) | (value << (32 - count))) & 0xffffffff

text = "Xin chào"
tet = "Xin chào "
has = sha256_hash(text)
hashed_text = sha256_hash(tet)
print(hashed_text)

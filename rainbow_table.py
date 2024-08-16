import hashlib
import string
import itertools

class RainbowTable:
    def __init__(self, hash_function='md5', chain_length=1000):
        self.hash_function = hash_function
        self.chain_length = chain_length
        self.table = {}

    def hash(self, plaintext):
        return hashlib.new(self.hash_function, plaintext.encode('utf-8')).hexdigest()

    def reduce(self, hash_value, step):
        chars = string.ascii_lowercase + string.digits
        reduced_text = ''.join(chars[int(hash_value[i:i+2], 16) % len(chars)] for i in range(0, len(hash_value), 2))
        return reduced_text[:6]  # Limiting to 6 characters

    def create_chain(self, start_text):
        current_text = start_text
        for i in range(self.chain_length):
            current_hash = self.hash(current_text)
            current_text = self.reduce(current_hash, i)
        return current_text

    def generate_table(self, plaintexts):
        for plaintext in plaintexts:
            end_text = self.create_chain(plaintext)
            self.table[end_text] = plaintext

    def save_table(self, filename='rainbow_table.txt'):
        with open(filename, 'w') as file:
            for end_text, start_text in self.table.items():
                file.write(f'{start_text} -> {end_text}\n')

    def load_table(self, filename='rainbow_table.txt'):
        with open(filename, 'r') as file:
            for line in file:
                start_text, end_text = line.strip().split(' -> ')
                self.table[end_text] = start_text

    def lookup(self, hash_value):
        for step in range(self.chain_length):
            reduced_text = self.reduce(hash_value, step)
            if reduced_text in self.table:
                current_text = self.table[reduced_text]
                for i in range(step + 1):
                    if self.hash(current_text) == hash_value:
                        return current_text
                    current_text = self.reduce(self.hash(current_text), i)
        return None

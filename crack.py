import hashlib
import concurrent.futures

def hash_password(password, num_hashes):
    print(password, end=":")
    for i in range(num_hashes):
        password = hashlib.md5(password.encode('utf-8')).hexdigest()
    print(password)
    return password

def dictionary_attack(dictionary, hashed_password, num_hashes):
    with open(dictionary, 'r', errors='ignore') as f:
        for word in f:
            word = word.strip()
            if hash_password(word, num_hashes) == hashed_password:
                return word
    return None

if __name__ == '__main__':
    dictionary = input('Enter the path to the dictionary file: ')
    hashed_password = input('Enter the hashed password to crack: ')
    num_hashes = int(input('Enter the number of times the password was hashed: '))

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(dictionary_attack, dictionary, hashed_password, num_hashes)
        result = future.result()

    if result is not None:
        print(f'The password is: {result}')
    else:
        print('Password not found in dictionary')


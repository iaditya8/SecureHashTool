import hashlib

def calculate_hash(file_path, algorithm='sha256'):
    try:
        with open(file_path, "rb") as f:
            file_data = f.read()
    except Exception as e:
        print(f"Error opening file: {e}")
        return None

    if algorithm == 'md5':
        hash_result = hashlib.md5(file_data).hexdigest()
    elif algorithm == 'sha1':
        hash_result = hashlib.sha1(file_data).hexdigest()
    elif algorithm == 'sha256':
        hash_result = hashlib.sha256(file_data).hexdigest()
    else:
        print("Unsupported hash type.")
        return None

    return hash_result

if __name__ == "__main__":
    print("Hash Calculator and Verifier")

    file_path = input("Enter file path: ").strip()
    algorithm = input("Choose algorithm (md5 / sha1 / sha256): ").lower().strip()

    hash_value = calculate_hash(file_path, algorithm)

    if hash_value:
        print(f"{algorithm.upper()} Hash: {hash_value}")

        choice = input("Do you want to verify with a known hash? (y/n): ").lower()
        if choice == 'y':
            known_hash = input("Enter the known hash: ").strip()
            if known_hash == hash_value:
                print("Hash matches. File is authentic.")
            else:
                print("Hash does not match. File may have been tampered with.")
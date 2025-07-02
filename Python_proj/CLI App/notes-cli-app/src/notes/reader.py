def read_notes(file_path, encryptor):
    decrypted_notes = []
    try:
        with open(file_path, 'r') as file:
            encrypted_notes = file.readlines()
            for encrypted_note in encrypted_notes:
                decrypted_note = encryptor.decrypt(encrypted_note.strip())
                decrypted_notes.append(decrypted_note)
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred while reading notes: {e}")
    return decrypted_notes
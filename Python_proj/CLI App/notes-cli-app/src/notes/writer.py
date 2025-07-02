def write_note(file_path, note, encryptor):
    encrypted_note = encryptor.encrypt(note)
    with open(file_path, 'a') as file:
        file.write(encrypted_note + '\n')
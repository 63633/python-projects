# Notes CLI Application

This is a command-line notes application that allows users to write and read notes securely using encryption. The application provides a simple interface for managing notes, ensuring that your thoughts and ideas are kept private.

## Features

- Write notes that are encrypted before being saved.
- Read notes that are decrypted when retrieved.
- Simple command-line interface for easy interaction.

## Installation

To get started with the Notes CLI Application, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd notes-cli-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:

```
python src/main.py
```

### Commands

- **Add a Note**: Follow the prompts to enter a note, which will be encrypted and saved.
- **View Notes**: Retrieve and view your saved notes, which will be decrypted for your convenience.

## Dependencies

This project requires the following Python package:

- `cryptography`: For encrypting and decrypting notes.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
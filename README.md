# Enigma Machine Emulator 

A Python-based emulator of the **Enigma Machine**, the famous World War II cipher device. This interactive command-line tool allows users to encrypt and decrypt messages using rotor-based substitution encryption.

##  Features

- **Fully functional rotors** (including stepping and ring settings)
- **Reflector implementation** for bidirectional encryption
- **Plugboard swaps** for additional security
- **Interactive CLI** for encrypting/decrypting messages
- **Configurable rotors, reflectors, and plugboard settings**

## Installation

Ensure you have Python **3.x** installed on your system.

1. Clone this repository:
   ```sh
   git clone https://github.com/pkalantzis/enigma-emulator
   cd enigma-emulator
   ```

2. (Optional) Create a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows
   ```

3. Run the program:
   ```sh
   python enigma_emulator.py
   ```

## Usage

1. Start the program and enter a message when prompted.
2. The message will be encrypted using the Enigma algorithm.
3. Enter the encrypted text again to decrypt it back to the original.
4. Type `exit` to quit.

### Example Session:

```
Enter a message to encrypt/decrypt (or 'exit' to quit): HELLO
Output: KANPR

Enter a message to encrypt/decrypt (or 'exit' to quit): KANPR
Output: HELLO
```

## Configuration

You can modify the Enigma machine's behavior by adjusting:

- **Rotors** (`rotor1`, `rotor2`, `rotor3` in `main()`)
- **Reflector wiring** (`reflector`)
- **Plugboard settings** (`plugboard` dictionary)

## Contribution

Feel free to **fork** this repository and submit a **pull request** for improvements! Some ideas:

- Add more rotor types
- Implement multiple reflectors
- GUI interface for better usability

## License

This project is licensed under the **MIT License**.

---

💡 **Fun Fact:** The real Enigma Machine was famously cracked by **Alan Turing** and his team at Bletchley Park, significantly shortening WWII!
```

---
import string
import itertools

class Rotor:
    def __init__(self, wiring, notch, ring_setting=0, position=0):
        """Initialize a rotor with specific wiring, notch position, ring setting, and initial position.
        - wiring: Defines how letters are mapped inside the rotor.
        - notch: Determines when the next rotor should step.
        - ring_setting: Offsets the internal wiring to modify encryption.
        - position: The starting position of the rotor."""
        self.alphabet = string.ascii_uppercase
        self.wiring = wiring
        self.notch = notch
        self.ring_setting = ring_setting
        self.position = position
    
    def encipher(self, char, forward=True):
        """Encipher a character by passing it through the rotor.
        - forward: If True, enciphers from right to left (entry to reflector).
          If False, it goes in reverse (left to right on return journey)."""
        idx = (self.alphabet.index(char) + self.position - self.ring_setting) % 26
        if forward:
            translated = self.wiring[idx]
        else:
            translated = self.alphabet[self.wiring.index(self.alphabet[idx])]
        return self.alphabet[(self.alphabet.index(translated) - self.position + self.ring_setting) % 26]
    
    def step(self):
        """Advance the rotor by one position. If the rotor reaches its notch position,
        return True to indicate that the next rotor should step as well."""
        self.position = (self.position + 1) % 26
        return self.alphabet[self.position] in self.notch

class Reflector:
    def __init__(self, wiring):
        """Initialize the reflector, which maps input letters to different output letters.
        Unlike rotors, the reflector does not rotate, and it always reflects a letter 
        in a fixed manner."""
        self.alphabet = string.ascii_uppercase
        self.wiring = wiring  # Fixed bidirectional wiring
    
    def reflect(self, char):
        """Reflect a character based on predefined wiring."""
        return self.wiring[self.alphabet.index(char)]

class Enigma:
    def __init__(self, rotors, reflector, plugboard={}):
        """Initialize the Enigma machine with a set of rotors, a reflector, and an optional plugboard."""
        self.rotors = rotors
        self.reflector = reflector
        self.plugboard = plugboard
    
    def swap_plugboard(self, char):
        """Swap characters using the plugboard configuration before and after rotor passage."""
        return self.plugboard.get(char, char)
    
    def encipher(self, message):
        """Encrypt or decrypt a message using the Enigma machine logic."""
        ciphertext = ""
        for char in message.upper():
            if char not in string.ascii_uppercase:
                ciphertext += char
                continue
            
            step_next = True
            for rotor in self.rotors:
                if step_next:
                    step_next = rotor.step()
                else:
                    break
            
            char = self.swap_plugboard(char)
            
            for rotor in reversed(self.rotors):
                char = rotor.encipher(char, forward=True)
            
            char = self.reflector.reflect(char)
            
            for rotor in self.rotors:
                char = rotor.encipher(char, forward=False)
            
            char = self.swap_plugboard(char)
            
            ciphertext += char
        return ciphertext

# Interactive command-line interface
def main():
    rotor1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
    rotor2 = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
    rotor3 = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
    reflector = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
    plugboard = {"A": "Z", "Z": "A"}  # Example plugboard settings

    enigma = Enigma([rotor1, rotor2, rotor3], reflector, plugboard)
    
    while True:
        user_input = input("Enter a message to encrypt/decrypt (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        encrypted_message = enigma.encipher(user_input)
        print("Output:", encrypted_message)

if __name__ == "__main__":
    main()
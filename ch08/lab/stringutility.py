class StringUtility:
    def __init__(self, input_string):
        self.input_string = input_string

    def display_string(self):
        print(self.input_string)

    def __str__(self):
        return f"StringUtility: {self.input_string}"

    def vowels(self):
        vowel_count = sum(1 for char in self.input_string if char.lower() in 'aeiou')
        if vowel_count < 5:
            return str(vowel_count)
        else:
            return "many"

    def bothEnds(self):
        if len(self.input_string) <= 2:
            return self.input_string
        else:
            return self.input_string[:2] + self.input_string[-2:]

    def fixStart(self):
        if len(self.input_string) <= 1:
            return self.input_string
        else:
            first_char = self.input_string[0]
            modified_string = first_char + self.input_string[1:].replace(first_char, '*')
            return modified_string

    def asciiSum(self):
        return sum(ord(char) for char in self.input_string)

    def cipher(self):
        shift = len(self.input_string)
        encoded_string = ''.join(
            chr((ord(char) - ord('a' if char.islower() else 'A') + shift) % 26 + ord('a' if char.islower() else 'A'))
            if char.isalpha() else char
            for char in self.input_string)

        return encoded_string

import subprocess
import json as js

class Correction():
    def __init__(self, text, full_json):
        self.text = text
        self.full_json = full_json
        self.output = None
        self.parsed = None
        self.json = None
        self.errors = []
    
    def get_correction(self):
        output = subprocess.check_output(["curl", "-d", self.text, "-d", "language=auto", "https://api.languagetool.org/v2/check"])
        parsed = js.loads(output)
        json = js.dumps(parsed, indent=4, sort_keys=True)
        self.output, self.parsed, self.json = output, parsed, json

    def display_correction(self):
        if self.full_json:
            print('Full JSON: ')
            print(self.json)
            print('#############')
    
    def get_errors(self):
        for match in self.parsed['matches']:
            length = match['length']
            offset = match['offset']
            value = match['replacements'][0]['value']
            self.errors.append(self.Error(length, offset, value))
    
    def display_errors(self):
        print('Sentence: ', self.text[5:])
        print('Errors detected: ')
        for error in self.errors:
            print('length: ',error.length)
            print('offset: ',error.offset)
            print('value of replacement: '+error.value)
            print('#############')

    class Error():
        def __init__(self, length, offset, value):
            self.length = length
            self.offset = offset
            self.value = value
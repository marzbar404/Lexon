import re
import sys

class Lexon:
    def __init__(self):
        self.variables = {}
        self.commands = []
        self._register_core_commands()

    def _register_core_commands(self):
        self.commands.append((re.compile(r'^say "(.*)"$'), self._cmd_say))
        self.commands.append((re.compile(r'^remember (\w+) is "(.*)"$'), self._cmd_remember))
        self.commands.append((re.compile(r'^recall (\w+)$'), self._cmd_recall))
        self.commands.append((re.compile(r'^ask "(.*)" as (\w+)$'), self._cmd_ask))

    def _cmd_say(self, match):
        print(match.group(1))

    def _cmd_remember(self, match):
        var, value = match.groups()
        self.variables[var] = value

    def _cmd_recall(self, match):
        var = match.group(1)
        if var in self.variables:
            print(self.variables[var])
        else:
            print(f"Lexon: I don’t have anything saved as '{var}'.")

    def _cmd_ask(self, match):
        question, var = match.groups()
        answer = input(question + " ")
        self.variables[var] = answer

    def execute(self, line):
        line = line.strip()
        if not line:
            return
        for regex, handler in self.commands:
            m = regex.match(line)
            if m:
                handler(m)
                return
        print(f"Lexon: I didn’t quite catch that → {line}")

def main():
    lang = Lexon()
    for line in sys.stdin:
        lang.execute(line)

if __name__ == "__main__":
    main()






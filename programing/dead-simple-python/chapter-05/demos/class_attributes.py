class Nutrimatic:
    output = 'Something almost, but not quite, entirely unlike tea.'
    
    def request(self, beverage):
        return self.output
    
machine = Nutrimatic()
mug = machine.request('Tea')
print(mug)      # Something almost, but not quite, entirely unlike tea.

print(machine.output)       # Something almost, but not quite, entirely unlike tea.
print(Nutrimatic.output)    # Something almost, but not quite, entirely unlike tea.
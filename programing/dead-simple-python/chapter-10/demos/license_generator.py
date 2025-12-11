from itertools import product
from string import ascii_uppercase as alphabet

def gen_license_plates():
    for letters in product(alphabet, repeat=3):
        letters = ''.join(letters)
        if letters == 'GOV':
            continue
        
        for number in range(1000):
            yield f"{letters} {number:03}"
            
            
license_plates = gen_license_plates()

registrations = {}

def new_registration(owner):
    if owner not in registrations:
        plate = next(license_plates)
        registrations[owner] = plate
        return plate
    else:
        return None

skip_total = (6 * 26 * 26 * 1000) + (14 * 26 * 1000) + (21 * 1000)
for _ in range(skip_total):
    next(license_plates)
print(next(license_plates))
nearby_properties = {
    "N. Anywhere Ave.": {
        123: 156_852,
        124: 157_923,
        126: 163_821,
        127: 133_121,
        128: 166_356
    },
    "N. Everywhere St.": {
        4567: 175_753,
        4568: 166_212,
        4569: 185_123
    }
}

real_estate_listings = open('listings.txt', 'w')
real_estate_listings.__enter__()
try:
    for street, properties in nearby_properties.items():
        for address, value in properties.items():
            print(street, address, f"${value:,}", sep=' | ', file=real_estate_listings)
finally:
    real_estate_listings.__exit__()
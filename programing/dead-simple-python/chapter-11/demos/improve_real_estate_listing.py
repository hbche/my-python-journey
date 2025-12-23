with open('78SomewhereRd.txt', 'r+') as real_estate_listing:
    contents = []
    for line in real_estate_listing:
        line = line.replace("Tiny", "Cozy")
        line = line.replace("Needs repairs", "Full of potential")
        line = line.replace("Small", "Compact")
        line = line.replace("old storage shed", "datached workshop")
        line = line.replace("Built on ancient burial ground.", "Unique atmosphere.")
        contents.append(line)
    
    real_estate_listing.seek(0)
    real_estate_listing.writelines(contents)
    real_estate_listing.truncate()
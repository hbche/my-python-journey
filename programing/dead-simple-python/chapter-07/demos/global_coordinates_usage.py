from global_coordinates import GlobalCoordinates

nostarch = GlobalCoordinates(latitude=(37, 46, 32.6, "N"), longitude=(122, 24, 39.4, "W"))

psf = GlobalCoordinates(latitude=(45, 27, 7.7, "N"), longitude=(122, 47, 30.2, "W"))

distance = nostarch(psf)
print(distance)     # 852.6857266443297
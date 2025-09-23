import math

class GlobalCoordinates:
    
    def __init__(self, *, latitude, longitude):
        
        self._lat_deg = latitude[0]
        self._lat_min = latitude[1]
        self._lat_sec = latitude[2]
        self._lat_dir = latitude[3]
        
        self._lon_deg = longitude[0]
        self._lon_min = longitude[1]
        self._lon_sec = longitude[2]
        self._lon_dir = longitude[3]
        
    @staticmethod
    def degree_from_decimal(dec, *, lat):
        if lat:
            direction = "S" if dec < 0 else "N"
        else:
            direction = "W" if dec < 0 else "E"
        dec = abs(dec)
        degrees = int(dec)
        dec -= degrees
        minutes = int(dec * 60)
        dec -= minutes / 60
        seconds = round(dec * 3600, 1)
        return (degrees, minutes, seconds, direction)
    
    @staticmethod
    def decimal_from_degrees(degrees, minutes, seconds, direction):
        dec = degrees + minutes/60 + seconds / 3600
        if direction == 'S' or direction == 'W':
            dec = -dec
        return round(dec, 6)
    
    @property
    def latitude(self):
        return self.decimal_from_degrees(self._lat_deg, self._lat_min, self._lat_sec, self._lat_dir)
    
    @property
    def longitude(self):
        return self.decimal_from_degrees(self._lon_deg, self._lon_min, self._lon_sec, self._lon_dir)
    
    def __repr__(self):
        return (
            f"<GlobalCoordinates lat={self._lat_deg}° {self._lat_min}′ {self._lat_sec}″ \\ {self._lat_dir} lon={self._lon_deg}° {self._lon_min}′ {self._lon_sec}″ \\ {self._lon_dir}>"    
        )
        
    def __str__(self):
        return (
            f"lat={self._lat_deg}° {self._lat_min}′ {self._lat_sec}″ \\ {self._lat_dir} lon={self._lon_deg}° {self._lon_min}′ {self._lon_sec}″ \\ {self._lon_dir}"
        )
    
    def __hash__(self):
        return hash((self._lat_deg, self._lat_min, self._lat_sec, self._lat_dir, self._lon_deg, self._lon_min, self._lon_sec, self._lon_dir))
    
    def __invert__(self):
        # 实现取反运算符
        return GlobalCoordinates(latitude=self.degree_from_decimal(-self.latitude, lat=True), longitude=self.degree_from_decimal(-self.longitude, lat=False))
    
    def __call__(self, other):
        EARTH_RADIUS_KM = 6371
        distance_lat = math.radians(other.latitude - self.latitude)
        distance_lon = math.radians(other.longitude - self.longitude)
        lat = math.radians(self.latitude)
        lon = math.radians(self.longitude)
        a = (
            math.sin(distance_lat / 2) *
            math.sin(distance_lat / 2) +
            math.sin(distance_lon) *
            math.sin(distance_lon / 2) * 
            math.cos(lat) *
            math.cos(lon)
        )
        c = 2 *  math.atan2(math.sqrt(a), math.sqrt(1-a))

        return c * EARTH_RADIUS_KM
def formatted_city_country(city, country, population=0):
    """测试存储城市和国家"""
    if population:
        formatted_content = f"{city.title()}, {country.title()} - population {population}"
    else:
        formatted_content = f"{city.title()}, {country.title()}"
    return formatted_content
def city_info2(city_name, country_name, population=0):
    info = f"{city_name} , {country_name}"
    if population:
        info += f" - population {population}"
    return info.title()

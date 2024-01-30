from suntime import Sun

if __name__ == "__main__":
    # TODO
    latitude = 38.7077507
    longitude = -9.1365919

    sun = Sun(latitude, longitude)

    print(sun.get_sunrise_time(), sun.get_sunset_time())

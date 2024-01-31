from datetime import date, timedelta

import geocoder
from suntime import Sun

PLACES = ["Lisboa", "Redondo", "Alvito"]
TODAY = date.today()

# TODO: Use print utility package constant
EXTRA_NL = "\n" * 2


# TODO: Use print utility package function
def line_break(skip=False):
    n_lines = 0 if skip else 2
    lines = "\n" * n_lines

    print(sep=None, end=lines)


if __name__ == "__main__":
    for index, place in enumerate(PLACES, start=1):
        osm_data = geocoder.osm(place)
        sun = Sun(lat=osm_data.lat, lon=osm_data.lng)

        print(
            osm_data.address,
            {"Longitude": osm_data.lng, "Latitude": osm_data.lat},
            end=EXTRA_NL,
        )

        for n_days in range(0, 3):
            delta = timedelta(days=n_days)
            updated_dt = TODAY + delta

            # sunrise = sun.get_local_sunrise_time(date=updated_dt)
            sunrise = sun.get_sunrise_time(date=updated_dt)

            # sunset = sun.get_local_sunset_time(date=updated_dt)
            sunset = sun.get_sunset_time(date=updated_dt)

            print(sunrise, sunset)

        is_last = index == len(PLACES)
        line_break(skip=is_last)

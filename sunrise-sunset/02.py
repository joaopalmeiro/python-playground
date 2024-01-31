from datetime import datetime

import ephem

if __name__ == "__main__":
    # https://github.com/brandon-rhodes/pyephem/blob/4.1.5/ephem/cities.py#L16
    # https://github.com/brandon-rhodes/pyephem/blob/4.1.5/ephem/cities.py#L141
    lisbon_data = ephem.city("Lisbon")

    lisbon = ephem.Observer()
    sun = ephem.Sun()

    lisbon.lat = lisbon_data.lat
    lisbon.lon = lisbon_data.lon
    lisbon.date = datetime.now()

    print(ephem.localtime(lisbon.next_rising(sun)))
    print(ephem.localtime(lisbon.next_setting(sun)))

    print(lisbon.next_rising(sun))
    print(lisbon.next_setting(sun))

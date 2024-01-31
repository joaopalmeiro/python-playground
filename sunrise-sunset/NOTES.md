# Notes

- https://github.com/SatAgro/suntime
- https://pypi.org/project/suntime/
- https://geocoder.readthedocs.io/api.html#installation
- https://github.com/DenisCarriere/geocoder
- https://github.com/DenisCarriere/geocoder/issues/466
- https://github.com/DenisCarriere/geocoder/blob/39b9999ec70e61da9fa52fe9fe82a261ad70fa8b/geocoder/api.py#L451
- https://github.com/DenisCarriere/geocoder/blob/39b9999ec70e61da9fa52fe9fe82a261ad70fa8b/geocoder/api.py#L179
- https://github.com/DenisCarriere/geocoder/blob/39b9999ec70e61da9fa52fe9fe82a261ad70fa8b/geocoder/osm.py#L306
- https://github.com/DenisCarriere/geocoder/blob/39b9999ec70e61da9fa52fe9fe82a261ad70fa8b/geocoder/base.py#L38
- https://nominatim.org/release-docs/latest/api/Search/
- https://github.com/osm-search/Nominatim
- https://geocoder.readthedocs.io/providers/OpenStreetMap.html
- https://github.com/sffjunkie/astral
- https://nominatim.openstreetmap.org/search?q=Lisboa&format=json&limit=1
- https://nominatim.openstreetmap.org/search?q=Redondo&format=json&limit=1
- https://sunrisewhen.com/
- https://wego.here.com/
- https://tabuademares.com/pt/lisboa/lisboa/previsao/saida-por-sol
- https://docs.python.org/3.10/library/datetime.html#date-objects
- https://docs.python.org/3.10/library/datetime.html#datetime.timedelta
- https://docs.mapbox.com/help/glossary/lat-lon/
- https://observablehq.com/@clhenrick/lat-lon-or-lon-lat
- https://macwright.com/lonlat/
- https://github.com/doniseferi/suntimes
- https://www.npmjs.com/package/suncalc
- https://github.com/mourner/suncalc
- https://github.com/dateutil/dateutil
- https://github.com/SatAgro/suntime/blob/v1.2.5/suntime/suntime.py#L180: `return datetime.datetime(year, month, day, hr, int(min), tzinfo=tz.tzutc())`
- https://dateutil.readthedocs.io/en/stable/tz.html#dateutil.tz.tzutc
- https://developer.mozilla.org/en-US/docs/Web/HTML/Element/br
- https://switowski.com/blog/checking-for-true-or-false/:
  - "To check if a variable is equal to True/False (and you don't have to distinguish between `True`/`False` and truthy/falsy values), use `if variable` or `if not variable`."
  - If you want to check that a variable is explicitly True or False (and is not truthy/falsy), use `is` (`if variable is True`).
- https://open-meteo.com/
- https://open-meteo.com/en/docs
- https://open-meteo.com/en/docs#hourly=&daily=sunrise,sunset&timezone=Europe%2FLondon
- https://github.com/requests-cache/requests-cache
- https://gist.github.com/scivision/228cad3ee5efe74dd5230ddb19bf36fe
- https://github.com/brandon-rhodes/pyephem
- https://rhodesmill.org/pyephem/tutorial#computations-for-particular-observers
- https://rhodesmill.org/pyephem/quick.html#observers: "Describes a position on Earth's surface."
- https://rhodesmill.org/pyephem/quick.html#transit-rising-and-setting
- https://rhodesmill.org/pyephem/quick.html#bodies
- https://rhodesmill.org/pyephem/quick.html#dates
- https://docs.python.org/3.10/library/zoneinfo.html

## Commands

```bash
pipenv install --skip-lock suntime==1.2.5 geocoder==1.38.1 ephem==4.1.5 && pipenv install --dev --skip-lock ruff==0.1.11 codespell==2.2.6
```

```bash
pipenv --rm
```

```bash
pipenv run codespell --help
```

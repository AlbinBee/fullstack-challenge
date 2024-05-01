import requests

def fetch_countries_data():
    url = "https://gist.githubusercontent.com/ofou/df09a6834a8421b4f376c875194915c9/raw/"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data. Status code: {response.status_code}")

    data_lines = response.text.splitlines()
    if len(data_lines) <= 1:
        raise Exception("No data found in the response.")

    countries_data = []
    id_counter = 1
    for line in data_lines[1:]:
        parts = line.split(",")
        if len(parts) != 6:
            continue

        country_data = {
            "id": id_counter,
            "country": parts[0].strip(),
            "capital": parts[1].strip(),
            "latitude": float(parts[2].strip()),
            "longitude": float(parts[3].strip()),
            "population": int(parts[4].strip()),
            "capital_type": parts[5].strip()
        }
        countries_data.append(country_data)
        id_counter += 1

    # I had to add my country :)
    kosovo_data = {
        "id": id_counter,
        "country": "Kosovo",
        "capital": "Pristina",
        "latitude": 42.666667,
        "longitude": 21.166667,
        "population": 1795000,
        "capital_type": "Capital"
    }
    countries_data.append(kosovo_data)

    return countries_data
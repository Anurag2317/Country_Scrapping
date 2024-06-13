from django.shortcuts import render
import requests, re
from countryapp.models import Country


def get_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")
        return None


def display(req):
    url = "https://countrycode.org/"
    content = get_content(url)
    if not content:
        error = "Failed to fetch data from the website."
        context = {"error": error}
        return render(req, "error.html", context)

    # Regular expressions for scraping data
    country_pattern = re.compile(r'<td><a href="(/.*?)">(.*?)</a></td>')
    code_pattern = re.compile(r"<td>(\d+)</td>")
    iso_pattern = re.compile(r"<td>([A-Z]{2} / [A-Z]{3})</td>")
    population_pattern = re.compile(r"<td>([\d,]+)</td>")
    area_pattern = re.compile(r"<td>([\d,]+)</td>")
    gdp_pattern = re.compile(r"<td>(.*?)</td>")

    countries = country_pattern.findall(content)
    codes = code_pattern.findall(content)
    isos = iso_pattern.findall(content)
    populations = population_pattern.findall(content)
    areas = area_pattern.findall(content)
    gdps = gdp_pattern.findall(content)

    data = []

    for i in range(len(countries)):
        country_url, country_name = countries[i]
        country_code = codes[i]
        iso_code = isos[i]
        population = populations[i]
        area = areas[i]
        gdp = gdps[i]

        country_url = f"https://countrycode.org{country_url}"
        capital = "N/A"

        html = get_content(country_url)
        if html:
            capital_pattern = re.compile(r"<td>Capital:</td>\s*<td>(.*?)</td>")
            capital_match = capital_pattern.search(html)
            if capital_match:
                capital = capital_match.group(1).strip()

        # Create or update the Country object
        Country.objects.update_or_create(
            country_name=country_name,
            defaults={
                "country_code": country_code,
                "iso_codes": iso_code,
                "population": population.replace(",", ""),
                "area_km2": area.replace(",", ""),
                "gdp_usd": gdp.replace(",", ""),
                "capital": capital,
            },
        )

        data.append(
            {
                "Sr": i + 1,
                "COUNTRY": country_name,
                "COUNTRY CODE": country_code,
                "ISO CODES": iso_code,
                "POPULATION": population,
                "AREA KM2": area,
                "GDP $USD": gdp,
                "Capital": capital,
            }
        )

    context = {"data": data}
    return render(req, "scraper.html", context)

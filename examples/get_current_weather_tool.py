import json
from typing import Optional, Union
from urllib.parse import quote

import requests

from hot_tool import HotTool


class GetCurrentWeatherTool(HotTool):
    def run(
        self, arguments: Optional[str] = None, context: Optional[str] = None
    ) -> str:
        default_city_name = "New York"
        city_name: Union[str, None] = None

        try:
            args = json.loads(arguments or "{}")
            if not isinstance(args, dict):
                raise ValueError("Arguments is invalid")

            city_name = (
                args.get("city_name")
                or args.get("city")
                or args.get("location")
                or None
            )
        except Exception as e:
            print(f"Error: {type(e).__name__}: {e}")

        if city_name is None:
            print("Can not get city of client, try use server location as default")
            response = requests.get("http://ip-api.com/json/", timeout=5)
            try:
                response.raise_for_status()
                data = response.json()
                if data["status"] == "success":
                    city_name = data["city"]
                else:
                    print(f"Error: {data}")
            except requests.RequestException as e:
                print(f"Error: {type(e).__name__}: {e}")
        else:
            print(f"Use client provided city name: {city_name}")

        if city_name is None:
            print(
                "Can not get server location, "
                + f"use default city name: {default_city_name}"
            )
            city_name = default_city_name
        else:
            print(f"Use server city name: {city_name}")

        safe_city_name = quote(city_name)
        query_params = {"format": "3"}
        base_url = f"https://wttr.in/{safe_city_name}"
        response = requests.get(base_url, params=query_params, timeout=5)
        try:
            response.raise_for_status()
            output = response.text.strip()
        except Exception as e:
            print(f"Error: {type(e).__name__}: {e}")
            output = "Can not get current weather information, please try again later."

        return output

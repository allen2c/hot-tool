from typing import Optional

import requests

from hot_tool import HotTool


class GetMyIpTool(HotTool):
    def run(
        self, arguments: Optional[str] = None, context: Optional[str] = None
    ) -> str:
        response = requests.get("https://ifconfig.me")
        try:
            response.raise_for_status()
            return response.text.strip()
        except Exception as e:
            print(f"Error: {type(e).__name__}: {e}")
            return "Can not get my IP, please try again later."

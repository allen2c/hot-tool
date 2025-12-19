"""
hot-tool build examples/get_my_ip.py
"""

from typing import Optional

import requests

from hot_tool import FunctionDefinition, HotTool


class GetMyIpTool(HotTool):
    def function_definition(self) -> FunctionDefinition:
        return {
            "name": "get_my_ip",
            "description": "Get my IP address",
            "parameters": {},
        }

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

"""
hot-tool build examples/hello_world.py
"""

from typing import Optional

from hot_tool import FunctionDefinition, HotTool


class HelloWorldTool(HotTool):
    def function_definition(self) -> FunctionDefinition:
        return {
            "name": "hello_world",
            "description": "Say hello to the world",
            "parameters": {},
        }

    def run(
        self, arguments: Optional[str] = None, context: Optional[str] = None
    ) -> str:
        return "Hello, World!"

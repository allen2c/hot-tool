# Hot-Tool

[![PyPI version](https://img.shields.io/pypi/v/hot-tool.svg)](https://pypi.org/project/hot-tool/)
[![Python Version](https://img.shields.io/pypi/pyversions/hot-tool.svg)](https://pypi.org/project/hot-tool/)
[![License](https://img.shields.io/pypi/l/hot-tool.svg)](https://opensource.org/licenses/MIT)

Hot-Tool is a library for creating hot-pluggable tools for LLM.

## Features

## Installation

## Quick Start

### Define Hot Tool

```python
# get_my_ip.py
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
```

### Run Programmatically

```python
# main.py
from get_my_ip import GetMyIpTool
from hot_tool.run import run_tool

print(run_tool(GetMyIpTool))
# 198.51.100.156
```

### Build Standalone Executable and Run as Executable

```shell
hot-tool build get_my_ip.py -o get_my_ip
# Starting Nuitka compilation...
# ...
# Nuitka-Plugins:upx: Compressing 'get_my_ip'.
# Nuitka: Successfully created 'get_my_ip'.
# Compilation completed successfully.
# Standalone script saved to '/Users/me/path/to/get_my_ip'
```

```shell
./get_my_ip
# 198.51.100.156
```

### Basic Usage

## Configuration

## License

MIT License

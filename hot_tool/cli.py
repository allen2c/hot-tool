"""
# `hot-tool` CLI.

## Build

```shell
hot-tool build -o script script.py

`-o, --output`: Output standalone script file path. Default is stem of input script.

```

## Run

"""

import argparse
from pathlib import Path


def main():
    import subprocess
    import sys
    from tempfile import NamedTemporaryFile

    from hot_tool.run import make_script_runnable

    parser = argparse.ArgumentParser(description="HotTool CLI")
    parser.add_argument("script", help="Input script file path")
    parser.add_argument("-o", "--output", help="Output standalone script file path")

    args = parser.parse_args()

    script_filepath = Path(args.script)
    if not script_filepath.is_file():
        raise FileNotFoundError(f"Script file not found: {script_filepath}")

    if args.output is None:
        output_filepath = script_filepath.parent.joinpath(script_filepath.stem)
    else:
        output_filepath = Path(args.output)
    output_filepath.parent.mkdir(parents=True, exist_ok=True)

    with NamedTemporaryFile() as temp_file:
        temp_file.write(
            make_script_runnable(script_filepath.read_text()).encode("utf-8")
        )
        temp_file.flush()
        temp_file.seek(0)

        command = [
            sys.executable,
            "-m",
            "nuitka",
            "--standalone",
            "--onefile",
            "--plugin-enable=upx",
            "--output-dir=.",
            "--remove-output",
            "-o",
            str(output_filepath),
            temp_file.name,
        ]

        try:
            print("Starting Nuitka compilation...")
            subprocess.check_call(command)
            print("Compilation completed successfully.")

        except subprocess.CalledProcessError as e:
            print(f"Compilation failed with return code {e.returncode}")
        except FileNotFoundError:
            print("Error: Nuitka or Python interpreter not found.")

        print(f"Standalone script saved to '{output_filepath.resolve()}'")

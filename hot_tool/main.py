import argparse
import logging
import sys

import hot_tool

logger = logging.getLogger(__name__)

main_script = """
from hot_tool.main import main

main()
""".strip()


def main():
    subclasses = hot_tool.HotTool.__subclasses__()
    if len(subclasses) == 0:
        raise hot_tool.HotToolImplementationNotFoundError(
            "No implementation found for HotTool."
        )
    elif len(subclasses) > 1:
        raise hot_tool.HotMultipleToolImplementationsFoundError(
            "Multiple implementations found for HotTool, "
            + "only one in script is allowed."
        )

    subclass_cls = subclasses[0]

    parser = argparse.ArgumentParser(description="")
    parser.add_argument(
        "--arguments",
        type=str,
        default=None,
        help="Arguments for the tool. default is None.",
    )
    parser.add_argument(
        "--context",
        type=str,
        default=None,
        help="Context for the tool. default is None.",
    )
    args = parser.parse_args()

    try:
        result = subclass_cls().run(arguments=args.arguments, context=args.context)
        logger.info(f"Tool result: {str(result)[:100]}")
        print(result)

    except Exception as e:
        logger.exception(e)
        logger.error(f"Error running tool: {e}")
        sys.exit(1)

    return None

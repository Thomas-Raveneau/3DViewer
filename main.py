##
# KEIMYUNG PROJECT, 2021
# 3DViewer
# File description:
# main
##

# --- IMPORTS ---

from src.Core.Core import Core
import sys

# ---------------


def main() -> int:
    if (len(sys.argv) > 1):
        core: Core = Core(sys.argv[1])
    else:
        core: Core = Core();
    core.run()

    return 0


if __name__ == '__main__':
    main()

##
# KEIMYUNG PROJECT, 2021
# 3DViewer
# File description:
# main
##

# --- IMPORTS ---

from src.Core.Core import Core

# ---------------


def main() -> int:
    
    core: Core = Core()

    core.run()

    return 0


if __name__ == '__main__':
    main()

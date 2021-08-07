from pathlib import Path
from typing import Dict

from numpy import absolute

env = {}


def add_path_env():

    # ROOT = Path(__file__).resolve().parent
    # DATA = ROOT / "data"
    # SCRIPTS = ROOT / "scripts"
    # DOTENV = ROOT / ".env"

    # env["PATHS] = []

    env["ROOT"] = Path(__file__).resolve().parent.parent
    env["DATA"] = env["ROOT"] / "data"
    env["SCRIPTS"] = env["ROOT"] / "scripts"
    env["DOTENV"] = env["ROOT"] / ".env"


def add_to_env(path: Path):
    pass


def export_dotenv():
    with open(env["DOTENV"], mode="w") as dotenv:
        for key in env:
            # lines = f.read().splitlines()
            # last_line = lines[-1]
            dotenv.write(f"{key}={env[key]}")
            dotenv.write("\n")
            # if type(env[key]) == Path:
            #     ENV.writelines(env[key].as_posix())
            # else:
            #     ENV.writelines(env[key])


def main() -> None:
    """Main function."""
    env = {}
    add_path_env()
    export_dotenv()


if __name__ == "__main__":
    main()

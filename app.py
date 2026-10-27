
import json
import os


def load_config():
    config = os.getenv("APP_CONFIG", "{}")
    return json.loads(config)


def main():
    config = load_config()
    print("RelixQ compatibility test")
    print(f"Config keys: {list(config.keys())}")


if __name__ == "__main__":
    main()

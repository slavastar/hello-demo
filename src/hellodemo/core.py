def say_hello(name: str = "world") -> str:
    return f"Hello, {name}!"


def main() -> None:
    # CLI entry point
    import argparse
    parser = argparse.ArgumentParser(description="Say hello from hello-demo-pkg.")
    parser.add_argument("-n", "--name", default="world", help="Name to greet")
    args = parser.parse_args()
    print(say_hello(args.name))
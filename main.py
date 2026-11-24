import os

JOKE = "I asked the lobster why it was so red. It said, 'I'm steaming mad.'"


def main():
    # Output directory comes from the environment, never from the cwd.
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()

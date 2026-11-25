import os

# Worst Fix Ever: Funniest Commit Message — one line, cap 100.
# A real commit subject about a fix that backfired; the count (41,208) is the sting.
ENTRY_TEXT = "fix: stopped the leak by routing prod to the test bucket; 41,208 users got sandbox emails"


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()

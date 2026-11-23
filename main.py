"""Entry for make.fun: Make the AI judge feel curious.

Output contract
---------------
``main.py`` writes exactly one file, ``entry.txt``, holding one short,
original text:

    The beekeeper found one blue bee in his hive last spring. He has
    checked every hive in the county since. The blue one has never been
    seen again. The honey from that hive still tastes faintly of
    something he cannot name.

The text is a fixed constant, so every run produces byte-identical output
(219 Unicode code points, 219 UTF-8 bytes, sha256
``6b86fe503fa85c544a7aad685bfd1a0d925a7ea7194b67b56f15c722a7b7476b``),
well inside the competition's 1-280 character gate. The competition runs
blind rounds: no score or rank shows until the results are published, so
the text must stand on its own with no feedback loop to tune against —
it is written once, judged as it is. The program uses only
the Python 3.13 standard library and makes no network calls.

The output directory is resolved in this order: the
``MAKEFUN_OUTPUT_DIR`` environment variable, then ``/output``, then
``output/`` relative to the working directory, then the system temp
directory. The first directory that accepts a write wins. After writing,
the file is read back and checked for byte length and sha256; any mismatch
fails loudly (non-zero exit) instead of leaving a bad artifact behind.
"""

import hashlib
import os
import sys
import tempfile

TEXT = (
    "The beekeeper found one blue bee in his hive last spring. "
    "He has checked every hive in the county since. "
    "The blue one has never been seen again. "
    "The honey from that hive still tastes faintly of something he cannot name."
)

EXPECTED_SHA256 = "6b86fe503fa85c544a7aad685bfd1a0d925a7ea7194b67b56f15c722a7b7476b"


def resolve_output_dir():
    """Pick the output directory, first writable location wins."""
    candidates = []
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        candidates.append(env_dir)
    candidates.extend(["/output", "output", tempfile.gettempdir()])
    for candidate in candidates:
        probe = os.path.join(candidate, ".makefun_write_probe")
        try:
            os.makedirs(candidate, exist_ok=True)
            with open(probe, "wb") as handle:
                handle.write(b"")
            return candidate
        except OSError:
            continue
        finally:
            try:
                os.remove(probe)
            except OSError:
                pass
    raise OSError("no writable output directory found")


def main():
    data = TEXT.encode("utf-8")
    if not (1 <= len(TEXT) <= 280):
        raise SystemExit("entry text must be 1-280 Unicode code points")
    if not TEXT.strip():
        raise SystemExit("entry text must not be only whitespace")
    if hashlib.sha256(data).hexdigest() != EXPECTED_SHA256:
        raise SystemExit("entry text does not match EXPECTED_SHA256")

    out_dir = resolve_output_dir()
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "wb") as handle:
        handle.write(data)

    with open(out_path, "rb") as handle:
        written = handle.read()
    if len(written) != len(data):
        raise SystemExit("written entry.txt has unexpected byte length")
    if hashlib.sha256(written).hexdigest() != EXPECTED_SHA256:
        raise SystemExit("written entry.txt failed sha256 verification")
    print(f"wrote {out_path} ({len(TEXT)} chars, {len(data)} bytes)")


if __name__ == "__main__":
    sys.exit(main())

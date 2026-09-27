import argparse
import sys
from caesar import encrypt_cesar, decrypt_cesar
from affine import encrypt_affine, decrypt_affine, check_a_affine
from monoalpha import encrypt_mono, decrypt_mono, key_from_keyword_affine
from vigenere import encrypt_vigenere, decrypt_vigenere, cosets
from break_caesar import break_caesar, chi_squared
from break_affine import break_affine
from break_vigenere import break_vigenere
from frequencies import LETTER_FREQUENCIES


def build_parser():
    parser = argparse.ArgumentParser(prog="crypto.py", description="Cryptography command-line tool")
    ciphers = parser.add_subparsers(dest="cipher", required=True)

    # aaesar
    caesar = ciphers.add_parser("caesar")
    modes = caesar.add_subparsers(dest="mode", required=True)

    for mode in ("encrypt", "decrypt"):
        p = modes.add_parser(mode)
        p.add_argument("--key", type=int, required=True)
        p.add_argument("--in", dest="input_file")
        p.add_argument("--out", dest="output_file")
        p.add_argument("--lang", choices=["en", "es"])

    # affine
    affine = ciphers.add_parser("affine")
    modes = affine.add_subparsers(dest="mode", required=True)

    for mode in ("encrypt", "decrypt"):
        p = modes.add_parser(mode)
        p.add_argument("--a", type=int, required=True)
        p.add_argument("--b", type=int, required=True)
        p.add_argument("--in", dest="input_file")
        p.add_argument("--out", dest="output_file")
        p.add_argument("--lang", choices=["en", "es"])

    # monoalphabetic
    mono = ciphers.add_parser("mono")
    modes = mono.add_subparsers(dest="mode", required=True)

    for mode in ("encrypt", "decrypt"):
        p = modes.add_parser(mode)
        p.add_argument("--keyword", required=True)
        p.add_argument("--in", dest="input_file")
        p.add_argument("--out", dest="output_file")
        p.add_argument("--lang", choices=["en", "es"])

    # vigenere
    vigenere = ciphers.add_parser("vigenere")
    modes = vigenere.add_subparsers(dest="mode", required=True)

    for mode in ("encrypt", "decrypt"):
        p = modes.add_parser(mode)
        p.add_argument("--key", required=True)
        p.add_argument("--in", dest="input_file")
        p.add_argument("--out", dest="output_file")
        p.add_argument("--lang", choices=["en", "es"])

    # break
    br = ciphers.add_parser("break")
    breaks = br.add_subparsers(dest="break_type", required=True)

    p = breaks.add_parser("caesar")
    p.add_argument("--in", dest="input_file", required=True)
    p.add_argument("--lang", choices=["en", "es"])

    p = breaks.add_parser("affine")
    p.add_argument("--in", dest="input_file", required=True)

    p = breaks.add_parser("vigenere")
    p.add_argument("--m", type=int, required=True)
    p.add_argument("--in", dest="input_file", required=True)

    return parser


def read_input(filename):
    if filename is None:
        return sys.stdin.read()
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def write_output(text, filename):
    if filename is None:
        print(text, end="")
        return
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    parser = build_parser()
    args = parser.parse_args()

    try:
        text = read_input(args.input_file)

        if args.cipher == "caesar":
            if args.mode == "encrypt":
                result = encrypt_cesar(text, args.key)
            else:
                result = decrypt_cesar(text, args.key)

        elif args.cipher == "affine":
            if args.mode == "encrypt":
                result = encrypt_affine(text, args.a, args.b)
            else:
                result = decrypt_affine(text, args.a, args.b)

        elif args.cipher == "mono":
            key = key_from_keyword_affine(args.keyword)

            if args.mode == "encrypt":
                result = encrypt_mono(text, key)
            else:
                result = decrypt_mono(text, key)

        elif args.cipher == "vigenere":
            if args.mode == "encrypt":
                result = encrypt_vigenere(text, args.key)
            else:
                result = decrypt_vigenere(text, args.key)

        elif args.cipher == "break":
            if args.break_type == "caesar":
                result = break_caesar(text, args.lang)
            elif args.break_type == "affine":
                result = break_affine(text)
            elif args.break_type == "vigenere":
                result = break_vigenere(text, args.m)

        elif args.cipher == "assist":
            result = break_caesar(text, "es")

        write_output(result, getattr(args, "output_file", None))

    except OSError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
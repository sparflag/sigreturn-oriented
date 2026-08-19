#!/usr/bin/env python3
"""Sigreturn Oriented — real mini-challenge (sigreturn-oriented)."""
import base64, hashlib, json, os, struct, sys, zlib, wave, io, math, random, re, textwrap
sys.path.insert(0, "/challenge/_shared")
from fetch_material import fetch_material

CHALLENGE_KEY = os.environ.get("CHALLENGE_KEY", 'srop-frame')


def main():
    mat = fetch_material()
    with open("/challenge/flag.enc", "w") as fh:
        fh.write(mat.get("delivery_blob", ""))
    with open("/challenge/srop.frame", "w") as fh:
        fh.write("sigreturn frame (SROP):\n")
        fh.write("  rax = 15 (rt_sigreturn)\n")
        fh.write("  rip = pivot to controlled stack\n")
        fh.write("  rsi = buffer, rdx = len, rdi = 1 (write)\n")
        fh.write(f"frame dumps seed: {CHALLENGE_KEY}\n")
    print("Sigreturn oriented — controlled sigframe in srop.frame.")


if __name__ == "__main__":
    main()

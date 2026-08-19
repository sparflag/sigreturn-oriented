# Sigreturn Oriented (`sigreturn-oriented`)

**Category:** binary exploitation · **Difficulty:** hard · **Points:** 450

No useful gadgets — build a fake sigframe and SROP into a read of the seed.

## Run it

```bash
docker build -t sparflag/sigreturn-oriented .
# `deca-ai start sigreturn-oriented` (or the web UI) prints the docker run line with your
# SPARFLAG_SERVER + SPARFLAG_INSTANCE_TOKEN
```

## Recover the flag

The delivery blob is Fernet ciphertext. Discover the key seed, derive the Fernet key, then decrypt.

The plaintext flag is never written to disk or served — only the encoded delivery blob
is. When you have it:

```bash
deca-ai submit sigreturn-oriented 'sparflag{...}'
```

## Hints

- Set rax to the rt_sigreturn syscall number and pivot to the frame.
- Use the controlled registers to call a write/read of the seed.

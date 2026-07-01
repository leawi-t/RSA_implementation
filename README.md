# Constructing and Deconstructing RSA: The Path to Quantum Cryptography

An exploration of RSA encryption, built and then broken with a classical
period-finding attack

This project was completed as part of an internship training task at iCog.

## Overview

The script demonstrates the full lifecycle of RSA:

1. **Key Generation** — pick two primes `p`, `q`, derive the modulus `N`,
   Euler's totient `φ(N)`, and a public/private exponent pair `(e, d)`.
2. **Encryption & Decryption** — encrypt an integer message with the public
   key `(e, N)` and recover it with the private key `(d, N)`.
3. **The Period-Finding Attack** — a classical brute-force loop that finds
   the period `r` of `a^r ≡ 1 (mod N)` for a random `a` coprime to `N`, then
   uses `gcd(a^(r/2) ± 1, N)` to recover the original primes `p` and `q`.

The classical loop in step 3 is intentionally slow — small primes (< 100)
are used on purpose.

## Files

| File | Description |
|---|---|
| `rsa_attack.py` | Main script: RSA key generation, encryption/decryption, and the classical period-finding attack |

## Requirements

- Python 3.8+ (uses `pow(e, -1, phi_N)` for modular inverse, added in 3.8)
- No external dependencies — only the standard library (`math`, `random`)

## Usage

```bash
python3 rsa_attack.py
```

Running the script will print:
- the generated modulus `N` and totient `φ(N)`
- the public/private key pair
- the ciphertext and successfully decrypted message
- the period `r` found by the brute-force loop
- the prime factors `p`, `q` recovered from the attack

## Example Output

```
N=3233, phi_N=3120
Public key: (17, 3233)
Private key: (2753, 3233)
Ciphertext: 2557
Decrypted message: 42
Found period r: 260
Discovered factors: 61 and 53
```

## Background / Concepts Used

- Modular arithmetic & modular inverses
- Prime numbers, GCD, and coprimality
- Euler's Totient function `φ(N) = (p-1)(q-1)`
- Non-trivial square roots of 1 mod N, and how they expose factors of `N`
  via `gcd(x ± 1, N)`
- Classical period-finding as a brute-force analogue of Shor's Algorithm

## Part of a Larger Task

This repo covers Deliverable 1 (the coding task) of the training assignment.

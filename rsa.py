import math
import random

p = 61
q = 53
N = p * q
phi_N = (p-1) * (q-1)

# choosing an e which is coprime to phi_N
e = 17

#modular inverse
d = pow(e, -1, phi_N)

message = 300

#encryption:
ciphertext = pow(message, e, N)
print(f"This is the cipher text: {ciphertext}")

decrypted_msg = pow(ciphertext, d, N)
print(f"This is the decrypted text: {decrypted_msg}")

# Period finding attack

import math
import random

def find_period(a, N):
    r = 1
    while pow(a, r, N) != 1:
        r += 1
    return r

def period_finding_attack(N, max_tries=20):
    for attempt in range(max_tries):
        a = random.randint(2, N - 2)
        g = math.gcd(a, N)
        if g != 1:
            # lucky accident: a itself shares a factor with N
            print(f"Attempt {attempt+1}: a={a} shares a factor with N directly")
            return g, N // g

        r = find_period(a, N)

        if r % 2 != 0:
            print(f"Attempt {attempt+1}: a={a}, r={r} is odd — retrying")
            continue

        x = pow(a, r // 2, N)
        if x == N - 1:  # trivial square root, x == -1 mod N
            print(f"Attempt {attempt+1}: a={a}, r={r} gives trivial root — retrying")
            continue

        p = math.gcd(x - 1, N)
        q = math.gcd(x + 1, N)
        print(f"Attempt {attempt+1}: succeeded with a={a}, r={r}")
        return p, q

    return None, None

factor_p, factor_q = period_finding_attack(N)
print(f"Discovered Factors: {factor_p} and {factor_q}")


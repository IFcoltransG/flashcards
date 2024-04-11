# coding: utf-8
import random
import operator
import sys

def starsigns():
    i = iter("""
        aries       cardinal  fire
        taurus      fixed     earth
        gemini      mutable   air

        cancer      cardinal  water
        leo         fixed     fire
        virgo       mutable   earth

        libra       cardinal  air
        scorpio     fixed     water
        sagittarius mutable   fire

        capricorn   cardinal  earth
        aquarius    fixed     air
        pisces      mutable   water
    """.split())
    return list(zip(i, i, i))

def hexbits():
    return [(f"{i:X}", f"{i:04b}") for i in range(16)]

def pick():
    line = list(random.choice(z))
    gone = random.randrange(0, len(line))
    answer = line[gone]
    line[gone] = None
    return line, answer
    
def query():
    q, a = pick()
    r = input(" - ".join(x or "???" for x in q) + "\n")
    if r.casefold() != a.casefold():
        print("-----------------------------")
        print("... Wrong, it was", a, "...")
        print("-----------------------------")
        matches = [(len(set(l) & set(q)), l) for l in z if r in l]
        top = max(matches, default=None)
        if top:
            for m in matches:
                if m[0] >= top[0]:
                    print("By " + r + " you might be thinking " + " - ".join(m[1]))
        print()
        return (True, r, a)
    else:
        print("*** Right! ***")
        print()
        return (False, r, a)

def response():
    return query()[1] == ""

if __name__ == "__main__":
    match sys.argv:
        case [_, "hex"]:
            z = hexbits()
        case [_, "star"]:
            z = starsigns()
        case [_, _]:
            print("unrecognised mode")
            sys.exit(1)
        case _:
            z = starsigns()
    for _ in iter(response, True):
        pass

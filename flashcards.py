# coding: utf-8
import random
import operator

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
z = list(zip(i, i, i))

def pick():
    line = list(random.choice(z))
    gone = random.randrange(0, len(line))
    answer = line[gone]
    line[gone] = None
    return line, answer
    
def query():
    q, a = pick()
    r = input(" - ".join(x or "???" for x in q) + "\n")
    if r != a:
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
    for _ in iter(response, True):
        pass

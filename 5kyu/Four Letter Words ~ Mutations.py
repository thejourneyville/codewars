def mutations(alice, bob, word, first):
    data_alice = {"player": alice}
    data_bob = {"player": bob}
    data = [data_alice, data_bob]
    no_match = 0
    winner = -1
    unfound = 0

    while True:

        for w in data[first]["player"]:
            print(f"player: {first}")
            if any(
                    [w[1:] == word[1:],
                     all([w[0] == word[0], w[2:] == word[2:]]),
                     all([w[:2] == word[:2], w[3] == word[3]]),
                     w[:3] == word[:3]]
            ):
                idx = data[first]["player"].index(w)
                word = data[first]["player"].pop(idx)
                break

            else:
                 unfound += 1

        first = (first + 1) % 2

            if w[1:] == word[1:]:
                if first == 0:
                    winner = 0
                else:
                    winner = 1
                break
            elif w[0] == word[0] and w[2:] == word[2:]:
                if first == 0:
                    winner = 0
                else:
                    winner = 1
                break
            elif w[:2] == word[:2] and w[3] == word[3]:
                if first == 0:
                    winner = 0
                else:
                    winner = 1
                break
            elif w[:3] == word[:3]:
                if first == 0:
                    winner = 0
                else:
                    winner = 1
                break

        if match:
            print(first, match, w)
            # print(data[first]["player"])
            idx = data[first]["player"].index(w)
            word = data[first]["player"].pop(idx)

            first = (first + 1) % 2


a = ["plat", "rend", "bear", "soar", "mare", "pare", "flap", "neat", "clan", "pore"]
b = ["boar", "clap", "farm", "lend", "near", "peat", "pure", "more", "plan", "soap"]
print(mutations(a, b, "boat", 0))

# first_let, second_let, third_let, fourth_let = word[0], word[1], word[2], word[3]

# for idx, player in enumerate([alice, bob]):
#
# if idx == 0:
#     name = "alice"
#     check = data_alice
#     check[name] = alice
# else:
#     name = "bob"
#     check = data_bob
#     check[name] = bob

# check.setdefault(name, [])
# check[name].append(sorted(player, key=lambda n: n[0]))
# check[name].append(sorted(player, key=lambda n: n[1]))
# check[name].append(sorted(player, key=lambda n: n[2]))
# check[name].append(sorted(player, key=lambda n: n[3]))

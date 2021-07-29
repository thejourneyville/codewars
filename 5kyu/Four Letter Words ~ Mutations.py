"""Our Setup Alice and Bob work in an office. When the workload is light and the boss isn't looking, they often play
simple word games for fun. This is one of those days!

This Game Today Alice and Bob are playing what they like to call Mutations, where they take turns trying to "think
up" a new four-letter word identical to the prior word except for one letter. They just keep on going until their
memories fail out.

Their Words Alice and Bob have memories of the same size, each able to recall 10 to 2000 different four-letter words.
Memory words and initial game word are randomly taken from a list of 4000 (unique, four-letter, lowercased) words,
any of which may appear in both memories.

The expression to "think up" a new word means that for their turn, the player must submit as their response word the
first valid, unused word that appears in their memory (by lowest array index), as their memories are ordered from the
most "memorable" words to the least.

The Rules
 - a valid response word must contain four different letters
 - 1 letter is replaced while the other 3 stay in position
 - it must be the lowest indexed valid word in their memory
 - this word cannot have already been used during the game
 - the final player to provide a valid word will win the game
 - if 1st player fails 1st turn, 2nd can win with a valid word
 - when both players fail the initial word, there is no winner

Your Task
To determine the winner!
"""


def mutations(alice, bob, word, first):
    """
    :param alice: player 1 list of words
    :param bob: player 2 list of words
    :param word: starting word to try matching
    :param first: player who will go first
    :return: int -> -1 = no winner, 0 = player 1 winner, 1 = player 2 winner
    """
    data = [alice, bob]  # creating a nested list to access by index 0 and 1
    players = [None, None]  # will hold boolean values to determine winner
    found = [word]  # a list of words which cannot be searched for again

    def determine_winner(potential_winner):
        """
        :param potential_winner: passes 'players' list to determine potential winner
        :return: value which represents the outcome of the game (see return statement from the 'mutations' function)
        """
        if potential_winner[0] is True and potential_winner[1] is False:
            return 0
        elif potential_winner[0] is False and potential_winner[1] is True:
            return 1
        elif potential_winner[0] is False and potential_winner[1] is False:
            return -1
        else:
            return 2

    while True:

        for w in data[first]:  # looking at current player's word list

            if w not in found:  # ensuring the word is not in the 'found' list

                #  ensuring the word has 4 unique letters (rule)
                #  ensuring 3 of the 4 letters match and match index position
                if len(set(w)) == 4 and \
                        any(
                            [
                                all([w[1:] == word[1:], w[0] != word[0]]),
                                all([w[0] == word[0], w[2:] == word[2:], w[1] != word[1]]),
                                all([w[:2] == word[:2], w[3] == word[3], w[2] != word[2]]),
                                all([w[:3] == word[:3], w[3] != word[3]])
                            ]
                        ):

                    players[first] = True  # if criteria is met, the player's boolean value is set as found (True)

                    result = determine_winner(players)  # helper function to determine game outcome
                    if -1 <= result <= 1:
                        return result

                    found.append(w)  # added word to found list
                    word = found[-1]  # setting word as the word to match for in the next round

                    first = (first + 1) % 2  # moving to other player
                    break

        else:
            players[first] = False  # if word is not found, the player's boolean value is set as NOT found (False)

            result = determine_winner(players)  # helper function to determine game outcome
            if -1 <= result <= 1:
                return result

            first = (first + 1) % 2  # moving to other player


tests = (
    ("maze", 0),  # 0
    ("send", 0),  # 1
    ("boat", 0),  # 1
    ("apse", 0),  # -1
    ("neat", 1),  # 1
    ("soar", 1),  # 0
    ("mark", 1),  # 0
    ("calm", 1),  # -1
)

a = ["plat", "rend", "bear", "soar", "mare", "pare", "flap", "neat", "clan", "pore"]
b = ["boar", "clap", "farm", "lend", "near", "peat", "pure", "more", "plan", "soap"]


for test in tests:
    print(mutations(a, b, test[0], test[-1]))

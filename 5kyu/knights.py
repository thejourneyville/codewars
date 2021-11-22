def knights(ranks, p, r):
    
    ranks.insert(p, r)
    winner = True
    match_right, match_left = True, True
    l_idx_jump, r_idx_jump  = 1, 1
    fights, total_fights = 0, 0
    reset = 0

    while winner:
        
        winner = False

        # print(f"rank: {r}")
        # print(f"current left: {ranks[(p - l_idx_jump) % len(ranks)]}")
        # print(f"current right: {ranks[(p + r_idx_jump) % len(ranks)]}")

        while match_left:
            # print(f"count: {len(ranks) - total_fights}")
            if r == ranks[(p - l_idx_jump) % len(ranks)]:
                # print("left match")
                fights += 1
                l_idx_jump += 1
                winner = True
            else:
                break
        
        while match_right:
            # print(f"count: {len(ranks) - total_fights}")
            if r == ranks[(p + r_idx_jump) % len(ranks)]:
                # print("right match")
                fights += 1
                r_idx_jump += 1
                winner = True
            else:
                break

        r += fights
        total_fights += fights
        # print(f"total_fights: {total_fights}")
        fights = reset
        # print(f"orginal idx: {p}\ncurrent left idx: {(p - r_idx_jump) % len(ranks)}\ncurrent right idx: {r_idx_jump}")

        if not winner:
            if len(ranks) - total_fights == 0:
                return 1
            else:
                return len(ranks) - total_fights
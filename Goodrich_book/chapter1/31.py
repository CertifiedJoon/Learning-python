def permute_notes(notes_comb, notes_avail, change):
    if not notes_avail or sum(notes_comb) >= change:
        if (sum(notes_comb) == change):
            print('100x{} / 500x{} / 1000x{} / 5000x{} / 10000x{} / 50000x{}'
                  .format(notes_comb.count(100), notes_comb.count(500),
                          notes_comb.count(1000), notes_comb.count(5000),
                          notes_comb.count(10000), notes_comb.count(500000)))
            return True
        return False
    if not permute_notes(notes_comb + notes_avail[:1], notes_avail, change):
        return permute_notes(notes_comb, notes_avail[1:], change)
    else:
        return permute_notes(notes_comb[:-1], notes_avail[1:], change)


def change_maker(notes, charged, recieved):
    permute_notes(list(), notes, recieved - charged)


money = [50000, 10000, 5000, 1000, 500, 100]
change_maker(money, 90000, 100000)
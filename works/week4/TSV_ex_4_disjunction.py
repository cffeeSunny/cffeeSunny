def disjunction(set1: set, set2: set) -> bool:
    acc = []
    for a in set1:
        if a not in set2:
            acc.append(True)
        else:
            acc.append(False)
    if False in acc:
        return False
    else:
        return True
    pass



def main() -> None:
    # Tests for student side debugging only
    assert not disjunction({1, 2, 3}, {2, 5})
    assert disjunction({"Pizza"}, {"Pineapple", "Cucumbers", "lettuce"})


if __name__ == '__main__':
    main()

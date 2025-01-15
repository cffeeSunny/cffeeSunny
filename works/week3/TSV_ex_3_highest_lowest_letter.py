def highest_lowest_letter(s: str) -> tuple[int, int]:
    string_list = list(s)
    max_acc= -1
    min_acc=256
    for element in string_list:
        if max_acc<ord(element):
            max_acc=ord(element)
        else:
            max_acc=max_acc
    for element in string_list:
        if min_acc>ord(element):
            min_acc=ord(element)
        else:
            min_acc=min_acc
    return(max_acc,min_acc)
    pass


def main() -> None:
    assert highest_lowest_letter("Hello World!") == (114, 32)
    assert highest_lowest_letter("AAA") == (65, 65)
    assert highest_lowest_letter(
        "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et "
        "dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet "
        "clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, "
        "consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, "
        "sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, "
        "no sea takimata sanctus est Lorem ipsum dolor sit amet.") == (121, 32)


if __name__ == '__main__':
    main()

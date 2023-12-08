from collections import Counter
from functools import cmp_to_key

hand_types = ['HI', '1P', '2P', '3', 'FH', '4', '5']
card_rank = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
card_rank_2 = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']


def parse_v2(lines):
    hands = []
    for line in lines:
        hand, bid = line.split()
        m = Counter(hand).most_common(2)
        tmp = hand.replace('J', m[0][0] if m[0][0] != 'J' else m[1][0]) if hand != 'JJJJJ' else hand
        match Counter(tmp).most_common(2):
            case [(_, 5), *_]:
                hands.append((hand, int(bid), 6))
            case [(_, 4), *_]:
                hands.append((hand, int(bid), 5))
            case [(_, 3), (_, 2)]:
                hands.append((hand, int(bid), 4))
            case [(_, 3), (_, 1)]:
                hands.append((hand, int(bid), 3))
            case [(_, 2), (_, 2)]:
                hands.append((hand, int(bid), 2))
            case [(_, 2), (_, 1)]:
                hands.append((hand, int(bid), 1))
            case [(_, 1), _]:
                hands.append((hand, int(bid), 0))
            case x:
                print("umatched v2: ", x)
    return hands


def parse(lines):
    hands = []
    for line in lines:
        hand, bid = line.split()
        match Counter(hand).most_common(2):
            case [(_, 5), *_]:
                hands.append((hand, int(bid), 6))
            case [(_, 4), *_]:
                hands.append((hand, int(bid), 5))
            case [(_, 3), (_, 2)]:
                hands.append((hand, int(bid), 4))
            case [(_, 3), (_, 1)]:
                hands.append((hand, int(bid), 3))
            case [(_, 2), (_, 2)]:
                hands.append((hand, int(bid), 2))
            case [(_, 2), (_, 1)]:
                hands.append((hand, int(bid), 1))
            case [(_, 1), _]:
                hands.append((hand, int(bid), 0))
            case x:
                print("umatched v1: ", x)
    return hands


def order(a, b):
    if a[-1] != b[-1]:
        if a[2] > b[2]:
            return 1
        return -1
    for d, e in zip(a[0], b[0]):
        if d != e:
            if card_rank.index(d) > card_rank.index(e):
                return 1
            return -1
    return 0


def order_v2(a, b):
    if a[-1] != b[-1]:  # different card types
        if a[2] > b[2]:  # check order
            return 1
        return -1
    for d, e in zip(a[0], b[0]):
        if d != e:
            if card_rank_2.index(d) > card_rank_2.index(e):
                return 1
            return -1


cmp = cmp_to_key(order)
cmp2 = cmp_to_key(order_v2)


def part1(lines):
    hands = parse(lines)
    return sum(((i + 1) * j[1] for i, j in enumerate(sorted(hands, key=cmp))))


def part2(lines):
    hands = parse_v2(lines)
    return sum(((i + 1) * j[1] for i, j in enumerate(sorted(hands, key=cmp2))))


def solve(inputpath):
    with open(inputpath) as f:
        data = f.readlines()
    return part1(data), part2(data)


def main():
    print(solve("aoc/seven/input.txt"))


if __name__ == "__main__":
    main()

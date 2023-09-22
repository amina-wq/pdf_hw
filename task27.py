from collections import Counter


def find_winner(votes: list):
    vote_count = Counter(votes)

    max_votes = max(vote_count.values())
    winners = [candidate for candidate, votes in vote_count.items() if votes == max_votes]

    if len(winners) > 1:
        winner = min(winners, key=lambda x: len(x))
    else:
        winner = winners[0]

    winner_vote_count = max_votes

    return winner, winner_vote_count


if __name__ == '__main__':
    votes = ['Аскаров', 'Бекмуханов', 'Ернур', 'Пешая', 'Карим', 'Шаримазданов', 'Аскаров', 'Пешая', 'Ернур', 'Карим']

    winner, vote_count = find_winner(votes)

    print(f"Победитель: {winner}")
    print(f"Число голосов: {vote_count} / {len(votes)}")

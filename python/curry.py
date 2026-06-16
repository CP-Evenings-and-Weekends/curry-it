def batting_average(player):
    def get_games(games):
        def get_hits(hits):
            def get_at_bats(at_bats):
                avg = hits / at_bats
                return f"{player} had {at_bats} at bats in {games} games, with {hits} hits and a{avg: .3f} batting average"
            return get_at_bats
        return get_hits
    return get_games

class Player:

    def __init__(self, id = None, username = None, percent_for = 0,
                 percent_against = 0, won = 0, drawn = 0, lost = 0):
        self.id = id
        self.username =username
        self.percent_for = percent_for
        self.percent_against = percent_against
        self.percent_difference = self.calculate_difference(self.percent_for, self.percent_against)
        self.won = won
        self.lost = lost
        self.drawn = drawn
        self.points = self.calculate_points(self.won, self.drawn)

    def __str__(self):
        return (f'Player: ID: {self.id}, username: {self.username}, points: {self.points}, '
                f'percent_for: {self.percent_for}, percent_against: {self.percent_against}, '
                f'percent_difference: {self.percent_difference}, won: {self.won}, lost: {self.lost}, '
                f'drawn: {self.drawn}')

    def calculate_difference(self, percent_for, percent_against):
        return percent_for - percent_against

    def calculate_points(self, won, drawn):
        return 3*won + drawn

if __name__ == '__main__':
    player1 = Player(username = 'Noc', won = 10, lost = 2, drawn = 1, percent_for = 20, percent_against = 40)
    print(player1)
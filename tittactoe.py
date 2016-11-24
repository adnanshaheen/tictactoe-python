import os

class player:
    """player class"""

    def __init__(self, name, mark, stats={ 'won' : 0, 'lost' : 0, 'drawn' : 0 }):
        """Constructor"""
        self.name = name
        self.mark = mark
        self.stats = stats

    def get_score():
        """get score"""
        return (stats.value('won') * 2) + stats.value('drawn') - stats.value('lost')

    def __str__(self):
        """overloading str"""
        return "Player: " + Name + ", Mark: " + PlayerMark + ", Score: " + str(get_score())

    def __lt__(self, other):
        """overloading less then"""
        return self.get_score() < other.get_score()

class deck:
    """deck class"""

    def __init__(self):
        """Constructor"""
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.p1_choices = []
        self.p2_choices = []

    def __str__(self):
        """overloading str"""
        return ("       |       |\n" +
                "   " + self.board[0] + "   |   " + self.board[1] + "   |   " + self.board[2] + "\n" +
                "  _____|_______|_____\n" +
                "       |       |\n" +
                "   " + self.board[3] + "   |   " + self.board[4] + "   |   " + self.board[5] + "\n" +
                "  _____|_______|_____\n" +
                "       |       |\n"  +
                "   " + self.board[6] + "   |   " + self.board[7] + "   |   " + self.board[8] + "\n" +
                "       |       |     \n\n")


class tictactoe:
    """tictactoe class"""

    def __init__(self):
        """Constructor"""
        name = str(input("Please enter player one name: "))
        self.p1 = player(name, 'X')
        name = str(input("Please enter player two name: "))
        self.p2 = player(name, 'O')
        self.deck_list = []
        self.turn = False

    def start(self):
        """Start game"""

        while True:
            self.deck_list.append(deck())
            while True:
                if self.get_user_input():
                    break

                if self.is_game_over(self.p1.mark):
                    """player 1 won"""
                    print("Player: ", self.p1.name, " won")
                    self.p1.stats['won'] += 1
                    self.p2.stats['lost'] += 1
                    break
                elif self.is_game_over(self.p2.mark):
                    """player 2 won"""
                    print("Player: ", self.p2.name, " won")
                    self.p2.stats['won'] += 1
                    self.p1.stats['lost'] += 1
                    break
                else:
                    if len(self.deck_list[-1].p1_choices) + len(self.deck_list[-1].p2_choices) == 9:
                        """game is drawn"""
                        self.p1.stats['drawn'] += 1
                        self.p2.stats['drawn'] += 1
                        print('It\'s a draw')
                        break

                self.turn = not self.turn

            restart = str(input('New game? (y/n): '))
            if restart.lower() == 'n':
                break

    def validate_user_input(self):
        """validate user input"""
        if self.turn:
            name = self.p1.name
        else:
            name = self.p2.name
        while True:
            try:
                userInput = int(input("Enter player  " + name  + "  Move : "))
            except ValueError:
                print("Invalid input, please enter an integer")
                continue
            if (0 <= userInput <= 8):
                if (self.deck_list[-1].board[userInput] == " "):
                    return userInput
                else:
                    print("The cell", userInput, " was already token")
            else:
                print("Invalid move, enter a position between 0 and 8")

    def is_game_over(self, mark):
        """is game over"""
        if (self.deck_list[-1].board[0] == mark and self.deck_list[-1].board[1] == mark and self.deck_list[-1].board[2] == mark) or \
           (self.deck_list[-1].board[3] == mark and self.deck_list[-1].board[4] == mark and self.deck_list[-1].board[5] == mark) or \
           (self.deck_list[-1].board[6] == mark and self.deck_list[-1].board[7] == mark and self.deck_list[-1].board[8] == mark) or \
           (self.deck_list[-1].board[0] == mark and self.deck_list[-1].board[3] == mark and self.deck_list[-1].board[6] == mark) or \
           (self.deck_list[-1].board[1] == mark and self.deck_list[-1].board[4] == mark and self.deck_list[-1].board[7] == mark) or \
           (self.deck_list[-1].board[2] == mark and self.deck_list[-1].board[5] == mark and self.deck_list[-1].board[8] == mark) or \
           (self.deck_list[-1].board[0] == mark and self.deck_list[-1].board[4] == mark and self.deck_list[-1].board[8] == mark) or \
           (self.deck_list[-1].board[2] == mark and self.deck_list[-1].board[4] == mark and self.deck_list[-1].board[6] == mark):
            file = open("TicTacToe.txt", "a")
            file.write("Game No. " + str(len(self.deck_list)) + "\n")
            file.write("------------------------------\n")
            deck_string = str(self.deck_list[-1])
            file.write(deck_string)
            file.write("------------------------------\n")
            file.close()
            return True
        else:
            return False

    def get_user_input(self):
        """get user input"""
        user_input = self.validate_user_input()

        if self.turn:
            self.deck_list[-1].p1_choices.append(user_input)
        else:
            self.deck_list[-1].p2_choices.append(user_input)
        if self.deck_list[-1].board[user_input] != 'X' or self.deck_list[-1].board[user_input] != 'O':
            if self.turn:
                self.deck_list[-1].board[user_input] = 'X'
            else:
                self.deck_list[-1].board[user_input] = 'O'
            os.system('cls')
            print(self.deck_list[-1])

def main():
    """main function"""
    t = tictactoe()
    t.start()

main()
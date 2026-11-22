

figure_symbols = {
    "white": {
        "Pawn": "♙",
        "Rook": "♖",
        "Knight": "♘",
        "Bishop": "♗",
        "Queen": "♕",
        "King": "♔"
    },
    "black": {
        "Pawn": "♟",
        "Rook": "♜",
        "Knight": "♞",
        "Bishop": "♝",
        "Queen": "♛",
        "King": "♚"
    }
}# DEUTSCH: "Bauer", "Turm", "Springer", "Läufer", "Dame", "König"


class Spielfeld:
    def __init__(self):
        self.felder = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],

        ] # Schachbrett

    def print_board(self):
        for zahl, reihe in zip(range(9, 0, -1), self.felder):
                Liste = [str(row) for row in reihe]
                print(zahl - 1, "#  ", " | ".join(Liste)) 

        print("      _____________________________ ")   
        print("      A | B | C | D | E | F | G | H")   

    def move_figure(self, start_pos, end_pos):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        figure = self.felder[start_row][start_col]

        self.felder[start_row][start_col] = 0
        self.felder[end_row][end_col] = figure

        figure.position = end_pos

        

        



class Figure:
    def __init__(self, name, position, color):
        self.name = name
        self.position = position
        self.color = color

    def __str__(self):
        return figure_symbols[self.color][self.name]

    def possible_moves(self, board):
        pass


class Pawn(Figure):
    pass

class Rook(Figure):
    pass

class Knight(Figure):
    pass

class Bishop(Figure):
    pass

class Queen(Figure):
    pass

class King(Figure):
    pass



def sort_input(eingabe, figur):

    eingabe = eingabe.strip()

    if len(eingabe) != 2:
        print("Ungültiges Feld!")
        return None

    if not eingabe[0].isalpha() or not eingabe[1].isdigit():
        print ("Ungültiges Feld")
        return None
    


    buchstaben = "".join(zeichen for zeichen in eingabe if zeichen.isalpha())
    zahlen = "".join(zeichen for zeichen in eingabe if zeichen.isdigit())


    number_bu = ord(buchstaben) - 65
    number = 8 - int(zahlen)

    if number_bu < 0 or number_bu > 7 or number < 0 or number > 7:
        print("Ungültiges Feld")
        return None

    print (number, number_bu)
    return (number, number_bu)


def game():
    running = True
    current_player = "white"

    bauer = Pawn("Pawn", (6, 4), "white")

    print(bauer.name)
    print(bauer.position)
    print(bauer.color)


    brett = Spielfeld()

    for spalte in range(8):
        if spalte == 0 or spalte == 7:
            brett.felder[7][spalte] = Rook("Rook", (7, spalte), "white")
            brett.felder[0][spalte] = Rook("Rook", (0, spalte), "black")
        elif spalte == 1 or spalte == 6:
            brett.felder[7][spalte] = Knight("Knight", (7, spalte), "white")
            brett.felder[0][spalte] = Knight("Knight", (0, spalte), "black")
        elif spalte == 2 or spalte == 5:
            brett.felder[7][spalte] = Bishop("Bishop", (7, spalte), "white")
            brett.felder[0][spalte] = Bishop("Bishop", (0, spalte), "black")
        elif spalte == 3:
            brett.felder[7][spalte] = Queen("Queen", (7, spalte), "white")
            brett.felder[0][spalte] = Queen("Queen", (0, spalte), "black")
        elif spalte == 4:
            brett.felder[7][spalte] = King("King", (7, spalte), "white")
            brett.felder[0][spalte] = King("King", (0, spalte), "black")

        brett.felder[6][spalte] = Pawn("Pawn", (6, spalte), "white")
        brett.felder[1][spalte] = Pawn("Pawn", (1, spalte), "black")

    brett.print_board()


    while running:
        print ("––––––––––––––––––––––––––––––––––––––––––––––––")
        print("1. Bauer")
        print("2. Turm")
        print("3. Springer")
        print("4. Läufer")
        print("5. Dame")
        print("6. König")
        print ("––––––––––––––––––––––––––––––––––––––––––––––––")


        figur = input(f"{current_player} gib deine Figur ein!")



        if not figur.strip():
            print("Bitte gib eine Figur an.")
            continue
        if figur in ["1", "2", "3", "4", "5", "6"]:
            figur = list(figure_symbols[current_player].keys())[int(figur) - 1]
        elif figur == "0":
            print("Spiel beendet.")
            running = False
            break
        else:
            print("Ungültige Eingabe. Bitte wähle eine Zahl zwischen 1 und 6.")
            continue

        start_pos = sort_input(input("Startfeld: "), figur)
        end_pos = sort_input(input("Endfeld: "), figur)
        if start_pos is None or end_pos is None:
            continue

        print(f"{current_player} ist am Zug!")
        
        brett.move_figure(start_pos, end_pos)


        brett.print_board()
        print ("––––––––––––––––––––––––––––––––––––––––––––––––")
        print ("––––––––––––––––––––––––––––––––––––––––––––––––")

        
        current_player = "black" if current_player == "white" else "white"

game()
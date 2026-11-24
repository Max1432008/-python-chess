

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
        print("      A | B | C | D | E | F | G | H")   
        print("      _____________________________ ")   


        for zahl, reihe in zip(range(9, 0, -1), self.felder):
                Liste = [str(row) for row in reihe]
                print(zahl - 1, "#  ", " | ".join(Liste)) 

        print("      _____________________________ ")   
        print("      A | B | C | D | E | F | G | H")   

    def move_figure(self, start_pos, end_pos):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        figure = self.felder[start_row][start_col]

        if figure == 0:
            print("Auf diesem Feld steht keine Figur!")
            return False

        moves = figure.possible_moves(self)

        if not moves:
            print("Keine gültigen Züge für diese Figur!")
            return False


        if end_pos not in moves:
            print("Ungültiger Zug!")
            return False

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

    def calculate_moves(self, board, moves):
        row, col = self.position
        possible = []

        for row_offset, col_offset in moves:
            new_row = row + row_offset
            new_col = col + col_offset

            if 0 <= new_row < 8 and 0 <= new_col < 8:
                target = board.felder[new_row][new_col]

                if target == 0 or target.color != self.color:
                    possible.append((new_row, new_col))

        return possible




    def calculate_sliding_moves(self, board, directions):
        row, col = self.position
        possible = []

        for row_offset, col_offset in directions:

            for k in range(1, 8):

                new_row = row + k * row_offset
                new_col = col + k * col_offset


                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    target = board.felder[new_row][new_col]


                    if target == 0:
                        possible.append((new_row, new_col))

                    elif target.color != self.color:
                        possible.append((new_row, new_col))
                        break

                    else:
                        break

                else: 
                    break

        return possible





class Pawn(Figure):
    def possible_moves(self, board):
        row, col = self.position
        possible = []

        direction = -1 if self.color == "white" else 1
        start_row = 6 if self.color == "white" else 1
        next_row = row + direction

        # Ein Feld vorwärts
        if 0 <= next_row < 8 and board.felder[next_row][col] == 0:
            possible.append((next_row, col))

            # Zwei Felder vorwärts: nur von der Startreihe
            # und wenn beide Felder frei sind.
            two_rows = row + 2 * direction
            if (
                row == start_row
                and board.felder[two_rows][col] == 0
            ):
                possible.append((two_rows, col))

        # Diagonal schlagen
        for col_offset in (-1, 1):
            target_col = col + col_offset

            if 0 <= next_row < 8 and 0 <= target_col < 8:
                target = board.felder[next_row][target_col]

                if target != 0 and target.color != self.color:
                    possible.append((next_row, target_col))

        return possible
                

class Rook(Figure):
    def possible_moves(self, board):
        row, col = self.position

        moves = [
            (-1, 0), (1, 0),
            (0, -1), (0, 1)
        ]
        
        return self.calculate_sliding_moves(board, moves)

class Knight(Figure):
    def possible_moves(self, board):

        moves = [
            (-2, -1),
            (-2,  1),
            ( 2, -1),
            ( 2,  1),
            (-1, -2),
            (-1,  2),
            ( 1, -2),
            ( 1,  2)
        ]
        return self.calculate_moves(board, moves)



class Bishop(Figure):
    def possible_moves(self, board):

        moves = [
            (-1, -1), (-1, 1),
            (1, -1), (1, 1)
        ]
    
        return self.calculate_sliding_moves(board, moves)

class Queen(Figure):
    def possible_moves(self, board):
        row, col = self.position

        moves = [
            (-1, 0), (1, 0),
            (0, -1), (0, 1),
            (-1, -1), (-1, 1),
            (1, -1), (1, 1)]

        return self.calculate_sliding_moves(board, moves)
        


class King(Figure):
    def possible_moves(self, board):

        moves = [
            (-1, 0), (1, 0),
            (0, -1), (0, 1),
            (-1, -1), (-1, 1),
            (1, -1), (1, 1)
        ]
        return self.calculate_moves(board, moves)




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
        
        isValidMove = brett.move_figure(start_pos, end_pos)

        if isValidMove is None:
            print("Ungültiger Zug. Bitte versuche es erneut.")
            continue

        else: 
            current_player = "black" if current_player == "white" else "white"




        brett.print_board()
        print ("––––––––––––––––––––––––––––––––––––––––––––––––")
        print ("––––––––––––––––––––––––––––––––––━━━━━━━━━━━━━━")

        

game()
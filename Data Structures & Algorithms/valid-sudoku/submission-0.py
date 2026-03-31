class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # RAWBIDI
        # REPEAT THE QUESTION
        # ASK CLARIFICATION (CONSTRAINTS, EDGE CASES, ASSUMPTIONS)
        # WORK THROUGH AN EXAMPLE
        # BRAINSTORM SOLUTION
        # ASK FOR GO AHEAD
        # IMPLEMENT SOLUTION
        # DEBUG
        # IMPROVE

        # TIME COMPLEXITY:
        # SPACE COMPLEXITY:

        # THE FIRST THING THAT I NEED TO DO IS ANALYZE THE ROWS

        # THE SECOND THING I NEED TO DO IS ANALYZE THE COLS

        # THE THIRD THAT I NEED TO ANALYZE IS THE BOXES

        # NEED TO KEEP A SET AND ADD ONLY THE NUMBERS TO THE SET
        # COMPARE THE NUMBER THAT I SEE IF IT'S IN THE SET
        # IF IT IS NOT IN THE SET, KEEP GOING
        # IF IT IS IN THE SET, RETURN FALSE

        rows = len(board)
        cols = len(board[0])

        # ANALYZE THE COLS FIRST
        for i in range(rows):
            seen = set()
            for j in range(cols):
                if board[i][j] != ".":
                    if board[i][j] not in seen:
                        seen.add(board[i][j])
                    else:
                        return False

        # ANALYZE THE ROWS SECOND
        for i in range(cols):
            seen = set()
            for j in range(rows):
                if board[j][i] != ".":
                    if board[j][i] not in seen:
                        seen.add(board[j][i])
                    else:
                        return False

        starts = [
            (0, 0),
            (0, 3),
            (0, 6),
            
            (3, 0),
            (3, 3),
            (3, 6),

            (6, 0),
            (6, 3),
            (6, 6)
        ]

        for x, y in starts:
            seen = set()
            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    if board[i][j] != ".":
                        if board[i][j] not in seen:
                            seen.add(board[i][j])
                        else:
                            return False

        return True
            







        
import random
import time


class EightPuzzle:
    def __init__(self,
                 initial_state=None,
                 goal_state=[0, 1, 2, 3, 4, 5, 6, 7, 8],
                 delay=1):

        # if the initial state is None, generate one randomly
        if initial_state is None:
            initial_state = [x for x in range(9)]
            random.shuffle(initial_state)

        self.state = self.check_state(initial_state)
        self.goal_state = self.check_state(goal_state)
        self.delay = delay

    def check_state(self, state):
        """Makes sure that the state is a valid eight puzzle state.
        If it is not, an assert will prevent other code from executing"""

        assert len(state) == 9, "eight puzzle state has to have 9 values"
        sorted_state = sorted(state)
        state_template = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        assert sorted_state == state_template, \
            "eight puzzle state has to have all values from 0 to 8"
        # if we pass the tests let us return the state
        return state

    def check_move(self, state1, state2):
        """Checks whether a proposed move is a valid one."""
        state1 = self.check_state(state1)
        state2 = self.check_state(state2)

        diff = []
        zero_changed = False
        for i in range(len(state1)):
            if state1[i] != state2[i]:
                diff.append(i)
            if state1[i] == 0 or state2[i] == 0:
                zero_changed = True

        if not zero_changed:
            return False

        if len(diff) > 2:
            return False

        dist = abs(diff[0] - diff[1])
        if dist == 1 or dist == 3:
            return True
        else:
            return False

    def print(self, state=None):
        """Prints the given state as an eight puzzle board. If no state is
        given, the internal state is used"""
        state = self.state if state is None else state
        print("+-+-+-+")
        for x in range(3):
            print("|", end='')
            for y in range(3):
                print(state[x*3 + y], end='|')
            print("\n+-+-+-+")
        print()

    def in_goal_state(self):
        """Checks whether the goal state has been reached."""
        return self.state == self.goal_state

    def solve(self):
        """Tries to solve the puzzle by executing moves until the goal state is
        reached."""
        moves = 0
        self.print()
        prev_state = self.state

        while not self.in_goal_state():
            new_state = self.move(self.state)

            moves += 1
            print("\nMove #{}:\n".format(moves))
            self.print(new_state)

            if not self.check_move(prev_state, new_state):
                raise Exception("Invalid move executed.")
            self.state = new_state

            time.sleep(self.delay)
            if prev_state == self.state:
                print("No state change after move, exiting")
                return
            prev_state = new_state
        print("Puzzle solved, congratulations!")

    def index_to_coords(self, index):
        """Transforms an index in the internal state into x,y coordinates."""
        return (index // 3, index % 3)

    def get_successors(self, state):
        """Returns a list of valid successor states for a given state."""
        return []

    def h(self, state):
        """Returns value of the heuristics function for a given state."""
        return 0

    def move(self, state):
        """Generates next state from the current state by executing a valid
        move."""
        return []


if __name__ == '__main__':
    eight_puzzle = EightPuzzle(initial_state=[4, 1, 2, 3, 0, 5, 6, 7, 8])
    eight_puzzle.solve()

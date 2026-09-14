from game import Game
from mage import Mage


def main() -> None:
    mage = Mage("Mage", 100, 25, 40)
    game = Game(mage)
    game.run()


if __name__ == "__main__":
    main()

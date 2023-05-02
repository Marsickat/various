import zombiedice

class my_zombie:
    def __init__(self, name):
        # У каждого зомби должно быть имя
        self.name = name

    def turn(self, game_state):
        # game_state - это словарь с информацией о текущем состоянии игры (его можно игнорировать)

        dice_roll_results = zombiedice.roll()   # первый бросок
        """
            Метод roll() возвращает словарь с ключами "brains", "shotgun" и "footsteps", показывающими, сколько раз 
            выпали кубики каждого типа. Ключ "rolls" - это список кортежей (цвет, пиктограмма) с информацией о броске.
            Пример словаря, возвращаемого функцией roll():
            {"brains": 1, "footsteps": 1, "shotgun": 1,
            "rolls": [("yellow", "brains"), ("red", "footsteps"), ("green", "shotgun")]}
                                                                                                                    """
        # ЗАМЕНИТЕ ЭТОТ КОД СОБСТВЕННЫМ
        brains = 0
        while dice_roll_results is not None:
            brains += dice_roll_results["brains"]

            if brains < 2:
                dice_roll_results = zombiedice.roll()   # ещё бросок
            else:
                break

zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name="Random"),
    zombiedice.examples.RollsUntilInTheLeadZombie(name="Until Leading"),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name="Stop at 2 Shotguns", minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name="Stop at 1 Shotgun", minShotguns=1),
    my_zombie(name="My Zombie Bot"),
    # Добавьте здесь любых других зомби
)

# Раскомментируйте одну из следующих строк, чтобы запустить игру в режиме командной строки или в режиме браузера
# zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)
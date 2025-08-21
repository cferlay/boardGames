from typing import Callable

values = [str(i)+str(j)+str(k) for i in range(1,6) for j in range(1,6) for k in range(1,6)]

class Verificator:
    def __init__(self, description: str, test: Callable[[str], bool]):
        self.description = description
        self.test = test
        self.valid_values = [value for value in values if test(value)]

class Criterion:
    def __init__(self, id: int, description: str, verificators: list[Verificator]):
        self.id = id
        self.description = description
        self.verificators = verificators

all_criteria = []

all_criteria.append(
    Criterion(
        id = 0,
        description = "Yellow Square is compared to 4",
        verificators = [
            Verificator(
                description = "Yellow Square is smaller than 4",
                test = lambda x: int(str(x)[1]) < 4
            ),
            Verificator(
                description = "Yellow Square is equal to 4",
                test = lambda x: int(str(x)[1]) == 4
            ),
            Verificator(
                description = "Yellow Square is greater than 4",
                test = lambda x: int(str(x)[1]) > 4
            )
        ]
    )
)

all_criteria.append(
    Criterion(
        id = 1,
        description = "Count the number of even numbers",
        verificators = [
            Verificator(
                description = "There are 0 even numbers",
                test = lambda x: sum(int(digit) % 2 == 0 for digit in str(x)) == 0
            ),
            Verificator(
                description = "There is 1 even number",
                test = lambda x: sum(int(digit) % 2 == 0 for digit in str(x)) == 1
            ),
            Verificator(
                description = "There are 2 even numbers",
                test = lambda x: sum(int(digit) % 2 == 0 for digit in str(x)) == 2
            ),
            Verificator(
                description = "There are 3 even numbers",
                test = lambda x: sum(int(digit) % 2 == 0 for digit in str(x)) == 3
            )
        ]
    )
)

all_criteria.append(
    Criterion(
        id = 2,
        description = "One value is equal to 3",
        verificators = [
            Verificator(
                description = "Blue Triangle is equal to 3",
                test = lambda x: int(str(x)[0]) == 3
            ),
            Verificator(
                description = "Yellow Square is equal to 3",
                test = lambda x: int(str(x)[1]) == 3
            ),
            Verificator(
                description = "Purple Circle is equal to 3",
                test = lambda x: int(str(x)[2]) == 3
            )
        ]
    )
)

all_criteria.append(
    Criterion(
        id = 3,
        description = "One value is greater than 1",
        verificators = [
            Verificator(
                description = "Blue Triangle is greater than 1",
                test = lambda x: int(str(x)[0]) > 1
            ),
            Verificator(
                description = "Yellow Square is greater than 1",
                test = lambda x: int(str(x)[1]) > 1
            ),
            Verificator(
                description = "Purple Circle is greater than 1",
                test = lambda x: int(str(x)[2]) > 1
            )
        ]
    )
)

all_criteria.append(
    Criterion(
        id = 4,
        description = "The sum of values is a multiple",
        verificators = [
            Verificator(
                description = "The sum of values is a multiple of 3",
                test = lambda x: sum(int(digit) for digit in str(x)) % 3 == 0
            ),
            Verificator(
                description = "The sum of values is a multiple of 4",
                test = lambda x: sum(int(digit) for digit in str(x)) % 4 == 0
            ),
            Verificator(
                description = "The sum of values is a multiple of 5",
                test = lambda x: sum(int(digit) for digit in str(x)) % 5 == 0
            )
        ]
    )
)

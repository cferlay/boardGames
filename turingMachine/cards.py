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

#1 Blue Triangle is compared to 1
all_criteria.append(
    Criterion(
        id = 1,
        description = "Blue Triangle is compared to 1",
        verificators = [
            Verificator(
                description = "Blue Triangle is equal to 1",
                test = lambda x: int(str(x)[0]) == 1
            ),
            Verificator(
                description = "Blue Triangle is greater than 1",
                test = lambda x: int(str(x)[0]) > 1
            )
        ]
    )
)

#2 Blue Triangle is compared to 3
all_criteria.append(
    Criterion(
        id = 2,
        description = "Blue Triangle is compared to 3",
        verificators = [
            Verificator(
                description = "Blue Triangle is less than 3",
                test = lambda x: int(str(x)[0]) < 3
            ),
            Verificator(
                description = "Blue Triangle is equal to 3",
                test = lambda x: int(str(x)[0]) == 3
            ),
            Verificator(
                description = "Blue Triangle is greater than 3",
                test = lambda x: int(str(x)[0]) > 3
            )
        ]
    )
)

#3 Yellow Square is compared to 3
all_criteria.append(
    Criterion(
        id = 3,
        description = "Yellow Square is compared to 3",
        verificators = [
            Verificator(
                description = "Yellow Square is less than 3",
                test = lambda x: int(str(x)[1]) < 3
            ),
            Verificator(
                description = "Yellow Square is equal to 3",
                test = lambda x: int(str(x)[1]) == 3
            ),
            Verificator(
                description = "Yellow Square is greater than 3",
                test = lambda x: int(str(x)[1]) > 3
            )
        ]
    )
)

#4 Yellow Square is compared to 4   
all_criteria.append(
    Criterion(
        id = 4,
        description = "Yellow Square is compared to 4",
        verificators = [
            Verificator(
                description = "Yellow Square is less than 4",
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

#5 Check the parity of Blue Triangle
all_criteria.append(
    Criterion(
        id = 5,
        description = "Check the parity of Blue Triangle",
        verificators = [
            Verificator(
                description = "Blue Triangle is even",
                test = lambda x: int(str(x)[0]) % 2 == 0
            ),
            Verificator(
                description = "Blue Triangle is odd",
                test = lambda x: int(str(x)[0]) % 2 == 1
            )
        ]
    )
)

#6 Check the parity of Yellow Square    
all_criteria.append(
    Criterion(
        id = 6,
        description = "Check the parity of Yellow Square",
        verificators = [
            Verificator(
                description = "Yellow Square is even",
                test = lambda x: int(str(x)[1]) % 2 == 0
            ),
            Verificator(
                description = "Yellow Square is odd",
                test = lambda x: int(str(x)[1]) % 2 == 1
            )
        ]
    )
)

#7 Check the parity of Purple Circle
all_criteria.append(
    Criterion(
        id = 7,
        description = "Check the parity of Purple Circle",
        verificators = [
            Verificator(
                description = "Purple Circle is even",
                test = lambda x: int(str(x)[2]) % 2 == 0
            ),
            Verificator(
                description = "Purple Circle is odd",
                test = lambda x: int(str(x)[2]) % 2 == 1
            )
        ]
    )
)

#8 Count the number of 1s
all_criteria.append(
    Criterion(
        id = 8,
        description = "Count the number of 1s",
        verificators = [
            Verificator(
                description = "There are no 1s",
                test = lambda x: str(x).count('1') == 0
            ),
            Verificator(
                description = "There is one 1",
                test = lambda x: str(x).count('1') == 1
            ),
            Verificator(
                description = "There are two 1s",
                test = lambda x: str(x).count('1') == 2
            ),
            Verificator(
                description = "There are three 1s",
                test = lambda x: str(x).count('1') == 3
            )
        ]
    )
)

#9 Count the number of 3s
all_criteria.append(
    Criterion(
        id = 9,
        description = "Count the number of 3s",
        verificators = [
            Verificator(
                description = "There are no 3s",
                test = lambda x: str(x).count('3') == 0
            ),
            Verificator(
                description = "There is one 3",
                test = lambda x: str(x).count('3') == 1
            ),
            Verificator(
                description = "There are two 3s",
                test = lambda x: str(x).count('3') == 2
            ),
            Verificator(
                description = "There are three 3s",
                test = lambda x: str(x).count('3') == 3
            )
        ]
    )
)

#10 Count the number of 4s
all_criteria.append(
    Criterion(
        id = 10,
        description = "Count the number of 4s",
        verificators = [
            Verificator(
                description = "There are no 4s",
                test = lambda x: str(x).count('4') == 0
            ),
            Verificator(
                description = "There is one 4",
                test = lambda x: str(x).count('4') == 1
            ),
            Verificator(
                description = "There are two 4s",
                test = lambda x: str(x).count('4') == 2
            ),
            Verificator(
                description = "There are three 4s",
                test = lambda x: str(x).count('4') == 3
            )
        ]
    )
)

#11 Blue Triangle is compared to Yellow Square
all_criteria.append(
    Criterion(
        id = 11,
        description = "Blue Triangle is compared to Yellow Square",
        verificators = [
            Verificator(
                description = "Blue Triangle is less than Yellow Square",
                test = lambda x: int(str(x)[0]) < int(str(x)[1])
            ),
            Verificator(
                description = "Blue Triangle is equal to Yellow Square",
                test = lambda x: int(str(x)[0]) == int(str(x)[1])
            ),
            Verificator(
                description = "Blue Triangle is greater than Yellow Square",
                test = lambda x: int(str(x)[0]) > int(str(x)[1])
            )
        ]
    )
)

#12 Blue Triangle is compared to Purple Circle
all_criteria.append(
    Criterion(
        id = 12,
        description = "Blue Triangle is compared to Purple Circle",
        verificators = [
            Verificator(
                description = "Blue Triangle is less than Purple Circle",
                test = lambda x: int(str(x)[0]) < int(str(x)[2])
            ),
            Verificator(
                description = "Blue Triangle is equal to Purple Circle",
                test = lambda x: int(str(x)[0]) == int(str(x)[2])
            ),
            Verificator(
                description = "Blue Triangle is greater than Purple Circle",
                test = lambda x: int(str(x)[0]) > int(str(x)[2])
            )
        ]
    )
)

#13 Yellow Square is compared to Purple Circle
all_criteria.append(
    Criterion(
        id = 13,
        description = "Yellow Square is compared to Purple Circle",
        verificators = [
            Verificator(
                description = "Yellow Square is less than Purple Circle",
                test = lambda x: int(str(x)[1]) < int(str(x)[2])
            ),
            Verificator(
                description = "Yellow Square is equal to Purple Circle",
                test = lambda x: int(str(x)[1]) == int(str(x)[2])
            ),
            Verificator(
                description = "Yellow Square is greater than Purple Circle",
                test = lambda x: int(str(x)[1]) > int(str(x)[2])
            )
        ]
    )
)

#14 Check which colour's number is smaller than the others
all_criteria.append(
    Criterion(
        id = 14,
        description = "Check which colour's number is smaller than the others",
        verificators = [
            Verificator(
                description = "Blue Triangle is smaller than Yellow Square and Purple Circle",
                test = lambda x: int(str(x)[0]) < int(str(x)[1]) and int(str(x)[0]) < int(str(x)[2])
            ),
            Verificator(
                description = "Yellow Square is smaller than Blue Triangle and Purple Circle",
                test = lambda x: int(str(x)[1]) < int(str(x)[0]) and int(str(x)[1]) < int(str(x)[2])
            ),
            Verificator(
                description = "Purple Circle is smaller than Blue Triangle and Yellow Square",
                test = lambda x: int(str(x)[2]) < int(str(x)[0]) and int(str(x)[2]) < int(str(x)[1])
            )
        ]
    )
)

#15 Check which colour's number is larger than the others
all_criteria.append(
    Criterion(
        id = 15,
        description = "Check which colour's number is larger than the others",
        verificators = [
            Verificator(
                description = "Blue Triangle is larger than Yellow Square and Purple Circle",
                test = lambda x: int(str(x)[0]) > int(str(x)[1]) and int(str(x)[0]) > int(str(x)[2])
            ),
            Verificator(
                description = "Yellow Square is larger than Blue Triangle and Purple Circle",
                test = lambda x: int(str(x)[1]) > int(str(x)[0]) and int(str(x)[1]) > int(str(x)[2])
            ),
            Verificator(
                description = "Purple Circle is larger than Blue Triangle and Yellow Square",
                test = lambda x: int(str(x)[2]) > int(str(x)[0]) and int(str(x)[2]) > int(str(x)[1])
            )
        ]
    )
)

#16 Compares the number of even and odd numbers
all_criteria.append(
    Criterion(
        id = 16,
        description = "Compares the number of even and odd numbers",
        verificators = [
            Verificator(
                description = "There are more even numbers than odd numbers",
                test = lambda x: sum(int(digit) % 2 == 0 for digit in str(x)) > sum(int(digit) % 2 == 1 for digit in str(x))
            ),
            Verificator(
                description = "There are more odd numbers than even numbers",
                test = lambda x: sum(int(digit) % 2 == 1 for digit in str(x)) > sum(int(digit) % 2 == 0 for digit in str(x))
            )
        ]
    )
)

#17 Count the number of even numbers
all_criteria.append(
    Criterion(
        id = 17,
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

#18 Check the parity of the sum of all numbers
all_criteria.append(
    Criterion(
        id = 18,
        description = "Check the parity of the sum of all numbers",
        verificators = [
            Verificator(
                description = "The sum of all numbers is even",
                test = lambda x: sum(int(digit) for digit in str(x)) % 2 == 0
            ),
            Verificator(
                description = "The sum of all numbers is odd",
                test = lambda x: sum(int(digit) for digit in str(x)) % 2 == 1
            )
        ]
    )
)

#19 The sum of Blue Triangle and Yellow Square is compared to 6
all_criteria.append(
    Criterion(
        id = 19,
        description = "The sum of Blue Triangle and Yellow Square is compared to 6",
        verificators = [
            Verificator(
                description = "The sum of Blue Triangle and Yellow Square is smaller than 6",
                test = lambda x: int(str(x)[0]) + int(str(x)[1]) < 6
            ),
            Verificator(
                description = "The sum of Blue Triangle and Yellow Square is equal to 6",
                test = lambda x: int(str(x)[0]) + int(str(x)[1]) == 6
            ),
            Verificator(
                description = "The sum of Blue Triangle and Yellow Square is greater than 6",
                test = lambda x: int(str(x)[0]) + int(str(x)[1]) > 6
            )
        ]
    )
)

#20 Check if a number is repeated
all_criteria.append(
    Criterion(
        id = 20,
        description = "Check if a number is repeated",
        verificators = [
            Verificator(
                description = "There is a triple number",
                test = lambda x: len(set(str(x))) == 1
            ),
            Verificator(
                description = "There is a double number",
                test = lambda x: len(set(str(x))) == 2
            ),
            Verificator(
                description = "There are no repeated numbers",
                test = lambda x: len(set(str(x))) == 3
            )
        ]
    )
)

#21 Check if a number is present exactly twice
all_criteria.append(
    Criterion(
        id = 21,
        description = "Check if a number is repeated exactly twice",
        verificators = [
            Verificator(
                description = "There is a number repeated exactly twice",
                test = lambda x: len(set(str(x))) == 2
            ),
            Verificator(
                description = "There are no numbers repeated exactly twice",
                test = lambda x: len(set(str(x))) != 2
            )
        ]
    )
)

#22 Check whether the three numbers are in ascending order, descending order or not in order
all_criteria.append(
    Criterion(
        id = 22,
        description = "Check whether the three numbers are in ascending order, descending order or not in order",
        verificators = [
            Verificator(
                description = "The numbers are in ascending order",
                test = lambda x: int(str(x)[0]) < int(str(x)[1]) < int(str(x)[2])
            ),
            Verificator(
                description = "The numbers are in descending order",
                test = lambda x: int(str(x)[0]) > int(str(x)[1]) > int(str(x)[2])
            ),
            Verificator(
                description = "The numbers are not in order",
                test = lambda x: (int(str(x)[0]) - int(str(x)[1])) * (int(str(x)[1]) - int(str(x)[2])) <= 0
            )
        ]
    )
)

#23 The sum of all numbers is compared to 6
all_criteria.append(
    Criterion(
        id = 23,
        description = "The sum of all numbers is compared to 6",
        verificators = [
            Verificator(
                description = "The sum of all numbers is smaller than 6",
                test = lambda x: sum(int(digit) for digit in str(x)) < 6
            ),
            Verificator(
                description = "The sum of all numbers is equal to 6",
                test = lambda x: sum(int(digit) for digit in str(x)) == 6
            ),
            Verificator(
                description = "The sum of all numbers is greater than 6",
                test = lambda x: sum(int(digit) for digit in str(x)) > 6
            )
        ]
    )
)

#24 Check if there is a sequence in consecutive ascending order
all_criteria.append(
    Criterion(
        id = 24,
        description = "Check if there is a sequence in ascending order (consecutive numbers)",
        verificators = [
            Verificator(
                description = "3 consecutive numbers are in ascending order (ex: 234)",
                test = lambda x: set(int(str(x)[1]) - int(str(x)[0]), int(str(x)[2]) - int(str(x)[1])) == {1}
            ),
            Verificator(
                description = "2 consecutive numbers are in ascending order (ex: 233)",
                test = lambda x: 1 in set(int(str(x)[1]) - int(str(x)[0]), int(str(x)[2]) - int(str(x)[1])) and len(set(int(str(x)[1]) - int(str(x)[0]), int(str(x)[2]) - int(str(x)[1]))) == 2
            ),
            Verificator(
                description = "No sequence is in consecutive ascending order (ex: 135)",
                test = lambda x: 1 not in set(int(str(x)[1]) - int(str(x)[0]), int(str(x)[2]) - int(str(x)[1]))
            )
        ]
    )
)

# 25 Check if there is a sequence in consecutive ascending or descending order
all_criteria.append(
    Criterion(
        id = 25,
        description = "Check if there is a sequence in ascending or descending order (consecutive numbers)",
        verificators = [
            Verificator(
                description = "No sequence of consecutive numbers in ascending or descending order (ex: 135, 531)",
                test = lambda x: 1 not in set(abs(int(str(x)[1]) - int(str(x)[0])), abs(int(str(x)[2]) - int(str(x)[1])))
            ),
            Verificator(
                description = "There is a sequence of exactly 2 consecutive numbers in ascending or descending order (ex: 235, 532)",
                test = lambda x: 1 in set(abs(int(str(x)[1]) - int(str(x)[0])), abs(int(str(x)[2]) - int(str(x)[1]))) and len(set(int(str(x)[1]) - int(str(x)[0]), int(str(x)[2]) - int(str(x)[1]))) == 2
            ),
            Verificator(
                description = "There is a sequence of 3 consecutive numbers in ascending or descending order (ex: 234, 432)",
                test = lambda x: 1 in set(abs(int(str(x)[1]) - int(str(x)[0])), abs(int(str(x)[2]) - int(str(x)[1]))) and len(set(int(str(x)[1]) - int(str(x)[0]), int(str(x)[2]) - int(str(x)[1]))) == 1
            )
        ]
    )
)

#26 A specific colour is less than 3
all_criteria.append(
    Criterion(
        id = 26,
        description = "A specific colour is less than 3",
        verificators = [
            Verificator(
                description = "Blue Triangle is less than 3",
                test = lambda x: int(str(x)[0]) < 3
            ),
            Verificator(
                description = "Yellow Square is less than 3",
                test = lambda x: int(str(x)[1]) < 3
            ),
            Verificator(
                description = "Purple Circle is less than 3",
                test = lambda x: int(str(x)[2]) < 3
            )
        ]
    )
)

#27 A specific colour is less than 4
all_criteria.append(
    Criterion(
        id = 27,
        description = "A specific colour is less than 4",
        verificators = [
            Verificator(
                description = "Blue Triangle is less than 4",
                test = lambda x: int(str(x)[0]) < 4
            ),
            Verificator(
                description = "Yellow Square is less than 4",
                test = lambda x: int(str(x)[1]) < 4
            ),
            Verificator(
                description = "Purple Circle is less than 4",
                test = lambda x: int(str(x)[2]) < 4
            )
        ]
    )
)

#28 A specific colour is equal to 1
all_criteria.append(
    Criterion(
        id = 28,
        description = "One number is equal to 1",
        verificators = [
            Verificator(
                description = "Blue Triangle is equal to 1",
                test = lambda x: int(str(x)[0]) == 1
            ),
            Verificator(
                description = "Yellow Square is equal to 1",
                test = lambda x: int(str(x)[1]) == 1
            ),
            Verificator(
                description = "Purple Circle is equal to 1",
                test = lambda x: int(str(x)[2]) == 1
            )
        ]
    )
)

#29 A specific colour is equal to 3
all_criteria.append(
    Criterion(
        id = 29,
        description = "A specific colour is equal to 3",
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

#30 A specific colour is equal to 4
all_criteria.append(
    Criterion(
        id = 30,
        description = "A specific colour is equal to 4",
        verificators = [
            Verificator(
                description = "Blue Triangle is equal to 4",
                test = lambda x: int(str(x)[0]) == 4
            ),
            Verificator(
                description = "Yellow Square is equal to 4",
                test = lambda x: int(str(x)[1]) == 4
            ),
            Verificator(
                description = "Purple Circle is equal to 4",
                test = lambda x: int(str(x)[2]) == 4
            )
        ]
    )
)

#31 A specific colour is greater than 1
all_criteria.append(
    Criterion(
        id = 31,
        description = "A specific colour is greater than 1",
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

#32 A specific colour is greater than 3
all_criteria.append(
    Criterion(
        id = 32,
        description = "A specific colour is greater than 3",
        verificators = [
            Verificator(
                description = "Blue Triangle is greater than 3",
                test = lambda x: int(str(x)[0]) > 3
            ),
            Verificator(
                description = "Yellow Square is greater than 3",
                test = lambda x: int(str(x)[1]) > 3
            ),
            Verificator(
                description = "Purple Circle is greater than 3",
                test = lambda x: int(str(x)[2]) > 3
            )
        ]
    )
)

#33 Check the parity of a specific colour
all_criteria.append(
    Criterion(
        id = 33,
        description = "Check the parity of a specific colour",
        verificators = [
            Verificator(
                description = "Blue Triangle is even",
                test = lambda x: int(str(x)[0]) % 2 == 0
            ),
            Verificator(
                description = "Blue Triangle is odd",
                test = lambda x: int(str(x)[0]) % 2 == 1
            ),
            Verificator(
                description = "Yellow Square is even",
                test = lambda x: int(str(x)[1]) % 2 == 0
            ),
            Verificator(
                description = "Yellow Square is odd",
                test = lambda x: int(str(x)[1]) % 2 == 1
            ),
            Verificator(
                description = "Purple Circle is even",
                test = lambda x: int(str(x)[2]) % 2 == 0
            ),
            Verificator(
                description = "Purple Circle is odd",
                test = lambda x: int(str(x)[2]) % 2 == 1
            )
        ]
    )
)

#34 A specific colour is smallest, or tied for smallest
all_criteria.append(
    Criterion(
        id = 34,
        description = "One number is smallest, or tied for smallest",
        verificators = [
            Verificator(
                description = "Blue Triangle is smallest (or tied for smallest)",
                test = lambda x: int(str(x)[0]) == min(int(digit) for digit in str(x))
            ),
            Verificator(
                description = "Yellow Square is smallest (or tied for smallest)",
                test = lambda x: int(str(x)[1]) == min(int(digit) for digit in str(x))
            ),
            Verificator(
                description = "Purple Circle is smallest (or tied for smallest)",
                test = lambda x: int(str(x)[2]) == min(int(digit) for digit in str(x))
            )
        ]
    )
)

#35 A specific colour is largest, or tied for largest
all_criteria.append(
    Criterion(
        id = 35,
        description = "A specific colour is largest, or tied for largest",
        verificators = [
            Verificator(
                description = "Blue Triangle is largest (or tied for largest)",
                test = lambda x: int(str(x)[0]) == max(int(digit) for digit in str(x))
            ),
            Verificator(
                description = "Yellow Square is largest (or tied for largest)",
                test = lambda x: int(str(x)[1]) == max(int(digit) for digit in str(x))
            ),
            Verificator(
                description = "Purple Circle is largest (or tied for largest)",
                test = lambda x: int(str(x)[2]) == max(int(digit) for digit in str(x))
            )
        ]
    )
)

#36 The sum of all numbers is a multiple of 3, 4 or 5
all_criteria.append(
    Criterion(
        id = 36,
        description = "The sum of all numbers is a multiple of 3, 4 or 5",
        verificators = [
            Verificator(
                description = "The sum of all numbers is a multiple of 3",
                test = lambda x: sum(int(digit) for digit in str(x)) % 3 == 0
            ),
            Verificator(
                description = "The sum of all numbers is a multiple of 4",
                test = lambda x: sum(int(digit) for digit in str(x)) % 4 == 0
            ),
            Verificator(
                description = "The sum of all numbers is a multiple of 5",
                test = lambda x: sum(int(digit) for digit in str(x)) % 5 == 0
            )
        ]
    )
)

#37 The sum of two specific colours is equal to 4
all_criteria.append(
    Criterion(
        id = 37,
        description = "The sum of two specific colours is equal to 4",
        verificators = [
            Verificator(
                description = "The sum of Blue Triangle and Yellow Square is equal to 4",
                test = lambda x: int(str(x)[0]) + int(str(x)[1]) == 4
            ),
            Verificator(
                description = "The sum of Blue Triangle and Purple Circle is equal to 4",
                test = lambda x: int(str(x)[0]) + int(str(x)[2]) == 4
            ),
            Verificator(
                description = "The sum of Yellow Square and Purple Circle is equal to 4",
                test = lambda x: int(str(x)[1]) + int(str(x)[2]) == 4
            )
        ]
    )
)

#38 The sum of two specific colours is equal to 6
all_criteria.append(
    Criterion(
        id = 38,
        description = "The sum of two specific colours is equal to 6",
        verificators = [
            Verificator(
                description = "The sum of Blue Triangle and Yellow Square is equal to 6",
                test = lambda x: int(str(x)[0]) + int(str(x)[1]) == 6
            ),
            Verificator(
                description = "The sum of Blue Triangle and Purple Circle is equal to 6",
                test = lambda x: int(str(x)[0]) + int(str(x)[2]) == 6
            ),
            Verificator(
                description = "The sum of Yellow Square and Purple Circle is equal to 6",
                test = lambda x: int(str(x)[1]) + int(str(x)[2]) == 6
            )
        ]
    )
)

#39 A specific colour is compared to 1
all_criteria.append(
    Criterion(
        id = 39,
        description = "A specific colour is compared to 1",
        verificators = [
            Verificator(
                description = "Blue Triangle is equal to 1",
                test = lambda x: int(str(x)[0]) == 1
            ),
            Verificator(
                description = "Blue Triangle is greater than 1",
                test = lambda x: int(str(x)[0]) > 1
            ),
            Verificator(
                description = "Yellow Square is equal to 1",
                test = lambda x: int(str(x)[1]) == 1
            ),
            Verificator(
                description = "Yellow Square is greater than 1",
                test = lambda x: int(str(x)[1]) > 1
            ),
            Verificator(
                description = "Purple Circle is equal to 1",
                test = lambda x: int(str(x)[2]) == 1
            ),
            Verificator(
                description = "Purple Circle is greater than 1",
                test = lambda x: int(str(x)[2]) > 1
            )
        ]
    )
)

#40 A specific colour is compared to 3
all_criteria.append(
    Criterion(
        id = 40,
        description = "A specific colour is compared to 3",
        verificators = [
            Verificator(
                description = "Blue Triangle is less than 3",
                test = lambda x: int(str(x)[0]) < 3
            ),
            Verificator(
                description = "Blue Triangle is equal to 3",
                test = lambda x: int(str(x)[0]) == 3
            ),
            Verificator(
                description = "Blue Triangle is greater than 3",
                test = lambda x: int(str(x)[0]) > 3
            ),
            Verificator(
                description = "Yellow Square is less than 3",
                test = lambda x: int(str(x)[1]) < 3
            ),
            Verificator(
                description = "Yellow Square is equal to 3",
                test = lambda x: int(str(x)[1]) == 3
            ),
            Verificator(
                description = "Yellow Square is greater than 3",
                test = lambda x: int(str(x)[1]) > 3
            ),
            Verificator(
                description = "Purple Circle is less than 3",
                test = lambda x: int(str(x)[2]) < 3
            ),
            Verificator(
                description = "Purple Circle is equal to 3",
                test = lambda x: int(str(x)[2]) == 3
            ),
            Verificator(
                description = "Purple Circle is greater than 3",
                test = lambda x: int(str(x)[2]) > 3
            )
        ]
    )
)

#41 A specific colour is compared to 4
all_criteria.append(
    Criterion(
        id = 41,
        description = "A specific colour is compared to 4",
        verificators = [
            Verificator(
                description = "Blue Triangle is less than 4",
                test = lambda x: int(str(x)[0]) < 4
            ),
            Verificator(
                description = "Blue Triangle is equal to 4",
                test = lambda x: int(str(x)[0]) == 4
            ),
            Verificator(
                description = "Blue Triangle is greater than 4",
                test = lambda x: int(str(x)[0]) > 4
            ),
            Verificator(
                description = "Yellow Square is less than 4",
                test = lambda x: int(str(x)[1]) < 4
            ),
            Verificator(
                description = "Yellow Square is equal to 4",
                test = lambda x: int(str(x)[1]) == 4
            ),
            Verificator(
                description = "Yellow Square is greater than 4",
                test = lambda x: int(str(x)[1]) > 4
            ),
            Verificator(
                description = "Purple Circle is less than 4",
                test = lambda x: int(str(x)[2]) < 4
            ),
            Verificator(
                description = "Purple Circle is equal to 4",
                test = lambda x: int(str(x)[2]) == 4
            ),
            Verificator(
                description = "Purple Circle is greater than 4",
                test = lambda x: int(str(x)[2]) > 4
            )
        ]
    )
)

#42 A specific colour is the smallest or the largest
all_criteria.append(
    Criterion(
        id = 42,
        description = "A specific colour is the smallest or the largest",
        verificators = [
            Verificator(
                description = "Blue Triangle is the smallest",
                test = lambda x: int(str(x)[0]) < int(str(x)[1]) and int(str(x)[0]) < int(str(x)[2])
            ),
            Verificator(
                description = "Blue Triangle is the largest",
                test = lambda x: int(str(x)[0]) > int(str(x)[1]) and int(str(x)[0]) > int(str(x)[2])
            ),
            Verificator(
                description = "Yellow Square is the smallest",
                test = lambda x: int(str(x)[1]) < int(str(x)[0]) and int(str(x)[1]) < int(str(x)[2])
            ),
            Verificator(
                description = "Yellow Square is the largest",
                test = lambda x: int(str(x)[1]) > int(str(x)[0]) and int(str(x)[1]) > int(str(x)[2])
            ),
            Verificator(
                description = "Purple Circle is the smallest",
                test = lambda x: int(str(x)[2]) < int(str(x)[0]) and int(str(x)[2]) < int(str(x)[1])
            ),
            Verificator(
                description = "Purple Circle is the largest",
                test = lambda x: int(str(x)[2]) > int(str(x)[0]) and int(str(x)[2]) > int(str(x)[1])
            )
        ]
    )
)

#43 Blue Triangle is compared the the number of another specific colour
all_criteria.append(
    Criterion(
        id = 43,
        description = "Blue Triangle is compared the the number of another specific colour",
        verificators = [
            Verificator(
                description = "Blue Triangle is less than Yellow Square",
                test = lambda x: int(str(x)[0]) < int(str(x)[1])
            ),
            Verificator(
                description = "Blue Triangle is equal to Yellow Square",
                test = lambda x: int(str(x)[0]) == int(str(x)[1])
            ),
            Verificator(
                description = "Blue Triangle is greater than Yellow Square",
                test = lambda x: int(str(x)[0]) > int(str(x)[1])
            ),
            Verificator(
                description = "Blue Triangle is less than Purple Circle",
                test = lambda x: int(str(x)[0]) < int(str(x)[2])
            ),
            Verificator(
                description = "Blue Triangle is equal to Purple Circle",
                test = lambda x: int(str(x)[0]) == int(str(x)[2])
            ),
            Verificator(
                description = "Blue Triangle is greater than Purple Circle",
                test = lambda x: int(str(x)[0]) > int(str(x)[2])
            )
        ]
    )
)

#44 Yellow Square is compared the the number of another specific colour
all_criteria.append(
    Criterion(
        id = 44,
        description = "Yellow Square is compared the the number of another specific colour",
        verificators = [
            Verificator(
                description = "Yellow Square is less than Blue Triangle",
                test = lambda x: int(str(x)[1]) < int(str(x)[0])
            ),
            Verificator(
                description = "Yellow Square is equal to Blue Triangle",
                test = lambda x: int(str(x)[1]) == int(str(x)[0])
            ),
            Verificator(
                description = "Yellow Square is greater than Blue Triangle",
                test = lambda x: int(str(x)[1]) > int(str(x)[0])
            ),
            Verificator(
                description = "Yellow Square is less than Purple Circle",
                test = lambda x: int(str(x)[1]) < int(str(x)[2])
            ),
            Verificator(
                description = "Yellow Square is equal to Purple Circle",
                test = lambda x: int(str(x)[1]) == int(str(x)[2])
            ),
            Verificator(
                description = "Yellow Square is greater than Purple Circle",
                test = lambda x: int(str(x)[1]) > int(str(x)[2])
            )
        ]
    )
)

#45 Counts how many 1s are in the code, or how many 3s are in the code
all_criteria.append(
    Criterion(
        id = 45,
        description = "Counts how many 1s are in the code, or how many 3s are in the code",
        verificators = [
            Verificator(
                description = "There are no 1s in the code",
                test = lambda x: str(x).count('1') == 0
            ),
            Verificator(
                description = "There is one 1 in the code",
                test = lambda x: str(x).count('1') == 1
            ),
            Verificator(
                description = "There are two 1s in the code",
                test = lambda x: str(x).count('1') == 2
            ),
            Verificator(
                description = "There are no 3s in the code",
                test = lambda x: str(x).count('3') == 0
            ),
            Verificator(
                description = "There is one 3 in the code",
                test = lambda x: str(x).count('3') == 1
            ),
            Verificator(
                description = "There are two 3s in the code",
                test = lambda x: str(x).count('3') == 2
            )
        ]
    )
)

#46 Counts how many 3s are in the code, or how many 4s are in the code
all_criteria.append(
    Criterion(
        id = 46,
        description = "Counts how many 3s are in the code, or how many 4s are in the code",
        verificators = [
            Verificator(
                description = "There are no 3s in the code",
                test = lambda x: str(x).count('3') == 0
            ),
            Verificator(
                description = "There is one 3 in the code",
                test = lambda x: str(x).count('3') == 1
            ),
            Verificator(
                description = "There are two 3s in the code",
                test = lambda x: str(x).count('3') == 2
            ),
            Verificator(
                description = "There are no 4s in the code",
                test = lambda x: str(x).count('4') == 0
            ),
            Verificator(
                description = "There is one 4 in the code",
                test = lambda x: str(x).count('4') == 1
            ),
            Verificator(
                description = "There are two 4s in the code",
                test = lambda x: str(x).count('4') == 2
            )
        ]
    )
)

#47 Counts how many 1s are in the code, or how many 4s are in the code
all_criteria.append(
    Criterion(
        id = 47,
        description = "Counts how many 1s are in the code, or how many 4s are in the code",
        verificators = [
            Verificator(
                description = "There are no 1s in the code",
                test = lambda x: str(x).count('1') == 0
            ),
            Verificator(
                description = "There is one 1 in the code",
                test = lambda x: str(x).count('1') == 1
            ),
            Verificator(
                description = "There are two 1s in the code",
                test = lambda x: str(x).count('1') == 2
            ),
            Verificator(
                description = "There are no 4s in the code",
                test = lambda x: str(x).count('4') == 0
            ),
            Verificator(
                description = "There is one 4 in the code",
                test = lambda x: str(x).count('4') == 1
            ),
            Verificator(
                description = "There are two 4s in the code",
                test = lambda x: str(x).count('4') == 2
            )
        ]
    )
)
Various board game solver implementations.

# Turing Machine

*"Codes are a puzzle. A game, just like any other game."* - Alan Turing in The Imitation Game.

*Turing Machine is a fascinating and competitive deduction game. It offers a unique experience of questioning a proto-computer that works without electricity or any sort of technology, paving the way for a new generation of deduction games.*

*The Goal? Find the secret code before the other players, by cleverly questioning the machine. With Turing Machine, you’ll use an analog computer with unique components made of never-before-seen perforated cards.*
*The game offers more than seven million problems from simple to mind-staggeringly complex combinations, making the gameplay practically endless!*

*Including the original competitive mode, you can combine your brain power as a team or try to beat the game itself while playing solo.*

*Are you ready for an intense cerebral gaming experience?* --- From Board Game Geek.

### Solver Implementation
A set of solution candidates is computed by defining each sub-criterion as the subset of its valid solutions, then looking for intersections of size one using one sub-criterion from each criterion card. Then, all solutions for which one sub-criterion is redundant (intersection remains of size one when removing one of the criteria) are removed, leaving only the candidates that require all cards.

An optimal testing decision tree is computed by recursively building all possible testing trees, then evaluating them based on the expected number of rounds, then tests required. These values are computed assuming uniform distribution of size 1, non-redundant intersections.

# Ricochet Robot

*Still to come...*

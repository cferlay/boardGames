from cards import all_criteria, Criterion, Verificator
from itertools import product

letters = ['A', 'B', 'C', 'D', 'E', 'F']

class Solution:
    def __init__(self, verificators: list[Verificator], value: int):
        self.verificators = verificators
        self.value = value
    
    def __str__(self):
        string = f"\nSolution: {self.value}"
        for i, verificator in enumerate(self.verificators):
            string += f"\n{letters[i]}: {verificator.description}"
        return string

class DecisionTree:
    def __init__(self, value: int, letter: str = None, left: 'DecisionTree' = None, right: 'DecisionTree' = None, prob_left: float = None, prob_right: float = None):
        self.value = value
        self.letter = letter
        self.left = left
        self.right = right
        self.prob_left = prob_left
        self.prob_right = prob_right

    def __str__(self):
        if self.letter is None:
            return f"{self.value}"
        text = []
        if self.left is not None:
            left = str(self.left).split('\n')
        else:
            left = ['']
        right = [''] if self.right is None else str(self.right).split('\n')
        if len(left) > len(right):
            right += [' ' * len(right[0])] * (len(left) - len(right))
        if len(right) > len(left):
            left += [' ' * len(left[0])] * (len(right) - len(left))

        length = len(left[0])+len(right[0])+1
        left_i = left[0].index('-') if '-' in left[0] else 1
        right_i = len(left[0]) + 1 + (right[0].index('-') if '-' in right[0] else 1)
        root_i = (left_i+right_i)//2

        text.append(' '*(root_i-3) + f" {self.value}-{self.letter} "+' '*(length-(root_i-3)-5))
        text.append(' '*(root_i)+' │ '+' '*(length-root_i-1))
        text.append(' '*(left_i)+'┌'+'─'*(root_i-left_i-1)+'─┴─'+'─'*(right_i-root_i-1)+'┐'+' '*(length-right_i-1))
        text.append(' '*(left_i)+'│'+' '*(root_i-left_i-1)+'   '+' '*(right_i-root_i-1)+'│'+' '*(length-right_i-1))
        text.append(' '*(left_i)+'✓'+' '*(root_i-left_i-1)+'   '+' '*(right_i-root_i-1)+'X'+' '*(length-right_i-1))
        
        for i in range(len(left)):
            text.append(f"{left[i]}   {right[i]}")

        return '\n'.join(text)

    #def score(self):
    #    return 0 if self.letter is None else self.prob_left*self.left.score() + self.prob_right*self.right.score() + 1

    def paths(self):
        if self.letter is None:
            return [([],1)]
        paths = []
        for path, prob in self.left.paths():
            paths.append(([self.value] + path, prob*self.prob_left))
        for path, prob in self.right.paths():
            paths.append(([self.value] + path, prob*self.prob_right))
        return paths

    def score(self):
        def aux(path: list[int]):
            length = 1
            prev = path[0]
            group_count = 1
            for val in path[1:]:
                if val == prev:
                    group_count += 1
                    if group_count > 3:
                        length += 1
                        group_count = 1
                else:
                    length += 1
                    prev = val
                    group_count = 1
            return length
        paths = self.paths()
        return (sum(aux(path)*prob for path, prob in paths), sum(len(path)*prob for path, prob in paths), min(len(path) for path, _ in paths))
        

def treeList(criteria: list[Criterion], solutions: list[Solution], current_test: int = None):
    all_trees = []
    for solution in [current_test]+solutions:
        if solution is None: continue
        for c, criterion in enumerate(criteria):
            verificators = [v for v in criterion.verificators if v.test(solution.value)]
            left_solutions = [s for s in solutions if s.verificators[c] in verificators]
            right_solutions = [s for s in solutions if s.verificators[c] not in verificators]
            prob_left = len(left_solutions)/len(solutions)
            prob_right = len(right_solutions)/len(solutions)
            if len(left_solutions) == 0 or len(right_solutions) == 0: #Useless test: ignore
                continue
            if len(list(set(s.value for s in left_solutions))) == 1: #Single option remains: solution found
                left_trees = [DecisionTree(left_solutions[0].value)]
            else:
                left_trees = treeList(criteria, left_solutions, solution)
            if len(list(set(s.value for s in right_solutions))) == 1: #Single option remains: solution found
                right_trees = [DecisionTree(right_solutions[0].value)]
            else:
                right_trees = treeList(criteria, right_solutions, solution)
            for left_tree in left_trees:
                for right_tree in right_trees:
                    all_trees.append(DecisionTree(solution.value, letters[c], left_tree, right_tree, prob_left, prob_right))
    return all_trees


class Problem:
    def __init__(self, id: str, criteria: list[int]):
        self.id = id
        self.criteria = [all_criteria[i] for i in criteria]

    def solve(self, verbose = 0):
       
        #Find all verificator combinations that have a unique solution
        #Filter out verificator combinations that have a redundant verificator
        n_uniques = 0
        solutions = []
        verificators_lists = [criteria.verificators for criteria in self.criteria]
        if verbose >= 3:
            print("\nFINDING UNIQUE SOLUTIONS & ELIMINATING REDUNDANT SOLUTIONS ##########################################################")
        for verificator_combo in product(*verificators_lists):
            valid_sets = [set(v.valid_values) for v in verificator_combo]
            intersection = set.intersection(*valid_sets)
            if len(intersection) == 1:
                n_uniques += 1
                redundancy = False
                for i in range(len(verificator_combo)):
                    sets_without_i = [valid_sets[j] for j in range(len(valid_sets)) if j != i]
                    intersection_without_i = set.intersection(*sets_without_i)
                    if len(intersection_without_i) == 1:
                        redundancy = True
                        if verbose >= 3:
                            print(Solution(verificator_combo, int(list(intersection)[0])))
                            print(f"Redundant verificator: {verificator_combo[i].description}\n")
                        break
                if not redundancy:
                    solutions.append(Solution(verificator_combo, int(list(intersection)[0])))

        
        if verbose >= 2:
            print("\nAVAILABLE SOLUTIONS ##########################################################################################")
            for solution in solutions:
                print(solution)
            
            print("\nCRITERIA OPTIONS ##########################################################################################\n")
            for i in range(len(self.criteria)):
                print(f"{letters[i]}: {', '.join(list(set(solution.verificators[i].description for solution in solutions)))}")

            print("\nSOLVING FOR OPTIMAL TREE... \n")
        
        #Build all possible decision trees; choose the one with the least absolute & average depth
        trees = treeList(self.criteria, solutions)
        trees.sort(key=lambda x: (round(x.score()[0], 2), round(x.score()[1], 2), round(x.score()[2], 2))) #Round due to floating point precision errors

        if verbose >= 1:
            print(f"Number of unique solutions: {n_uniques}")
            print(f"Number of non-redundant solutions: {len(set(solution.value for solution in solutions))} ({', '.join(list(set(str(solution.value) for solution in solutions)))})")
            print(f"{len(trees)} trees considered.")
            
        print("\nBest decision tree:")
        print(trees[0])
        print(f"Average: {trees[0].score()[0]:.2f} rounds, {trees[0].score()[1]:.2f} tests")
        
        return trees[0]


        
pb = Problem("test", [0, 1, 2, 3, 4])
pb.solve(verbose = 3)

#To solve: When test is false, value is removed from pool, despite the fact that it can still be used for remaining tests
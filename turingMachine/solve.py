from problem import Problem
from argparse import ArgumentParser

parser = ArgumentParser(description="Solve the Turing Machine problem with given criteria indices.")
parser.add_argument('criteria', nargs='+', type=int, help='List of criteria indices')
parser.add_argument('--verbose', '-v', type=int, default=0, help='Verbosity level')
parser.add_argument('--id', type=str, default="", help='Problem ID')
args = parser.parse_args()

problem = Problem(args.id, args.criteria)
problem.solve(verbose=args.verbose)
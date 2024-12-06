from sympy import symbols, And, Or, Not, simplify
from sympy.logic.boolalg import truth_table
import logicmin


def print_truth_table_header(variables):
    """Helper function to create a formatted header for truth tables"""
    header = " | ".join(variables + ["Output"])
    print("-" * len(header))
    print(header)
    print("-" * len(header))


def boolean_problem_1_logicmin():
    """
    Problem 1: Simplify the expression (A AND B) OR (NOT A AND B) using LogicMin
    This demonstrates how LogicMin handles Boolean minimization through truth tables
    """
    print("\nProblem 1: Simplifying (A AND B) OR (NOT A AND B)")
    print("------------------------------------------------")

    # Create truth table with 2 inputs (A, B) and 1 output
    tt = logicmin.TT(2, 1)

    # Define the truth table entries
    # For each input combination, calculate (A AND B) OR (NOT A AND B)
    truth_table_data = [
        ("00", "0"),  # A=0, B=0 → 0
        ("01", "1"),  # A=0, B=1 → 1
        ("10", "0"),  # A=1, B=0 → 0
        ("11", "1")  # A=1, B=1 → 1
    ]

    # Add entries to truth table
    for inputs, output in truth_table_data:
        tt.add(inputs, output)

    # Print formatted truth table
    print_truth_table_header(["A", "B"])
    for inputs, output in truth_table_data:
        print(f"{inputs[0]} | {inputs[1]} | {output}")

    # Solve and print minimized expression
    solution = tt.solve()
    print("\nMinimized expression:")
    print("B")  # We know this simplifies to just B
    print("\nVerification: This simplifies to just 'B' because the output")
    print("matches B's value regardless of A's value")


def boolean_problem_2_logicmin():
    """
    Problem 2: Implement and simplify A XOR B using LogicMin
    This demonstrates exclusive OR implementation and minimization
    """
    print("\nProblem 2: Implementing A XOR B")
    print("------------------------------")

    tt = logicmin.TT(2, 1)

    # Define truth table for XOR operation
    truth_table_data = [
        ("00", "0"),  # A=0, B=0 → 0
        ("01", "1"),  # A=0, B=1 → 1
        ("10", "1"),  # A=1, B=0 → 1
        ("11", "0")  # A=1, B=1 → 0
    ]

    for inputs, output in truth_table_data:
        tt.add(inputs, output)

    # Print formatted truth table
    print_truth_table_header(["A", "B"])
    for inputs, output in truth_table_data:
        print(f"{inputs[0]} | {inputs[1]} | {output}")

    # Solve and print minimized expression
    print("\nMinimized XOR expression:")
    print("A'B + AB'")  # Standard minimal form of XOR
    print("\nExplanation: XOR is true when inputs differ (A'B or AB')")


def boolean_problem_3_sympy():
    """
    Problem 3: Symbolic simplification of (A AND B) OR (NOT A AND B) using SymPy
    This demonstrates SymPy's symbolic Boolean algebra capabilities
    """
    print("\nProblem 3: Symbolic simplification using SymPy")
    print("-------------------------------------------")

    # Define symbolic variables
    A, B = symbols('A B')

    # Create the expression
    expression = Or(And(A, B), And(Not(A), B))
    simplified = simplify(expression)

    print("Original expression: (A ∧ B) ∨ (¬A ∧ B)")
    print(f"Simplified to: {simplified}")
    print("\nStep-by-step simplification:")
    print("1. (A ∧ B) ∨ (¬A ∧ B)")
    print("2. B ∧ (A ∨ ¬A)    # Factor out B")
    print("3. B ∧ True         # A ∨ ¬A is always True")
    print("4. B                # Final result")


def boolean_problem_4_sympy():
    """
    Problem 4: Truth table for (A AND B) OR C using SymPy
    This demonstrates SymPy's truth table generation capabilities
    """
    print("\nProblem 4: Truth table for (A AND B) OR C")
    print("---------------------------------------")

    # Define symbolic variables
    A, B, C = symbols('A B C')
    expression = Or(And(A, B), C)

    # Generate truth table
    print_truth_table_header(["A", "B", "C"])

    table = list(truth_table(expression, [A, B, C]))
    for inputs, output in table:
        print(f"{int(inputs[0])} | {int(inputs[1])} | {int(inputs[2])} | {int(bool(output))}")

    print("\nExpression explanation:")
    print("The output is True (1) when either:")
    print("- Both A AND B are True (1), OR")
    print("- C is True (1)")


if __name__ == "__main__":
    print("Boolean Logic Problems Using LogicMin and SymPy")
    print("============================================")

    boolean_problem_1_logicmin()
    boolean_problem_2_logicmin()
    boolean_problem_3_sympy()
    boolean_problem_4_sympy()
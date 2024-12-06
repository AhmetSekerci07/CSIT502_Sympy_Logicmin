from sympy import symbols, And, Or, Not, simplify, Xor
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
    Problem 1: Design a 3-input majority circuit
    A majority circuit outputs 1 when most inputs are 1
    This is useful in voting systems and fault-tolerant design
    """
    print("\nProblem 1: Three-Input Majority Circuit")
    print("------------------------------------")

    # Create truth table with 3 inputs (A, B, C) and 1 output
    tt = logicmin.TT(3, 1)

    # Define truth table for majority function
    # Output is 1 when two or more inputs are 1
    truth_table_data = [
        ("000", "0"),  # No 1s
        ("001", "0"),  # One 1
        ("010", "0"),  # One 1
        ("100", "0"),  # One 1
        ("011", "1"),  # Two 1s
        ("101", "1"),  # Two 1s
        ("110", "1"),  # Two 1s
        ("111", "1")  # Three 1s
    ]

    for inputs, output in truth_table_data:
        tt.add(inputs, output)

    print("Truth Table for Majority Function:")
    print_truth_table_header(["A", "B", "C"])
    for inputs, output in truth_table_data:
        print(f"{inputs[0]} | {inputs[1]} | {inputs[2]} | {output}")

    print("\nMinimized expression:")
    print("AB + BC + AC")
    print("\nExplanation: Output is 1 when at least 2 inputs are 1")
    print("This is used in voting circuits and error detection")


def boolean_problem_2_logicmin():
    """
    Problem 2: Design a 4-bit even parity generator
    Parity is used for error detection in digital communication
    """
    print("\nProblem 2: Four-Bit Even Parity Generator")
    print("--------------------------------------")

    tt = logicmin.TT(4, 1)

    # Generate truth table for even parity
    # Output should be 1 when number of 1s is odd (to make total even)
    def count_ones(binary_str):
        return sum(1 for bit in binary_str if bit == '1')

    truth_table_data = []
    for i in range(16):  # 4 bits = 16 combinations
        inputs = format(i, '04b')  # Convert to 4-bit binary
        # Output 1 if odd number of 1s (to make total even)
        output = "1" if count_ones(inputs) % 2 == 1 else "0"
        truth_table_data.append((inputs, output))

    for inputs, output in truth_table_data:
        tt.add(inputs, output)

    print("Truth Table (showing first 8 rows):")
    print_truth_table_header(["A", "B", "C", "D"])
    for inputs, output in truth_table_data[:8]:  # Show first 8 rows
        print(f"{inputs[0]} | {inputs[1]} | {inputs[2]} | {inputs[3]} | {output}")

    print("\nMinimized expression:")
    print("A ⊕ B ⊕ C ⊕ D")
    print("\nExplanation: Output makes total number of 1s even")
    print("This is used for error detection in data transmission")


def boolean_problem_3_sympy():
    """
    Problem 3: Full Adder implementation using SymPy
    Demonstrates symbolic manipulation of a fundamental circuit
    """
    print("\nProblem 3: Full Adder Circuit")
    print("---------------------------")

    # Define symbolic variables
    A, B, Cin = symbols('A B Cin')

    # Define Sum and Carry expressions
    Sum = Xor(Xor(A, B), Cin)
    Cout = Or(And(A, B), And(Cin, Xor(A, B)))

    print("Full Adder Expressions:")
    print(f"Sum = {Sum}")
    print(f"Carry Out = {Cout}")

    # Generate truth table for Sum
    print("\nTruth Table:")
    print_truth_table_header(["A", "B", "Cin"])

    table = list(truth_table(Sum, [A, B, Cin]))
    carry_table = list(truth_table(Cout, [A, B, Cin]))

    for i, ((inputs, sum_out), (_, carry_out)) in enumerate(zip(table, carry_table)):
        a_val = 1 if inputs[0] else 0
        b_val = 1 if inputs[1] else 0
        c_val = 1 if inputs[2] else 0
        s_val = 1 if sum_out else 0
        cout_val = 1 if carry_out else 0
        print(f"{a_val} | {b_val} | {c_val} | {s_val} | {cout_val}")


def boolean_problem_4_sympy():
    """
    Problem 4: 2-to-1 Multiplexer with Enable
    Shows how to implement a common digital building block
    """
    print("\nProblem 4: 2-to-1 Multiplexer with Enable")
    print("-------------------------------------")

    # Define symbolic variables
    A, B, Sel, En = symbols('A B Sel En')

    # Define multiplexer expression:
    # When En=1: Output = Sel ? B : A
    # When En=0: Output = 0
    expression = And(En, Or(And(Sel, B), And(Not(Sel), A)))

    print("Multiplexer Expression:")
    print("Out = En·(Sel·B + Sel'·A)")

    print("\nTruth Table:")
    print_truth_table_header(["En", "Sel", "A", "B"])

    table = list(truth_table(expression, [En, Sel, A, B]))
    for inputs, output in table:
        en_val = 1 if inputs[0] else 0
        sel_val = 1 if inputs[1] else 0
        a_val = 1 if inputs[2] else 0
        b_val = 1 if inputs[3] else 0
        out_val = 1 if output else 0
        print(f"{en_val} | {sel_val} | {a_val} | {b_val} | {out_val}")

    print("\nExplanation:")
    print("- When Enable (En) is 0, output is 0")
    print("- When Enable (En) is 1:")
    print("  * If Sel is 0, output = A")
    print("  * If Sel is 1, output = B")


if __name__ == "__main__":
    print("Advanced Boolean Logic Problems Using LogicMin and SymPy")
    print("================================================")

    boolean_problem_1_logicmin()
    boolean_problem_2_logicmin()
    boolean_problem_3_sympy()
    boolean_problem_4_sympy()
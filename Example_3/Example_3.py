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
    Problem 1: 4-bit Binary to Gray Code Converter
    Converts binary numbers to Gray code, where consecutive numbers
    differ by only one bit. Used in rotary encoders and error correction.
    """
    print("\nProblem 1: 4-bit Binary to Gray Code Converter")
    print("------------------------------------------")

    # Create truth table with 4 inputs and 4 outputs
    tt = logicmin.TT(4, 4)

    # Generate binary to Gray code conversion table
    def binary_to_gray(binary):
        # Convert binary number to Gray code
        binary_int = int(binary, 2)
        gray = binary_int ^ (binary_int >> 1)
        return format(gray, '04b')

    # Generate all 4-bit combinations
    truth_table_data = []
    for i in range(16):
        binary = format(i, '04b')
        gray = binary_to_gray(binary)
        truth_table_data.append((binary, gray))

    # Add to truth table
    for inputs, outputs in truth_table_data:
        tt.add(inputs, outputs)

    print("Truth Table (first 8 entries):")
    print_truth_table_header(["B3", "B2", "B1", "B0", "G3", "G2", "G1", "G0"])
    for inputs, outputs in truth_table_data[:8]:
        print(f"{inputs[0]} | {inputs[1]} | {inputs[2]} | {inputs[3]} | "
              f"{outputs[0]} | {outputs[1]} | {outputs[2]} | {outputs[3]}")

    print("\nGray Code Conversion Rules:")
    print("G3 = B3")
    print("G2 = B3 ⊕ B2")
    print("G1 = B2 ⊕ B1")
    print("G0 = B1 ⊕ B0")
    print("\nThis is used in rotary encoders and error correction systems")


def boolean_problem_2_logicmin():
    """
    Problem 2: 7-Segment Display Decoder (for digit '2')
    Implements logic for displaying the number '2' on a 7-segment display
    with blanking input and error detection
    """
    print("\nProblem 2: 7-Segment Display Decoder with Blanking")
    print("---------------------------------------------")

    # 5 inputs: 4 BCD inputs + 1 blanking input
    # 7 outputs: segments a-g
    tt = logicmin.TT(5, 7)

    # Define segment patterns for digit '2'
    # Segments: a b c d e f g
    #  a_
    # f |b
    #  g_
    # e |c
    #  d_

    def get_segments(bcd_input, blanking):
        if blanking == '1':  # If blanking is active, all segments off
            return "0000000"

        bcd_value = int(bcd_input, 2)
        if bcd_value == 2:  # Pattern for '2': a,b,g,e,d
            return "1101101"
        return "0000000"  # All other numbers are blank for this example

    # Generate truth table
    truth_table_data = []
    for i in range(32):  # 5 inputs = 32 combinations
        inputs = format(i, '05b')  # 4 BCD + 1 blanking
        bcd = inputs[:4]
        blanking = inputs[4]
        outputs = get_segments(bcd, blanking)
        truth_table_data.append((inputs, outputs))
        tt.add(inputs, outputs)

    print("Truth Table (showing pattern for digit '2'):")
    print_truth_table_header(["D3", "D2", "D1", "D0", "BL", "a", "b", "c", "d", "e", "f", "g"])
    # Show only relevant entries
    for inputs, outputs in truth_table_data:
        if inputs[:4] == "0010":  # Show entry for digit 2
            print(f"{inputs[0]} | {inputs[1]} | {inputs[2]} | {inputs[3]} | {inputs[4]} | "
                  f"{outputs[0]} | {outputs[1]} | {outputs[2]} | {outputs[3]} | "
                  f"{outputs[4]} | {outputs[5]} | {outputs[6]}")

    print("\nSegment activation for digit '2':")
    print("a: top horizontal")
    print("b: top right vertical")
    print("d: bottom horizontal")
    print("e: bottom left vertical")
    print("g: middle horizontal")


def boolean_problem_3_sympy():
    """
    Problem 3: 4-bit Magnitude Comparator
    Compares two 4-bit numbers and indicates if A > B, A = B, or A < B
    """
    print("\nProblem 3: 4-bit Magnitude Comparator")
    print("----------------------------------")

    # Define symbolic variables for two 4-bit numbers
    A3, A2, A1, A0, B3, B2, B1, B0 = symbols('A3 A2 A1 A0 B3 B2 B1 B0')

    # Define comparison logic for A > B
    greater_than = Or(
        And(A3, Not(B3)),
        And(A3.equals(B3), A2, Not(B2)),
        And(A3.equals(B3), A2.equals(B2), A1, Not(B1)),
        And(A3.equals(B3), A2.equals(B2), A1.equals(B1), A0, Not(B0))
    )

    # Define equality comparison
    equal_to = And(
        A3.equals(B3),
        A2.equals(B2),
        A1.equals(B1),
        A0.equals(B0)
    )

    print("Comparator Logic Expressions:")
    print("\nA > B:")
    print("(A3·B3') + (A3≡B3)·(A2·B2') + (A3≡B3)·(A2≡B2)·(A1·B1') + "
          "(A3≡B3)·(A2≡B2)·(A1≡B1)·(A0·B0')")

    print("\nA = B:")
    print("(A3≡B3)·(A2≡B2)·(A1≡B1)·(A0≡B0)")

    print("\nA < B can be derived from ¬(A>B) · ¬(A=B)")

    print("\nExample comparisons:")
    # Show a few example comparisons with simplified values
    print("When A = 1010 and B = 1001:")
    print("A > B: True")
    print("A = B: False")
    print("A < B: False")


def boolean_problem_4_sympy():
    """
    Problem 4: 4-bit Binary Arithmetic Logic Unit (ALU)
    Implements basic arithmetic operations based on operation select inputs
    Operations: ADD, SUBTRACT, INCREMENT, DECREMENT
    """
    print("\nProblem 4: 4-bit Arithmetic Logic Unit")
    print("---------------------------------")

    # Define symbolic variables
    A3, A2, A1, A0 = symbols('A3 A2 A1 A0')  # First operand
    B3, B2, B1, B0 = symbols('B3 B2 B1 B0')  # Second operand
    S1, S0 = symbols('S1 S0')  # Operation select

    print("ALU Operations:")
    print("S1 S0 | Operation")
    print("-------------")
    print("0  0  | ADD")
    print("0  1  | SUBTRACT")
    print("1  0  | INCREMENT A")
    print("1  1  | DECREMENT A")

    # Define carry propagate and generate terms for addition
    def carry_logic(a, b, cin):
        return Or(
            And(a, b),
            And(a, cin),
            And(b, cin)
        )

    # Define sum term
    def sum_logic(a, b, cin):
        return Xor(Xor(a, b), cin)

    print("\nExample operation (ADD):")
    print("Sum0 = A0 ⊕ B0 ⊕ Cin")
    print("Carry1 = A0·B0 + A0·Cin + B0·Cin")

    print("\nControl Logic:")
    print("B input modification based on operation:")
    print("- ADD: B = B")
    print("- SUBTRACT: B = B' (One's complement)")
    print("- INCREMENT: B = 0001")
    print("- DECREMENT: B = 1111 (One's complement of 0001)")

    print("\nThis ALU can perform:")
    print("1. Addition of two 4-bit numbers")
    print("2. Subtraction using two's complement")
    print("3. Increment operation (+1)")
    print("4. Decrement operation (-1)")


if __name__ == "__main__":
    print("Complex Digital Logic Design Problems")
    print("==================================")

    boolean_problem_1_logicmin()
    boolean_problem_2_logicmin()
    boolean_problem_3_sympy()
    boolean_problem_4_sympy()
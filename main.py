def evaluate_solution(solution_output, expected_output):
    return solution_output.strip() == expected_output.strip()


if __name__ == "__main__":
    generated_output = "42"
    expected_output = "42"

    result = evaluate_solution(generated_output, expected_output)

    print("Pass" if result else "Fail")

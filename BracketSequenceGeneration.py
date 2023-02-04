def generate_bracket_sequence(size, str, open, close, answer):
    if open == size and close == size:
        answer.append(str)
        return
    if open < size:
        generate_bracket_sequence(size, str + "(", open + 1, close, answer)
    if open > close:
        generate_bracket_sequence(size, str + ")", open, close + 1, answer)

n = int(input())
answer = []
generate_bracket_sequence(n, "", 0, 0, answer)
print("\n".join(answer))

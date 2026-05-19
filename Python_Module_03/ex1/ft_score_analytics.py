import sys


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    arguments = []
    for i in range(1, len(sys.argv)):
        try:
            arg = int(sys.argv[i])
            arguments.append(arg)
        except ValueError:
            print(f"Invalid parameter: '{sys.argv[i]}'")
    if (len(arguments) == 0):
        print("No socres provided. Usage: python3"
              " ft_score_analytics.py <score1> <score2> ...")
    else:
        print(f"Scores processed: {arguments}")
        print(f"Total players: {len(arguments)}")
        print(f"Total score: {sum(arguments)}")
        print(f"Average score: {sum(arguments)/len(arguments)}")
        print(f"High score: {max(arguments)}")
        print(f"Low score: {min(arguments)}")
        print(f"Score range: {max(arguments) - min(arguments)}")

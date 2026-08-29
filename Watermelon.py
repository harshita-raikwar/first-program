import sys


def solve():
  # Read the weight w from standard input
  w = int(sys.stdin.read().strip())

  # Check if w is even and strictly greater than 2
  if w > 2 and w % 2 == 0:
    print("YES")
  else:
    print("NO")


if __name__ == "__main__":
  solve()

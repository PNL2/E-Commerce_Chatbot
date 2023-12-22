def Components(n, d, x, a, b, t):
    from collections import defaultdict

    def find_failing_components(dependencies, component, time_left):
        visited = set()
        stack = [component]
        count = 0
        max_time = float('-inf')

        while stack:
            current_component = stack.pop()
            if current_component not in visited:
                visited.add(current_component)
                count += 1
                max_time = max(max_time, time_left[current_component])

                for dep_component, t in dependencies[current_component]:
                    if dep_component not in visited:
                        if time_left[dep_component] >= t:
                            stack.append(dep_component)
                        else:
                            stack.append(dep_component)
                            time_left[dep_component] = t

        return count, max_time

    dependencies = defaultdict(list)
    time_left = {i: float('inf') for i in range(1, n + 1)}

    for i in range(d):
        dependencies[a[i]].append((b[i], t[i]))

    failing_components, last_component_time = find_failing_components(dependencies, x, time_left)
    return failing_components, last_component_time


def main():
    S = input().split()
    n = int(S[0])
    d = int(S[1])
    x = int(S[2])

    a = []
    b = []
    t = []

    for i in range(d):
        P = input().split()
        a.append(int(P[0]))
        b.append(int(P[1]))
        t.append(int(P[2]))

    result = Components(n, d, x, a, b, t)
    print(result)  # Modify this line to display the output properly

if __name__ == "__main__":
    main()

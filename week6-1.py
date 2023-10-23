from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque([(i, p) for i, p in enumerate(priorities)])

    while queue:
        doc = queue.popleft()
        if any(doc[1] < q[1] for q in queue):
            queue.append(doc)
        else:
            answer += 1
            if doc[0] == location:
                break

    return answer

if __name__ == "__main__":
    priorities = [2, 1, 3, 2]
    location = 2
    print(solution(priorities, location))

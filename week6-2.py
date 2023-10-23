from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        price = prices.popleft()
        count = 0
        for p in prices:
            count += 1
            if price > p:
                break
        answer.append(count)
    return answer

if __name__ == "__main__":
    prices = [1000, 2000, 3000, 2000, 3000]
    print("prices")
    print(prices)
    print("result")
    print(solution(prices))

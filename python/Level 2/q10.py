import collections


def solution(cacheSize: int, cities: list):
    """캐시"""
    cache = collections.deque(maxlen=cacheSize)

    total_time = 0
    for city in [city.lower() for city in cities]:
        if city in cache:
            total_time += 1
            cache.remove(city)
            cache.append(city)

        else:
            total_time += 5
            cache.append(city)
    return total_time


if __name__ == "__main__":
    print(
        solution(
            0,
            ["LA", "LA"],
        )
    )

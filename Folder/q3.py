def find_overloaded_users(events):
    """
    Identify users with 3+ events within any 10-second window.
    """
    from collections import defaultdict
    
    user_events = defaultdict(list)

    # Group events by user
    for user, ts in events:
        user_events[user].append(ts)

    overloaded = set()

    # Check each user's timestamps
    for user, timestamps in user_events.items():
        timestamps.sort()
        n = len(timestamps)

        # Sliding window: i = start, j = end
        i = 0
        for j in range(n):
            # Shrink window until it fits within < 10 seconds
            while timestamps[j] - timestamps[i] >= 10:
                i += 1
            # Check count: j - i + 1 events in window
            if (j - i + 1) >= 3:
                overloaded.add(user)
                break

    return overloaded

if __name__ == "__main__":
    events = [
        (1, 10), (1, 12), (1, 18),
        (3, 1), (3, 2), (3, 3)
    ]
    print(find_overloaded_users(events))  # Should print: {1, 3}

    print(find_overloaded_users([]))  # Should print: set()

    print(find_overloaded_users([(1, 1), (1, 20), (1, 40)]))  # Should print: set()

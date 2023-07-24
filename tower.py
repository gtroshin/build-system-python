"""
List of boxes represented as tuples of (height, weight) returns the maximum height of a tower that can be built by
stacking the boxes on top of each other, subject to the constraint that a box can only be stacked on top of another
box if its weight is strictly less than the weight of the box below it and its height is strictly less than the
height of the box below it.

Args:
    boxes (List[Tuple[int, int]]): A list of boxes represented as tuples of (height, weight)

Returns:
    int: The maximum height of a tower that can be built by stacking the boxes on top of each other
"""
def max_tower(boxes):
    # Sort the boxes by height and then by weight
    boxes.sort(key=lambda x: (x[0], x[1]))

    # Initialize dp array to store maximum tower size ending at each box
    dp = [1] * len(boxes)

    # Fill dp[] using a bottom up DP approach
    for i in range(1, len(boxes)):
        for j in range(i):
            # Check if the current box can be stacked upon box j while maintaining the height and weight constraints
            if boxes[i][1] > boxes[j][1] and boxes[i][0] > boxes[j][0] and dp[i] < dp[j] + 1:
                # If stacking the current box on top of box j results in a higher tower, update the maximum tower
                # size at index i
                dp[i] = dp[j] + 1

    # The maximum value in dp[] will be the maximum tower size
    return max(dp)


if __name__ == '__main__':
    boxes = [(1, 1), (2, 2), (3, 3), (2, 1), (4, 5), (5, 6), (7, 8), (8, 9)]
    print(max_tower(boxes))


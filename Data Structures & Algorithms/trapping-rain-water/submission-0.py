class Solution:
    def trap(self, height: List[int]) -> int:
        # Number of bars in the elevation map
        n = len(height)

        # Variables to track the tallest wall seen so far
        # when scanning from the left and from the right
        l_wall = 0
        r_wall = 0

        # l_max[i] will store the maximum height to the LEFT of index i
        # r_max[i] will store the maximum height to the RIGHT of index i
        l_max = [0] * n
        r_max = [0] * n

        # Build l_max and r_max in a single pass
        for i in range(n):
            j = -i - 1

            # Before updating the walls, store the current wall height
            # This ensures we do NOT include height[i] itself
            l_max[i] = l_wall
            r_max[j] = r_wall

            # Update the tallest wall seen so far from each side
            l_wall = max(l_wall, height[i])
            r_wall = max(r_wall, height[j])

        # Total trapped water
        summ = 0

        # Calculate trapped water at each index
        for i in range(n):
            # Water level at index i is limited by the
            # shorter of the tallest walls on each side
            potential = min(l_max[i], r_max[i])

            # Water trapped is the difference between water level
            # and the height of the bar at index i (cannot be negative)
            summ += max(0, potential - height[i])

        return summ

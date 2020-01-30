def trap(self, height):
    if height == None or len(height) == 0: return 0
    water, puddle = 0, 0
    prev = height[0]
    for each in range(1, len(height)):
        if height[each] >= prev:
            water += puddle
            puddle = 0
            prev = height[each]
        else:
            puddle += prev - height[each]
    puddle = 0
    prev = height[-1]
    for each in range(len(height) - 2, -1, -1):

        if height[each] > prev:
            print(water, puddle)
            water += puddle
            puddle = 0
            prev = height[each]
        else:
            puddle += prev - height[each]
    return water

def Problem1(grid, m):
    n = len(grid)
    
    # center se web kitna aage jayega
    stretch = m // 2
    
    maxPakde = -1
    bestCenter = None

    # sirf un tiles par check karenge jahan se web bahar na gire
    for r in range(stretch, n - stretch):
        for c in range(stretch, n - stretch):
            
            # rule ke hisaab se center tile par criminal hona zaruri hai
            if grid[r][c] == 1:
                abhi_ka_count = 0
                
                # ab pura 3x3 box scan maro
                for i in range(r - stretch, r + stretch + 1):
                    for j in range(c - stretch, c + stretch + 1):
                        if grid[i][j] == 1:
                            abhi_ka_count += 1
                
                # naya high score check karna
                if abhi_ka_count > maxPakde:
                    maxPakde = abhi_ka_count
                    
                    # matrix wale index ko cartesian form me flip kar diya
                    bestX = c
                    bestY = n - 1 - r
                    bestCenter = (bestX, bestY)

    return bestCenter, maxPakde


# --- Test wala part ---
exampleGrid = [
 [1, 0, 0, 0, 1],
 [1, 0, 1, 1, 1],
 [1, 1, 0, 1, 1],
 [1, 0, 1, 1, 0],
 [0, 1, 0, 1, 1]
]
m = 3

# Function call kiya aur values variables me save ki
launchSpot, max_captured = Problem1(exampleGrid, m)

# Ekdum exact wahi output format jo chahiye

print(f"Best launch coordinate: {launchSpot}")
print(f"Maximum criminals captured: {max_captured}")
print("Coordinates are Cartesian coordinates, not matrix indices.")
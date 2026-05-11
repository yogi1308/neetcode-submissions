class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            # We only enter the collision check loop if:
            # 1. There is something to collide with (stack)
            # 2. Current asteroid is moving LEFT (< 0)
            # 3. Top asteroid is moving RIGHT (> 0)
            while stack and asteroid < 0 and stack[-1] > 0:
                # Check magnitudes
                diff = asteroid + stack[-1]
                
                if diff < 0:
                    # Stack top is smaller (e.g., stack: [5], ast: -10 -> diff: -5)
                    # The stack top explodes, and we continue the loop to check the next one
                    stack.pop()
                elif diff > 0:
                    # Stack top is larger (e.g., stack: [10], ast: -5 -> diff: 5)
                    # The current asteroid explodes. We break to stop processing it.
                    break
                else:
                    # Magnitudes are equal (e.g., stack: [5], ast: -5 -> diff: 0)
                    # Both explode. Pop the stack top and break.
                    stack.pop()
                    break
            else:
                # The 'else' block of a while loop runs ONLY if the loop
                # completed without hitting a 'break'.
                # This means the asteroid survived all collisions (or had none).
                stack.append(asteroid)
                
        return stack
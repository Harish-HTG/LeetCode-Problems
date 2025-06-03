from collections import deque

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        total_candies = 0
        queue = deque(initialBoxes)  # Boxes we can access
        visited = set()  # Boxes fully processed
        have_boxes = set(initialBoxes)  # Boxes we have (accessible but possibly locked)
        have_keys = set()  # Keys we have collected
        
        while queue:
            box = queue.popleft()
            if box in visited:
                continue
                
            # Check if we can open this box
            can_open = status[box] == 1 or box in have_keys
            if can_open:
                # Collect candies
                total_candies += candies[box]
                visited.add(box)  # Mark as fully processed
                # Collect keys
                for key in keys[box]:
                    have_keys.add(key)
                # Collect contained boxes
                for new_box in containedBoxes[box]:
                    have_boxes.add(new_box)
                    queue.append(new_box)
            
            # Check if any locked boxes can now be opened
            for locked_box in have_boxes:
                if locked_box not in visited and (status[locked_box] == 1 or locked_box in have_keys):
                    queue.append(locked_box)
        
        return total_candies
def isValid(s: str) -> bool:
    queue = []
    closing_elements = [')', '}', ']']
    opening_elements = ['(', '{', '[']
    for bracket in s:
        if bracket in closing_elements:
            if len(queue) == 0 or bracket != queue.pop(0):
                return False
            continue
        if bracket == opening_elements[0]:
            queue.insert(0, closing_elements[0])
            continue
        if bracket == opening_elements[1]:
            queue.insert(0, closing_elements[1])
            continue
        if bracket == opening_elements[2]:
            queue.insert(0, closing_elements[2])
            continue
    return len(queue) == 0

isValid("([)]")
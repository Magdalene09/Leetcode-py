from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students=deque(students)
        sandwiches=deque(sandwiches)
        
        while len(students)>0 and len(sandwiches)>0:
            if students[0]==sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
            else:
                students.append(students.popleft())
                if sandwiches[0] not in students:
                    break
        return len(students)



        

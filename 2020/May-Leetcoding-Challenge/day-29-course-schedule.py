class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict


        c = defaultdict(list)


        for i in prerequisites:
            c[i[0]].append(i[1])


        not_visited,visited,completed = 0,1,2

        courses = [not_visited for _ in range(numCourses)]


        def isdeadlock(course):

            if(courses[course]==visited):
                return True

            elif(courses[course] == completed):
                return False


            courses[course] = visited

            for i in c[course]:

                 if(isdeadlock(i)):
                    return True
            
            courses[course] = completed
            
            return False


        for i in range(numCourses):

            if(isdeadlock(i)):

                return False


        return True





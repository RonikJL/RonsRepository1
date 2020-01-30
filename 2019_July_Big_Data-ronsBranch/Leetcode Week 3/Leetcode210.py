from pip._vendor.msgpack.fallback import xrange

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = {}
        in_degrees = {}

        for i in xrange(numCourses):
            graph[i] = []
            in_degrees[i] = 0
        for c, p in prerequisites:
            graph[p].append(c)
            in_degrees[c] += 1
        curr_courses = [i for i in xrange(numCourses) if in_degrees[i] == 0]
        courses_taken = 0
        course_order = []
        while curr_courses:
            curr_course = curr_courses.pop(0)
            courses_taken += 1
            course_order.append(curr_course)
            for next_course in graph[curr_course]:
                in_degrees[next_course] -= 1
                if in_degrees[next_course] == 0:
                    curr_courses.append(next_course)

        return course_order if courses_taken == numCourses else []

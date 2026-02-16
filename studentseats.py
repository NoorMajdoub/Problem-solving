class Solution(object):
    def minMovesToSeat(self, seats, students):
        idk1=sorted(seats)
        idk2=sorted(students)
        return sum(abs(s - stu) for s, stu in zip(idk1, idk2))

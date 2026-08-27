class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        Otyp= students.count(0)
        Ityp = students.count(1)
        i=0
        while i < len(sandwiches):
            if Otyp==0 and sandwiches[i]==0:
                return Ityp
            if Ityp == 0 and sandwiches[i]==1:
                return Otyp
            if sandwiches[i] == 0:
                Otyp-=1
            if sandwiches[i] ==1:
                Ityp-=1
            i +=1
            
        return 0
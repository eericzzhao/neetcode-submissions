class Solution:
    def dailyTemperatures(self, temperatures:List[int]) -> List[int]:
        resres = [0] * len(temperatures)
        stack = []

        for idx in range(len(temperatures)):
            while stack and temperatures[idx] > temperatures[stack[-1]]:
                prev_day = stack.pop()
                resres[prev_day] = (idx - prev_day)
            stack.append(idx)
        return resres
            
            
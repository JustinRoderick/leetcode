# 165. Compare Version Numbers

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")
        version2 = version2.split(".")
        n = len(version1)
        m = len(version2)
        if n < m:
            for i in range(m-n):
                version1.append("0")
                n += 1
        if m < n:
            for i in range(n-m):
                version2.append("0")
                m += 1

        for i in range(n):
            num1 = int(version1[i])
            num2 = int(version2[i])
            if num1 == num2:
                continue
            if num1 < num2:
                return -1
            else:
                return 1

        return 0
class Solution:
    def countBits(self, n: int) -> List[int]:
        results = [0]
        sigBit = 1
        for i in range(1,n+1):
            if i == sigBit * 2:
                sigBit *= 2
            results.append(results[i-sigBit] + 1)

        return results[:n+1]

        # def countOnes(num):
        #     count = 0

        #     while num:
        #         count += (num % 2)
        #         num = num // 2

        #     return count

        # results = []
        # curr = 0b0
        # oneBit = 0b1
        # for i in range(n+1):
        #     count = countOnes(curr)
        #     results.append(count)
        #     curr += oneBit

        # return results
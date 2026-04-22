import math
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #HLQ: what should be the first coin used?
        #Let G(i) be the minimum # of coins needed to make amount i
        #G(i) = min_{c in coins} {G(i - value(c))}
        #BC: G(0) = 0
        if amount == 0:
            return 0

        G = [-1] * (amount+1)

        def coinChange_dp(a: int):
            if a < 0:
                return math.inf
            if a == 0:
                return 0
            elif G[a] >= 0:
                return G[a]
            else:
                #print(str(a) + ": G[" + str(a) + "]?")
                amounts = [0]*len(coins)
                for i in range(len(coins)):
                    amounts[i] = coinChange_dp(a=a-coins[i])
                    #print(str(a) + ": G[" + str(a-coins[i]) + "] = " + str(amounts[i]))
                best = min(amounts)
                #print(str(a) + ": G[" + str(a) + "] = " + str(best + 1))
                G[a] = best + 1
                return G[a]

        coinChange_dp(a=amount)
        if G[amount] < math.inf:
            return G[amount]
        else:
            return -1
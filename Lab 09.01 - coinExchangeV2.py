def convert_key(data):
    """JSON"""
    return {int(k): v for k, v in data.items()}
 
def coinExchangeV2(amount, coins):
    dp = [None] * (amount + 1)

    dp[0] = (0, {coin: 0 for coin in coins})

    coin_values = sorted(coins, reverse=True)

    for coin in coin_values:

        for _ in range(coins[coin]):

            for i in range(amount, coin - 1, -1):

                if dp[i - coin] is not None:
                    prev_count, prev_dict = dp[i - coin]

                    new_dict = prev_dict.copy()
                    new_dict[coin] += 1
                    new_count = prev_count + 1

                    if dp[i] is None or new_count < dp[i][0]:
                        dp[i] = (new_count, new_dict)

    print("Amount:", amount)

    if dp[amount] is None:
        print("Can not exchange.")
        return

    print("Coin exchange result:")

    total, result = dp[amount]

    for k in coin_values:
        print(f"  {k} baht = {result[k]} coins")

    print("Number of coins:", total)




def main():
    import json
    #   data = convert_key(json.loads(input()))
    amount = int(input())
    coins = json.loads(input())
    coins = {int(k): v for k, v in coins.items()}

    coinExchangeV2(amount, coins)

main()
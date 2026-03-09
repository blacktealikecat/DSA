def convert_key(data):
  """JSON"""
  return {int(k): v for k, v in data.items()}

def coinExchange(amount, coins):

    ten = five = two = one = 0
    used = 0

    print(f"Amount: {amount}")

    while amount > 0:

        if amount >= 10 and coins[10] > 0:
            amount -= 10
            coins[10] -= 1
            ten += 1
            used += 1

        elif amount >= 5 and coins[5] > 0:
            amount -= 5
            coins[5] -= 1
            five += 1
            used += 1

        elif amount >= 2 and coins[2] > 0:
            amount -= 2
            coins[2] -= 1
            two += 1
            used += 1

        elif amount >= 1 and coins[1] > 0:
            amount -= 1
            coins[1] -= 1
            one += 1
            used += 1
            
        else:
            print("Coins are not enough.")
            return
        
    print("Coin exchange result:")
    
    print(f"  10 baht = {ten} coins")
    print(f"  5 baht = {five} coins")
    print(f"  2 baht = {two} coins")
    print(f"  1 baht = {one} coins")
    
    print(f"Number of coins: {ten + five + two + one}")




def main():
    import json
    #   data = convert_key(json.loads(input()))
    amount = int(input())
    coins = convert_key(json.loads(input()))
    coinExchange(amount, coins)

main()
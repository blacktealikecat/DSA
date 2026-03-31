def lcs(s1, s2):
    left, right = 0, len(s1)
    best_len = 0
    best_sub = ""

    while left <= right:
        mid = (left + right) // 2

        seen = set()
        for j in range(len(s2) - mid + 1):
            seen.add(s2[j:j+mid])

        found = False
        for i in range(len(s1) - mid + 1):
            sub = s1[i:i+mid]

            if sub in seen:
                best_len = mid
                best_sub = sub
                found = True
                break
        
        if found:
            left = mid + 1

        else:
            right = mid - 1
    
    if best_len == 0:
        print("No common substring.")

    else:
        print(best_sub)
        print(best_len)

s1 = input().strip()
s2 = input().strip()

lcs(s1, s2)
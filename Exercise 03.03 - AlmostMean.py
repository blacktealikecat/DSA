def main():
    n = int(input())
    
    total = 0
    count = 0
    
    id_data = ""
    score_data = ""
    
    for _ in range(n):
        line = input().strip()
        splited = line.split('\t')
        stdid = next(iter(splited))
        score = float(next(iter(reversed(splited))))
        
        if count == 0:
            id_data = stdid
            score_data = str(score)

        else:
            id_data = id_data + "," + stdid
            score_data = score_data + "," + str(score)
        
        total += score
        count += 1
    
    avg = total / n

    closest = ""
    min_diff = float("inf")
    closest_score = 0.0
    
    id_iter = iter(id_data.split(','))
    score_iter = iter(score_data.split(','))
    
    for _ in range(count):
        stdid = next(id_iter)
        score = float(next(score_iter))
        
        if score <= avg:
            diff = avg - score

            if diff < min_diff:
                min_diff = diff
                closest = stdid
                closest_score = score

    print(f"closest\t{closest_score}".replace("closest", closest))





if __name__ == "__main__":
    main()
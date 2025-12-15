def convert_string_to_tuples(text_in):
    values = text_in.strip('()').split(', ')
    return tuple(map(float, values))

laongdao_data = convert_string_to_tuples(input())
ans = [laongdao_data[1], laongdao_data[0]]
print(tuple(ans))
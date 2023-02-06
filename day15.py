def find_and_insert_data(pokemon,strength):
    findPos = -1
    for i in range(len(pokemon_list)):
        pair = pokemon_list[i]
        if strength>=pair[1]:
            findPos=i
            break
        if findPos == -1:
            findPos = len(pokemon_list)

    insert_data(findPos, [pokemon, strength])
def insert_data(position,pokemon):

    if position<0 or position>len(pokemon_list):
        print("데이터가 삽입할 범위를 벗어났습니다.")
        return
    pokemon_list.append(None)

    for i in range(len(pokemon_list)-1,position,-1):

        pokemon_list[i] = pokemon_list[i - 1]
        pokemon_list[i-1] =None
    pokemon_list[position] = pokemon

pokemon_list = [['피카츄',200],['라이츄',150],['파이리',90],['꼬부기',30],['이상해',15]]


if __name__=="__main__":
    while True:
        data = input("추가할 포켓몬 -->")
        count = int(input("체력 -->"))
        find_and_insert_data(data,count)
        print(pokemon_list)
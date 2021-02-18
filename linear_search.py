def linear_search(array, length, target):
    i = 0
    while i < len(array):
        if (array[i] == target):
            print(str(i) + '番目の要素が一致しました')
            break
        else:
            i += 1
    else:
        print('見つかりませんでした')

if __name__ == '__main__':
    array = [4, 3, 6, 1, 5]
    length = len(array)
    target = 5
    linear_search(array, length, target)

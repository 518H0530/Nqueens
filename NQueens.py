def isSafe(zip, row, col):

    # Nếu hai quận hậu cùng nằm trên một cột =>> Trả về False
    for i in range(N):
        if (zip[i][col] == 'Q'):
            return False

    # Nếu hai quân hậu cùng nằm trên một đường chéo "\" =>> Trả về False
    (i, j) = (row, col)
    while (i >= 0 and j >= 0):
        if (zip[i][j] == 'Q'):
            return False
        i -= 1
        j -= 1

    # Nếu hai quân hậu cùng nằm trên một đường chéo "/" =>> Trả về False
    (i, j) = (row, col)
    while (i >= 0 and j < N):
        if (zip[i][j] == 'Q'):
            return False
        i -= 1
        j += 1

    return True


def nQueen(zip, row=0):
    # Print ra Solution nếu N quân hậu được đặt thành công
    if row == N:
        for i in range(N):
            for j in range(N):
                print(zip[i][j], end=' ')
            print()
        print()
    else:    
        for i in range(N):
            if isSafe(zip, row, i):
            # Đặt quân hậu vào ô
                zip[row][i] = 'Q'
            # recur lại cho hàng tiếp theo
                nQueen(zip, row + 1)

            # backtrack and remove quân hậu
                zip[row][i] = '-'
            

if __name__ == '__main__':
    N = 8
    zip = [['-' for x in range(N)] for y in range(N)]
    nQueen(zip)
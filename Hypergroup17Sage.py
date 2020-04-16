from array import array


from beautifultable import BeautifulTable
import numpy as np

count = 0

# First subtable
table2 = BeautifulTable()
table2.set_style(BeautifulTable.STYLE_COMPACT)

# Second subtable
table3 = BeautifulTable()
table3.set_style(BeautifulTable.STYLE_COMPACT)

table2.append_row(['a22(1)', 0, 'a23(1)', 0, 'a24(1)', 0])
table2.append_row(['a22(2)', 0, 'a23(2)', 0, 'a24(2)', 0])
table2.append_row(['a22(3)', 0, 'a23(3)', 0, 'a24(3)', 0])
table2.append_row(['a22(4)', 0, 'a23(4)', 0, 'a24(4)', 0])

table3.append_row(['a33(1)', 0, 'a34(1)', 0, 'a44(1)', 0])
table3.append_row(['a33(2)', 0, 'a34(2)', 0, 'a44(2)', 0])
table3.append_row(['a33(3)', 0, 'a34(3)', 0, 'a44(3)', 0])
table3.append_row(['a33(4)', 0, 'a34(4)', 0, 'a44(4)', 0])

table = BeautifulTable()

table.append_row([table2])
table.append_row([table3])

#############################################################

def fillChart (n, n2, a22_2, a22_3, a24_2):

    mat = np.zeros((4,4,4))

    # Since a24(3) = n2-a22(3)-a22(2) > 0 and a44(2) > 0
    if (n2 > a22_2):
        a24_3 = n2 - a22_2

        a22_4 = int(n2 / n4) * (n2 - a22_2)  # assign a22(4)
        a23_4 = int(n2 / n4) * (n2 - 2 * a22_2 - 1)  # assign a23(4)
        a24_4 = n2 - a23_4 - a22_4
        a44_2 = n - 4 * n2 + 3 * a22_2 + a22_3
        a44_4 = n4 - 2 * a24_4 - 1

        if a22_4 > 0 and a23_4 > 0 and a24_4 > 0 and a44_2 > 0 and a44_4 > 0:
            table.column_headers = [f"n: {n}, n2: {n2}, a22(2): {a22_2}, a22_3: {a22_3}"]


            mat[0,0,0] = 1
            mat[1,0,1] = 1
            mat[1,1,0] = 1
            mat[2,0,2] = 1
            mat[2,2,0] = 1
            mat[3,0,3] = 1
            mat[3,3,0] = 1



            table2[1][1] = a22_2  # a22(2)
            mat[1,1,1] = a22_2
            table2[2][1] = a22_3  # a22(3)
            mat[2,1,1] = a22_3
            table2[3][1] = a22_4  # a22(4)
            mat[3,1,1] = a22_4

            table2[0][3] = n2     # a23(1)
            mat[0,1,2] = n2
            table2[1][3] = a22_2  # a23(2)
            mat[1,1,2] = a22_2
            table2[2][3] = a22_2  # a23(3)
            mat[2,1,2] = a22_2
            table2[3][3] = a23_4  # a23(4)
            mat[3,1,2] = a23_4

            table2[1][5] = a24_2  # a24(2)
            mat[1,1,3] = a24_2
            table2[2][5] = a24_3  # a24(3)
            mat[2,1,3] = a24_3
            table2[3][5] = a24_4  # a24(4)
            mat[3,1,3] = a24_4

            table3[1][1] = a22_3  # a33(2)
            mat[1,2,2] = a22_3
            table3[2][1] = a22_2  # a33(3)
            mat[2,2,2] = a22_2
            table3[3][1] = a22_4  # a33(4)
            mat[3,2,2] = a22_4

            table3[1][3] = a24_3  # a34(2)
            mat[1,2,3] = a24_3
            table3[2][3] = a24_2  # a34(3)
            mat[2,2,3] = a24_2
            table3[3][3] = a24_4  # a34(4)
            mat[3,2,3] = a24_4

            table3[0][5] = n4  # a44(1)
            mat[0,3,3] = n4
            table3[1][5] = a44_2  # a44(2)
            mat[1,3,3] = a44_2
            table3[2][5] = a44_2  # a44(3)
            mat[2,3,3] = a44_2
            table3[3][5] = a44_4  # a44(4)
            mat[3,3,3] = a44_4

            #print(table)
            print(mat)



########################

# In this hypergroup, a22(3) = 0
# Thus a24(4) = n/2-n2-2

n = int(input("Order: "))

# for n in range (1, 201):
for n2 in range(1, int((n - 1) / 2) + 1):             # n=n4+2n2+1 -> 2n2<=n-1
    n4 = n - 2 * n2 - 1

    if n4 > 0 and (n2 / n4).is_integer():
        for a22_2 in range(1, n2 - 1 + 1):
            a24_2 = n2 - (2 * a22_2) - 1
            if a24_2 > 0:
                a22_3 = 0
                fillChart(n, n2, a22_2, a22_3, a24_2)

# if not (n2 / n4).is_integer():  # If not an int, n2-2a22(2)-1=0, so a22(2)=(n2-1)/2
#     continue
#     if n2 % 2 == 1:
#         a22_2 = int((n2 - 1) / 2)
#         a22_3 = n2 - a22_2
#         a24_2 = n2 - (2 * a22_2) - 1  # should be 0, which means this branch isn't possible
#         fillChart(n, n2, a22_2, a22_3, a24_2)
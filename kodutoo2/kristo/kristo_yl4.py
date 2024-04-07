# leetcode yl


# kogu array summa
# sumOfArr = sum(arr)
#
# # osa summa peaks olema part_sum
# part_sum = sumOfArr / 3
#
# counter = 0
# part_size = 0
# def differentParts(og_arr, part_sum, part_size, counter):
#     part_arr = []
#     for i in og_arr:
#         part_size += i
#         part_arr.append(i)
#         counter += 1
#         if part_size == part_sum:
#             del og_arr[:counter]
#             break
#
#     return part_arr, og_arr
#
# part1, arr = differentParts(arr, part_sum, part_size, counter)
# part2, arr = differentParts(arr, part_sum, part_size, counter)
# part3, arr = differentParts(arr, part_sum, part_size, counter)
#
# print(arr)
#
# if part1 != part2 != part3:
#     flag = True
# elif arr == []:
#     flag = False
#
# print(flag)
arr = [0,2,1,-6,6,-7,9,1,2,0,1]
# arr = [0,2,1,-6,6,7,9,-1,2,0,1]
# arr = [3,3,6,5,-2,2,5,1,-9,4]
# arr = [1,-1,1,-1]
def canThreePartsEqualSum(arr):
    # Arvutan array summa
    sumOfArr = sum(arr)
    # Kui summa ei jagune kolmega ja jääb mingi osa alles, siis pole mõtet edasi teha
    if sumOfArr % 3 != 0:
        return False

    # Jagan summa kolmega, et saada vastav summa mille järgi osasid peaksin leidma
    part_sum = sumOfArr // 3

    current_sum = 0
    found_parts = 0
    for i in arr:
        current_sum += i
        if current_sum == part_sum:
            found_parts += 1
            current_sum = 0

        if found_parts == 3:
            return True

print(canThreePartsEqualSum(arr))
print('有一组不同高度的台阶，有一个整数数组表示，数组中每个数是台阶的高度，'
      '当开始下雨了（雨水足够多）台阶之间的水坑会积水多少呢？ '
      '如下图，可以表示为数组[0,1,0,2,1,0,1,3,2,1,2,1]，返回积水量6。')

print('方法一：（两次遍历）'
      '先在这个数组中找到最大值，然后从左右两边遍历。'
      '以左边为例，只要当前的数字比下一个数字大，那么这个数字的右边就可以存水，'
      '按照这个思路去分析就可以了，右边的也是一样的道理。代码如下：')


def water_volume(arr_list):
    """
    返回积水量
    :param arr_list: 台阶数组
    :return: 返回积水量
    """
    arr_length = len(arr_list)  # 数组的长度
    arr_max = 0  # 定义数组的最大值
    arr_max_pos = 0  # 定义数组最大值的下标

    for i in range(0, arr_length):
        if arr_max < arr_list[i]:
            arr_max = arr_list[i]
            arr_max_pos = i

    arr_max_left = 0  # 定义从最左边开始遍历的极大值
    arr_max_right = 0  # 定义从最右边开始遍历的极大值
    volumes = 0  # 定义容水量

    for j in range(0, arr_max_pos):
        if arr_max_left < arr_list[j]:
            arr_max_left = arr_list[j]
        else:
            volumes += (arr_max_left - arr_list[j])

    for k in range(arr_length - 1, arr_max_pos, -1):
        if arr_max_right < arr_list[k]:
            arr_max_right = arr_list[k]
        else:
            volumes += (arr_max_right - arr_list[k])

    return volumes


arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 6]
res = water_volume(arr)
print(res)


print('方法二：（一次遍历）'
      '整个的原理和方法一是一样的，就是从左右两边同时遍历，这样只用一次就可以实现了。代码如下：')


def water_volume(arr_list):
    """
    返回积水量
    :param arr_list: 台阶数组
    :return: 返回积水量
    """
    arr_length = len(arr_list)  # 数组的长度
    arr_left_pos = 0  # 从左开始遍历的指针的下标
    arr_right_pos = arr_length - 1  # 从右开始遍历的指针的下标
    arr_max_left = arr_list[arr_left_pos]  # 从左开始遍历的过程中的极大值
    arr_max_right = arr_list[arr_right_pos]  # 从右开始遍历的过程中的极大值
    volumes = 0  # 保存容积的变量

    while arr_left_pos < arr_right_pos:
        if arr_max_left < arr_max_right:
            arr_left_pos += 1
            if arr_list[arr_left_pos] >= arr_max_left:
                arr_max_left = arr_list[arr_left_pos]
            else:
                volumes += (arr_max_left - arr_list[arr_left_pos])
        else:
            arr_right_pos -= 1
            # tmp_right = arr_list[arr_right_pos]

            if arr_list[arr_right_pos] >= arr_max_right:
                arr_max_right = arr_list[arr_right_pos]
            else:
                volumes += (arr_max_right - arr_list[arr_right_pos])
    return volumes


arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
res = water_volume(arr)
print(res)






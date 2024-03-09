from world_engine.utils.imports import *


def array_split(array, indicies_or_sections):
    # array = array
    # final_array = []
    # current_index = 0
    # for i in range(len(array) // indicies_or_sections):
    #     list = []
    #     for j in range(indicies_or_sections):
    #         current_index = (i * indicies_or_sections) + j
    #         list.append(array[current_index])
    #     final_array.append(list)
    #     # array.remove(array[(i * indicies_or_sections) + j])
    
    # if (len(final_array) * indicies_or_sections) != len(array):
    #     list = []
    #     current_array += 1
    #     list.append(array[current_index])


    # # if len(array) != 0:
    # #     for i in array:
    # #         list.append(array[i])
    # #         array.remove(array[i])
    # #     final_array.append(list)
    # return final_array
    array = np_array_split(array, indicies_or_sections)

    # main_array = []

    # for i in range(len(array) // 4):
    #     list = []
    #     main_array.append(list)

    # print(main_array, 72 / 4)


    # for y in range(len(array)):
        # for x in range(indicies_or_sections):
            # tile_index = (y * indicies_or_sections) + x
            # main_array.remove()
            # array.append()

    return array
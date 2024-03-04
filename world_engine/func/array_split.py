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

    list = np_array_split(array, indicies_or_sections)
    return list
def array_split(array, indicies_or_sections):
    final_array = []
    for i in range(len(array) // indicies_or_sections):
        list = []
        for j in range(indicies_or_sections):
            list.append(array[(i * indicies_or_sections) + j])
        final_array.append(list)
    return final_array
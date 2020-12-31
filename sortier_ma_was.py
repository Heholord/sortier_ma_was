#
#
#Care: recheck file_endings_to_be_deleted


import os
from os import listdir

root_movie_folder='E:\\Filme' 

movie_list= sorted(listdir(root_movie_folder))

simulation = True
#TODO 
# simulation fuer wenn file endung dann (move/delete -> kommentieren) 

file_endings_to_be_deleted = [ '.jpg', '.nfo', '.txt', '.gz', '.png', '.YIFY', '.rar', '.idx', '.lnk', '.tbn']

for movie_index, movie_titel in enumerate(movie_list):
    movie_path = os.path.join(root_movie_folder, movie_titel)
    movie_sub_folder = listdir(movie_path)

    # print("\n", movie_index, movie_titel, "[","Number of Files:", len(movie_sub_folder), "]") #,"Size:",folder_size.st_size,

    

    for index_sub, file_name in enumerate(movie_sub_folder):
        # TODO filesize
        # size=os.path.getsize(file_name)
        # file_stats = os.stat(movie_path)
        # print(file_stats)
        if not os.path.isdir(os.path.join(movie_path, file_name)):
        
            file_ending_index = file_name.rfind(".")
            if file_ending_index == -1:
                print("\t File ending non existant", file_name)
            else: 
                file_ending = file_name[file_ending_index:]
            # print("\t -", index_sub +1, file_name, " ")

    recommended_deletion = any(ele in file_ending for ele in file_endings_to_be_deleted)
    # print(file_name,"[", recommended_deletion, "]")

    # if recommendended_deletion == true:
    #     os.remove(os.path.join(movie_path, file_name))


size=os.path.getsize(root_movie_folder)
print(size)

print(file_endings_to_be_deleted)


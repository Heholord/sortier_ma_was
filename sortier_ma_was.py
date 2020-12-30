import os
from os import listdir

movie_folder='E:\\Filme'

movie_list= sorted(listdir(movie_folder))

# # for movie_list in movie_folder:
# #     enumerate
# # WIE INDEX UND ENUMERATE?

for xyz, movie_index in enumerate(movie_list):
    movie_path = os.path.join(movie_folder, movie_index)
    file_count = listdir(movie_path)

    print(xyz, movie_index, "[","Number of Files:", len(file_count),"]")



# IDEE FÜR COUNT
# def count(dir, counter=0):
#     "returns number of files in dir and subdirs"
#     for pack in os.walk(dir):
#         for f in pack[2]:
#             counter += 1
#     return dir + " : " + str(counter) + "files"

# file_count= len(movie_list)
# print(file_count)

 # file_count= 0
    # for files in os.walk(movie_path):
    #     for files in movie_path:
    #         file_count=file_count+1

# Number_Of_Files=0
# for files in os.walk(movie_folder):
#     for files in movie_folder:
#         Number_Of_Files=Number_Of_Files+1

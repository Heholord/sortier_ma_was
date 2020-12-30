import os
from os import listdir

root_movie_folder='E:\\Filme' 

movie_list= sorted(listdir(root_movie_folder))

# # for movie_list in root_movie_folder:
# #     enumerate
# # WIE INDEX UND ENUMERATE?
file_endings = []

for movie_index, movie_titel in enumerate(movie_list):
    movie_path = os.path.join(root_movie_folder, movie_titel)
    movie_sub_folder = listdir(movie_path)

    print("\n", movie_index, movie_titel, "[","Number of Files:", len(movie_sub_folder), "]") #,"Size:",folder_size.st_size,

    

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
                # Help to find file endings, not needed for normal mode
                if not file_ending in file_endings:
                    file_endings.append(file_ending)
                # print(file_name[file_ending_index:])

            # print("\t -", index_sub +1, file_name, " ")

size=os.path.getsize(root_movie_folder)
print(size)

print(file_endings)

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
# for files in os.walk(root_movie_folder):
#     for files in root_movie_folder:
#         Number_Of_Files=Number_Of_Files+1

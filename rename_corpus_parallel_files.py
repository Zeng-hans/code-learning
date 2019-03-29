"""
Rename files in corpus parallel folder to modify its name more suitable for class torchtext.data.Dataset
Example:
    original_filename= data_ps.declarations.test
    moidified_filename = data_ps.test.declarations
"""
import os

def rename_corpus_parallel_files(folder='../parallel-corpus-torch', target_folder='../parallel-corpus-torch'):
    """
    folder: the name of corpus-parallel folder
    target_folder: the name of target folder
    """
    if os.path.exists(target_folder) == False:
        os.mkdir(target_folder)
    for filename in os.listdir(folder):
        if not filename.endswith('.gz'):
            file_part = filename.split('.')
            if len(file_part) == 2:
                new_filename = file_part[1] + '.' + file_part[0]
                origin_path = os.path.join(folder, filename)
                target_path = os.path.join(target_folder, new_filename)
                os.rename(origin_path, target_path)

if __name__ == '__main__':
    rename_corpus_parallel_files()

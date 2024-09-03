import os

def get_list(dir_path):
    # check directory
    if True != os.path.isdir(dir_path):
        return None
    
    entries = os.listdir(dir_path)
    ret     = {}
    for entry in entries:
        full_path = os.path.join(dir_path, entry)
        if os.path.isdir(full_path):
            ret[entry] = {'type': 'dir'}
        elif os.path.isfile(full_path):
            ret[entry] = {'type': 'file'}
        elif os.path.islink(full_path):
            ret[entry] = {'type': 'symlink'}
        else:
            ret[entry] = {'type': 'unknown'}  # 他のタイプ（特殊ファイルなど）

    return ret
    


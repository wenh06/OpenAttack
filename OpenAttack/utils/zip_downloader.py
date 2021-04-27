import requests
import zipfile
import os
from tqdm import tqdm

CHUNK_SIZE = 1024

def make_zip_downloader(URL, file_list=None):
    """
    :param str URL: URL of the file to be downloaded

    This function is used to make a zipfile downloader for data.
    """
    if isinstance(file_list, str):
        file_list = [file_list]

    def DOWNLOAD(path):
        name = os.path.basename(path)
        with open(path + ".zip", "wb") as f:
            resp = requests.get(URL, stream=True)
            total_length = int(resp.headers.get("content-length"))
            with tqdm(total=total_length, unit='B', desc="Downloading %s" % name, unit_scale=True) as pbar:
                for chunk in resp.iter_content(chunk_size=CHUNK_SIZE):
                    if chunk:
                        f.write(chunk)
                        f.flush()
                        pbar.update(len(chunk))
        zf = zipfile.ZipFile(path + ".zip")
        
        os.makedirs(path, exist_ok=True)
        if file_list is not None:
            for file in file_list:
                zf.extract(file, path)
        else:
            zf.extractall(path)
        zf.close()
        os.unlink(path + ".zip")
        return

    return DOWNLOAD

import pkgutil
import pickle
import requests
from tqdm import tqdm
from ..exceptions import DataConfigErrorException


def load_data():
    def pickle_loader(path):
        return pickle.load(open(path, "rb"))

    def url_downloader(url, name):
        def DOWNLOAD(path):
            CHUNK_SIZE = 1024
            resp = requests.get(url, stream=True)
            with open(path, "wb") as f:
                total_length = int(resp.headers.get("content-length"))
                with tqdm(total=total_length, unit='B', desc="Downloading %s" % name, unit_scale=True) as pbar:
                    for chunk in resp.iter_content(chunk_size=CHUNK_SIZE):
                        if chunk:
                            f.write(chunk)
                            f.flush()
                            pbar.update(len(chunk))
            return True

        return DOWNLOAD

    ret = []
    for data in pkgutil.iter_modules(__path__):
        data = data.module_finder.find_loader(data.name)[0].load_module()
        if hasattr(data, "NAME") and hasattr(data, "DOWNLOAD"):  # is a data module
            tmp = {"name": data.NAME}
            if callable(data.DOWNLOAD):
                tmp["download"] = data.DOWNLOAD
            elif isinstance(data.DOWNLOAD, str):
                tmp["download"] = url_downloader(data.DOWNLOAD, data.NAME)
            else:
                raise DataConfigErrorException(
                    "Data Module: %s\n dir: %s\n type: %s"
                    % (data, dir(data), type(data.DOWNLOAD))
                )

            if hasattr(data, "LOAD"):
                tmp["load"] = data.LOAD
            else:
                tmp["load"] = pickle_loader
            ret.append(tmp)
        else:
            pass  # this is not a data module
    return ret


data_list = load_data()
del load_data

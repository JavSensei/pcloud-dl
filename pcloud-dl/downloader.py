import requests
from tqdm import tqdm

def download_file(url, file_path):
    with requests.get(url, stream=True) as response:
        total_size = int(response.headers.get("content-length", 0))
        block_size = 8192
        progress_bar = tqdm(total=total_size, unit="iB", unit_scale=True)
        with open(file_path, "wb") as f:
            for chunk in response.iter_content(block_size):
                progress_bar.update(len(chunk))
                f.write(chunk)
        progress_bar.close()
    print("Done!")
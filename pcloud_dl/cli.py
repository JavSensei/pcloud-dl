import argparse, re
from .downloader import download_file

try:
    from pcloud import PyCloud
except ImportError:
    import os

    print("installing external requirements from github...")
    os.system("pip install git+https://github.com/JavSensei/pycloud > /dev/null")
    print("Done!")
    from pcloud import PyCloud

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("link_or_code", help="Link o código del archivo de pCloud")
    parser.add_argument("--endpoint", help="Tipo de endpoint (default: api, eapi para el endpoint alternativo)", default="api")
    args = parser.parse_args()

    link_regex = r"^https?://(u|e)\.pcloud\.link/publink/show\?code=(?P<code>\w+)$"
    code_regex = r"^(?P<code>\w+)$"
    link_match = re.match(link_regex, args.link_or_code)
    code_match = re.match(code_regex, args.link_or_code)

    if link_match:
        code = link_match.group("code")
        endpoint = "api" if link_match.group(1) == "u" else "eapi"
    elif code_match:
        code = code_match.group("code")
        endpoint = args.endpoint
    else:
        print("Error: el argumento debe ser un enlace o un código de pCloud")
        return

    pc = PyCloud("", "", endpoint=endpoint)

    response = pc.getpublinkdownload(code=code)
    if response["result"] == 0:
        file_path = response["path"]
        host = response["hosts"][0]
        download_url = f"https://{host}{file_path}"
        print(download_url)
        download_file(download_url, file_path.split("/")[-1])
    else:
        print("Error:", response["error"])

if __name__ == "__main__":
    main()

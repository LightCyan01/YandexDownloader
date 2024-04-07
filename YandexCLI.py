import argparse
import requests
import urllib.parse
from tqdm import tqdm
import os

class YandexDiskDownloader:
    def __init__(self, link, download_location, folder_path=None):
        self.link = urllib.parse.quote(link, safe='') 
        self.download_location = os.path.normpath(download_location)
        self.folder_path = folder_path 

    def download(self):
        if self.folder_path:
            url = f"https://cloud-api.yandex.net/v1/disk/public/resources/download?public_key={self.link}&path={urllib.parse.quote(self.folder_path)}"
        else:
            url = f"https://cloud-api.yandex.net/v1/disk/public/resources/download?public_key={self.link}"

        response = requests.get(url)
        if 'application/json' in response.headers.get('Content-Type', ''):
            json_response = response.json()
            if 'href' in json_response:
                download_url = json_response["href"]
                file_name = urllib.parse.unquote(download_url.split("filename=")[1].split("&")[0])
                self.download_file(download_url, file_name)
            else:
                print("Error: Download URL not found in response.")
        else:
            print("Error: Unexpected response content type.")

    def download_file(self, download_url, file_name):
        save_path = os.path.join(self.download_location, file_name)
        with open(save_path, "wb") as file:
            download_response = requests.get(download_url, stream=True)
            total_size = int(download_response.headers.get('content-length', 0))

            if total_size > 0:
                progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True, desc=f"Downloading {file_name}")
                for chunk in download_response.iter_content(chunk_size=1024):
                    if chunk:
                        file.write(chunk)
                        progress_bar.update(len(chunk))
                progress_bar.close()
                if progress_bar.n != total_size:
                    print("WARNING: Downloaded size does not match expected size.")
                else:
                    print(f"\nDownload complete: {file_name}")
            else:
                print(f"Downloading {file_name} without progress (unknown size)")
                for chunk in download_response.iter_content(chunk_size=1024):
                    if chunk:
                        file.write(chunk)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Yandex Disk Downloader')
    parser.add_argument('-l', '--link', type=str, help='Link for Yandex Disk URL', required=True)
    parser.add_argument('-d', '--download_location', type=str, help='Download location in PC', required=True)
    parser.add_argument('-f', '--folder', type=str, help='Specific folder path within the Yandex link', default=None)
    args = parser.parse_args()

    downloader = YandexDiskDownloader(args.link, args.download_location, args.folder)
    downloader.download()
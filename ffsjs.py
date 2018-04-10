import argparse
from os import makedirs
from os.path import dirname, join
from shutil import copyfileobj

from requests import Session


get = Session().get
parser = argparse.ArgumentParser()
parser.add_argument('package', metavar='PACKAGE')
parser.add_argument('version', metavar='VERSION', default=None, nargs='?')


def download(url, destination):
    response = get(url, stream=True)
    response.raise_for_status()
    response.raw.decode_content = True
    with open(destination, 'wb') as f:
        copyfileobj(response.raw, f)


def main():
    args = parser.parse_args()
    result = get("https://api.cdnjs.com/libraries/{}".format(args.package))
    result.raise_for_status()
    package_info = result.json()

    version = args.version or package_info["version"]
    for version_dict in package_info["assets"]:
        if version_dict["version"] == version:
            files = version_dict["files"]
            break

    makedirs(args.package, exist_ok=False)
    for filename in files:
        full_path = join(args.package, filename)
        makedirs(dirname(full_path), exist_ok=True)
        url = "https://cdnjs.cloudflare.com/ajax/libs/{}/{}/{}".format(
            args.package,
            version,
            filename,
        )
        print("{} -> {}".format(url, full_path))
        download(url, full_path)

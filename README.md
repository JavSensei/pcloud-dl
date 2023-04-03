# pcloud-dl

pcloud-dl is a Python package that allows you to download public files from pCloud using their public link or code.

## Installation

You can install pcloud-dl using pip:

```
pip install pcloud-dl
```

## Usage

To download a file, simply run:

```
pcloud-dl <link/code>
```

where `<link/code>` is the public link or code of the file you want to download.

The downloaded file will be saved in the current directory with the same name as the original file.

## Example

To download a file with the public link `https://u.pcloud.link/publink/show?code=XZtTpwVZnMvzSRIY2vhs6zCQgfHtI8Oya3YV`, run:

```
pcloud-dl https://u.pcloud.link/publink/show?code=XZtTpwVZnMvzSRIY2vhs6zCQgfHtI8Oya3YV
```

This will download the file to your current directory with the same name as the original file.

## License

pcloud-dl is licensed under the MIT License. See [LICENSE](https://github.com/javsensei/pcloud-dl/blob/main/LICENSE) for more information.

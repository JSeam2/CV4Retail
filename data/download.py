import wget
import os


def download_data(dataset='imdb_crop', output_path='datasets'):
    if dataset.lower() == 'imdb_crop':
        link = "https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_crop.tar"

        # Check if folder exists
        try:
            os.path.makedirs(os.path.join(output_path, dataset))
        except FileExistsError:
            pass

        wget.download(link, os.path.join(output_path, dataset))

    else:
        raise AttributeError("Unrecognized data_src parameter.")

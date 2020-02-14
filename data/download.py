import wget
import os


def download_data(dataset='imdb_crop', output_path='datasets'):
    if dataset.lower() in ('imdb_crop',
                           'imdbcrop',
                           'imdb-crop'):
        # link = "https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_crop.tar"
        link = 'https://i.imgur.com/I86rTVl.jpg'

        print("Downloading imdb_crop data set from {}".format(link))

        # Check if folder exists
        try:
            os.makedirs(os.path.join(output_path, dataset))
        except FileExistsError:
            pass

        wget.download(link, os.path.join(output_path, dataset))

    else:
        raise AttributeError("Unrecognized data_src parameter.")

import wget
import os


def _download_helper(link, output_path, dataset):
    try:
        os.makedirs(os.path.join(output_path, dataset))
    except FileExistsError:
        pass

    wget.download(link, os.path.join(output_path, dataset))


def download_data(dataset='imdb_crop', output_path='datasets'):
    try:
        if dataset.lower() in (
                'imdb_crop', 'imdbcrop', 'imdb-crop'):
            link = "https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/imdb_crop.tar"  # noqa

            print("Downloading imdb_crop data set from {}".format(link))
            _download_helper(link, output_path, dataset)

        elif dataset.lower() in ('test'):
            link = 'https://github.com/JSeam2/CV4Retail/blob/master/requirements.txt'  # noqa
            _download_helper(link, output_path, dataset)

        else:
            raise AttributeError("Unrecognized dataset parameter.")
    except AttributeError:
        raise AttributeError(
            "Unrecognized parameters check your input arguments")

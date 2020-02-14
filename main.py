from data import preprocess, download
import argparse


def main():
    parser = argparse.ArgumentParser(description="Computer Vision for Retail and Venues")

    subparser = parser.add_subparsers(dest='command')

    download_parser = subparser.add_parser(
        'download',
        help='download dataset for training'
    )
    download_parser.add_argument(
        '-d',
        '--dataset',
        required=True,
        type=str,
        help="Specify the dataset to be downloaded. Available datasets: imdb-crop"
    )
    download_parser.add_argument(
        '-o',
        '--output-path',
        type=str,
        help="Specify the output path for the dataset to be saved at"
    )

    args = parser.parse_args()

    if args.command == 'download':
        if args.output_path is not None:
            download.download_data(args.dataset, args.output_path)
        else:
            download.download_data(args.dataset)



if __name__ == "__main__":
    main()

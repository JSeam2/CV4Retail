from data import preprocess, download
import argparse


def main():
    parser = argparse.ArgumentParser(description="Computer Vision for Retail and Venues")
    parser.add_argument(
        '--download_data',
        type=str,
        help='download dataset for training'
    )


if __name__ == "__main__":
    main()

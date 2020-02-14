import pytest
from data.download import download_data


def test_download_data_fail():
    with pytest.raises(AttributeError):
        download_data(dataset=None)

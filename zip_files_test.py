import os
from zipfile import ZipFile
import utils


def test_zip_file_names():
    with ZipFile(os.path.join(utils.TMP_PATH, "resources.zip")) as zip_file:
        resource_file_names = os.listdir(utils.RESOURCES_PATH)
        zip_file_names = zip_file.namelist()
        assert len(zip_file_names) == len(resource_file_names)
        for file in resource_file_names:
            assert file in zip_file_names


def test_zip_file_contents():
    with ZipFile(os.path.join(utils.TMP_PATH, "resources.zip")) as zip_file:
        for file in zip_file.namelist():
            with open(os.path.join(utils.RESOURCES_PATH, file), 'rb') as f:
                assert zip_file.read(file) == f.read()
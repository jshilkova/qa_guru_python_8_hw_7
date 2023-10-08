import os
import shutil
from zipfile import ZipFile

from _pytest.fixtures import fixture

import utils


@fixture(scope="function", autouse=True)
def zip_resources():
    if not os.path.exists(utils.TMP_PATH):
        os.mkdir(os.path.join(utils.PROJECT_ROOT_PATH, "tmp"))

    with ZipFile(os.path.join(utils.TMP_PATH, "resources.zip"), 'w') as zip_object:
        for filename in os.listdir(utils.RESOURCES_PATH):
            zip_object.write(os.path.join(utils.RESOURCES_PATH, filename), arcname=filename)

    yield

    shutil.rmtree(utils.TMP_PATH)

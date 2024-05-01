# https://github.com/keras-team/keras-cv/blob/master/keras_cv/src/version_utils.py

# Copyright 2023 The KerasCV Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# from keras_cv.src.api_export import keras_cv_export
# modified: commented

# Unique source of truth for the version number.
__version__ = "0.10.0"


# keras_cv_export("keras_cv.version") ### modified: commented
def version():
    return __version__
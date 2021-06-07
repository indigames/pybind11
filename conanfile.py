import os
from conans import ConanFile, CMake

class IgeConan(ConanFile):
    name = 'pybind11'
    version = '2.4.3'
    license = "MIT"
    author = "Indi Games"
    url = "https://github.com/indigames"
    description = name + " library for IGE Engine"
    topics = ("#Python", "#IGE", "#Games")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "cmake"
    exports_sources = "*"
    short_paths = True

    def package(self):
        self.copy("*")
        error_code = self.run(f'conan upload {self.name}/{self.version}@ige/test --all --remote ige-center --force --confirm', ignore_errors=True)
        if(error_code != 0):
            print(f'Conan upload failed, error code: {error_code}')
            os.exit(1)

    def package_id(self):
        self.info.header_only()
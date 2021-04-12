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

    def package_id(self):
        self.info.header_only()
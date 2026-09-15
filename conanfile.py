# type: ignore

from conan import ConanFile
from conan.tools.cmake import cmake_layout


class Atacsw(ConanFile):
    name = "atacsw"
    version = "0.1.0"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"

    def requirements(self):
        # prod dependencies
        self.requires("cnats/[>=3.12.0]")
        self.requires("protobuf/[>=7.35.0]")
        self.requires("yaml-cpp/[>=0.9.0]")
        self.requires("pybind11/[>=2.11.0]")
        self.requires("openssl/[>=3.6]")

        # test dependencies
        self.test_requires("gtest/[>=1.17.0]")

    def build_requirements(self):
        self.tool_requires("cmake/[>=3.26.5]")
        self.tool_requires("ninja/[>=1.13.2]")

    def layout(self) -> None:
        self.folders.build = f"build/{self.settings.build_type}"
        cmake_layout(self)

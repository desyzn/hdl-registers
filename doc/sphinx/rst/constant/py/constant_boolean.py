# --------------------------------------------------------------------------------------------------
# Copyright (c) Lukas Vik. All rights reserved.
#
# This file is part of the hdl_registers project, a HDL register generator fast enough to run
# in real time.
# https://hdl-registers.com
# https://gitlab.com/hdl_registers/hdl_registers
# --------------------------------------------------------------------------------------------------

# Standard libraries
import sys
from pathlib import Path

# First party libraries
from hdl_registers.generator.c.header import CHeaderGenerator
from hdl_registers.generator.cpp.interface import CppInterfaceGenerator
from hdl_registers.generator.html.page import HtmlPageGenerator
from hdl_registers.generator.vhdl.register_package import VhdlRegisterPackageGenerator
from hdl_registers.parser import from_toml
from hdl_registers.register_list import RegisterList

THIS_DIR = Path(__file__).parent


def parse_toml() -> RegisterList:
    """
    Create the register list by parsing a TOML data file.
    """
    return from_toml(
        module_name="caesar", toml_file=THIS_DIR.parent / "toml" / "constant_boolean.toml"
    )


def create_from_api() -> RegisterList:
    """
    Alternative method: Create the register list by using the Python API.
    """
    register_list = RegisterList(name="caesar")

    register_list.add_constant(
        name="supports_pre_filtering",
        value=True,
        description="Will indicate **True** if the module supports data pre-filtering.",
    )

    register_list.add_constant(
        name="is_release_version",
        value=False,
        description="",
    )

    return register_list


def generate(register_list: RegisterList, output_folder: Path):
    """
    Generate the artifacts that we are interested in.
    """
    CHeaderGenerator(register_list=register_list, output_folder=output_folder).create()
    CppInterfaceGenerator(register_list=register_list, output_folder=output_folder).create()
    HtmlPageGenerator(register_list=register_list, output_folder=output_folder).create()
    VhdlRegisterPackageGenerator(register_list=register_list, output_folder=output_folder).create()


def main(output_folder: Path):
    generate(register_list=parse_toml(), output_folder=output_folder / "toml")
    generate(register_list=create_from_api(), output_folder=output_folder / "api")


if __name__ == "__main__":
    main(output_folder=Path(sys.argv[1]))

# --------------------------------------------------------------------------------------------------
# Copyright (c) Lukas Vik. All rights reserved.
#
# This file is part of the hdl-registers project, an HDL register generator fast enough to run
# in real time.
# https://hdl-registers.com
# https://github.com/hdl-registers/hdl-registers
# --------------------------------------------------------------------------------------------------

# Standard libraries
import sys
from pathlib import Path

# First party libraries
from hdl_registers.generator.html.constant_table import HtmlConstantTableGenerator
from hdl_registers.generator.html.page import HtmlPageGenerator
from hdl_registers.generator.html.register_table import HtmlRegisterTableGenerator
from hdl_registers.parser.toml import from_toml

THIS_DIR = Path(__file__).parent


def main(output_folder: Path):
    """
    Create register HTML artifacts from the TOML example file.
    """
    register_list = from_toml(
        name="example",
        toml_file=THIS_DIR.parent.parent / "user_guide" / "toml" / "toml_format.toml",
    )

    HtmlPageGenerator(register_list=register_list, output_folder=output_folder).create()
    HtmlRegisterTableGenerator(register_list=register_list, output_folder=output_folder).create()
    HtmlConstantTableGenerator(register_list=register_list, output_folder=output_folder).create()


if __name__ == "__main__":
    main(output_folder=Path(sys.argv[1]))

# Copyright (c) 2019, Hans Jerry Illikainen <hji@dyntopia.com>
#
# SPDX-License-Identifier: BSD-2-Clause

from . import __project__, cli


def main() -> None:
    cli.cli(auto_envvar_prefix=__project__)  # pylint: disable=E1120,E1123


if __name__ == "__main__":
    main()

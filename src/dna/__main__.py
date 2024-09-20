"""Command-line entries for the module."""
from __future__ import annotations

from pathlib import Path
from typing import Any

import click


@click.group()
@click.pass_context
@click.version_option(message="%(version)s")
@click.option("--verbose", "-v", count=True, help="Verbosity of messages.")
@click.option("--out", "-o", type=click.Path(), help="Output folder.")
def dna(ctx: click.Context, verbose: int, out: str) -> None:  # pragma: no cover
    """Create `dna` group command."""
    ctx.ensure_object(dict)
    ctx.obj["VERBOSE"] = verbose
    if out:
        ctx.obj["OUT"] = out

@dna.command()
@click.pass_context
@click.argument("fpath", type=click.Path(exists=True))
def subcommand(ctx: click.Context, fpath: Path) -> None:
    """Do something."""
    print(fpath)
    print(ctx.obj["OUT"])

"""
SafeGuard CLI Entry Point
"""

import sys
import click
from pathlib import Path

from safeguard.core import Scanner
from safeguard import __version__


@click.command()
@click.option(
    "--scan",
    type=click.Path(exists=True),
    help="Verzeichnis oder Datei zum Scannen"
)
@click.option(
    "--verbose",
    "-v",
    is_flag=True,
    help="Ausführliche Ausgabe"
)
@click.option(
    "--version",
    is_flag=True,
    help="Versionsinformation"
)
def main(scan, verbose, version):
    """SafeGuard - Sicherer Antivirus-Scanner"""
    
    if version:
        click.echo(f"SafeGuard v{__version__}")
        return
    
    if not scan:
        click.echo("SafeGuard v{__version__}")
        click.echo("\nBenutzung: python -m safeguard [OPTIONS]")
        click.echo("\nOptionen:")
        click.echo("  --scan <PATH>    Verzeichnis/Datei scannen")
        click.echo("  -v, --verbose    Ausführliche Ausgabe")
        click.echo("  --version        Versionsinformation")
        return
    
    click.echo(f"🛡️  SafeGuard v{__version__}")
    click.echo(f"📁 Starte Scan: {scan}\n")
    
    scanner = Scanner(verbose=verbose)
    results = scanner.scan(scan)
    
    if results["threats_found"] > 0:
        click.secho(f"⚠️  {results['threats_found']} Bedrohungen gefunden!", fg="red")
    else:
        click.secho("✅ Keine Bedrohungen gefunden!", fg="green")


if __name__ == "__main__":
    main()

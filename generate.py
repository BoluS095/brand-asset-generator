#!/usr/bin/env python3
"""Brand Asset Generator — main entry point."""
import click
import yaml
from pathlib import Path
from rich.console import Console
from rich.table import Table

console = Console()


@click.command()
@click.option("--brief", required=True, help="Path to brand brief YAML file")
@click.option("--output", default="./output", help="Output directory")
@click.option("--dry-run", is_flag=True, help="Show what would be generated without running")
def generate(brief: str, output: str, dry_run: bool):
    """Generate brand assets from a creative brief."""
    brief_path = Path(brief)
    if not brief_path.exists():
        console.print(f"[red]Error:[/red] Brief not found: {brief}")
        return

    with open(brief_path) as f:
        config = yaml.safe_load(f)

    brand = config.get("brand", {})
    assets = config.get("assets", [])

    console.print(f"\n[bold]Brand:[/bold] {brand.get('name', 'Unknown')}")
    console.print(f"[bold]Tagline:[/bold] {brand.get('tagline', 'N/A')}")
    console.print(f"[bold]Style:[/bold] {brand.get('style', 'N/A')}")

    table = Table(title="\nAssets to Generate")
    table.add_column("Type", style="cyan")
    table.add_column("Quantity", style="green")
    table.add_column("Theme", style="yellow")

    total = 0
    for asset in assets:
        qty = asset.get("quantity", 1)
        total += qty
        table.add_row(asset.get("type", "?"), str(qty), asset.get("theme", ""))

    console.print(table)
    console.print(f"\n[bold]Total assets:[/bold] {total}")

    if dry_run:
        console.print("\n[yellow]Dry run — no assets generated.[/yellow]")
        return

    # TODO: Implement generation engines
    console.print("\n[yellow]Generation engines coming soon.[/yellow]")
    console.print("Run with --dry-run to preview what would be generated.")


if __name__ == "__main__":
    generate()

import csv

import click


def ingest_microtrait_file(path: str) -> None:
    """Ingest microtrait file."""
    csvreader = csv.DictReader(open(path, "r"), delimiter="\t")
    for row in csvreader:
        print("[Term]")
        id = row['microtrait_trait_name'].replace(" ", "_")
        print(f"id: MICROTRAIT:{id}")
        print(f"name: {row['microtrait_trait_displaynameshort']}")
        print(f"synonym: \"{row['microtrait_trait_displaynamelong']}\" EXACT []")
        print("")


@click.command
@click.argument("path")
def ingest(path: str) -> None:
    """Ingest microtrait file."""
    print("Ingesting microtrait file...")
    ingest_microtrait_file(path)


if __name__ == "__main__":
    ingest()
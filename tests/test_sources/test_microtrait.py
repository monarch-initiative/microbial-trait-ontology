from linkml_runtime.loaders import csv_loader
from linkml_runtime.utils.introspection import package_schemaview

from microbial_trait_ontology.datamodel.microtrait import Trait, TraitDocument
from microbial_trait_ontology.etl.ingest_microtrait import ingest_microtrait_file
from tests import INPUT_DIR


def test_microtrait():
    trait = Trait(microtrait_trait_name="test")
    assert trait

def test_load_microtrait():
    """Load microbial_trait_ontology."""
    test_path = str(INPUT_DIR / "microtraits_subset.tsv")
    ingest_microtrait_file(test_path)


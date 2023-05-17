# Auto generated from microtrait.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-05-17T15:39:15
# Schema: microtraits
#
# id: https://w3id.org/microtraits
# description: microtraits
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Integer, String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MICROTRAITS = CurieNamespace('microtraits', 'https://w3id.org/microtraits')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = MICROTRAITS


# Types
class Identifier(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "identifier"
    type_model_uri = MICROTRAITS.Identifier


# Class references



@dataclass
class TraitDocument(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROTRAITS.TraitDocument
    class_class_curie: ClassVar[str] = "microtraits:TraitDocument"
    class_name: ClassVar[str] = "TraitDocument"
    class_model_uri: ClassVar[URIRef] = MICROTRAITS.TraitDocument

    traits: Optional[Union[Union[dict, "Trait"], List[Union[dict, "Trait"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.traits, list):
            self.traits = [self.traits] if self.traits is not None else []
        self.traits = [v if isinstance(v, Trait) else Trait(**as_dict(v)) for v in self.traits]

        super().__post_init__(**kwargs)


@dataclass
class Trait(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MICROTRAITS.Trait
    class_class_curie: ClassVar[str] = "microtraits:Trait"
    class_name: ClassVar[str] = "Trait"
    class_model_uri: ClassVar[URIRef] = MICROTRAITS.Trait

    microtrait_trait_name: Optional[Union[str, Identifier]] = None
    microtrait_trait_displaynameshort: Optional[str] = None
    microtrait_trait_displaynamelong: Optional[Union[str, Identifier]] = None
    microtrait_trait_strategy: Optional[Union[str, "MicrotraitTraitStrategyEnum"]] = None
    microtrait_trait_type: Optional[Union[str, "MicrotraitTraitTypeEnum"]] = None
    microtrait_trait_granularity: Optional[int] = None
    microtrait_trait_version: Optional[Union[str, "MicrotraitTraitVersionEnum"]] = None
    microtrait_trait_displayorder: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.microtrait_trait_name is not None and not isinstance(self.microtrait_trait_name, Identifier):
            self.microtrait_trait_name = Identifier(self.microtrait_trait_name)

        if self.microtrait_trait_displaynameshort is not None and not isinstance(self.microtrait_trait_displaynameshort, str):
            self.microtrait_trait_displaynameshort = str(self.microtrait_trait_displaynameshort)

        if self.microtrait_trait_displaynamelong is not None and not isinstance(self.microtrait_trait_displaynamelong, Identifier):
            self.microtrait_trait_displaynamelong = Identifier(self.microtrait_trait_displaynamelong)

        if self.microtrait_trait_strategy is not None and not isinstance(self.microtrait_trait_strategy, MicrotraitTraitStrategyEnum):
            self.microtrait_trait_strategy = MicrotraitTraitStrategyEnum(self.microtrait_trait_strategy)

        if self.microtrait_trait_type is not None and not isinstance(self.microtrait_trait_type, MicrotraitTraitTypeEnum):
            self.microtrait_trait_type = MicrotraitTraitTypeEnum(self.microtrait_trait_type)

        if self.microtrait_trait_granularity is not None and not isinstance(self.microtrait_trait_granularity, int):
            self.microtrait_trait_granularity = int(self.microtrait_trait_granularity)

        if self.microtrait_trait_version is not None and not isinstance(self.microtrait_trait_version, MicrotraitTraitVersionEnum):
            self.microtrait_trait_version = MicrotraitTraitVersionEnum(self.microtrait_trait_version)

        if self.microtrait_trait_displayorder is not None and not isinstance(self.microtrait_trait_displayorder, int):
            self.microtrait_trait_displayorder = int(self.microtrait_trait_displayorder)

        super().__post_init__(**kwargs)


# Enumerations
class MicrotraitTraitStrategyEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="MicrotraitTraitStrategyEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Resource Use",
                PermissibleValue(text="Resource Use",
                                 description="Resource Use") )
        setattr(cls, "Stress Tolerance",
                PermissibleValue(text="Stress Tolerance",
                                 description="Stress Tolerance") )
        setattr(cls, "Resource Acquisition",
                PermissibleValue(text="Resource Acquisition",
                                 description="Resource Acquisition") )

class MicrotraitTraitTypeEnum(EnumDefinitionImpl):

    count = PermissibleValue(text="count",
                                 description="count")
    binary = PermissibleValue(text="binary",
                                   description="binary")

    _defn = EnumDefinition(
        name="MicrotraitTraitTypeEnum",
    )

class MicrotraitTraitVersionEnum(EnumDefinitionImpl):

    production = PermissibleValue(text="production",
                                           description="production")

    _defn = EnumDefinition(
        name="MicrotraitTraitVersionEnum",
    )

# Slots
class slots:
    pass

slots.microtrait_trait_name = Slot(uri=MICROTRAITS.microtrait_trait_name, name="microtrait_trait_name", curie=MICROTRAITS.curie('microtrait_trait_name'),
                   model_uri=MICROTRAITS.microtrait_trait_name, domain=None, range=Optional[Union[str, Identifier]])

slots.microtrait_trait_displaynameshort = Slot(uri=MICROTRAITS.microtrait_trait_displaynameshort, name="microtrait_trait_displaynameshort", curie=MICROTRAITS.curie('microtrait_trait_displaynameshort'),
                   model_uri=MICROTRAITS.microtrait_trait_displaynameshort, domain=None, range=Optional[str])

slots.microtrait_trait_displaynamelong = Slot(uri=MICROTRAITS.microtrait_trait_displaynamelong, name="microtrait_trait_displaynamelong", curie=MICROTRAITS.curie('microtrait_trait_displaynamelong'),
                   model_uri=MICROTRAITS.microtrait_trait_displaynamelong, domain=None, range=Optional[Union[str, Identifier]])

slots.microtrait_trait_strategy = Slot(uri=MICROTRAITS.microtrait_trait_strategy, name="microtrait_trait_strategy", curie=MICROTRAITS.curie('microtrait_trait_strategy'),
                   model_uri=MICROTRAITS.microtrait_trait_strategy, domain=None, range=Optional[Union[str, "MicrotraitTraitStrategyEnum"]])

slots.microtrait_trait_type = Slot(uri=MICROTRAITS.microtrait_trait_type, name="microtrait_trait_type", curie=MICROTRAITS.curie('microtrait_trait_type'),
                   model_uri=MICROTRAITS.microtrait_trait_type, domain=None, range=Optional[Union[str, "MicrotraitTraitTypeEnum"]])

slots.microtrait_trait_granularity = Slot(uri=MICROTRAITS.microtrait_trait_granularity, name="microtrait_trait_granularity", curie=MICROTRAITS.curie('microtrait_trait_granularity'),
                   model_uri=MICROTRAITS.microtrait_trait_granularity, domain=None, range=Optional[int])

slots.microtrait_trait_version = Slot(uri=MICROTRAITS.microtrait_trait_version, name="microtrait_trait_version", curie=MICROTRAITS.curie('microtrait_trait_version'),
                   model_uri=MICROTRAITS.microtrait_trait_version, domain=None, range=Optional[Union[str, "MicrotraitTraitVersionEnum"]])

slots.microtrait_trait_displayorder = Slot(uri=MICROTRAITS.microtrait_trait_displayorder, name="microtrait_trait_displayorder", curie=MICROTRAITS.curie('microtrait_trait_displayorder'),
                   model_uri=MICROTRAITS.microtrait_trait_displayorder, domain=None, range=Optional[int])

slots.traitDocument__traits = Slot(uri=MICROTRAITS.traits, name="traitDocument__traits", curie=MICROTRAITS.curie('traits'),
                   model_uri=MICROTRAITS.traitDocument__traits, domain=None, range=Optional[Union[Union[dict, Trait], List[Union[dict, Trait]]]])

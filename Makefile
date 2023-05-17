RUN = poetry run

# LinkML


src/microbial_trait_ontology/datamodel/%.py:  src/microbial_trait_ontology/datamodel/%.yaml
#	$(RUN) gen-pydantic $< > $@
	$(RUN) gen-python $< > $@

# ETL

data/microtrait_traits.txt:
	curl -L -s https://raw.githubusercontent.com/ukaraoz/microtrait/master/data-raw/microtrait_traits.txt > $@.tmp && mv $@.tmp $@

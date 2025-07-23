from nomad.config.models.plugins import ParserEntryPoint
from pydantic import Field


class NewParserEntryPoint(ParserEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self, **kwargs):
        from sidpyhdf5.parsers.parser import HDF5Parser

        return HDF5Parser(**kwargs)


parser_entry_point = NewParserEntryPoint(
    name='NewParser',
    description='New parser entry point configuration.',
    mainfile_name_re=r'.*\.sidh5',
)

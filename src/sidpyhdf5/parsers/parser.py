from typing import (
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

from nomad.config import config
from nomad.datamodel.metainfo.workflow import Workflow
from nomad.parsing.parser import MatchingParser
import datetime
import numpy as np
from nomad.datamodel import EntryArchive
from nomad.datamodel.metainfo.workflow import Workflow
from nomad.parsing.file_parser import Quantity, TextParser
from nomad.units import ureg as units
from nomad.datamodel import EntryArchive
from nomad.parsing.parser import MatchingParser
from .hdf5_parser import HDF5Reader
from nomad.datamodel import EntryArchive, EntryMetadata

configuration = config.get_plugin_entry_point(
    'sidpyhdf5.parsers:parser_entry_point'
)

"""
class NewParser(MatchingParser):
    def parse(
        self,
        mainfile: str,
        archive: 'EntryArchive',
        logger: 'BoundLogger',
        child_archives: dict[str, 'EntryArchive'] = None,
    ) -> None:
        logger.info('NewParser.parse', parameter=configuration.parameter)

        archive.workflow2 = Workflow(name='test')"""

class HDF5Parser():
    def parse(self, mainfile: str, archive: EntryArchive, logger):
        print('We are inside parse()')
        logger.info(f"🔥 HDF5Parser invoked on file: {mainfile}")
        from sidpyhdf5.parsers.hdf5_parser import HDF5Reader
        from sidpyhdf5.schema_packages.schema_package import HDF5Metadata

        reader = HDF5Reader(mainfile)
        data = reader.extract_metadata()

        section = HDF5Metadata()
        section.file_structure = str(data)
        section.temperature = float(
            data.get('experiment', {}).get('temperature', {}).get('value', 0.0)
        )

        # Initialize metadata 
        if archive.metadata is None:
            from nomad.datamodel import EntryMetadata
            archive.metadata = EntryMetadata()

        archive.metadata.entry_name = 'HDF5 extracted entry'
        archive.data = section
        logger.info(f"Successfully completed")
        


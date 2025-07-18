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
from nomad.datamodel.data import Schema
from nomad.datamodel.metainfo.annotations import ELNAnnotation, ELNComponentEnum
from nomad.metainfo import Quantity, SchemaPackage
from nomad.metainfo import Package, Section, Quantity
from nomad.datamodel.metainfo.basesections import ArchiveSection 

configuration = config.get_plugin_entry_point(
    'sidpyhdf5.schema_packages:schema_package_entry_point'
)

m_package = SchemaPackage()

class HDF5Metadata(ArchiveSection):

    description = 'Metadata extracted from an HDF5 file'
    m_def = Section(
        label='HDF5 metadata',
        description='Metadata extracted from HDF5 files.'
    )

    file_structure = Quantity(
        type=str,
        description='String representation of the HDF5 file structure'
    )

    temperature = Quantity(
        type=float,
        unit='kelvin',
        description='Example temperature extracted from HDF5'
    )

m_package.__init_metainfo__()


"""class NewSchemaPackage(Schema):
    name = Quantity(
        type=str, a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity)
    )
    message = Quantity(type=str)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)

        logger.info('NewSchema.normalize', parameter=configuration.parameter)
        self.message = f'Hello {self.name}!'"""

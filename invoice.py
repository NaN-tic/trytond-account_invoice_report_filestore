from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['Invoice']


class Invoice:
    __name__ = 'account.invoice'
    __metaclass__ = PoolMeta

    report_file_id = fields.Char('Report File ID', readonly=True)

    @classmethod
    def __setup__(cls):
        super(Invoice, cls).__setup__()

        cls.invoice_report_cache.file_id = 'report_file_id'

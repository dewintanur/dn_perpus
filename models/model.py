from odoo import models, fields, api


class ProductProduct(models.Model):
    _inherit = 'product.product'

    isbn = fields.Char('ISBN Code', unique=True, help="Shows International Standard Book Number")
    catalog_num = fields.Char('Catalog Number', help="Shows Identification number of books")
    lang = fields.Selection(string='Language', selection='_get_lang')
    author_id = fields.Many2one('res.partner', 'Author', domain=[('penulis', '=', True)])
    publisher_id = fields.Many2one('res.partner', 'Publisher', domain=[('penerbit', '=', True)])
    nbpage = fields.Integer('Number of Pages')
    location_id = fields.Many2one('stock.location', 'Location', help="Shows position of book", domain=[('lokasi_buku', '=', True)])
    num_edition = fields.Integer('No. Edition', help="Edition number of book")
    resensi = fields.Text('Resensi')
    state = fields.Selection([('available', 'Available'), ('rent', 'Rented')], 'State', readonly=True, default='available')

    _sql_constraints = [
        ('unique_barcode', 'unique(barcode)', 'barcode field must be unique across all the products'),
        ('code_uniq', 'unique (default_code)', 'Code of the product must be unique !')
    ]

    @api.model
    def _get_lang(self):
        return self.env['res.lang'].get_installed()



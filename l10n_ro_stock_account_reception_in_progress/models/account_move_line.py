# Copyright (C) 2022 NextERP Romania
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models


class AccountMoveLine(models.Model):
    _name = "account.move.line"
    _inherit = ["account.move.line", "l10n.ro.mixin"]

    def _get_computed_account(self):
        if self.product_id.type == "product" and self.is_l10n_ro_record:
            if self.move_id.is_purchase_document():
                purchase = self.purchase_order_id
                if purchase and self.product_id.purchase_method == "receive":
                    self = self.with_context(l10n_ro_reception_in_progress=True)
        return super(AccountMoveLine, self)._get_computed_account()

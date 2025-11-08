# Copyright (c) 2025, Arun Joy Thekkiniyath and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class MedicalData(Document):
    def before_save(self):
		# user should always be logged in user.
        self.user = frappe.session.user

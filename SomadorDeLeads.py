visol_leads = """		"""

visol_leads_array = [int(n) for n in visol_leads.split()]

total_leads = sum(visol_leads_array)
print(f"Total de leads: {total_leads}")

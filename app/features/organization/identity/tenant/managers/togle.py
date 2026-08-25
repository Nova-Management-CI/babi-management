
class OrgTogleManager():
    async def toggle_block_status(self, org_id: int, is_blocked: bool):
        """Bascule l'état de blocage d'une organisation (Super Admin)."""
        updated_org = await self.crud.update(id=org_id, is_blocked=is_blocked)
        status_label = "bloquée" if is_blocked else "débloquée"
        return updated_org
        



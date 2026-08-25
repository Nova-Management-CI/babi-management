import secrets

from ..schemas.invitation import InvitationCodeCreate


class InvitationManager:
    async def create_invitation_code(self, data: InvitationCodeCreate):
        """Génère un code d'invitation unique pour le staff (Async & ManuelManager)."""

        # 1. Génération d'un code unique lisible (ex: STAFF-8F29A)
        random_code = f"STAFF-{secrets.token_hex(3).upper()}"

        # 2. Préparation des données avec les valeurs par défaut
        payload = data.model_dump()
        payload.update(
            {
                "code": random_code,
                "is_active": True,
                "is_expired": False,
                "used_count": 0,
                "status": "active",
            }
        )

        # 3. Ajout via le CRUD et retour asynchrone
        return await self.crud.add(unique_fields=["code"], **payload)

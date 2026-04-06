import uuid
from django.core.management.base import BaseCommand
from django.db import transaction
from core.models import Branch, CashRegister

class Command(BaseCommand):
    help = 'Crea una caja registradora para la sucursal PT1 compatible con el Serializer'

    def handle(self, *args, **options):
        self.stdout.write("--- Iniciando Seed de Caja Registradora ---")

        try:
            with transaction.atomic():
                # 1. Asegurar que existe la sucursal PT1
                # El serializer usa branch.code, así que este campo es vital.
                branch, b_created = Branch.objects.get_or_create(
                    code="PT1",
                    defaults={
                        "name": "PT1",
                        "is_active": True
                    }
                )

                if b_created:
                    self.stdout.write(self.style.SUCCESS(f"Sucursal {branch.code} creada."))

                # 2. Crear la Caja Registradora
                # El serializer usa 'public_id' como 'cash_register_id'
                # Usamos get_or_create para evitar duplicados por nombre y sucursal
                register, r_created = CashRegister.objects.get_or_create(
                    name="Caja Principal PT1",
                    branch=branch,
                    defaults={
                        "public_id": uuid.uuid4(), # Genera el UUID que pide tu Serializer
                        "register_type": "BRANCH",
                        "is_active": True
                    }
                )

                if r_created:
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Éxito: Caja '{register.name}' creada con ID: {register.public_id}"
                        )
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(f"La caja '{register.name}' ya existía en {branch.code}.")
                    )

                self.stdout.write("--- Proceso Finalizado ---")

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error fatal en el seed: {str(e)}"))
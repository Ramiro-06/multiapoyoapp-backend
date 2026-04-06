import uuid
from django.core.management.base import BaseCommand
from django.db import transaction
# Cambia 'core' por el nombre de tu app si es diferente
from core.models import Branch, CashRegister 

class Command(BaseCommand):
    help = 'Crea la caja registradora para la sucursal PT1'

    def handle(self, *args, **options):
        self.stdout.write("Configurando datos iniciales...")

        try:
            with transaction.atomic():
                # Buscar o crear la sucursal necesaria para el Serializer
                branch, _ = Branch.objects.get_or_create(
                    code="PT1",
                    defaults={
                        "name": "Sucursal Potosí",
                        "address": "Centro Potosí",
                        "is_active": True
                    }
                )

                # Crear la caja con el public_id que espera tu frontend
                register, created = CashRegister.objects.get_or_create(
                    name="Caja Principal PT1",
                    branch=branch,
                    defaults={
                        "public_id": uuid.uuid4(),
                        "register_type": "BRANCH",
                        "is_active": True
                    }
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f"Caja creada con ID: {register.public_id}"))
                else:
                    self.stdout.write(self.style.WARNING("La caja ya existe en la base de datos."))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error: {e}"))
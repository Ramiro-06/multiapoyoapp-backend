# crear_cajero.py
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "configuracion.settings")  # cambia esto
django.setup()

from django.contrib.auth import get_user_model
from core.models_security import Role, UserRole
from core.models import Branch, UserBranchAccess  # ajusta si UserBranchAccess está en models_security

User = get_user_model()

# ── Datos del cajero ───────────────────────────────────────────
USERNAME  = "dueno"
PASSWORD  = "dueno1234"
ROLE_CODE = "OWNER_ADMIN"
BRANCH_CODE = "PT1"

# Crear usuario
if User.objects.filter(username=USERNAME).exists():
    print(f"Ya existe el usuario '{USERNAME}'")
else:
    user = User.objects.create(username=USERNAME, is_active=True)
    user.set_password(PASSWORD)
    user.save()

    # Asignar rol
    role = Role.objects.get(code=ROLE_CODE)
    UserRole.objects.create(user=user, role=role)

    # Asignar sucursal
    branch = Branch.objects.get(code=BRANCH_CODE)
    UserBranchAccess.objects.create(user=user, branch=branch)

    print(f"✓ Cajero '{USERNAME}' creado con rol {ROLE_CODE} y sucursal {BRANCH_CODE}")
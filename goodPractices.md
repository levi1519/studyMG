# Buenas Prácticas para Control de Versiones y Contenedores

## 1. Convenciones de Nombres

### Ramas (Branches)
- **feature/nombre-funcionalidad** - Para nuevas funcionalidades
- **fix/descripcion-bug** - Para correcciones de errores
- **docs/tema** - Para cambios en documentación
- **refactor/componente** - Para refactorización de código

**Ejemplos:**
- ✅ `feature/login-system`
- ✅ `fix/database-connection`
- ❌ `mi-rama` (muy genérico)
- ❌ `test` (no descriptivo)

### Mensajes de Commit
Usar prefijos convencionales seguidos de descripción clara:

- **feat:** Nueva funcionalidad
- **fix:** Corrección de bugs
- **docs:** Cambios en documentación
- **refactor:** Refactorización sin cambiar funcionalidad
- **test:** Añadir o modificar tests
- **ci:** Cambios en configuración de CI/CD
- **style:** Cambios de formato (espacios, punto y coma, etc.)

**Formato recomendado:**
**Ejemplos:**
- ✅ `feat: Add user authentication module`
- ✅ `fix: Resolve login validation error`
- ✅ `docs: Update README with installation steps`
- ❌ `cambios` (no descriptivo)
- ❌ `fixed bug` (demasiado genérico)

## 2. Workflow de Desarrollo con Git

### Proceso recomendado:

1. **Antes de empezar:**
```bash
   git checkout main
   git pull origin main
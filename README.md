# clabmiming

## Scraping(Sin integrar al proyecto...)
**Note:**
> - Version de python = 2.7

Para probarlos
  1. Instalar requirements.txt
  2. Ejecutar los scripts individualmente
  ```sh
    cd apps/collection/scripts
    python aptitus.py
    python indeeed.py
  ```
  ## Tests
  ```
    coverage run manage.py test
    coverage report
    python manage.py jenkins --enable-coverage
  ```

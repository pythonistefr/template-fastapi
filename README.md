# Template pour un projet FastAPI

## Description

Template FastAPI pour commencer un projet Proprement avec ce Framework.

Ce template contient tous les outils indispensables pour commencer un projet et le maintenir à un niveau de qualité optimal.

## ⚙️ Pré-requis

Les seuls prérequis sont au moins Git pout télécharger le projet et Docker pour pouvoir l'utiliser.

<ul>
  <li>🐋 Docker </li>
  <li>📦 Docker Compose V2</li>
  <li>🎮 Git</li>
</ul>

## Environnement de développement

Spécificité du mode développement :

- Code source monté automatiquement dans le conteneur docker de façon à pouvoir coder en temps réel ;
- Tous les outils pour tester et vérifier le code sont disponibles dans le conteneur.

Rappel, la documentation de l'API Swagger est disponible ici: [Swagger](https://localhost:8000/docs)

### 🚀 Installer l'environnement

  ```bash
  docker-compose -f compose.yml -f compose-dev.yml build
  ```

### 🚀 Exécuter le projet

  ```bash
  docker-compose -f compose.yml -f compose-dev.yml up
  ```

### 🚀 Vérifier le code source

  ```bash
  docker run -v ./:/template_fastapi/ project-api:dev git config --global --add safe.directory /template_fastapi && pre-commit run --all-files
  ```

### 🚀 Tester le code source

  ```bash
  docker run -v ./:/template_fastapi/ project-api:dev pytest
  ```

## Environnement de production

Spécificité du mode production :

- Seul le strict nécessaire est présent dans le conteneur ;

Rappel, la documentation de l'API Swagger est disponible ici: [Swagger](https://localhost:8000/docs)

### 🚀 Installer l'environnement

  ```bash
  docker-compose -f compose.yml build
  ```

### 🚀 Exécuter le projet

  ```bash
  docker-compose -f compose.yml up
  ```

## Bonus spécifique aux utilisateurs de Linux

Cette section est dédiée aux utilisateurs linux afin qu'ils puissent utiliser les outils de vérification et de test localement sur leur machine.
Le seul prérequis supplémentaire à avoir est `Make`.

NB pour les utilisateurs de windows : Vous pouvez aussi installer un terminal ubuntu avec WSL-2 afin de l'utiliser localement chez vous.

### (Linux) Installer l'environnement de développement localement

  ```bash
  make dev-env
  ```

### (Linux) Vérifier le code source

  ```bash
  make pre-commit
  ```


### (Linux) Tester le code source

  ```bash
  make pytest
  ```

### Mémo - Supprimer l'environnement de travail

  ```bash
  pyenv virtualenv-delete -f project-api && rm -rf .venv && rm -f .python-version
  ```

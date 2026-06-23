# Source Lock Policy

- `manifest.json` declares package files and their SHA-256 hashes.
- Active tickets must be addressed by full ticket ID.
- Active ticket files must be absolute paths inside the package root.
- Repository-local files with the same basename or ID are not substitutes for
  package tickets.

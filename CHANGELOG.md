# Changelog
All notable changes to this project are documented in this file.

The project follows simple versioning:
- v1.0 → Initial implementation
- v2.0 → Major revamp and structural improvements

---

## [v2.0] – Final Modular Release
**Release Type:** Major Revamp  
**Status:** Stable / Final Version  

### Added
- Menu-driven CLI interface for improved navigation
- Fixed **5-round match system** to reduce repetitive prompts
- Persistent score saving and loading using `.txt` file
- Match history viewer with:
  - Match serial number
  - Player score
  - Computer score
  - Match result (WIN / LOSE / DRAW)
- Dedicated **Rules** section accessible from the menu

### Improved
- Refactored entire codebase into a **modular structure**
  - `main.py` → UI and menu handling
  - `game.py` → Core game logic
  - `scores.py` → File I/O and score management
- Cleaner input validation and user feedback
- Better separation of concerns for maintainability

### Removed
- Infinite gameplay loop from v1.0
- Repetitive “play again?” prompts after every round
- Monolithic single-file structure

### Notes
- This version is considered **final**
- Any future enhancements will be released as a **remastered version**, not patches to v2.0

---

## [v1.0] – Initial Release
**Release Type:** First Implementation  

### Features
- Basic Rock–Paper–Scissors gameplay
- Single-file, procedural Python script
- Continuous gameplay until user exits manually
- Simple score tracking during runtime

### ⚠ Limitations
- No persistent score storage
- No match history
- No fixed round limit (game could become repetitive)
- Game logic, UI, and input handling mixed in one file

---

##  Versioning Summary

|---------|---------------------------------------------------|
| Version |               Description                         |
|---------|---------------------------------------------------|
|  v1.0   | Basic functional implementation                   |
|  v2.0   | Complete revamp with modular design & persistence |

---
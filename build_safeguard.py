#!/usr/bin/env python3
"""
SafeGuard Build System
https://github.com/lol8908-rgb/Virus-Defender
"""

import os
import sys
import shutil
import argparse
from pathlib import Path
from datetime import datetime


class BuildSystem:
    def __init__(self):
        self.project_root = Path(__file__).parent
        self.build_dir = self.project_root / "build"
        self.dist_dir = self.project_root / "dist"
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
    def log(self, message, level="INFO"):
        """Logging-Funktion"""
        prefix = f"[{level}]"
        print(f"{prefix} {message}")
    
    def clean(self):
        """Entfernt Build-Artefakte"""
        self.log("Räume Build-Verzeichnis auf...")
        for directory in [self.build_dir, self.dist_dir]:
            if directory.exists():
                shutil.rmtree(directory)
                self.log(f"Gelöscht: {directory}")
        self.log("Cleanup abgeschlossen ✓")
    
    def prepare_directories(self):
        """Erstellt notwendige Verzeichnisse"""
        self.build_dir.mkdir(exist_ok=True)
        self.dist_dir.mkdir(exist_ok=True)
        self.log(f"Verzeichnisse erstellt ✓")
    
    def copy_sources(self):
        """Kopiert Source-Dateien in Build-Verzeichnis"""
        self.log("Kopiere Source-Dateien...")
        
        src_dir = self.project_root / "safeguard"
        if src_dir.exists():
            shutil.copytree(src_dir, self.build_dir / "safeguard", dirs_exist_ok=True)
            self.log(f"Source-Dateien kopiert ✓")
        else:
            self.log(f"Warnung: {src_dir} nicht gefunden", "WARN")
    
    def optimize(self):
        """Optimiert Python-Dateien"""
        self.log("Optimiere Python-Dateien...")
        
        try:
            import py_compile
            for py_file in self.build_dir.rglob("*.py"):
                py_compile.compile(str(py_file), doraise=True)
                self.log(f"Optimiert: {py_file.name}")
            self.log("Optimierung abgeschlossen ✓")
        except Exception as e:
            self.log(f"Fehler bei Optimierung: {e}", "ERROR")
            return False
        return True
    
    def create_manifest(self):
        """Erstellt eine Manifest-Datei"""
        manifest = f"""# SafeGuard Build Manifest
Build Time: {datetime.now().isoformat()}
Version: 1.0.0
Build ID: {self.timestamp}
Platform: {sys.platform}
Python: {sys.version}
"""
        manifest_path = self.build_dir / "MANIFEST.txt"
        manifest_path.write_text(manifest)
        self.log(f"Manifest erstellt: {manifest_path}")
    
    def build(self, optimize=False, clean_first=True):
        """Führt den Build-Prozess aus"""
        self.log("🔨 SafeGuard Build wird gestartet...\n")
        
        if clean_first:
            self.clean()
        
        self.prepare_directories()
        self.copy_sources()
        self.create_manifest()
        
        if optimize:
            if not self.optimize():
                self.log("Build fehlgeschlagen!", "ERROR")
                return False
        
        self.log("\n✅ Build erfolgreich abgeschlossen!")
        self.log(f"Build-Verzeichnis: {self.build_dir}")
        return True


def main():
    parser = argparse.ArgumentParser(
        description="SafeGuard Build System",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Beispiele:
  python build.py                    # Standard Build
  python build.py --optimize         # Build mit Optimierungen
  python build.py --clean            # Cleanup nur
  python build.py --optimize --clean # Optimiertes Build mit Cleanup
        """
    )
    
    parser.add_argument(
        "--optimize",
        action="store_true",
        help="Erstellt eine optimierte Version"
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Entfernt Build-Artefakte"
    )
    
    args = parser.parse_args()
    
    build = BuildSystem()
    
    if args.clean:
        build.clean()
        return 0
    
    if not build.build(optimize=args.optimize):
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())

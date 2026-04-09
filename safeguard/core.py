"""
SafeGuard Core - Scanning Engine
"""

from pathlib import Path
from typing import Dict, List
import hashlib


class Scanner:
    """Haupt-Scanner für Dateien und Verzeichnisse"""
    
    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.scanned_files = 0
        self.threats_found = 0
        
    def scan(self, path: str) -> Dict:
        """
        Scannt ein Verzeichnis oder eine Datei
        
        Args:
            path: Pfad zur Datei oder zum Verzeichnis
            
        Returns:
            Dict mit Scan-Ergebnissen
        """
        path_obj = Path(path)
        
        if not path_obj.exists():
            return {"error": f"Pfad existiert nicht: {path}"}
        
        if path_obj.is_file():
            self._scan_file(path_obj)
        else:
            self._scan_directory(path_obj)
        
        return {
            "scanned_files": self.scanned_files,
            "threats_found": self.threats_found,
            "status": "completed"
        }
    
    def _scan_file(self, file_path: Path) -> bool:
        """Scannt eine einzelne Datei"""
        self.scanned_files += 1
        
        if self.verbose:
            print(f"  📄 Scanne: {file_path.name}")
        
        # Beispiel: Prüfe auf verdächtige Dateitypen
        suspicious_extensions = [".exe", ".bat", ".cmd", ".scr", ".vbs"]
        if file_path.suffix.lower() in suspicious_extensions:
            self.threats_found += 1
            if self.verbose:
                print(f"    ⚠️  Verdächtige Datei erkannt: {file_path.suffix}")
            return True
        
        return False
    
    def _scan_directory(self, dir_path: Path):
        """Scannt ein Verzeichnis rekursiv"""
        try:
            for item in dir_path.rglob("*"):
                if item.is_file():
                    self._scan_file(item)
        except PermissionError as e:
            if self.verbose:
                print(f"  ❌ Zugriff verweigert: {e}")
    
    @staticmethod
    def get_file_hash(file_path: Path, algorithm: str = "sha256") -> str:
        """Berechnet Hash einer Datei"""
        hasher = hashlib.new(algorithm)
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
        return hasher.hexdigest()

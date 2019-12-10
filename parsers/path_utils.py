from pathlib import Path, PureWindowsPath

def get_correct_path(path: str) -> str:
	"""Convert path to valid format for all system using pathlib."""
	filename = PureWindowsPath(path)
	return Path(filename)
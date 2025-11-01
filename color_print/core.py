"""Core colored output functions."""

# ANSI color codes
COLORS = {
    'RED': '\033[91m',
    'GREEN': '\033[92m',
    'YELLOW': '\033[93m',
    'BLUE': '\033[94m',
    'MAGENTA': '\033[95m',
    'CYAN': '\033[96m',
    'WHITE': '\033[97m',
    'RESET': '\033[0m',
    'BOLD': '\033[1m',
    'DIM': '\033[2m',
    'ITALIC': '\033[3m',
    'UNDERLINE': '\033[4m',
}


def _colored(text, color, bold=False, underline=False):
    prefix = ""
    if bold:
        prefix += COLORS['BOLD']
    if underline:
        prefix += COLORS['UNDERLINE']
    prefix += COLORS[color]
    
    return f"{prefix}{text}{COLORS['RESET']}"


def success(text, bold=False):
    """Print green success message."""
    print(_colored(f"✓ {text}", 'GREEN', bold=bold))


def error(text, bold=True):
    """Print red error message."""
    print(_colored(f"✗ {text}", 'RED', bold=bold))


def warning(text, bold=False):
    """Print yellow warning message."""
    print(_colored(f"⚠ {text}", 'YELLOW', bold=bold))


def info(text, bold=False):
    """Print blue info message."""
    print(_colored(f"ℹ {text}", 'BLUE', bold=bold))


def debug(text, bold=False):
    """Print cyan debug message."""
    print(_colored(f"🐛 {text}", 'CYAN', bold=bold))

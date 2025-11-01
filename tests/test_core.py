"""Tests for color_print."""

from io import StringIO
import sys
from color_print import success, error, warning, info, debug


def capture_output(func, text):
    """Capture printed output."""
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    
    func(text)
    
    output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    return output


def test_success():
    """Test success message."""
    output = capture_output(success, "Operation completed")
    assert "Operation completed" in output
    assert "✓" in output


def test_error():
    """Test error message."""
    output = capture_output(error, "Something went wrong")
    assert "Something went wrong" in output
    assert "✗" in output


def test_warning():
    """Test warning message."""
    output = capture_output(warning, "Be careful")
    assert "Be careful" in output
    assert "⚠" in output


def test_info():
    """Test info message."""
    output = capture_output(info, "FYI")
    assert "FYI" in output
    assert "ℹ" in output


def test_debug():
    """Test debug message."""
    output = capture_output(debug, "Debug info")
    assert "Debug info" in output
    assert "🐛" in output

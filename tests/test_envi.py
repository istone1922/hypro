import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from hypro.ENVI import empty_envi_header, check_envi_required_fields, envi_fields


def test_empty_header_contains_all_fields():
    header = empty_envi_header()
    for field in envi_fields:
        assert field in header
        assert header[field] is None


def test_check_envi_required_fields_raises():
    header = empty_envi_header()
    header['byte order'] = 0
    header['data type'] = None
    header['interleave'] = 'bsq'
    header['bands'] = 1
    header['lines'] = 1
    header['samples'] = 1
    with pytest.raises(ValueError):
        check_envi_required_fields(header)
